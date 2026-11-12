# Use and Resale Overlays: what limits the use of records after they are lawfully obtained

**Last verified: 2026-11-12. The case citations in this file resolve to the named case on CourtListener (`scripts/check_case_citations.py`). Statutes, regulations and the propositions each case is cited for have not been checked.**

> How a record was obtained and what it may be used for are separate questions. A lawful download does not make every use lawful. Verify each citation with `/public-records-legal:verify-citations`; stale after 90 days.

## Federal

| Regime | When it applies | Why it matters to a records reseller |
|---|---|---|
| Fair Credit Reporting Act, 15 U.S.C. § 1681 et seq. | Information bearing on a person's creditworthiness, character or mode of living that is used or expected to be used for credit, insurance, employment, tenant screening or similar eligibility decisions | Court records (evictions, judgments, criminal) sold for screening make the seller a consumer reporting agency. Marketing lists are a different use, but the seller needs contract terms and controls that keep buyers from using them for eligibility decisions. |
| Driver's Privacy Protection Act, 18 U.S.C. §§ 2721-2725 | Personal information from state motor vehicle records | Not court records, but address-append and skip-trace vendors often source from DMV data. Ask the vendor. |
| Telephone Consumer Protection Act, 47 U.S.C. § 227, and the Do Not Call rules | Calls and texts | Applies to the buyer's outreach and can reach the seller who appends phone numbers and markets them for calling. |
| CAN-SPAM Act, 15 U.S.C. § 7701 et seq. | Commercial email | Same point for appended email addresses. |
| Mortgage Assistance Relief Services Rule (Regulation O), 12 C.F.R. part 1015 | Offers to help a consumer avoid foreclosure or change a mortgage | Limits how foreclosure leads may be solicited and bars advance fees. |
| Commercial speech doctrine | Any state restriction on solicitation | *Shapero v. Kentucky Bar Ass'n*, 486 U.S. 466 (1988); *Florida Bar v. Went For It*, 515 U.S. 618 (1995) (30-day ban on lawyer mail to accident victims upheld); *Sorrell v. IMS Health*, 564 U.S. 552 (2011). A restriction can be valid; whether it is, is a litigation question, not a planning assumption. |

## State patterns to check in every state

1. **Commercial-solicitation limits on public or court records.** Some states bar using records, or lists compiled from them, to solicit the people named. Record whether the limit is a statute that reaches anyone, or a condition that binds only portal users or bulk licensees. See `state-solicitation-map.md`.
2. **Foreclosure lead rules.** Foreclosure consultant and equity purchaser statutes (for example Cal. Civ. Code §§ 1695 et seq. and 2945 et seq.) regulate offers to homeowners in default: contract form, cancellation rights, sometimes licensing. They bind the buyer of the lead first, and a seller that scripts or directs the outreach second.
3. **Eviction records.** Sealing and masking rules (for example Cal. Code Civ. Proc. § 1161.2) make many eviction filings non-public for a period or permanently. A feed that republishes a later-sealed case needs a purge path.
4. **Probate and heirs.** Look for heir-finder regulation, limits on soliciting estates, and rules protecting minors, wards and protected persons, whose records should be excluded.
5. **Family cases.** Divorce and custody files have confidentiality rules that vary by state and by document.
6. **Data broker registration.** California (Civ. Code § 1798.99.80 et seq., with the Delete Act), Vermont (9 V.S.A. § 2430 et seq.), Texas (Bus. & Com. Code ch. 509) and Oregon require businesses that sell personal information they did not collect from the person to register. Exemptions for publicly available government records differ by state and are narrower than they look once data is appended or combined.
7. **Comprehensive privacy laws.** Most exempt "publicly available information" lawfully made available from government records. Check the definition: appended phones, emails, property matches and scores are usually outside it.
8. **Sealed, expunged and corrected records.** Bulk agreements often require the licensee to apply updates within days. A reseller needs the same duty in its own customer terms.

## Seller-side controls that follow from the above

- Customer terms that forbid eligibility uses (credit, tenant, employment, insurance) and require compliance with solicitation, foreclosure and telemarketing law.
- A purge and correction path that reaches data already delivered.
- Exclusion of minors, wards, protected persons and sealed matters at ingestion.
- A record, per jurisdiction, of how the data was obtained and under what terms.
