#!/usr/bin/env python3
"""Offline tests for check_case_citations.py. Run: python3 -m unittest test_check_case_citations -v"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_case_citations as cc  # noqa: E402

ENTRY = {"citation": "593 U.S. 374", "plaintiff": "Van Buren", "defendant": "United States", "year": "2021"}
CASE_URL = "https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/"
OTHER_URL = "https://www.courtlistener.com/opinion/1/smith-v-jones/"


class PartyWordsTests(unittest.TestCase):
    def test_drops_short_and_generic_words(self):
        self.assertEqual(cc.party_words("Van Buren", "United States", None), {"buren"})


class JudgeTests(unittest.TestCase):
    def test_matching_name_is_resolved(self):
        self.assertEqual(cc.judge(ENTRY, "case", CASE_URL)["status"], "resolved")

    def test_real_citation_with_wrong_name_is_a_mismatch(self):
        row = cc.judge(ENTRY, "case", OTHER_URL)
        self.assertEqual(row["status"], "name-mismatch")
        self.assertIn("smith-v-jones", row["note"])

    def test_missing_citation_is_not_found(self):
        self.assertEqual(cc.judge(ENTRY, "not-found", "u")["status"], "not-found")

    def test_shared_citation_resolves_by_name_or_stays_ambiguous(self):
        hit = cc.judge(ENTRY, "ambiguous", "u", [OTHER_URL, CASE_URL])
        self.assertEqual((hit["status"], hit["url"]), ("resolved", CASE_URL))
        self.assertEqual(cc.judge(ENTRY, "ambiguous", "u", [OTHER_URL])["status"], "ambiguous")

    def test_lookup_failure_is_an_error_not_a_verdict(self):
        row = cc.judge(ENTRY, "error: HTTP 503", "u")
        self.assertEqual((row["status"], row["note"]), ("error", "error: HTTP 503"))


class CandidateUrlsTests(unittest.TestCase):
    def test_lists_each_offered_case_once(self):
        body = b'<a href="/opinion/1/smith-v-jones/">x</a><a href="/opinion/1/smith-v-jones/">y</a>'
        self.assertEqual(cc.candidate_urls(body), [OTHER_URL])


class LookupUrlTests(unittest.TestCase):
    def test_reporter_is_url_quoted(self):
        self.assertEqual(cc.lookup_url("F. Supp. 2d", "964", "1178"), cc.BASE_URL + "/F.%20Supp.%202d/964/1178/")


try:
    import eyecite  # noqa: F401
except ImportError:
    eyecite = None


@unittest.skipUnless(eyecite, "eyecite not installed")
class ExtractTests(unittest.TestCase):
    def test_finds_distinct_full_citations_through_markdown_emphasis(self):
        text = "*Van Buren v. United States*, 593 U.S. 374 (2021); again 593 U.S. 374; *Feist v. Rural*, 499 U.S. 340 (1991)."
        found = cc.extract_citations(text)
        self.assertEqual([entry["citation"] for entry in found], ["593 U.S. 374", "499 U.S. 340"])
        self.assertEqual(found[0]["plaintiff"], "Van Buren")


if __name__ == "__main__":
    unittest.main()
