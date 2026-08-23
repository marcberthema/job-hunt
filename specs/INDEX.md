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
| [review](review.md) | Backlog review: `/review` walks `jobs/new/` one posting at a time (highest score first), shows a detailed view with pay/days-in-office/contract-type highlighted, and rejects/skips or helps apply (cover letter + application questions) before moving the file to `jobs/applied/` on confirmed submission | done |
| [check-indeed](check-indeed.md) | Bulk discovery: `/check-indeed <terms> [location]` searches Indeed, quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-dice](check-dice.md) | Bulk discovery: `/check-dice <terms> [location]` searches Dice, gates out clearance/US-work-authorization-only postings before scoring, then quick-scores the rest | done |
| [check-jobbank](check-jobbank.md) | Bulk discovery: `/check-jobbank [terms]` searches Job Bank (Canada), quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-builtin](check-builtin.md) | Bulk discovery: `/check-builtin [terms]` searches BuiltIn, quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-linkedin](check-linkedin.md) | Bulk discovery: `/check-linkedin [terms]` searches LinkedIn Jobs via Claude in Chrome (auth-wall workaround), quick-scores every result in a table, then offers the full `/addjob` treatment for picks | done |
| [check-wwr](check-wwr.md) | Bulk discovery: `/check-wwr [terms]` searches We Work Remotely via Claude in Chrome (bot-block workaround), gates out region-ineligible postings before scoring, then offers the full `/addjob` treatment for picks | done |
| [check-remoteok](check-remoteok.md) | Bulk discovery: `/check-remoteok [terms]` searches RemoteOK via Claude in Chrome (bot-block workaround), gates out region-ineligible postings before scoring using its reliable flag-emoji tags, then offers the full `/addjob` treatment for picks | done |
| [check-braintrust](check-braintrust.md) | Bulk discovery: `/check-braintrust [terms]` searches Braintrust via Claude in Chrome (client-side-rendering workaround, no login needed), gates out region-ineligible postings before scoring, then offers the full `/addjob` treatment for picks | done |
| [check-eluta](check-eluta.md) | Bulk discovery: `/check-eluta [terms]` searches Eluta.ca via Claude in Chrome, opens each posting's cached copy to work around JS-fragment links, no eligibility gate needed (Canada-only by construction), then offers the full `/addjob` treatment for picks | done |
| [check-sisystems](check-sisystems.md) | Bulk discovery: `/check-sisystems [terms]` searches S.i. Systems (Canada's largest IT staffing agency) via Claude in Chrome (WAF-block workaround), no eligibility gate needed (Canada-only by construction), then offers the full `/addjob` treatment for picks | done |
| [check-procom](check-procom.md) | Bulk discovery: `/check-procom [terms]` searches Procom's real jobs portal (`myprocom-portal.procomservices.com`) via Claude in Chrome, gates out US-only postings before scoring, then offers the full `/addjob` treatment for picks | done |
| [check-randstad](check-randstad.md) | Bulk discovery: `/check-randstad [terms]` browses Randstad Canada's Technologies category via Claude in Chrome (site-side keyword search is broken, so it filters client-side), no eligibility gate needed (Canada-only by construction), then offers the full `/addjob` treatment for picks | done |
| [check-roberthalf](check-roberthalf.md) | Bulk discovery: `/check-roberthalf [terms]` searches Robert Half Technology (Canada, Contract listings) via plain WebFetch — no Chrome workaround needed — no eligibility gate needed, then offers the full `/addjob` treatment for picks | done |
| [check-glassdoor](check-glassdoor.md) | Bulk discovery: `/check-glassdoor [terms]` searches Glassdoor Canada via Claude in Chrome, flags likely duplicates against other sources instead of gating eligibility, then offers the full `/addjob` treatment for picks | done |
