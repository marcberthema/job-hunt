# Plan: `/check-eluta` — Eluta.ca Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-eluta.md`.

## Deliverable

`.claude/commands/check-eluta.md` — a slash command definition, simpler than the other
Chrome-driven sources in one respect (no eligibility gate needed — Eluta is Canada-only by
construction) but with a unique mechanic: individual postings are read via Eluta's own cached
copy, opened in a new tab per result, not the live posting page.

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, create a new tab. No login check needed.

3. **Parse input** — `$ARGUMENTS` optional.

   ### Default role rotation
   ```
   DevOps Engineer
   Platform Engineer
   Site Reliability Engineer
   Cloud Engineer
   DevSecOps Engineer
   Forward Deployed Engineer
   ```
   Same rotation list as the other `/check-*` commands.

4. **Search per keyword** — `navigate` to:
   ```
   https://www.eluta.ca/search?q=<keyword, spaces as +>&filter-remote_jobs=only
   ```
   **Do not add a location parameter.** Confirmed during testing: `l=Canada` breaks the search
   entirely ("The location you entered does not exist in our database"). Results are already
   Canada-scoped by the site's own nature (aggregates Canadian employer career pages).

   **Always include `filter-remote_jobs=only`** — confirmed during a full live run (2026-08-20)
   that this is a real, working filter (discovered via the site's own "Remote" dropdown, which
   offers "Remote" and "On-Site" options) that narrows a noisy 1,700+-result unfiltered search
   down to a focused, still-substantial remote-only set (191 for "devops engineer") — a clear
   improvement over scoring on-site postings that would fail the reachable-range check in step 8
   anyway.

   `get_page_text` returns clean, complete listing data directly: title, company, city/province
   (or "Work Remotely"), salary if shown, snippet, posted-time. Cap at the first page (10 results)
   per keyword in rotation mode, same cap for a single custom query. Page 2+ is out of scope.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **Open each posting via its cached copy, not the direct title link**:
   - Confirmed during testing: the job title link (`href="#!"`) does **not** reliably fire on a
     synthetic click — clicking it produced no navigation and no new tab.
   - Instead, use `find` with a query like "cached page link for `<job title>` at `<company>`"
     (or "See how this page looked when Eluta indexed it" near that result) to locate the correct
     link, then click it via its `ref`.
   - This opens a **new browser tab** at `https://www.eluta.ca/cache?u=<id>:<domain>`. Call
     `tabs_context_mcp` immediately after the click to discover the new tab's ID (it won't be
     returned automatically the way `navigate` results are).
   - `get_page_text` on that new tab returns the full, clean posting content directly — no
     lazy-load or wrong-`<article>` issues observed during testing.
   - **Close the cache tab** once its content is extracted, before moving to the next posting —
     don't let tabs accumulate across the run.
   - If the cache link fails to open a tab, or the new tab errors/loads empty: mark "couldn't
     fetch," close whatever opened, continue with the rest.
   - **Not every result has a cache link** — confirmed during the 2026-08-20 live run that
     results from roughly the 5th position onward in a list commonly have no "See how this page
     looked..." link at all (only "Email"). When absent, don't force it — score from the
     search-results snippet alone and flag "full posting not fetchable, scored from listing
     summary" in the report.
   - **Some cache pages refuse to render** ("This cached document can not be displayed directly,"
     seen specifically for Workday-hosted postings). Fallback: navigate to
     `https://www.eluta.ca/cache_open?u=<same id>:<same domain>` instead of `cache?u=...` — this
     returns the raw underlying data (confirmed: a full JSON payload including the job
     description field for a Workday case) even when the pretty view fails. Extract from that.

8. **Score each posting 0–10**, skill/domain-first, same philosophy as the other `/check-*`
   commands. **No eligibility gate runs here** (see spec) — instead, apply `profile.md`'s normal
   on-site/hybrid reachable-range check as part of scoring, same as Indeed/BuiltIn results.

9. **Present a sorted table** (highest score first). No files written at this step.

10. **Offer to go deeper** — same pattern as the other commands: duplicate check via
    `grep -ril`, reuse content already fetched in step 7, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

11. **Close the main search tab** at the end of the run (cache tabs should already be closed per
    step 7).

## Testing

Manual (no automated test suite in this repo):

- Run `/check-eluta devops engineer` — confirm the search page loads without a location-param
  error, the cache-link mechanism reliably opens readable content for multiple postings in a row,
  and cache tabs get closed rather than accumulating.
- Confirm clicking the direct job-title link is never attempted (only the cache link).
- Confirm no "APPLY FOR THIS JOB" or "Email" link is ever clicked during a run.

## Out of Scope

Same as spec: pagination past page 1, an eligibility gate, auto-filing without confirmation.
