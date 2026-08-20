---
description: Search Job Bank (Canada), fetch every result, and produce a quick-score table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-jobbank.md` / `plans/check-jobbank.md`. Follow these steps in order.

## 1. Parse input

`$ARGUMENTS` is optional.

- If non-empty, treat it as a single search-terms query and run steps 2-6 once for it.
- If empty, run steps 2-4 once per keyword in the **default role rotation** below, then dedupe
  and continue to step 5 onward with the combined set.

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

Same rotation as `/check-indeed` and `/check-dice` — keep all three files' lists in sync if
Marc's positioning changes.

## 2. Search Job Bank (per keyword)

For each keyword being searched this run, build:
```
https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=<keyword, spaces as +>&locationstring=Remote
```
Fetch with WebFetch, asking for every `/jobsearch/jobposting/<id>` link with title, company,
location, and salary as shown on the results page.

- **Single custom query** (arguments given): cap at the first 15 job links.
- **Default rotation** (no arguments): cap at the first **8** job links per keyword.

Note: Job Bank's `locationstring` filter doesn't reliably restrict to remote-only postings — it
commonly returns a mix of on-site, hybrid, and remote roles. That's expected; on-site/hybrid
status gets flagged during scoring (step 6), not filtered out here.

If a keyword's search returns no job links, skip it and move to the next keyword. If every
keyword (or the single custom query) comes back empty, tell the user and stop.

## 3. Dedupe (rotation mode only)

Collapse the combined link list by company + title (case-insensitive) before fetching full
details, so each unique posting is only fetched and scored once.

## 4. Read profile.md

Read `profile.md` in full before scoring anything.

## 5. Fetch each posting

WebFetch each deduped job link individually, extracting: title, company, location,
remote/hybrid/onsite status, salary/rate, engagement type, and enough of the
responsibilities/requirements to score. If one fails to fetch, mark it "couldn't fetch" rather
than dropping it or aborting the batch.

## 6. Quick-score each (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (on-site, below-target pay) don't drag the score down — flag them
instead. One sentence rationale per posting.

## 7. Present the table

Sorted highest score first:

| Role — Company | Score | Why | Flags |
|---|---|---|---|

No files are written at this step. Note in the intro: Job Bank aggregates from multiple sources
including Indeed, so some overlap with `/check-indeed` results is expected — that's fine, the
duplicate check at filing time (step 8) catches it.

## 8. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 5 — don't re-fetch.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.
