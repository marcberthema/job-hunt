---
description: Search Glassdoor Canada via Claude in Chrome, flag likely duplicates against other sources (no eligibility gate needed, Canada-scoped by construction), then quick-score every result in a table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-glassdoor.md` / `plans/check-glassdoor.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools). Glassdoor
(`glassdoor.ca`) loads cleanly with no login wall to browse listings or full postings — sign-in is
only needed for reviews/salary-community content, which this command never touches.

**Known overlap with other sources**: initial testing (2026-08-20) found one Glassdoor result was
the exact same Deloitte posting already filed from Indeed, alongside several titles not seen
elsewhere (Cerebras, ZoomInfo, Teknion). Run this expecting partial overlap — it's still worth
running for the unique inventory.

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

## 4. Search Glassdoor (per keyword)

`navigate` to:
```
https://www.glassdoor.ca/Job/canada-<keyword-slug>-jobs-SRCH_IL.0,6_IN3_KO7,<N>.htm
```

`<keyword-slug>` is the keyword lowercased with spaces as hyphens (e.g. `devops-engineer`). `<N>`
is approximately the keyword's character count (spaces counted) — **the exact formula isn't fully
pinned down; confirmed during testing that `,20` worked and `,21` silently broke the search for
"devops engineer" (15 letters + 1 space = 16, so treat this as approximate, not exact)**.

**Always verify the result count before treating a query as exhausted.** The page title format is
`"<count> ... jobs in Canada, <month> <year> | Glassdoor"`. If `<count>` is 0, retry with `<N>`
adjusted ±1-2 before concluding the keyword has no matches.

**Alternative worth trying**: navigate to the Glassdoor Canada homepage and use the on-page
search box (type + submit) instead of constructing the URL directly — this may avoid the fragile
`KO7,<N>` encoding since the site builds the URL itself. If this proves more reliable in practice,
prefer it and note the finding in `job_sources.md`.

`get_page_text` returns the results list directly: title, company (with rating), location,
salary (employer-provided or Glassdoor-estimated), skill tags, and an Easy Apply flag.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results (after the retry above), skip it and move to the next
keyword. If every keyword (or the single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring anything.

## 7. No eligibility gate

The `canada-` URL prefix scopes results to Canada by construction. A "Remote" tag on an
individual posting could theoretically hide non-Canada bias (same caution as RemoteOK/WWR), but
this isn't confirmed as a widespread issue here — treat as a soft skim-the-body caution, not a
hard gate.

## 8. Open each candidate posting

Click the title link from the results list. Extract full description, salary, skill tags,
remote/hybrid/onsite, and company.

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **A "Sign in to see salary insights" or similar community-content prompt appears** → ignore it,
  the core job description remains readable without signing in. Never click Sign In.
- **Posting fails to load** → mark "couldn't fetch," continue with the rest.
- **Never click Apply or Easy Apply** — read-only navigation and text extraction only, at every
  step of this command.

## 9. Duplicate-aware check (before final scoring)

For each candidate, run:
```
grep -ril "<company>" jobs/new/ jobs/applied/ jobs/rejected/
```
(and a title-based grep if the company grep is ambiguous). If a match is found, note it as a
likely duplicate with the matched file's path in the results table — **don't silently exclude
it**. The overlap itself is useful confirmation, not noise to filter out.

## 10. Quick-score each posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. One sentence rationale per posting.

## 11. Present one results table

Sort highest score first:

| Role — Company | Score | Salary | Why | Possible Duplicate |
|---|---|---|---|---|

No files are written at this step.

## 12. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment — **skip
re-offering any posting already flagged as a duplicate in step 9**. For non-duplicate picks:

- Run the duplicate check again as a final safety net: `grep -ril "<company/role>" jobs/new/
  jobs/applied/ jobs/rejected/`.
- Reuse the posting content already fetched in step 8 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 13. Close the tab

Close the Glassdoor tab at the end of the run — success, empty-result, or early-stop path alike.
