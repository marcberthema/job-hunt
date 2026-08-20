---
description: Search BuiltIn, fetch every result, and produce a quick-score table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-builtin.md` / `plans/check-builtin.md`. Follow these steps in order.

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

Same rotation as `/check-indeed`, `/check-dice`, and `/check-jobbank` — keep all four files'
lists in sync if Marc's positioning changes.

## 2. Search BuiltIn (per keyword)

For each keyword being searched this run, build:
```
https://builtin.com/jobs/remote/dev-ops?search=<keyword, spaces as +>
```
Fetch with WebFetch, asking for every `/job/<slug>/<id>` link with title, company, location, and
remote status as shown on the results page.

- **Single custom query** (arguments given): cap at the first 15 job links.
- **Default rotation** (no arguments): cap at the first **8** job links per keyword.

Note: both the base path (`/jobs/remote/dev-ops`) AND the `?search=` query param are required.
The bare job-function URL without a search param returns noisy, largely irrelevant results
(sales, tax, insurance roles mixed in) — this was confirmed during testing.

If a keyword's search returns no job links, skip it and move to the next keyword. If every
keyword (or the single custom query) comes back empty, tell the user and stop.

## 3. Dedupe (rotation mode only)

Collapse the combined link list by company + **exact** title (not fuzzy matching) before
fetching full details. BuiltIn commonly lists genuinely distinct postings at the same company
with similar-sounding titles (e.g. "DevOps Engineer Backend" vs. "DevOps Engineer Mobile" at the
same company) — an aggressive fuzzy dedup would wrongly collapse these into one.

## 4. Read profile.md

Read `profile.md` in full before scoring anything.

## 5. Fetch each posting

WebFetch each deduped job link individually, extracting: title, company, location,
remote/hybrid/onsite status, salary/rate if stated, engagement type, and enough of the
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

No files are written at this step.

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
