---
description: Search Indeed, fetch every result, and produce a quick-score table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-indeed.md` / `plans/check-indeed.md`. Follow these steps in order.

## 1. Parse input

`$ARGUMENTS` is optional. Location is always `Remote` — not a user-supplied argument.

- If `$ARGUMENTS` is non-empty, treat it as a single search-terms query and run steps 2-6 once
  for it, same as before.
- If `$ARGUMENTS` is empty, run steps 2-4 once per keyword in the **default role rotation**
  below, then dedupe and continue to step 5 onward with the combined set.

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

This list represents Marc's core title (DevOps Engineer) plus the closest-adjacent titles his
actual work also matches (platform engineering, SRE, cloud engineering, DevSecOps/compliance
work, and forward-deployed/customer-facing engineering). Update this list directly in this file
if Marc's positioning changes — no need to touch the spec/plan for a wording tweak.

## 2. Search Indeed (per keyword)

For each keyword being searched this run, build
`https://ca.indeed.com/jobs?q=<keyword, spaces as +>&l=Remote` and fetch it with WebFetch, asking
explicitly for every markdown hyperlink pointing at a job posting (URLs containing `pagead/clk`,
`/viewjob?jk=`, or `/rc/clk`), each with its title and company, output as raw links — not
summarized away.

- **Single custom query** (arguments given): cap at the first 15 job links.
- **Default rotation** (no arguments): cap at the first **8** job links per keyword, to keep the
  total batch size reasonable across 6 keywords.

If a keyword's search returns no job links, skip it and move to the next keyword — don't abort
the whole rotation over one empty search. If every keyword in the rotation comes back empty (or
the single custom query does), tell the user and suggest a different query or `/addjob <url>`
with a direct posting link instead. Stop.

## 3. Dedupe (rotation mode only)

Postings often show up under more than one keyword (e.g. a "Platform Engineer" posting also
surfaces under "DevOps Engineer"). Before fetching full details, dedupe the combined link list by
company + title (case-insensitive, ignore minor punctuation differences) so each unique posting
is only fetched and scored once, even if it matched multiple keywords.

## 4. Read profile.md

Read `profile.md` in full before scoring anything — same hard requirement as `/addjob`.

## 5. Fetch each posting

WebFetch each deduped job link individually, extracting: title, company, location,
remote/hybrid/onsite status, salary/rate if stated, engagement type, and enough of the
responsibilities/requirements to score. If one fails to fetch, mark it "couldn't fetch" in the
table below rather than dropping it or aborting the batch.

## 6. Quick-score each (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (on-site, below-target pay) don't drag the score down — flag them
instead. Keep the rationale to **one sentence** per posting — this is a scan, not the full
`/addjob` writeup.

## 7. Present the table

Sorted highest score first. In rotation mode, note which keyword(s) surfaced each posting isn't
necessary in the table itself — the dedupe in step 3 already collapsed that — but mention in the
intro line how many keywords were searched and how many unique postings came back.

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
- Report back: score, one-line summary, flags, and the file path — same as `/addjob`.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.
