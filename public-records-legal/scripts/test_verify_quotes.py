#!/usr/bin/env python3
"""Offline tests for verify_quotes.py. Run: python3 -m unittest test_verify_quotes -v"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import verify_quotes as vq  # noqa: E402

RULE = (
    "Bulk distribution of court records for the purpose of commercial "
    "solicitation of the individuals named in them is not permitted."
)
PAGE_HTML = f"<html><style>p{{}}</style><body><p>Rule 4.&nbsp;{RULE}</p></body></html>"


class NormalizeTests(unittest.TestCase):
    def test_ignores_case_punctuation_entities_and_line_breaks(self):
        self.assertEqual(vq.normalize("“Bulk\n distribution,”&nbsp;OF"), "bulk distribution of")


class PageTextTests(unittest.TestCase):
    def test_strips_tags_and_style_blocks(self):
        text = vq.page_text(PAGE_HTML.encode(), "text/html; charset=utf-8")
        self.assertIn("Bulk distribution", text)
        self.assertNotIn("p{}", text)

    def test_returns_none_for_pdf_by_header_or_magic_bytes(self):
        self.assertIsNone(vq.page_text(b"x", "application/pdf"))
        self.assertIsNone(vq.page_text(b"%PDF-1.7 ...", "application/octet-stream"))

    def test_falls_back_to_utf8_on_unknown_charset(self):
        self.assertEqual(vq.page_text(b"plain", "text/plain; charset=not-a-charset"), "plain")


class MatchQuoteTests(unittest.TestCase):
    def setUp(self):
        self.page = vq.normalize(vq.page_text(PAGE_HTML.encode(), "text/html"))

    def test_exact_quote_is_found(self):
        status, note = vq.match_quote(RULE, self.page)
        self.assertEqual(status, "found")
        self.assertIn("exact", note)

    def test_quote_with_altered_tail_is_partial_match(self):
        altered = RULE.replace("is not permitted", "shall be a misdemeanor")
        status, note = vq.match_quote(altered, self.page)
        self.assertEqual(status, "found")
        self.assertIn("partial", note)

    def test_invented_quote_is_not_found(self):
        invented = "No person shall use an automated program to copy records from this website at any time."
        self.assertEqual(vq.match_quote(invented, self.page)[0], "not-found")

    def test_short_quote_is_skipped(self):
        self.assertEqual(vq.match_quote("not permitted", self.page)[0], "skipped")


class EntriesFromTests(unittest.TestCase):
    def test_accepts_list_and_known_wrapper_keys(self):
        entry = {"quote": "q", "url": "u"}
        self.assertEqual(vq.entries_from([entry, "junk"]), [entry])
        for key in vq.LIST_KEYS:
            self.assertEqual(vq.entries_from({key: [entry]}), [entry])

    def test_unknown_shape_yields_nothing(self):
        self.assertEqual(vq.entries_from({"other": [1]}), [])
        self.assertEqual(vq.entries_from("text"), [])


class FirstUrlTests(unittest.TestCase):
    def test_takes_first_of_several_urls_in_one_field(self):
        self.assertEqual(vq.first_url("https://a.gov/x ; https://b.com/y"), "https://a.gov/x")
        self.assertEqual(vq.first_url("https://a.gov/x; https://b.com/y"), "https://a.gov/x")
        self.assertEqual(vq.first_url(""), "")


class FetchTests(unittest.TestCase):
    def test_malformed_url_is_unfetchable_not_a_crash(self):
        text, note = vq.fetch("https://a.gov/x y")
        self.assertIsNone(text)
        self.assertIn("fetch failed", note)


class CheckFileTests(unittest.TestCase):
    def write(self, data) -> Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        with handle:
            handle.write(data if isinstance(data, str) else json.dumps(data))
        self.addCleanup(Path(handle.name).unlink)
        return Path(handle.name)

    def run_check(self, data, fetch_result):
        with mock.patch.object(vq, "fetch", return_value=fetch_result) as fetch, mock.patch.object(
            vq.time, "sleep"
        ):
            rows = vq.check_file(self.write(data), {})
        return rows, fetch

    def test_statuses_and_one_fetch_per_url(self):
        url = "https://courts.example.gov/rule4"
        data = {
            "provisions": [
                {"citation": "Rule 4", "quote": RULE, "url": url},
                {"citation": "Rule 9", "quote": "An invented sentence that the page does not contain anywhere.", "url": url},
                {"citation": "No quote", "url": url},
                {"citation": "Bad URL", "quote": RULE, "url": "ftp://x"},
            ]
        }
        rows, fetch = self.run_check(data, (PAGE_HTML, "fetched"))
        self.assertEqual([row["status"] for row in rows], ["found", "not-found", "skipped", "skipped"])
        self.assertEqual(fetch.call_count, 1)

    def test_unfetchable_page_is_reported_not_guessed(self):
        data = [{"citation": "Rule 4", "quote": RULE, "url": "https://courts.example.gov/rule4.pdf"}]
        rows, _ = self.run_check(data, (None, "HTTP 403"))
        self.assertEqual(rows[0]["status"], "unfetchable")
        self.assertEqual(rows[0]["note"], "HTTP 403")

    def test_unreadable_input_is_reported(self):
        rows, _ = self.run_check("{not json", (None, ""))
        self.assertEqual(rows[0]["status"], "skipped")
        self.assertIn("unreadable input", rows[0]["note"])


if __name__ == "__main__":
    unittest.main()
