---
name: collection-method-review
description: >
  Review whether and how a public records portal may be collected from. Reads the
  portal's terms, access rules and technical gates, sorts the source into a risk
  tier, and recommends a method: collect, ask for bulk access, file a records
  request, or skip. Use when the user says "can we scrape this", "is this portal
  okay", "review this county site", "what do the terms say", or adds a new source.
argument-hint: "[portal URL | pasted terms | source name]"
---

# /collection-method-review

1. Load `~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md`. If placeholders, stop and prompt setup.
2. Read `references/collection-law-primer.md`. Check its date; if older than 90 days, say so.
3. Gather the facts below from the source itself. Quote, do not paraphrase.
4. Sort into a tier, compare with the profile's collection posture, and recommend.
5. Write the memo. Offer to add the entry to the source register.

```
/public-records-legal:collection-method-review https://example-county-clerk.gov/search
```

---

# Collection Method Review

## Facts to gather

Record each with the URL and the date read. Save a copy of every terms page; terms change and the copy is the evidence.

| Fact | Where to look |
|---|---|
| Who the custodian is (court, clerk, county agency, vendor on their behalf) | Page footer, domain, about page |
| Whether a login, account or payment is needed | Try the search |
| Whether there is a click-through before results | The first search |
| Terms of use, disclaimer, acceptable use policy | Footer links, the click-through text, the account signup |
| Words on automation: robot, scrape, automated, bulk, harvest, script | Search the terms |
| Words on commercial use, resale, solicitation | Search the terms |
| A state court rule or administrative order on remote or bulk access | State judiciary site; see `references/primary-source-tools.md` |
| Technical gates: captcha, bot challenge, rate limits | Observe |
| `robots.txt` | Fetch it. It is not law, but ignoring a disallow is a bad fact |
| A sanctioned alternative: bulk program, API, subscriber tier, records request route | Clerk site, court administrative office |
| Any prior notice to this business from this custodian | The profile and the source register |

If a fact cannot be found, write "not found" and where you looked. Do not infer permission from silence.

## Tier

Apply the five tiers in the primer:

1. No gate, no assent
2. Technical friction only
3. Assent required and terms forbid automation or commercial use
4. Rule-based ban
5. Notice received

A source takes the highest tier any fact supports. A vendor-hosted portal takes the terms of both the vendor and the custodian.

## Recommendation

| Tier | Default recommendation |
|---|---|
| 1 | Collect, within the profile's rate and identification rules |
| 2 | Collect only if the profile allows that method; record the decision and who made it |
| 3 | Do not collect by automation. Pursue the sanctioned alternative; run `/public-records-legal:bulk-agreement-review` on what is offered |
| 4 | Do not collect. Sanctioned route or skip |
| 5 | Stopped. Run `/public-records-legal:notice-received` |

Where the profile is stricter than the default, the profile wins. Where it is looser, say so and flag it for the attorney.

Then answer the separate question: once obtained, may the records be used as the business intends? Point to `/public-records-legal:solicitation-use-check`. A tier 1 source can still feed an unlawful use.

## Memo format

```
DRAFT FOR ATTORNEY REVIEW
Source: [name, URL]            Custodian: [who]
Reviewed: [date]               Tier: [1-5]

Facts
- [fact]: "[quote]" ([URL], read [date])

Tier reasoning
[two or three sentences naming the fact that sets the tier]

Recommendation
[collect / collect with conditions / bulk / records request / skip]

Sanctioned alternative
[what exists, cost, how to apply, or "none found"]

Open questions for the attorney
- [question]

Citations not yet verified
- [citation]
```

Run `/public-records-legal:verify-citations` on any rule or case the memo relies on before it is treated as final.
