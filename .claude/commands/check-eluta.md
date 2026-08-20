---
description: Search Eluta.ca via Claude in Chrome, open each posting's cached copy (works around JS-fragment links), then quick-score every result — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-eluta.md` / `plans/check-eluta.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) because Eluta.ca's
job title links are JavaScript fragments (`href="#!"`) with no real URL — `WebFetch` can't drill
into individual postings. Chrome can click through them via a different mechanism (see step 7).
**No login required.** Eluta aggregates Canadian employer career pages, so results are Canada-only
by construction — **this command has no eligibility gate**, unlike the international sources.

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

Same rotation list as `/check-indeed`, `/check-dice`, `/check-jobbank`, `/check-builtin`,
`/check-wwr`, `/check-remoteok`, `/check-braintrust`.

## 4. Search Eluta.ca (per keyword)

`navigate` to:
```
https://www.eluta.ca/search?q=<keyword, spaces as +>&filter-remote_jobs=only
```

**Do not add a location parameter.** Confirmed during testing: `l=Canada` breaks the search
entirely ("The location you entered does not exist in our database"). Leave location blank —
results are already Canada-scoped since Eluta aggregates Canadian employer career pages.

**Always include `filter-remote_jobs=only`** — confirmed during a full live run (2026-08-20) this
is a real, working filter (found via the site's own "Remote" dropdown) that narrows a noisy
1,700+-result unfiltered search down to a focused, still-substantial remote-only set (191 for
"devops engineer") — a clear win, since on-site results would mostly fail the reachable-range
check in step 8 anyway.

`get_page_text` returns clean, complete listing data directly: title, company, city/province (or
"Work Remotely"), salary if shown, snippet, posted-time. Cap at the first page (10 results) per
keyword in rotation mode, same cap for a single custom query. Page 2+ is out of scope.

If a keyword returns no results, skip it and move to the next keyword. If every keyword (or the
single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring anything.

## 7. Open each posting via its CACHED copy — not the direct title link

**The job title link (`href="#!"`) does not reliably fire on a synthetic click** — confirmed
during testing that clicking it directly produces no navigation and no new tab. Use this
mechanism instead, for every posting:

1. Call `find` with a query like `"cached page link for <job title> at <company>"` or `"See how
   this page looked when Eluta indexed it"` near that specific result — each result has its own
   such link.
2. Click that link via its `ref`. This opens a **new browser tab** at
   `https://www.eluta.ca/cache?u=<id>:<domain>` — Eluta's own cached copy of the full posting.
3. Call `tabs_context_mcp` immediately after the click to discover the new tab's ID (it isn't
   returned automatically the way a `navigate` result is).
4. `get_page_text` on that new tab — confirmed during testing this returns the full, clean
   posting content directly (title, location, full description, "APPLY FOR THIS JOB" boundary
   marker), no lazy-load or wrong-content issues.
5. **Close that cache tab** once you've extracted its content, before moving to the next
   posting — don't let tabs pile up across the run.

- **Cache link fails to open a tab, or the new tab errors/loads empty** → mark "couldn't fetch,"
  close whatever opened, continue with the rest.
- **Not every result has a cache link** — confirmed results from roughly the 5th position onward
  in a list commonly have no "See how this page looked..." link at all (only "Email"). When
  absent, don't force it — score from the search-results snippet alone and flag "full posting not
  fetchable, scored from listing summary" in the report.
- **Some cache pages refuse to render** ("This cached document can not be displayed directly,"
  seen for Workday-hosted postings specifically) → navigate to
  `https://www.eluta.ca/cache_open?u=<same id>:<same domain>` instead of `cache?u=...` — this
  returns the raw underlying data (confirmed: a full JSON payload including the job description
  field for a Workday case) even when the pretty view fails. Extract from that instead.
- **reCAPTCHA or a blocking page appears** → stop the entire run immediately, tell the user
  exactly what happened, do not attempt to solve it.
- **Never click "APPLY FOR THIS JOB" or the "Email" link** — read-only extraction only, at every
  step of this command.

## 8. Quick-score each posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. **There is no eligibility gate on this source** (see header) — instead, apply
`profile.md`'s on-site/hybrid reachable-range check as part of normal scoring, exactly as you
would for an Indeed or BuiltIn result. One sentence rationale per posting.

## 9. Present the table

Sorted highest score first:

| Role — Company | Score | Why | Flags |
|---|---|---|---|

No files are written at this step.

## 10. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 7 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 11. Close the tab

Close the main Eluta search tab at the end of the run — cache tabs should already be closed per
step 7. Success, empty-result, or early-stop path alike.
