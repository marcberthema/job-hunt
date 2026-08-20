# Plan: `/check-wwr` — We Work Remotely Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-wwr.md`.

## Deliverable

`.claude/commands/check-wwr.md` — a slash command definition, same overall shape as
`/check-linkedin` (Chrome-driven) crossed with `/check-dice` (eligibility gate before scoring).

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, create a new tab. No login check needed — WWR is fully browsable without
   an account (confirmed during testing, 2026-08-20).

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
   Bare titles, same rotation as `/check-indeed`/`/check-dice`/`/check-jobbank`/`/check-builtin`
   — **not** the LinkedIn-style natural-phrase rotation, since WWR's search is plain keyword
   matching rather than semantic search.

4. **Search per keyword** — `navigate` to:
   ```
   https://weworkremotely.com/remote-jobs/search?term=<keyword, spaces as +>
   ```
   Confirmed during testing: this loads fully rendered with no scroll/lazy-load workaround needed
   (unlike LinkedIn) — `get_page_text` on the search-results page returns clean, complete listing
   data directly for title, company, posted-date, engagement type (Full-Time/Contract), and
   salary if shown. **`get_page_text` only surfaces the generic "Anywhere in the World" tag, not
   the real per-posting location** — for the job link and the actual specific location line
   (e.g. "Remote India, IN", "Paris, France"), use `find` (query like "\<title\> job link at
   \<company\>") then `read_page` on the matched ref. Do this for every candidate result kept
   after the initial title skim (see step 7 for why this matters).

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns zero results, skip it and continue. If everything comes back empty,
   report and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **Region-eligibility gate, before opening the full posting** — **corrected 2026-08-20 after
   the first live run found the original design broken**: the generic "Anywhere in the World" tag
   appears on nearly every WWR posting regardless of real eligibility (confirmed: 8/8
   DevOps/Platform postings sampled carried it while also being restricted to a single non-Canada
   country). **Never use that tag to decide eligibility.** Use the specific location line
   extracted per-result in step 4 instead:
   - Names Canada, "Worldwide," or is blank/absent → provisionally eligible; if blank, still open
     the full posting (step 8) to look for an explicit region statement before finalizing.
   - Names a single non-Canada country/city, or a region list excluding Canada (India, a European
     country, "US-only," etc.) → **ineligible** — skip, do not open the full posting, log
     title/company/reason only. Do not let the "Anywhere in the World" tag override this call.
   - Names a broad multi-country descriptor that plausibly includes Canada (e.g. "North America
     Only," a flag list containing Canada) → eligible, proceed.

8. **Open each eligible posting** — `navigate` to `https://weworkremotely.com/remote-jobs/<slug>`.
   **Do not rely on `get_page_text` here** — confirmed during testing it grabs the wrong
   `<article>` (a related-jobs sidebar, not the actual description). Instead: call `find` with a
   query such as "job description main content container", then `read_page` with that result's
   `ref_id` to extract the real description text (Role Purpose / Responsibilities /
   Qualifications sections, salary, engagement type).

   - CAPTCHA or a blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - Posting fails to load / 404s → mark "couldn't fetch," continue with the rest, skip the gate
     for it (nothing to check).
   - Never click Apply, "AI Auto-Apply", or Save job — read-only only.

9. **Score each eligible posting 0–10**, skill/domain-first, same philosophy as the other
   `/check-*` commands. One-sentence rationale.

10. **Present two tables**: eligible postings sorted highest score first; ineligible postings
    listed separately below with title, company, and the region-mismatch reason (not scored) —
    mirrors `/check-dice`'s reporting shape.

11. **Offer to go deeper** — same pattern as the other commands: duplicate check via `grep -ril`,
    reuse content already fetched in step 8, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

12. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-wwr platform engineer` — confirm search loads without a 403, region-eligibility
  info is correctly read off the results cards, and the gate correctly separates eligible from
  ineligible postings before scoring.
- Confirm the `find` + `read_page` pattern reliably extracts the real job description on at least
  2-3 different postings (structure may vary by employer).
- Confirm a region-restricted posting (e.g. Europe-only) is correctly gated out without an
  unnecessary full-page fetch.
- Confirm no Apply/Auto-Apply/Save button is ever clicked during a run.

## Out of Scope

Same as spec: pagination, extending the gate to other sources, auto-filing without confirmation.
