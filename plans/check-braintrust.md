# Plan: `/check-braintrust` — Braintrust Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-braintrust.md`.

## Deliverable

`.claude/commands/check-braintrust.md` — a slash command definition, same overall shape as
`/check-remoteok` (Chrome-driven + location gate), but using Braintrust's URL query-param
filtering instead of a free-text search box.

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, create a new tab. No login check needed — confirmed 2026-08-20 that
   Braintrust is fully browsable without an account (the old "needs login" note in
   `job_sources.md` was based on stale/incorrect testing; the real issue was always client-side
   rendering, which Chrome resolves).

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
   https://app.usebraintrust.com/jobs/?role=5%2C16&skills=<skill-id>
   ```
   `role=5,16` (Engineering + IT & System Admin) is confirmed correct for this rotation. The
   `skills=` ID must be looked up per keyword — confirmed `1338` = DevOps during testing. For
   keywords without a confirmed ID yet, open a tab, click the **Skills** filter pill, type the
   keyword into its search box, click the matching chip, click **Apply**, and read the resulting
   URL's `skills=` value — cache it in `specs/check-braintrust.md`'s Skill ID Table for future
   runs once confirmed. If no matching skill chip exists for a keyword, fall back to the
   unfiltered `role=5,16` results and title-skim (same triage pattern as Indeed's noisy default
   rotation).

   `get_page_text` on the results page returns clean, complete data directly: title, company,
   engagement type (Freelance/Employee), rate, hours/week, and the **Location column** on each
   card (e.g. "United States only," "Work from anywhere," "North America + 1 more," "United
   States | Canada"). Extract this alongside the "View job" link
   (`/jobs/<numeric-id>` pattern, via `find` on the job title if not directly in the text output).

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no results, skip it and continue. If everything comes back empty, report
   and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **Location-eligibility gate, using the Location column captured in step 4**:
   - "Work from anywhere," an explicit "Canada" mention, or "North America" → eligible, proceed
     to step 8.
   - "United States only," or a region list excluding Canada → ineligible — skip, do not open the
     full posting. Log title/company/reason.
   - A specific US city/state with no "only" qualifier (Braintrust's on-site convention) →
     ineligible unless the full posting says otherwise.

8. **Open each eligible posting** — `navigate` to `https://app.usebraintrust.com/jobs/<id>`.
   Confirmed during testing: `get_page_text` returns the full, correct description directly, no
   `find`+`read_page` workaround needed. Extract title, company, full description, rate, skills,
   and the "Preferred location" field in the body — skim for any statement that contradicts the
   card's Location column (apply the same caution learned from RemoteOK's tag mismatches, even
   though no mismatch was found in initial Braintrust testing).

   - Posting fails to load → mark "couldn't fetch," continue with the rest, skip the gate for it.
   - Never click Apply — read-only navigation and text extraction only.

9. **Score each eligible posting 0–10**, skill/domain-first, same philosophy as the other
   `/check-*` commands. Freelance/contract postings are a strong engagement-type match here, not
   a flag — Braintrust is fundamentally a contractor marketplace.

10. **Present two tables**: eligible sorted highest score first; ineligible listed separately
    below with title, company, and reason (not scored).

11. **Offer to go deeper** — same pattern as the other commands: duplicate check via `grep -ril`,
    reuse content already fetched in step 8, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

12. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-braintrust devops` — confirm the `skills=1338&role=5,16` URL returns relevant
  results, the location gate correctly separates eligible from ineligible postings, and
  `get_page_text` on a job detail page returns the real description directly.
- Confirm at least one Canada-eligible posting is found (Equal Experts' "Senior Java Software
  Engineer (Remote - US / Canada)" and MGT's "AI Automation Engineer... US, LATAM, Canada" both
  surfaced in initial testing as related postings — worth re-checking as direct candidates).
- For any new rotation keyword's skill ID lookup, confirm it correctly updates the URL before
  relying on it, and update `specs/check-braintrust.md`'s Skill ID Table with the confirmed value.
- Confirm no Apply button is ever clicked during a run.

## Out of Scope

Same as spec: pagination, signing up for a profile, auto-filing without confirmation.
