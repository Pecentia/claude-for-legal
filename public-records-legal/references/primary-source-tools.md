# Primary-Source Tools

Sources and tools for checking a citation or a quoted rule. Prefer the official source; use third-party tools to find, never to conclude.

| Need | Source | Access |
|---|---|---|
| US case law, citation lookup, dockets | CourtListener (Free Law Project) | The `CourtListener` MCP connector in this plugin; REST API at `https://www.courtlistener.com/api/rest/v4/` (free token) |
| Code of Federal Regulations, current text | eCFR | `https://www.ecfr.gov/api/versioner/v1/full/<date>/title-<n>.xml?part=<p>&section=<s>`, no key |
| Federal Register documents | Federal Register API | `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=...`, no key |
| US Code and public laws | govinfo | `https://api.govinfo.gov/` (free api.data.gov key); browse at `https://uscode.house.gov/` |
| State bills and session law | Open States API v3 | `https://v3.openstates.org/` (free key); LegiScan is an alternative |
| State statutes and court rules | The state legislature and state judiciary sites | No uniform API. Fetch the official page and quote it. |
| Court rule on public access and bulk data | The state court administrative office | Usually a PDF. Fetch and quote. |

## Open-source libraries worth knowing (Free Law Project, all on GitHub)

- `freelawproject/eyecite`: extracts legal citations from text. Useful before a batch verification.
- `freelawproject/courts-db` and `freelawproject/reporters-db`: canonical court and reporter identifiers.
- `freelawproject/juriscraper`: scrapers for court opinion sites and PACER. It shows how a long-lived project structures per-court scrapers and their tests.

## Community MCP servers

Third-party MCP servers exist for eCFR, govinfo, Open States and LegiScan. None is wired into this plugin: they are small, unreviewed projects, and a legal research tool that silently returns wrong text is worse than none. Put any of them through `/legal-builder-hub:skill-installer` review before use, and still confirm the text at the official source.

## The script in this plugin

`scripts/verify_quotes.py` takes a JSON file of `{citation, quote, url}` entries, fetches each URL, and reports whether the quoted sentence appears there. It catches the most common research failure: a real-looking citation with a quote the source does not contain. It cannot tell you the rule is still in force or that it means what the summary says.
