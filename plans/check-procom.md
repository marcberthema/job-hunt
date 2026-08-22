# Plan: `/check-procom` — Procom Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-procom.md`.

## Deliverable

`.claude/commands/check-procom.md` — a slash command definition, same overall shape as
`/check-sisystems` (Chrome-driven, working keyword search) but with a lightweight eligibility
gate (Procom mixes in some US postings despite being a Canadian firm).

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

4. **Search per keyword** — `navigate` to:
   ```
   https://myprocom-portal.procomservices.com/jobs?keyword=<keyword, spaces as +>
   ```
   Confirmed during testing: the `?keyword=` param works and returns relevant results (24 for
   "devops," including real "DevOps Engineer" and "Senior Cloud DevOps Engineer" titles). Each
   result card shows a **remote/hybrid/onsite tag** directly — a reliable filter/eligibility
   signal — plus title, location, posted-date, and pay rate when disclosed.

   **`get_page_text` only returns the first visible card's content, not the full list** —
   confirmed during testing on both the unfiltered and keyword-searched views. Use `read_page`
   (filter: interactive, to get job title/link elements) or repeated `find` calls to enumerate all
   results on the page before deciding which to open.

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no relevant results, skip it and continue. If everything comes back
   empty, report and stop.

5. **Dedupe** (rotation mode only) — collapse by company + exact title.

6. **Read `profile.md`** in full.

7. **Lightweight eligibility gate** — using the location field shown per result (confirmed during
   testing: Procom mixes in US postings — Colorado Springs, Raleigh NC — despite being a Canadian
   staffing firm):
   - **Canadian city/province**, or **"Remote"** with no US-specific qualifier → eligible.
   - **US city/state shown** → open the posting first to check for an explicit "open to
     Canada-based remote" line before excluding; if silent or US-only stated, mark ineligible
     with reason "US-based posting, no stated Canada eligibility."

8. **Open each eligible posting** — click the job title/link (found via `read_page`/`find` in
   step 4). Extract title, company (often just "Procom," client name may or may not be disclosed
   — normal for a staffing agency, not a red flag), full description, pay rate, job type
   (remote/hybrid/onsite), and location.

   - CAPTCHA or blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - Posting fails to load → mark "couldn't fetch," continue with the rest, skip the gate for it.
   - Never click Apply or any other write-side button.

9. **Score each eligible posting 0–10**, skill/domain-first, same philosophy as the other
   `/check-*` commands.

10. **Present two tables**: eligible sorted highest score first; ineligible listed separately
    below with title, company, and reason (not scored).

11. **Offer to go deeper** — same pattern as the other commands: duplicate check via `grep -ril`,
    reuse content already fetched in step 8, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the client is anonymized, use
    `procom` as the company slug unless the full posting reveals the real client name.

    Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
    only.

12. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-procom devops engineer` — confirm `read_page`/`find` successfully enumerates
  multiple results (not just the first card that `get_page_text` alone would return).
- Confirm the eligibility gate correctly flags US-location postings and doesn't silently include
  them.
- Confirm the remote/hybrid/onsite tag is captured and surfaced in the results table.
- Confirm no Apply button is ever clicked during a run.

## Out of Scope

Same as spec: the broken public `procom.ca/find-jobs/` path, pagination, auto-filing without
confirmation.
