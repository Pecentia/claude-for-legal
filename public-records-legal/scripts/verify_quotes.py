#!/usr/bin/env python3
"""Check that quoted legal text appears at the URL it is attributed to.

Input: one or more JSON files. Each may be a list of entries, or an object
holding a list under "provisions" or "clauses". An entry needs "quote" and
"url"; "citation" (or "topic") is used as its label.

Output: a JSON report on stdout (or --out FILE) with one row per entry:
  found        the normalized quote, or a long enough run of it, is on the page
  not-found    the page was fetched and the quote is not on it
  unfetchable  the page could not be fetched or is not text (PDF, 403, timeout)
  skipped      the entry has no quote or no http(s) URL

"found" proves the words are at that address today. It does not prove the
rule is in force, complete, or correctly summarized. A lawyer still reads it.

Standard library only. Sends a generic User-Agent and nothing else.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "Mozilla/5.0 (compatible; citation-check/1.0)"
TIMEOUT_SECONDS = 25
MAX_BYTES = 6_000_000
MIN_QUOTE_CHARS = 25
PARTIAL_WINDOW_WORDS = 8
DELAY_BETWEEN_FETCHES_SECONDS = 1.0
LIST_KEYS = ("provisions", "clauses", "entries")

TAG_RE = re.compile(r"<(script|style)\b.*?</\1>|<[^>]+>", re.S | re.I)
NON_WORD_RE = re.compile(r"[^a-z0-9]+")


def normalize(text: str) -> str:
    """Lowercase and reduce to single-spaced alphanumerics so punctuation,
    smart quotes and line breaks do not defeat a match."""
    return NON_WORD_RE.sub(" ", html.unescape(text).lower()).strip()


def page_text(raw: bytes, content_type: str) -> str | None:
    """Return visible text for HTML or plain text; None for anything else."""
    kind = content_type.lower()
    if "pdf" in kind or raw[:5] == b"%PDF-":
        return None
    charset_match = re.search(r"charset=([\w-]+)", kind)
    charset = charset_match.group(1) if charset_match else "utf-8"
    try:
        decoded = raw.decode(charset, errors="replace")
    except LookupError:
        decoded = raw.decode("utf-8", errors="replace")
    return TAG_RE.sub(" ", decoded)


def fetch(url: str) -> tuple[str | None, str]:
    """Return (text, note). text is None when the page is not usable."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read(MAX_BYTES)
            content_type = response.headers.get("Content-Type", "")
    except urllib.error.HTTPError as error:
        return None, f"HTTP {error.code}"
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
        return None, f"fetch failed: {type(error).__name__}"
    text = page_text(raw, content_type)
    if text is None:
        return None, "not text (PDF or binary): read it by hand"
    return text, "fetched"


def match_quote(quote: str, page: str) -> tuple[str, str]:
    """Return (status, note) for one quote against normalized page text."""
    wanted = normalize(quote)
    if len(wanted) < MIN_QUOTE_CHARS:
        return "skipped", "quote too short to check"
    if wanted in page:
        return "found", "exact (normalized) match"
    words = wanted.split()
    if len(words) > PARTIAL_WINDOW_WORDS:
        windows = [
            " ".join(words[i : i + PARTIAL_WINDOW_WORDS])
            for i in range(0, len(words) - PARTIAL_WINDOW_WORDS + 1)
        ]
        hits = sum(1 for window in windows if window in page)
        if hits >= max(1, len(windows) // 2):
            return "found", f"partial match ({hits}/{len(windows)} word windows): compare by eye"
    return "not-found", "page fetched, quote absent"


def entries_from(data: object) -> list[dict]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in LIST_KEYS:
            if isinstance(data.get(key), list):
                return [item for item in data[key] if isinstance(item, dict)]
    return []


def nested(entry: dict, key: str) -> str:
    """Read key from the entry, or from a nested {"quote","url"} rule object."""
    value = entry.get(key)
    if isinstance(value, str):
        return value.strip()
    return ""


def check_file(path: Path, cache: dict[str, tuple[str | None, str]]) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [{"file": path.name, "status": "skipped", "note": f"unreadable input: {error}"}]
    rows = []
    for entry in entries_from(data):
        label = nested(entry, "citation") or nested(entry, "topic") or "(no citation)"
        quote, url = nested(entry, "quote"), nested(entry, "url")
        row = {"file": path.name, "citation": label, "url": url}
        if not quote or not url.startswith(("http://", "https://")):
            rows.append({**row, "status": "skipped", "note": "no quote or no http(s) URL"})
            continue
        if url not in cache:
            text, note = fetch(url)
            cache[url] = (normalize(text) if text is not None else None, note)
            time.sleep(DELAY_BETWEEN_FETCHES_SECONDS)
        page, note = cache[url]
        if page is None:
            rows.append({**row, "status": "unfetchable", "note": note})
            continue
        status, detail = match_quote(quote, page)
        rows.append({**row, "status": status, "note": detail})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+", type=Path, help="JSON files to check")
    parser.add_argument("--out", type=Path, help="write the report here instead of stdout")
    args = parser.parse_args()

    cache: dict[str, tuple[str | None, str]] = {}
    rows = [row for path in args.files for row in check_file(path, cache)]
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    report = json.dumps({"counts": counts, "rows": rows}, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.write_text(report, encoding="utf-8")
        print(json.dumps(counts), file=sys.stderr)
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
