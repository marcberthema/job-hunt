---
description: Search S.i. Systems (Canada's largest IT staffing agency) via Claude in Chrome, no eligibility gate needed (Canada-only by construction), then quick-score every result in a table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-sisystems.md` / `plans/check-sisystems.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) instead of
`WebFetch`, because S.i. Systems returns a blocked/WAF page to direct fetches ("The requested URL
was rejected") but loads fine through a real browser session — confirmed 2026-08-20, no login
required.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

## 2. Open a tab

Call `tabs_context_mcp`, then `tabs_create_mcp` a new tab. No login check needed.

## 3. Parse input

`$ARGUMENTS` is optional.

- Non-empty → single custom query, run steps 4–5 once for it.
- Empty → run step 4 once per keyword in the default rotation below, then dedupe (step 5).

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

Bare titles, same rotation as the other `/check-*` commands.

## 4. Search S.i. Systems (per keyword)

`navigate` to:
```
https://www.sisystems.com/search-it-jobs/?expertise=3&q=<keyword, spaces as +>
```

`expertise=3` selects the "Networks and Infrastructure" specialization — confirmed during testing
as the closest category to DevOps/Cloud/SRE work (64 results at test time). **The site's own `?q=`
free-text param does NOT reliably filter by keyword** — a bare `?q=devops` search returned 151
results dominated by unrelated Business Analyst, QA, and Salesforce postings. Treat `q=` as a soft
narrowing signal on top of `expertise=3`, not a standalone filter.

Client-side rendered — after `navigate`, `wait` ~2 seconds before calling `get_page_text`, or
you'll get a "Loading..." placeholder instead of real results.

`get_page_text` returns clean data directly: title (often with a requisition ID suffix),
expertise category, job type (Contract/Permanent), location, and posted-date. It does **not**
include the job detail URL in the text output — use `find` on the posting's "DETAILS" link to get
a clickable element ref for step 8.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results, skip it and move to the next keyword. If every keyword
(or the single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring anything.

## 7. No eligibility gate

S.i. Systems is a Canadian IT staffing agency — every listing is Canada-scoped by construction,
same reasoning as `/check-eluta`. Skip straight to opening postings and scoring.

## 8. Open each candidate posting

Click the "DETAILS" element ref found via `find` in step 4 (or `navigate` directly if you already
have the URL — pattern `/jobs/<slug>/<encoded-id>/`). **`get_page_text` returns the full, correct
job description directly here** — confirmed during testing, no `find`+`read_page` workaround
needed. Extract title, company (often shown as "Our client" — normal for a staffing agency, not a
red flag), full description, pay rate (an explicit `$X-$Y/hr` for many Contract roles, or "Salary:
Negotiable" for many Permanent roles), job type, and location.

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **Posting fails to load** → mark "couldn't fetch," continue with the rest.
- **Never click Apply or any other write-side button** — read-only navigation and text
  extraction only, at every step of this command.

## 9. Quick-score each posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. **Job Type is a first-class signal here** — Contract roles align directly with the
consulting-engagement preference and should not be scored down for being agency-sourced;
Permanent roles should be flagged as FTE per the usual pattern but not auto-excluded given the
current lowered scoring bar. One sentence rationale per posting.

## 10. Present one results table

No eligible/ineligible split needed (no gate ran). Sort highest score first:

| Role — Company | Score | Job Type | Why | Flags |
|---|---|---|---|---|

No files are written at this step.

## 11. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 8 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the company is anonymized ("Our
  client"), use `sisystems` as the company slug unless the full posting reveals the real client
  name.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 12. Close the tab

Close the S.i. Systems tab at the end of the run — success, empty-result, or early-stop path
alike.
