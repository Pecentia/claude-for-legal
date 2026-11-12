---
name: verify-citations
description: >
  Check that legal citations and quoted rules are real and say what they are
  claimed to say, against primary sources. Runs a quote check over research files,
  looks up cases in CourtListener, and marks each citation verified, mismatch, or
  not checkable. Use when the user says "verify these citations", "check this
  research", "is this statute real", "did the agent make this up", or before any
  memo or reference file from this plugin is relied on.
argument-hint: "[file(s) | pasted citations]"
---

# /verify-citations

1. Collect the citations: from JSON research files, a memo, or a reference file in this plugin.
2. Statutes, rules and agreement clauses that carry a quote and a URL: run the script.
3. Cases: look each one up in CourtListener.
4. Anything left: fetch the official source by hand, per `references/primary-source-tools.md`.
5. Report in the format below. Update the "Last verified" line of any reference file checked in full.

```
/public-records-legal:verify-citations research/*.json
```

---

# Verify Citations

## Why this exists

Legal research written by a model, or by an agent told to return findings, fails in a predictable way: a plausible citation with a quote that the source does not contain, or a real rule attached to the wrong state. Nothing in this plugin is to be relied on until it has been through this skill and a person has read the source.

## Quoted rules: the script

```
python3 scripts/verify_quotes.py FILE [FILE ...] --out report.json
```

Input entries need `quote` and `url`, with `citation` as the label; a file may be a list or an object with a `provisions`, `clauses` or `entries` list. Statuses:

| Status | Meaning | Next step |
|---|---|---|
| `found` (exact) | The words are at that URL today | Check the URL is an official source, then read the provision in context |
| `found` (partial) | At least half of the 8-word runs match | Compare by eye; the quote may be trimmed or altered |
| `not-found` | Page fetched, quote absent | Treat the claim as unsupported. Find the official text and re-quote, or drop it |
| `unfetchable` | PDF, block, timeout | Open by hand. Many court rules are PDFs |
| `skipped` | No quote or URL | Cannot be verified as given |

`found` is necessary, not sufficient. It does not show the rule is in force, that the page is official, or that the summary is fair.

## Cases: CourtListener

For each case, use the CourtListener connector's citation lookup. Confirm:

- the reporter citation resolves to a case with that name and court and year
- the proposition it is cited for appears in the opinion; quote the passage
- later history, as far as CourtListener shows it. Say plainly that this is not a citator check.

A citation that does not resolve is reported as **not found**, never silently corrected. If a near match exists, report it as a suggestion.

## Official source test

A URL counts as official when it is the legislature, the judiciary, the agency, or the custodian itself. Commercial republishers and law firm articles do not count, even with an exact quote match; find the same text at the official source.

## Report format

```
Checked: [n]   Verified: [n]   Mismatch: [n]   Not checkable: [n]

| Citation | Claimed for | Result | Source read | Note |
|---|---|---|---|---|

Unsupported: remove or re-research
- [citation]: [why]

Read by hand still needed
- [citation]: [PDF or blocked URL]
```

**Verified** means: resolves, official source, quote or proposition present, read in context. Anything less is reported under the status it earned.
