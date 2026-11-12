---
name: cold-start-interview
description: >
  Run the setup interview for the public records plugin and write the practice
  profile: what records you collect, how, who buys them, your collection risk
  posture and your notice protocol. Use on first run, when CLAUDE.md is missing
  or has placeholders, or when the user says "set up the public records plugin",
  "onboard me", or wants to redo the interview.
argument-hint: "[--redo to re-run]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/claude-for-legal/public-records-legal/CLAUDE.md`. If populated and no `--redo`, confirm before overwriting.
2. Read `~/.claude/plugins/config/claude-for-legal/company-profile.md` if it exists. Do not re-ask what it answers. If it is missing, ask the company-level questions (name, what the business does, where it operates, practice setting) and create it.
3. Run the interview below, a few questions at a time.
4. Write the profile to the config path using the structure of this plugin's `CLAUDE.md` template. Leave no `[PLACEHOLDER]` markers; write "not decided" where the user has no answer, and list those at the end as open decisions.
5. Show a summary and offer a first task.

```
/public-records-legal:cold-start-interview
```

---

# Cold-Start Interview: Public Records

## Purpose

The other skills answer "may we" questions. The answer depends on facts and on risk appetite that only the user has. This interview captures both once.

## Seed documents

Ask for whichever exist, and read them before asking questions they answer:

- Customer terms of service or data license
- Any bulk data or subscriber agreement already signed
- Any letter, email or block notice received from a records custodian
- The list of sources collected from today

## Questions

**Records and product**
1. Which record types do you collect, and from which states and counties?
2. What do you deliver, and who buys it? What do buyers do with it: mail, calls, texts, door knocks, research?
3. Do you append anything to the record: mailing address, phone, email, property data? From which vendors?
4. Is any of it sold or used for credit, tenant screening, employment or insurance decisions? If yes, say plainly that FCRA changes the whole analysis and flag it for the attorney before continuing.

**Collection posture**
5. For each method in the profile table (plain requests, captcha, proxies, accounts with terms, bulk agreements, records requests): allowed, allowed with conditions, or never?
6. What are the hard stops?
7. How fast do you collect and how do you identify yourself?

**Notices**
8. Has any custodian ever told you to stop, blocked you, or changed its terms after you started? Capture each one: who, when, what you did.
9. Who decides when a source is stopped, and who may restart it?

**Use and resale**
10. What do your customer terms forbid?
11. Whom do you exclude at ingestion?
12. If a record is sealed or corrected after delivery, what happens?
13. How does a person ask to be removed, and is it honored across all products?
14. Are you registered as a data broker anywhere?

**Role**
15. Are you a lawyer? If not, do you have one to review output?

## After writing

List the open decisions. Point out any answer that conflicts with `references/collection-law-primer.md` tier 4 or 5 (collecting where a rule bans it, or continuing after a notice) as the first item for the attorney.
