# State Solicitation Map

**Status: 4 states partly populated, quote-verified 2026-11-12, none yet read by an attorney.**

This file holds, per state, the rules that limit using court or public records to solicit the people named in them. A row is added only after `scripts/verify_quotes.py` reports the quoted text as `found` (exact match) at an official source. A row moves from the first table to the second only after an attorney has read the provision in context. Research output that has not passed the quote check does not belong here.

A state missing from this file has not been checked. It does not mean the state has no rule.

## Row format

- **Kind**: statute, court rule, administrative order, portal terms, or bulk agreement term.
- **Reaches**: `anyone` (a law of general application), `portal users`, or `licensees only`. This column decides most questions. A term that binds only licensees does not bind someone who never signed.
- **Lead types**: probate, eviction, foreclosure, divorce or family, other civil, code violation or lien. `all` means the text does not distinguish.

## Quote-verified, awaiting attorney read

Open question on every statute below: whether "public records" or "agency" in that state's act reaches court records. In many states the judiciary sits outside the public records act.

| State | Citation | Kind | Reaches | Lead types | Quote (verified) | Penalty as stated | Official URL | Verified on |
|---|---|---|---|---|---|---|---|---|
| Kansas | K.S.A. 45-230(a) | statute | anyone | all | "No person shall knowingly sell, give or receive, for the purpose of selling or offering for sale any property or service to persons listed therein, any list of names and addresses contained in or derived from public records except:" | Civil penalty up to $500 per violation (45-230(b)); read the listed exceptions | https://ksrevisor.gov/statutes/chapters/ch45/045_002_0030.html | 2026-11-12 |
| South Carolina | S.C. Code 30-2-50(A) | statute | anyone | all | "A person or private entity shall not knowingly obtain or use personal information obtained from a state agency, a local government, or other political subdivision of the State for commercial solicitation directed to any person in this State." | Misdemeanor: fine up to $500, up to one year, or both (30-2-50(D)) | https://www.scstatehouse.gov/code/t30c002.php | 2026-11-12 |
| South Carolina | Rule 610, SCACR | court rule | bulk requesters | all | "The South Carolina Judicial Branch (SCJB) shall not provide bulk distribution of or compiled information from judicial records where those records are sought for any commercial purpose." | Request refused | https://www.sccourts.org/resources/general-public/rule-610-requests/ | 2026-11-12 |
| Idaho | Idaho Code 74-120(1) | statute | anyone | all | "(b) No list of persons prepared by the agency may be used as a mailing list or a telephone number list except by the agency or another agency without first securing the permission of those on the list." | Civil penalty up to $1,000 on a finding of deliberate bad faith (74-120(11)) | https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/SECT74-120/ | 2026-11-12 |
| Idaho | Idaho Code 74-120(2) | statute | anyone | all | "Except as may be otherwise provided in this chapter, this section does not prevent an individual from compiling a mailing list or a telephone number list by examination or copying of public records, original documents or applications otherwise open to public inspection." | None; this is a carve-out from (1) | https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/SECT74-120/ | 2026-11-12 |

## Read by an attorney

None yet.

## Leads that did not pass the quote check

Reported so nobody re-adds them from memory. Each needs the official text found and read by hand.

- Kentucky, Supreme Court Order 2026-32 (Rules of Administrative Procedure Part XXII), said to bar commercial use of court records: the source is a PDF the script cannot read.
- Colorado, C.R.S. 24-72-305.5: the quote matched, but only on a commercial republisher, not the official statute site. By its terms it covers criminal justice records.
- Connecticut, Conn. Gen. Stat. 47a-26j (removed eviction records): partial match only on the official site.
