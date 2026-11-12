---
name: solicitation-use-check
description: >
  Check whether records of a given type from a given state may be used to contact
  the people named in them, by a given channel, and what the seller of the list
  must do. Use when the user asks "can our customers mail these people", "can we
  sell foreclosure leads in this state", "is it legal to solicit from probate
  filings", "what are the rules for eviction lists", or before adding a state or
  a record type to a product.
argument-hint: "[state] [record type] [channel: mail | call | text | email | door]"
---

# /solicitation-use-check

1. Load `~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md`. If placeholders, stop and prompt setup.
2. Read `references/use-and-resale-overlays.md` and the state's rows in `references/state-solicitation-map.md`.
3. If the map has no verified rows for the state, research it (below) and say that the result is unverified until `/public-records-legal:verify-citations` has run.
4. Answer in the format below.

```
/public-records-legal:solicitation-use-check Ohio foreclosure mail
```

---

# Solicitation Use Check

## Three layers, in this order

**1. How the records were obtained.** A restriction can ride with the data. If the records came under a bulk agreement or portal terms, those terms come first; get them from the source register. A term that binds licensees binds this business only if it is one.

**2. State law of general application.** Look for each of these and record "none found" with where you looked:

- A public records act or court rule that bars use of records, or lists made from them, for commercial solicitation
- A waiting period before soliciting people named in a new filing
- Record-type rules: foreclosure consultant or equity purchaser statutes, eviction sealing or masking, heir-finder or estate solicitation rules, family case confidentiality
- Protected classes: minors, wards, protected persons, victims, address confidentiality program participants
- Data broker registration and consumer privacy law, and whether the public-records exemption survives appended data

For each rule, record whether it reaches **anyone**, **portal users**, or **licensees only**, and whom it burdens: the person who solicits, the person who sells the list, or both.

**3. Channel law.** Mail has the fewest federal limits. Calls and texts bring the TCPA and Do Not Call rules. Email brings CAN-SPAM. Foreclosure-rescue offers bring Regulation O in any channel.

## Where to research

Official sources only, per `references/primary-source-tools.md`: the state legislature site for statutes, the state judiciary site for court rules and administrative orders, the attorney general for data broker registration. Quote the provision and keep the URL. Secondary sources may point the way; they are not cited.

## Answer format

```
DRAFT FOR ATTORNEY REVIEW
State: [state]   Record type: [type]   Channel: [channel]
Records obtained by: [method, from source register]

Short answer
[may / may with conditions / may not / unclear], because [the deciding rule]

Rules found
| Citation | Reaches | Burdens | What it requires | Verified |
|---|---|---|---|---|

Looked for and not found
- [rule type]: [where searched]

What the seller must do
- [customer term, exclusion, purge, registration]

What the buyer must do
- [waiting period, disclosure, licence, opt-out]

Open questions for the attorney
- [question]
```

## Rules for the answer

- "Not found" is not "allowed". Say which it is.
- A rule that burdens only the solicitor still matters to the seller: customer terms should require compliance, and marketing the list for a barred use invites liability.
- If the profile shows any eligibility use, stop and flag FCRA before answering.
- Add a row to `state-solicitation-map.md` only after the quote is verified.
