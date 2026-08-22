---
description: Search Robert Half Technology (Canada, Contract listings) via plain WebFetch — no Chrome workaround needed, no eligibility gate needed (Canada/tech-scoped by construction) — then quick-score every result in a table, no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-roberthalf.md` / `plans/check-roberthalf.md`. Follow these steps in
order.

This command uses **plain `WebFetch` only** — Robert Half Technology is the one staffing-agency
source in this repo confirmed fetchable directly, no Claude in Chrome workaround needed
(confirmed 2026-08-20).

## 1. Parse input

`$ARGUMENTS` is optional.

- Non-empty → single custom query, run steps 2–3 once for it.
- Empty → run step 2 once per keyword in the default rotation below, then dedupe (step 3).

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

## 2. Search Robert Half (per keyword)

`WebFetch`:
```
https://www.roberthalf.com/ca/en/jobs?jobType=CONTRACT&specialty=TECHNOLOGY&keywords=<keyword, spaces as +>
```

Confirmed during testing: this returns clean, real, Canada-scoped **Contract** tech postings
directly (e.g. $123.50-$143/hr Senior Director Engineering, Toronto; $35-$45/hr Software Engineer
II, Mississauga). Extract title, location, job type, pay rate, and each posting's individual URL
from the fetched content.

**Always keep `jobType=CONTRACT&specialty=TECHNOLOGY` on every request** — dropping `jobType=`
would pull in Permanent/FTE listings against the consulting-engagement preference; only broaden
this if the user explicitly asks.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results, skip it and move to the next keyword. If every keyword
(or the single custom query) comes back empty, tell the user and stop.

## 3. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 4. Read profile.md

Read `profile.md` in full before scoring anything.

## 5. No eligibility gate

The `ca.` region path plus `specialty=TECHNOLOGY` filter keep results Canada/tech-scoped by
construction — no gate needed.

## 6. Fetch each candidate posting's individual page

`WebFetch` each posting's own URL. Extract full description, confirm pay rate and job type match
what was shown on the results page.

## 7. Quick-score each posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. **Robert Half is a general staffing firm** — expect some non-DevOps noise even
within `specialty=TECHNOLOGY` (SAP, plain developer, QA roles); skim titles before full-fetching
each one, same discipline as `/check-indeed`. One sentence rationale per posting.

## 8. Present one results table

Sort highest score first:

| Role — Company | Score | Rate | Why | Flags |
|---|---|---|---|---|

No files are written at this step.

## 9. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 6 — don't re-fetch.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.
