# Collection Law Primer: automated access to public records portals

**Last verified: 2026-11-12. All 11 case citations in this file resolve to the named case on CourtListener (`scripts/check_case_citations.py`). Statutes and the propositions each case is cited for have not been checked.**

> **Staleness and accuracy check.** Every citation here is a starting point for a lawyer, not a conclusion. Run `/public-records-legal:verify-citations` on any citation before it goes into advice, and treat this file as stale after 90 days. Scraping law is unsettled and differs by circuit and by state.

## The four theories a records custodian can use

| Theory | What triggers it | Authorities to read |
|---|---|---|
| Computer Fraud and Abuse Act, 18 U.S.C. § 1030 | Access "without authorization" or exceeding it: getting past a login, a paywall, or a block that was imposed on you specifically | *Van Buren v. United States*, 593 U.S. 374 (2021) (gates-up-or-down reading); *hiQ Labs v. LinkedIn*, 31 F.4th 1180 (9th Cir. 2022) (publicly available pages, no gate); *Facebook v. Power Ventures*, 844 F.3d 1058 (9th Cir. 2016) (continuing after a cease-and-desist and an IP block was without authorization); *Craigslist v. 3Taps*, 964 F. Supp. 2d 1178 (N.D. Cal. 2013) (same pattern) |
| Breach of contract (terms of use) | Assent to terms: a click-through, an account, or continued use after actual notice | *Register.com v. Verio*, 356 F.3d 393 (2d Cir. 2004); *Nguyen v. Barnes & Noble*, 763 F.3d 1171 (9th Cir. 2014) (browsewrap needs notice); *Meta Platforms v. Bright Data* (N.D. Cal. Jan. 23, 2024) (terms did not reach logged-out collection of public pages); note that hiQ ultimately lost on contract in the district court in 2022 |
| Trespass to chattels and state computer-crime statutes | Measurable burden or harm to the server; state statutes vary and some are broader than the CFAA | *eBay v. Bidder's Edge*, 100 F. Supp. 2d 1058 (N.D. Cal. 2000); *Intel v. Hamidi*, 30 Cal. 4th 1342 (2003) (harm required); Cal. Penal Code § 502; Tex. Penal Code § 33.02 |
| The custodian's own access rules | Court rules and clerk policies on remote access, bulk distribution and commercial use; these can bind regardless of contract theory when the custodian is a court | The state's public-access-to-court-records rule; see `state-solicitation-map.md` |

Facts in public records are not copyrightable (*Feist v. Rural*, 499 U.S. 340 (1991); *Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)), so copyright is rarely the custodian's theory. That does not remove the four above.

## The fact pattern that loses

The cases that went badly for the collector share a sequence: the custodian told this collector to stop (a letter, a block aimed at them, a terms change naming them), and the collector kept going by technical means such as rotating IP addresses. Evading a general anti-bot measure before any notice is a weaker claim against the collector than evading a block after notice, but it is not a safe harbor, and several state statutes do not draw the distinction.

## Sorting a portal

1. **No gate, no assent.** Public pages, no login, no click-through, terms silent or only linked in a footer. Lowest risk. Rate-limit, identify nothing false, keep evidence of what the page showed.
2. **Technical friction only.** Captcha or a bot challenge with no terms forbidding automation. Solving or avoiding it is a business risk decision; record it. Risk rises sharply after any notice.
3. **Assent required.** A click-through or account whose terms forbid automated or commercial use. Collecting here is a contract breach on its face. Prefer a bulk agreement or a records request.
4. **Rule-based ban.** A court rule or administrative order forbids scraping or bulk commercial use. Do not collect. Use the sanctioned route or skip the jurisdiction.
5. **Notice received.** Stop that source the same day. Run `/public-records-legal:notice-received`.

## Access rights are weaker than people assume

- No general constitutional right to obtain government records: *Los Angeles Police Dept. v. United Reporting Publishing Corp.*, 528 U.S. 32 (1999) (a state may condition access to records on not using them commercially); *McBurney v. Young*, 569 U.S. 221 (2013) (citizen-only public records laws upheld).
- Court records carry a common-law right of access (*Nixon v. Warner Communications*, 435 U.S. 589 (1978)), but the court controls the manner, and many state judiciaries sit outside the state public records act.
- A records request reaches records that exist on the day of the request. It is not a subscription.
