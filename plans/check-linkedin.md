# Plan: `/check-linkedin` — LinkedIn Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-linkedin.md`.

## Deliverable

`.claude/commands/check-linkedin.md` — a slash command definition, same overall shape as
`/check-builtin`, but driving `mcp__claude-in-chrome__*` tools instead of `WebFetch`.

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, then create a new tab for this run (don't reuse an existing tab unless
   the user explicitly points at one).

3. **Confirm login** — navigate to `https://www.linkedin.com/feed/`. Use `get_page_text` to
   check for feed content vs. a login/join page. If not logged in: stop, tell the user, close the
   tab, end the command.

4. **Parse input** — `$ARGUMENTS` optional, same rotation-vs-single-query branch as
   `/check-builtin`.

   ### Default phrase rotation
   ```
   DevOps Consultant Remote
   Senior Site Reliability Engineer Remote
   Platform Engineer Remote
   Cloud Engineer Remote
   DevSecOps Engineer Remote
   Forward Deployed Engineer Remote
   ```
   The first two are confirmed verbatim from Marc's real LinkedIn alert emails (2026-08-20); the
   rest follow the same `"<Role> Remote"` phrasing for consistency. This is a **different shape**
   than the other three `/check-*` commands' bare-title rotations — do not "sync" it back to bare
   titles; the "Remote" suffix and full-phrase form are what make LinkedIn's semantic search work.

5. **Search per keyword** — `navigate` to:
   ```
   https://www.linkedin.com/jobs/search/?keywords=<phrase, spaces as %20>&geoId=101174742&f_TPR=r172800&sortBy=DD
   ```
   `geoId=101174742` is the broad "Canada" geo (confirmed from real alert URLs — do not use
   `location=Canada` text or a city-specific `geoId`; testing showed the broad geoId returns
   equal-or-better results than city-anchored versions, with heavy overlap). `f_TPR=r172800` is
   the **past-2-days** relative time filter (confirmed preference, 2026-08-20). No `f_WT` param —
   "Remote" is already in the keyword phrase, matching the real alerts' construction.

   **Scroll the results panel before reading it.** The unscrolled view shows the same ~7-10
   "recently viewed/recommended" cards regardless of the keyword in the URL — genuinely relevant
   results only surface after scrolling. Use `computer` with `action: scroll` targeted at the
   results-list column (left panel, not the whole page) at least twice, ~10 ticks each, before
   extracting. Then `read_page` (filter: interactive) to extract each result's job title,
   company, location, and job ID (from the `/jobs/view/<id>/` link pattern in the results list
   markup) — `get_page_text` doesn't expose the href, so `read_page` is required here, not just
   `get_page_text`.

   - Single custom query: cap at first 20 results (post-scroll).
   - Default rotation: cap at first 12 results per keyword (post-scroll).

   Result volumes are much higher now (42-99+ per keyword observed) — scroll enough to comfortably
   clear the cap before extracting; a couple of extra scroll passes is cheap insurance.

   Clicking to page 2+ via the numbered pager is still out of scope — scrolling within page 1's
   panel is sufficient.

   If a keyword returns zero job links, skip it and continue. If everything comes back empty,
   report and stop.

6. **Dedupe** (rotation mode only) — collapse combined results by company + exact title, same
   rule as `/check-builtin`'s dedupe step.

7. **Read `profile.md`** in full.

8. **Open each deduped posting** — `navigate` to `https://www.linkedin.com/jobs/view/<job-id>/`,
   then **scroll down a few ticks before calling `get_page_text`**. Confirmed during testing:
   the description body lazy-loads and stays as skeleton placeholders in `get_page_text` right
   after navigation even with a multi-second `wait` — scrolling reliably triggers it to render.
   Extract: title, company, location, remote/hybrid/onsite, salary/rate if shown, engagement
   type, and enough of the description to score.

   - If a challenge/CAPTCHA page is detected instead of job content: stop the whole run
     immediately, tell the user exactly what happened and which job ID triggered it, and do not
     continue to further postings.
   - If a single posting shows "no longer accepting applications" or fails to load: mark
     "couldn't fetch / expired" and continue with the rest.
   - Never interact with Easy Apply/Apply buttons or any other write-side UI on the page —
     read-only navigation and text extraction only.

9. **Score each 0–10**, skill/domain-first, same philosophy and one-sentence rationale style as
   the other `/check-*` commands.

10. **Present a sorted table** (highest score first). No files written at this step.

11. **Offer to go deeper** — same pattern as `/check-builtin` step 8: duplicate check via
    `grep -ril`, reuse the content already fetched in step 8 (don't re-navigate), full `/addjob`
    schema output to `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

12. **Close the tab** at the end of the run (success, empty-result, or early-stop paths alike).

## Testing

Manual (no automated test suite in this repo, same as the other `/check-*` commands):

- Run `/check-linkedin devops engineer` while logged into LinkedIn in Chrome — confirm the login
  check passes, results are found, job pages open via direct navigation (not UI clicking), and a
  scored table comes back.
- Run `/check-linkedin` (no arguments) — confirm all 6 rotation keywords are searched and
  deduped correctly.
- Temporarily test the "not logged in" path (open an Incognito/logged-out context if feasible, or
  reason about it) — confirm the command stops cleanly with a clear message rather than trying to
  scrape a login page.
- Confirm no Easy Apply or Apply button is ever clicked during a run.

## Out of Scope

Same as spec: pagination/scrolling, login/2FA handling, challenge-solving, Easy Apply, InMail/
messages.

## Follow-on stories (not part of this plan)

`/check-linkedin` is validated (2026-08-20) and `/check-wwr`, `/check-remoteok`,
`/check-braintrust`, and `/check-eluta` have since shipped using the same Chrome-driven pattern —
see their specs. Every `job_sources.md` "Not usable" entry from the original list has now been
converted except:

- Toptal — login-gated dashboard; worth testing whether Chrome + a logged-in session (if Marc has
  an account) clears it, same as LinkedIn.

Each will need its own spec first — site-specific search URL shape, login requirements, and
result-list markup are all unknowns until tested, same as LinkedIn was before this spec was
written.
