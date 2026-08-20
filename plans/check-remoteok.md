# Plan: `/check-remoteok` — RemoteOK Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-remoteok.md`.

## Deliverable

`.claude/commands/check-remoteok.md` — a slash command definition, same overall shape as
`/check-wwr` (Chrome-driven + region-eligibility gate), but simpler on two points confirmed during
testing: no `find`+`read_page` workaround needed for job detail pages, and the region-eligibility
signal (flag-emoji list) is trustworthy directly off the search-results page.

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
   Bare titles, same rotation as `/check-indeed`/`/check-dice`/`/check-jobbank`/`/check-builtin`/
   `/check-wwr`.

4. **Search per keyword** — `navigate` to:
   ```
   https://remoteok.com/remote-jobs?search=<keyword, spaces as +>
   ```
   **Always use this search endpoint, never a category-browse URL** (e.g.
   `/remote-devops-jobs`) — confirmed during testing that category pages mix in large amounts of
   unrelated non-tech postings (retail, hospitality, logistics) despite being tagged with the
   category. The `?search=` endpoint returns much more relevant, keyword-matched results.

   `get_page_text` on the search-results page returns clean, complete data directly: title,
   company, posted-date ("Xd"/"Xmo" format), flag-emoji region list (or "Worldwide"/"Probably
   worldwide"), salary if shown (many show "Upgrade to Premium to see salary" — treat as "not
   stated"), and the job link (`/remote-jobs/<slug>-<numeric-id>` pattern, extractable via `find`
   on the job title if not directly visible in `get_page_text`'s output).

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no relevant results, skip it and continue. If everything comes back
   empty, report and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **Region-eligibility gate, using the flag list already captured in step 4** — confirmed during
   testing that RemoteOK's flag-emoji list is a reliable, consistent signal (cross-checked listing
   page vs. individual job page, they matched) — **unlike** We Work Remotely's decorative
   "Anywhere in the World" tag (see `specs/check-wwr.md`'s correction). Do not repeat that mistake
   here:
   - **🇨🇦 Canada explicitly in the flag list**, or **"Worldwide"/"Probably worldwide"** →
     eligible, proceed to step 8.
   - **Flag/region list present but excludes Canada** (US-only, Europe-only, a single other
     country) → **ineligible** — skip, do not open the full posting. Log title/company/reason.
   - **No region info shown at all** → open the posting (step 8) to check; if still silent, mark
     eligible with a flag: "confirm regional eligibility before applying."

8. **Open each eligible posting** — `navigate` to the job URL. Confirmed during testing:
   `get_page_text` returns the full, correct job description directly here — **no
   `find`+`read_page` workaround is needed** (this differs from `/check-wwr`, where
   `get_page_text` grabbed the wrong sidebar content). Extract title, company, full description,
   salary if shown, engagement type, and re-confirm the flag list.

   - CAPTCHA or blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - Posting fails to load → mark "couldn't fetch," continue with the rest, skip the gate for it.
   - Never click Apply or any other write-side button.

9. **Score each eligible posting 0–10**, skill/domain-first, same philosophy as the other
   `/check-*` commands. Flag (don't penalize) staffing-marketplace postings like Lemon.io — these
   can be a good contract/consulting fit even though they're not a direct employer.

10. **Present two tables**: eligible sorted highest score first; ineligible listed separately
    below with title, company, and reason (not scored).

11. **Offer to go deeper** — same pattern as the other commands: duplicate check via `grep -ril`,
    reuse content already fetched in step 8, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

12. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-remoteok platform engineer` — confirm the `?search=` endpoint returns relevant
  results (not category-page noise), the flag-based gate correctly separates eligible from
  ineligible postings, and `get_page_text` on a job detail page returns the real description
  without needing `find`/`read_page`.
- Confirm at least one Canada-eligible posting is found and scored (Lemon.io and Shakepay
  postings were both Canada-eligible during initial testing — good candidates to re-check).
- Confirm very old postings (6+ months) are flagged as possibly stale rather than silently
  included at face value.
- Confirm no Apply button is ever clicked during a run.

## Out of Scope

Same as spec: category-page browsing, pagination, extending the gate to other sources, auto-filing
without confirmation.
