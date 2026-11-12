---
name: bulk-agreement-review
description: >
  Review a bulk data agreement, subscriber agreement, API license or data
  dissemination contract from a court or clerk against what the business needs to
  do with the records: resell them, deliver them to customers, and have customers
  contact the people named. Use when the user says "review this bulk agreement",
  "can we resell under this", "the clerk sent a contract", or attaches a data
  license from a court or agency.
argument-hint: "[file | link | pasted text]"
---

# /bulk-agreement-review

1. Load `~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md`. If placeholders, stop and prompt setup.
2. Get the agreement and every document it incorporates: the court rule, fee schedule, policy, application form. An agreement that says "subject to Rule X" has Rule X as a term.
3. Run the clause table below. Quote each clause with its section number.
4. Give a verdict against the business model in the profile.
5. Output the memo.

```
/public-records-legal:bulk-agreement-review clerk-data-agreement.pdf
```

---

# Bulk Agreement Review

## Clause table

For each row: the clause quoted, the section, and one of **allows**, **limits**, **forbids**, **silent**.

| Topic | What to find | Why it decides the deal |
|---|---|---|
| Resale and redistribution | May the licensee pass records to third parties at all? In bulk, or only as part of a product? | A reseller with a no-redistribution clause has no product |
| Sole-user and internal-use clauses | "For the internal use of the requester only" and similar | Same |
| Commercial solicitation | Any bar on using the data, or letting others use it, to solicit the people named | Lead buyers solicit. Check whether the bar is on the licensee, on downstream users, or both |
| Downstream flow-down | Must customers sign the same restrictions? Must the licensee police them? | Decides customer terms and audit burden |
| Fields delivered | Party addresses, dates of birth, case type, filing date | Many programs strip addresses. Without an address the record may be worthless for mail |
| Excluded case types | Sealed, juvenile, protective orders, some family and probate matters | Compare with the record types in the profile |
| Update and purge duty | How fast must sealed, expunged or corrected records be removed, and from customers too? | Needs a purge path that reaches delivered data |
| Freshness | Daily, weekly, monthly; push or pull; lag from filing | A monthly file does not serve a weekly product |
| Eligibility and FCRA terms | Bars on credit, tenant, employment use; required disclaimers | Must match customer terms |
| Eligibility of the licensee | Residency, notarization, business type, bond, insurance, background check | Decides whether an out-of-state business can sign at all |
| Fees | Setup, per record, per request, annual; who may change them and on what notice | Sets the unit cost and the exposure to a price change |
| Audit and inspection | The custodian's right to audit the licensee and its customers | Customers must agree to it in their own terms |
| Indemnity and liability | Who pays if a record is wrong or a customer misuses it | Uncapped indemnity to a government body is common and often not negotiable |
| Term and termination | Termination at will; what happens to data held at termination | A delete-on-termination clause can empty the product |
| Governing law and venue | Which courts, which law | Cost of any dispute |
| Other access routes | Does signing bar the licensee from collecting the same data another way? | Signing can close a door that was open |

## Verdict

One of:

- **Workable**: allows resale and the intended downstream use, delivers the fields needed, on a usable schedule.
- **Workable with changes to our side**: needs customer-term changes, a purge path, or a registration. List each.
- **Not workable for this business model**: name the clause. Say what it would still be useful for, such as internal completeness checks, if the agreement allows that.
- **Cannot tell**: a term is ambiguous. Draft the exact question to put to the custodian in writing, and do not rely on a verbal answer.

Do not read silence as permission where the agreement incorporates a rule or statute; read the rule.

## Memo format

```
DRAFT FOR ATTORNEY REVIEW
Agreement: [title, custodian, version or date]
Documents incorporated: [list, each read: yes/no]
Verdict: [one of the four]

Deciding clauses
- [topic]: "[quote]" (s. [n]) -> [allows / limits / forbids]

Full clause table
[table]

What we would have to change
- [item]

Questions to put to the custodian in writing
- [question]

For the attorney
- [indemnity, venue, anything unusual]
```
