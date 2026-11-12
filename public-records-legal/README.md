# Public Records Legal

For a business that collects court and government records and sells or uses them: lead lists, data feeds, research products. The plugin sorts five questions that are usually blurred together.

| Question | Skill |
|---|---|
| May this portal be collected from, and by what method? | `/public-records-legal:collection-method-review` |
| What does this bulk-data or subscriber agreement let us do? | `/public-records-legal:bulk-agreement-review` |
| May these records be used to contact the people named in them? | `/public-records-legal:solicitation-use-check` |
| A custodian told us to stop. What now? | `/public-records-legal:notice-received` |
| Is this citation real and does the quote match? | `/public-records-legal:verify-citations` |

Start with `/public-records-legal:cold-start-interview`. It writes the practice profile the other skills read.

## Install

```
/plugin marketplace add Pecentia/claude-for-legal
/plugin install public-records-legal@pecentia-legal
```

## What is in the box

- `references/collection-law-primer.md`: the four theories a custodian can use against automated collection, and a five-tier sort for portals.
- `references/use-and-resale-overlays.md`: the federal and state rules that limit use after lawful collection.
- `references/primary-source-tools.md`: official sources and open-source tools for checking law.
- `references/state-solicitation-map.md`: per-state solicitation rules. Empty until rows are verified.
- `scripts/verify_quotes.py`: checks that a quoted rule appears at the URL it is attributed to. Standard library only.

```
python3 scripts/verify_quotes.py research/*.json --out report.json
```

## Connectors

CourtListener (official MCP from Free Law Project) for case law. Statutes, regulations and court rules are read at the official source; see `references/primary-source-tools.md`.

## Limits

This plugin drafts for review by a licensed attorney. It does not give legal advice. The reference files were written from model knowledge and say so at the top; nothing in them is verified until the verify skill has run and a lawyer has read the source. Scraping law is unsettled and varies by circuit and state.
