# Job Sources

Every job board/site evaluated for this search, whether it's automatable, and when it was last
checked. Ask "give me a status" any morning and Claude will read this file and tell you which
source is oldest (highest priority to check next).

**How to read `Last Checked`:** the date of the most recent `/check-*` run (or manual check) for
that source. Sources with no skill are checked manually — update the date yourself, or ask
Claude to do it after you've pasted results from a manual visit.

**Maintenance note for Claude:** after running any `/check-*` command, update that row's
`Last Checked` date to today. If a source's access method changes (starts/stops working, gets a
new skill), update the row rather than adding a duplicate.

---

## Working — automated via skill

| Site | Description | How to Check | Last Checked | Notes |
|---|---|---|---|---|
| Indeed (ca.indeed.com) | General job board, largest volume of results, good Canada/remote coverage | `/check-indeed [terms]` | 2026-07-21 | Best signal-to-noise of the three working sources; free-text search. Default-rotation runs return a lot of keyword-mismatched noise (civil engineer, embedded firmware, sales "solutions engineer" roles, etc.) alongside real hits — worth a quick title skim before full-fetching each one. Watch for explicit provincial/regional residency requirements (e.g. "must reside in Quebec/Alberta") buried in posting body text, not just the location field — now a hard-gate red flag in `profile.md` |
| Dice | Tech-specific job board, strong on contract/DevOps roles, US-market-heavy | `/check-dice [terms]` | 2026-07-21 | Gates out clearance/US-work-authorization-only postings before scoring — most US contract postings are ineligible for a Canadian-incorporated consultant. Link stability varies by run — some `job-detail` IDs return "Job Not Found". 2026-07-21 default-rotation run: `location=Remote&countryCode2=CA` returned mostly on-site/hybrid US staffing-agency noise — 22/34 postings gated out, remaining 12 eligible ones scored 1-4 (low rate, no Azure fit) — worth revisiting the location param per the note above |
| Job Bank (jobbank.gc.ca) | Government of Canada's official job board, aggregates from Indeed and other sources | `/check-jobbank [terms]` | 2026-07-21 | Lower signal — uses NOC occupation-code matching, not free-text search, so keyword rotation produces noisy/irrelevant results (e.g. "DevOps Engineer" surfaced RF Engineer, HVAC Design roles). Only "DevOps Engineer," "Cloud Engineer," and "Site Reliability Engineer" keywords return clean results; skip "Platform Engineer" and "Forward Deployed Engineer" here. 2026-07-21 run: "DevSecOps Engineer" also returned a single unrelated match (Engineer in Agronomy) — add to the skip list too. Two results were outright mislabeled (Regulatory Compliance Engineer, Cabinetry Engineer tagged as "DevOps Engineer") — worth a sanity check on titles before scoring. Watch for explicit provincial/regional residency requirements per the new hard-gate rule in `profile.md` |
| BuiltIn | Tech-company-direct job board, has a Toronto/Canada section | `/check-builtin [terms]` | 2026-07-14 | Requires both the `/jobs/remote/dev-ops` base path AND a `?search=` query param — either alone gives noisy or empty results. Clean, relevant results once combined |

## Not usable — blocked or broken

| Site | Description | Why it doesn't work | Last Checked |
|---|---|---|---|
| LinkedIn | Largest professional network, most recruiter activity | Sits behind an auth wall — WebFetch cannot retrieve postings. Paste the posting text directly and use `/addjob` instead | 2026-07-07 |
| We Work Remotely | Curated remote-only job board | HTTP 403 Forbidden — active bot-blocking | 2026-07-07 |
| RemoteOK | Remote-only job board | HTTP 403 Forbidden — active bot-blocking | 2026-07-07 |
| Braintrust | Contractor-owned freelance network | Job listings are client-side rendered (JavaScript) — WebFetch only sees an empty page shell | 2026-07-08 |
| Toptal | Vetted freelance/contract network, skews senior | Job/opportunity listings appear to sit behind a login-gated dashboard — no working public search URL found yet | 2026-07-08 |
| Eluta.ca | Canadian-focused job aggregator, pulls from employer career pages | Search results are visible (titles/companies/salary) but individual job links are JavaScript-generated fragments (`#!`) with no real URL — can't drill into postings; re-tested 2026-07-14, still broken (page returned a "Query Error" that run) | 2026-07-14 |

## Manual only — no skill, worth checking by hand periodically

| Site | Description | How to Check | Last Checked |
|---|---|---|---|
| LinkedIn | See above | Browse manually, paste posting text into `/addjob` | 2026-07-07 |

---

## Weekly manual-check list

These sites block automated fetches but are fine for a human to browse directly. Recommended
cadence: **once a week**, browse each and paste anything promising for `/addjob` to score. This
`Last Checked` column tracks when Marc himself last browsed the site (separate from the
automation-feasibility test dates in the tables above) — update it whenever you check one.

| Site | Why manual | What to do | Last Checked |
|---|---|---|---|
| LinkedIn | Auth wall — no automated access at all | Browse jobs/recruiter messages; paste promising postings' text | 2026-07-07 |
| We Work Remotely | Blocks automated fetches (403), site itself is fine for humans | Browse the DevOps/Sysadmin category; paste postings found | 2026-07-07 |
| RemoteOK | Same — bot-blocked, human-browsable | Browse remote DevOps/SRE listings; paste postings found | 2026-07-07 |
| Braintrust | Listings are JavaScript-rendered, invisible to automated fetch | Browse logged-in or out; paste postings found | 2026-07-07 |
| Eluta.ca | Search results visible but individual postings can't be clicked through by automation | Click through manually — worth a quick scan; paste anything relevant | 2026-07-14 |

**Not weekly — different cadence:** Toptal is an apply-once vetting network, not a browsable job
board — worth applying to join if not already done, but not a recurring check.

## Adding a new source

When a new site is worth checking:
1. Test whether its search-results page and individual postings are fetchable via WebFetch.
2. If both work cleanly, consider building a dedicated `/check-<site>` skill (see
   `specs/check-indeed.md` as the reference pattern) and move it to the "Working" table.
3. If it's blocked, client-rendered, or has broken links, log it in "Not usable" with the
   specific failure reason — this saves re-testing it later.
4. If it's fetchable but not worth automating yet (low volume, awkward URL structure), log it in
   "Manual only."
