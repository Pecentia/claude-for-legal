<!--
CONFIGURATION LOCATION

User-specific configuration for this plugin lives at a version-independent path that survives plugin updates:

  ~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md

Rules for every skill in this plugin:
1. READ configuration from that path. Not from this file.
2. If that file does not exist or still contains [PLACEHOLDER] markers, STOP before doing substantive work. Say: "This plugin needs setup before it can give you useful output. Run /public-records-legal:cold-start-interview. Without it, outputs will be generic and may not match your risk posture." The only skills that run without setup are /public-records-legal:cold-start-interview and /public-records-legal:verify-citations.
3. The cold-start interview WRITES to that path, creating parent directories as needed.
4. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

**Shared company profile.** Company-level facts live in `~/.claude/plugins/config/claude-for-legal/company-profile.md`, shared by all plugins. Read it before this practice profile. If it does not exist, this plugin's setup creates it.
-->

# Public Records Practice Profile
*Written by the cold-start interview. If you see `[PLACEHOLDER]`, run `/public-records-legal:cold-start-interview`.*

---

## What we do with records

**Record types collected:** [PLACEHOLDER: probate / eviction / foreclosure / divorce or family / other civil / code violations and liens / other]
**Jurisdictions:** [PLACEHOLDER: states and counties]
**What we sell or deliver:** [PLACEHOLDER: lead lists / data feed / API / research reports]
**Who buys it and for what:** [PLACEHOLDER: buyer types and their use, for example direct mail to property owners]
**Appended data:** [PLACEHOLDER: none / mailing address / phone / email / property match, and the vendor for each]
**Eligibility uses (credit, tenant, employment, insurance):** [PLACEHOLDER: never sold for these / sold for these]. If sold for these, FCRA applies and this plugin's marketing-list analysis does not.

---

## Who is using this

**Role:** [PLACEHOLDER: Lawyer | Non-lawyer with attorney access | Non-lawyer without attorney access]
**Attorney contact:** [PLACEHOLDER: name, firm, or N/A]

---

## Collection posture

| Method | Allowed? | Conditions |
|---|---|---|
| Plain automated requests to pages with no gate and no assent | [PLACEHOLDER] | |
| Solving or avoiding a captcha | [PLACEHOLDER] | |
| Proxy or residential egress | [PLACEHOLDER] | |
| Accounts or click-through terms that forbid automation | [PLACEHOLDER] | |
| Bulk data agreement or subscriber access | [PLACEHOLDER] | |
| Public records request | [PLACEHOLDER] | |

**Hard stops (never, whatever the business case):** [PLACEHOLDER: for example a court rule banning automated access, any source after a notice]
**Rate limit and identification rules:** [PLACEHOLDER]

---

## Notice protocol

**What counts as a notice:** [PLACEHOLDER: letter, email, a block aimed at us, a terms change naming us, a call from a clerk]
**Who is told, and how fast:** [PLACEHOLDER]
**Who may restart a stopped source:** [PLACEHOLDER: name]. Never restart by technical means alone.

---

## Use and resale controls

**Customer terms forbid:** [PLACEHOLDER: eligibility uses, unlawful solicitation, resale]
**Excluded at ingestion:** [PLACEHOLDER: minors, wards and protected persons, sealed matters]
**Purge and correction path:** [PLACEHOLDER: how a sealed or corrected record is removed from data already delivered, and how fast]
**Suppression list:** [PLACEHOLDER: how a person asks to be removed]
**Data broker registrations held:** [PLACEHOLDER: states, or none and why]

---

## Source register

Where the per-jurisdiction record is kept: [PLACEHOLDER: path or system]. One entry per source: method, terms captured (date and copy), tier from `collection-method-review`, agreement if any, last review date.

---

## Output style

**Review memo destination:** [PLACEHOLDER: folder]
**Label on every output:** DRAFT FOR ATTORNEY REVIEW unless the user is the attorney.
