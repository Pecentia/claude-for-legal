#!/usr/bin/env python3
"""Check that case citations in a document resolve to a real case of that name.

Reads text or Markdown files, extracts full case citations (volume, reporter,
page) with eyecite, and resolves each one through CourtListener's public
citation address (https://www.courtlistener.com/c/<reporter>/<vol>/<page>/).
No account or token is needed.

Output: a JSON report on stdout (or --out FILE), one row per distinct citation:
  resolved       the citation leads to one case whose name shares a party
                 name with the document
  name-mismatch  the citation leads to a case, but none of the party names in
                 the document appear in that case's name
  ambiguous      CourtListener lists more than one case at that citation and
                 none of them, or the page could not be read, matches by name
  not-found      CourtListener has no case at that citation
  error          the lookup failed (network, block)

"resolved" proves the case exists under that citation and name. It does not
prove the case holds what the document says, or that it is still good law.

Requires eyecite (pip install eyecite). Sends a generic User-Agent and the
citation, nothing else.
"""
from __future__ import annotations

import argparse
import http.client
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://www.courtlistener.com/c"
USER_AGENT = "Mozilla/5.0 (compatible; citation-check/1.0)"
TIMEOUT_SECONDS = 25
MAX_BYTES = 3_000_000
DELAY_BETWEEN_LOOKUPS_SECONDS = 1.0
OPINION_PATH_RE = re.compile(r"/opinion/\d+/([^/]+)/?")
WORD_RE = re.compile(r"[a-z0-9]+")
MIN_PARTY_WORD_CHARS = 4
MARKDOWN_EMPHASIS_RE = re.compile(r"[*_`]")
# Words too common in case names to count as a party-name match.
STOP_WORDS = frozenset(
    "united states state people commonwealth city county corp corporation company "
    "inc association labs board dept department publishing".split()
)


def party_words(*names: str | None) -> set[str]:
    """Distinctive lowercase words from party names."""
    words: set[str] = set()
    for name in names:
        for word in WORD_RE.findall((name or "").lower()):
            if len(word) >= MIN_PARTY_WORD_CHARS and word not in STOP_WORDS:
                words.add(word)
    return words


def extract_citations(text: str) -> list[dict]:
    """Return one entry per distinct full case citation found in text."""
    from eyecite import get_citations
    from eyecite.models import FullCaseCitation

    found: dict[tuple[str, str, str], dict] = {}
    for cite in get_citations(MARKDOWN_EMPHASIS_RE.sub("", text)):
        if not isinstance(cite, FullCaseCitation):
            continue
        groups = cite.groups
        key = (groups.get("volume", ""), groups.get("reporter", ""), groups.get("page", ""))
        if not all(key) or key in found:
            continue
        meta = cite.metadata
        found[key] = {
            "citation": cite.corrected_citation(),
            "volume": key[0],
            "reporter": cite.corrected_reporter(),
            "page": key[2],
            "plaintiff": meta.plaintiff,
            "defendant": meta.defendant,
            "year": meta.year,
        }
    return list(found.values())


def lookup_url(reporter: str, volume: str, page: str) -> str:
    return f"{BASE_URL}/{urllib.parse.quote(reporter)}/{volume}/{page}/"


def candidate_urls(body: bytes) -> list[str]:
    """Opinion addresses listed on a 'more than one case' page."""
    paths = dict.fromkeys(match.group(0) for match in OPINION_PATH_RE.finditer(body.decode("utf-8", "replace")))
    return [urllib.parse.urljoin(BASE_URL, path) for path in paths]


def resolve(url: str) -> tuple[str, str, list[str]]:
    """Follow the citation address. Return (outcome, final_url, candidates).
    outcome is 'case', 'ambiguous', 'not-found' or 'error: ...'; candidates
    holds the opinion addresses offered when the outcome is 'ambiguous'."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            final_url = response.geturl()
            body = b"" if OPINION_PATH_RE.search(final_url) else response.read(MAX_BYTES)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return "not-found", url, []
        if error.code == 300:  # Multiple Choices: several cases share the citation
            return "ambiguous", error.geturl() or url, candidate_urls(error.read(MAX_BYTES))
        return f"error: HTTP {error.code}", url, []
    except (urllib.error.URLError, http.client.HTTPException, TimeoutError, OSError, ValueError) as error:
        return f"error: {type(error).__name__}", url, []
    if OPINION_PATH_RE.search(final_url):
        return "case", final_url, []
    return "ambiguous", final_url, candidate_urls(body)


def judge(entry: dict, outcome: str, final_url: str, candidates: list[str] | None = None) -> dict:
    """Turn a lookup outcome into a report row."""
    row = {key: entry[key] for key in ("citation", "plaintiff", "defendant", "year")}
    row["url"] = final_url
    wanted = party_words(entry["plaintiff"], entry["defendant"])
    if outcome == "ambiguous" and wanted:
        for candidate in candidates or []:
            slug = OPINION_PATH_RE.search(candidate).group(1)
            if wanted & set(WORD_RE.findall(slug.lower())):
                note = f"one of {len(candidates)} cases at this citation: {slug}"
                return {**row, "url": candidate, "status": "resolved", "note": note}
    if outcome != "case":
        status = outcome if outcome in ("ambiguous", "not-found") else "error"
        note = {
            "ambiguous": "more than one case at this citation: open the address and pick by name",
            "not-found": "CourtListener has no case at this citation",
        }.get(outcome, outcome)
        return {**row, "status": status, "note": note}
    slug = OPINION_PATH_RE.search(final_url).group(1)
    slug_words = set(WORD_RE.findall(slug.lower()))
    if not wanted:
        return {**row, "status": "resolved", "note": f"no party name in the document to compare; found: {slug}"}
    if wanted & slug_words:
        return {**row, "status": "resolved", "note": f"found: {slug}"}
    return {**row, "status": "name-mismatch", "note": f"citation leads to a different case: {slug}"}


def check_text(text: str, source: str) -> list[dict]:
    rows = []
    for entry in extract_citations(text):
        outcome, final_url, candidates = resolve(lookup_url(entry["reporter"], entry["volume"], entry["page"]))
        rows.append({"file": source, **judge(entry, outcome, final_url, candidates)})
        time.sleep(DELAY_BETWEEN_LOOKUPS_SECONDS)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+", type=Path, help="text or Markdown files to check")
    parser.add_argument("--out", type=Path, help="write the report here instead of stdout")
    args = parser.parse_args()
    try:
        import eyecite  # noqa: F401
    except ImportError:
        print("eyecite is required: pip install eyecite", file=sys.stderr)
        return 2

    rows: list[dict] = []
    for path in args.files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            rows.append({"file": path.name, "status": "error", "note": f"unreadable input: {error}"})
            continue
        rows.extend(check_text(text, path.name))
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
