---
name: notice-received
description: >
  Handle a notice from a records custodian: a cease-and-desist letter, an email
  from a clerk, a block aimed at the business, new terms that forbid what it is
  doing, or a phone call asking it to stop. Use when the user says "we got a
  letter", "they blocked us", "the clerk emailed", "the site changed its terms",
  "cease and desist", or when collection from a source starts failing in a way
  that looks deliberate.
argument-hint: "[file | pasted notice | description of what happened]"
---

# /notice-received

1. Load `~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md` for the notice protocol. If the profile is missing, proceed anyway with the defaults below; this skill does not wait for setup.
2. Decide whether this is a notice (below). When unsure, treat it as one.
3. Walk the same-day steps.
4. Draft the internal record and, only if the attorney asks, a reply.

```
/public-records-legal:notice-received letter-from-clerk.pdf
```

---

# Notice Received

## Is it a notice?

Yes, if the custodian or its vendor has communicated that this business should stop or change its access: a letter, an email, a call, a block returned only to this business's addresses or account, an account suspension, or a terms change that names the activity. A generic bot challenge that every visitor gets is not by itself a notice. A challenge that appeared for this business right after heavy use might be; record it and ask the attorney.

## Same day

1. **Stop collecting from that source.** All jobs, all environments, all accounts. Confirm it stopped; do not assume.
2. **Do not route around it.** No new addresses, proxies, accounts, user agents or slower schedules. The cases that went worst for collectors turn on continuing by technical means after being told to stop (`references/collection-law-primer.md`, "The fact pattern that loses").
3. **Preserve.** Keep the notice with headers or envelope, the terms as they stood before and after, request logs for the source, and the source register entry. Suspend any routine deletion that would touch them.
4. **Do not reply yet.** No apology, no argument, no admission, no promise beyond what has been done. A reply is the attorney's call.
5. **Tell the people named in the profile's notice protocol**, and the attorney.
6. **Scope it.** Does the notice cover one portal, every portal of that custodian, or a vendor platform shared by many custodians? Stop everything it plausibly covers until the attorney narrows it.

## Within a few days, with the attorney

- What does the notice demand: stop, delete, account for past use, pay?
- Data already collected: the notice may demand deletion. Do not delete or keep delivering on your own judgment; this is a legal decision with preservation duties on one side and the demand on the other.
- Customers: does anything need to change in what they receive?
- Is there a sanctioned route to the same records? Run `/public-records-legal:bulk-agreement-review` on it.
- Do other sources share the same terms or vendor, so the same risk?

## Restart

Only on the written say-so of the person named in the profile, after the attorney has reviewed, and only by a route the custodian has agreed to. Never because the block lifted.

## Internal record

```
PRIVILEGED AND CONFIDENTIAL: PREPARED FOR COUNSEL
Source: [name]                  Custodian: [who]
Notice received: [date, time, channel, from whom]
What it says: "[quote the demand]"
Scope: [this portal / all custodian systems / vendor platform]

Actions taken
- Collection stopped: [when, by whom, how confirmed]
- Preserved: [list]
- Notified: [who, when]

Collection history for this source
- Started: [date]   Method: [method]   Tier at last review: [n]
- Terms on file dated: [date]

Not done, awaiting counsel
- Reply
- Decision on data already held
- Customer communication
```

The privilege label only helps if the record is in fact prepared for and sent to a lawyer. If the user has no lawyer, say that this is the moment to get one, and drop the label.
