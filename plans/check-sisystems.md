# Plan: `/check-sisystems` — S.i. Systems Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-sisystems.md`.

## Deliverable

`.claude/commands/check-sisystems.md` — a slash command definition, same overall shape as
`/check-remoteok` (Chrome-driven, no eligibility gate — like `/check-eluta` since S.i. Systems is
Canada-only by construction), but with a keyword-search caveat: the site's own `?q=` free-text
param doesn't reliably filter, so the command leans on the specialization `expertise=` param
instead.

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
   Bare titles, same rotation as the other `/check-*` commands.

4. **Search per keyword** — `navigate` to:
   ```
   https://www.sisystems.com/search-it-jobs/?expertise=3&q=<keyword, spaces as +>
   ```
   `expertise=3` selects "Networks and Infrastructure" — confirmed during testing as the closest
   specialization category to DevOps/Cloud/SRE work (64 results at test time, vs. 151
   keyword-only noise-heavy results for "devops" with no specialization filter). Combine with
   `q=` for extra narrowing, but **treat `q=` as a soft signal, not a hard filter** — confirmed
   during testing it doesn't reliably exclude unrelated specializations on its own (a pure
   `?q=devops` search returned Business Analyst, QA, and Salesforce roles alongside real DevOps
   ones).

   Client-side rendered — after `navigate`, `wait` ~2 seconds before calling `get_page_text`, or
   the page returns a loading placeholder ("Loading...") instead of real results.

   `get_page_text` on the search-results page returns clean data directly: title (often includes
   a requisition ID suffix), expertise category, job type (Contract/Permanent), location, and
   posted-date ("X days ago"). It does not include the job detail URL directly in the text —
   use `find` on the posting's "DETAILS" link/title to get a clickable ref.

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no relevant results, skip it and continue. If everything comes back
   empty, report and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **No eligibility gate** — S.i. Systems is a Canadian IT staffing agency; every listing is
   Canada-scoped by construction, same reasoning as `/check-eluta`. Skip straight to scoring.

8. **Open each candidate posting** — click the "DETAILS" ref (or `navigate` directly if the URL
   was captured via `find`). Confirmed during testing: `get_page_text` returns the full job
   description directly — **no `find`+`read_page` workaround needed**. URL pattern:
   `/jobs/<slug>/<encoded-id>/`. Extract title, company (often "Our client" — normal for a
   staffing agency, not a red flag), full description, pay rate (either an explicit `$X-$Y/hr`
   for many Contract roles, or "Salary: Negotiable" for many Permanent roles), job type, and
   location.

   - CAPTCHA or blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - Posting fails to load → mark "couldn't fetch," continue with the rest.
   - Never click Apply or any other write-side button.

9. **Score each posting 0–10**, skill/domain-first, same philosophy as the other `/check-*`
   commands. **Job Type (Contract vs. Permanent) is worth surfacing explicitly** — Contract roles
   align directly with `profile.md`'s consulting-engagement preference and shouldn't be scored
   down for coming through a staffing agency; flag Permanent roles as FTE per the usual pattern
   but don't auto-exclude given the current lowered scoring bar.

10. **Present a single results table** (no eligible/ineligible split needed here), sorted highest
    score first:

    | Role — Company | Score | Job Type | Why | Flags |
    |---|---|---|---|---|

    No files are written at this step.

11. **Offer to go deeper** — same pattern as the other commands: duplicate check via `grep -ril`,
    reuse content already fetched in step 8, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the company is anonymized
    ("Our client"), use S.i. Systems itself as the filed "company" identifier in the filename
    (e.g. `sisystems-<role-slug>`) unless the full posting reveals the real client name.

    Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
    only.

12. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-sisystems site reliability engineer` — confirm the `expertise=3` filter returns a
  cleaner result set than the bare `?q=` search, and that `get_page_text` on a job detail page
  returns the full description directly.
- Confirm the 2-second wait after `navigate` is enough for client-side rendering to complete
  before `get_page_text` is called (results shouldn't show "Loading...").
- Confirm both Contract and Permanent postings are surfaced and correctly labeled in the results
  table.
- Confirm no Apply button is ever clicked during a run.

## Out of Scope

Same as spec: trusting `?q=` alone, pagination, building the full specialization ID table beyond
what's needed, auto-filing without confirmation.
