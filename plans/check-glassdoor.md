# Plan: `/check-glassdoor` — Glassdoor Canada Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-glassdoor.md`.

## Deliverable

`.claude/commands/check-glassdoor.md` — a slash command definition, Chrome-driven like
`/check-remoteok`, but with a fragile URL-encoding quirk to work around and a duplicate-flagging
step (this source overlaps with others) instead of an eligibility gate.

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, create a new tab. No login check needed to browse.

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

4. **Search per keyword** — `navigate` to:
   ```
   https://www.glassdoor.ca/Job/canada-<keyword-slug>-jobs-SRCH_IL.0,6_IN3_KO7,<N>.htm
   ```
   where `<keyword-slug>` is the keyword lowercased with spaces as hyphens (e.g.
   `devops-engineer`), and `<N>` is the character count of `<keyword-slug>` with hyphens replaced
   by spaces (e.g. "devops engineer" = 15 characters → `KO7,15`... but confirmed during testing
   `,20` worked and `,21` didn't for "devops engineer" specifically, so **the exact formula isn't
   fully pinned down — treat `<N>` as approximately the keyword's character count and verify by
   result count, don't trust a fixed formula blindly**).

   **After navigating, always check the page title or result count before treating the query as
   exhausted.** The title format is `"<count> <keyword slug variant> jobs in Canada, <month>
   <year> | Glassdoor"` — if `<count>` is 0, retry with `<N>` incremented and decremented by 1-2
   before concluding the keyword has no matches on this site.

   **Alternative approach worth trying during implementation**: navigate to the Glassdoor Canada
   homepage, use the on-page search box (type keyword, submit) rather than constructing the
   `KO7,<N>` URL directly — this may sidestep the fragile encoding entirely since the site builds
   the URL itself. Compare reliability of both approaches during first real use and note findings
   in `job_sources.md`.

   `get_page_text` returns the results list directly: title, company (with Glassdoor rating),
   location, salary (employer-provided or Glassdoor-estimated), skill tags, and an Easy Apply
   flag.

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no relevant results after the retry above, skip it and continue. If
   everything comes back empty, report and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **No eligibility gate** — the `canada-` URL prefix scopes results to Canada by construction.
   A `Remote` tag on an individual posting could theoretically hide non-Canada bias (same
   RemoteOK/WWR caution), but this hasn't been confirmed as a widespread issue on Glassdoor —
   treat as a soft skim-the-body caution, not a hard gate step.

8. **Open each candidate posting** — click the title link from the results list. Extract full
   description, salary, skill tags, remote/hybrid/onsite, and company.

   - CAPTCHA or blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - A "Sign in to see salary insights" or similar community-content prompt appears mid-page →
     ignore it, the core job description remains readable without signing in; don't click Sign In.
   - Posting fails to load → mark "couldn't fetch," continue with the rest.
   - Never click Apply, Easy Apply, or Sign In.

9. **Duplicate-aware check, before final scoring** — for each candidate, run
   `grep -ril "<company>" jobs/new/ jobs/applied/ jobs/rejected/` (and a title-based grep if the
   company grep is ambiguous). If a match is found, note it as a likely duplicate with the
   matched file's path — **don't silently exclude it**, since Glassdoor confirmed both real
   overlap (a Deloitte posting also found via Indeed) and real unique inventory (Cerebras,
   ZoomInfo, Teknion) in initial testing — the overlap itself is useful confirmation, not noise.

10. **Score each posting 0–10**, skill/domain-first, same philosophy as the other `/check-*`
    commands.

11. **Present a single results table**, sorted highest score first:

    | Role — Company | Score | Salary | Why | Possible Duplicate |
    |---|---|---|---|---|

    No files are written at this step.

12. **Offer to go deeper** — same pattern as the other commands, but **skip re-offering any
    posting already flagged as a duplicate in step 9** (don't file the same posting twice under a
    different filename). For non-duplicate picks:

    - Run the duplicate check again as a final safety net: `grep -ril "<company/role>" jobs/new/
      jobs/applied/ jobs/rejected/`.
    - Reuse the posting content already fetched in step 8 — don't re-navigate.
    - Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
      (`specs/addjob.md`), including the `Flags` field, written to
      `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
    - Report back: score, one-line summary, flags, and the file path.

    Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
    only.

13. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-glassdoor devops engineer` — confirm the URL-encoding retry logic recovers from a
  0-result page rather than silently reporting "no results" when results actually exist.
- Confirm the duplicate check correctly flags a posting already in `jobs/new/`, `jobs/applied/`,
  or `jobs/rejected/` without excluding it from the results table.
- Confirm no Apply/Easy Apply/Sign In button is ever clicked during a run.

## Out of Scope

Same as spec: a fully robust general solution to the `KO7,<N>` encoding, pagination, signing in
for community features, auto-filing without confirmation.
