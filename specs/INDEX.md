# Job Seeking — Specs Index

All automation stories for the job seeking pipeline.

**Status legend:** `pending` — not yet implemented · `done` — delivered

---

## How to add a story

Describe the capability you want in a Claude Code session. Claude will write the spec here and the
plan in `plans/`. No slash commands needed — just conversation.

---

## Pipeline Automation

| Story | Description | Status |
|-------|-------------|--------|
| _(none yet)_ | | |

---

## Job Flow Commands

| Story | Description | Status |
|-------|-------------|--------|
| [addjob](addjob.md) | Manual intake: `/addjob <url>` fetches, scores, and drafts a posting into `jobs/new/` | done |
| [check-indeed](check-indeed.md) | Bulk discovery: `/check-indeed <terms> [location]` searches Indeed, quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-dice](check-dice.md) | Bulk discovery: `/check-dice <terms> [location]` searches Dice, gates out clearance/US-work-authorization-only postings before scoring, then quick-scores the rest | done |
| [check-jobbank](check-jobbank.md) | Bulk discovery: `/check-jobbank [terms]` searches Job Bank (Canada), quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-builtin](check-builtin.md) | Bulk discovery: `/check-builtin [terms]` searches BuiltIn, quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
