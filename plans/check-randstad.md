# Plan: `/check-randstad` — Randstad Canada Technologies Search & Bulk Quick-Score (via Claude in Chrome)

Implements `specs/check-randstad.md`.

## Deliverable

`.claude/commands/check-randstad.md` — a slash command definition. Unlike the other `/check-*`
commands, this one **cannot drive a site-side keyword search** (confirmed broken on `randstad.ca`)
— it browses the Technologies category page and filters client-side instead.

## Command Steps

1. **Load Chrome tools up front** — one `ToolSearch` call:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find`

2. **Get tab context**, create a new tab. No login check needed.

3. **Parse input** — `$ARGUMENTS` optional, used as a client-side filter term (not a search query).

   ### Default role rotation (used as filter terms, not separate searches)
   ```
   DevOps Engineer
   Platform Engineer
   Site Reliability Engineer
   Cloud Engineer
   DevSecOps Engineer
   Forward Deployed Engineer
   ```

4. **Navigate once** to:
   ```
   https://www.randstad.ca/jobs/s-technologies/
   ```
   Confirmed during testing: loads directly with real listings — title, location, job type
   (Contract/Permanent), pay rate when disclosed, posted-date. **Do not attempt `?query=`
   free-text search on this domain** — confirmed during testing it returns 0 results even for
   "devops." The category-browse page is the only reliable path.

5. **Enumerate results** — use `get_page_text` or `read_page` to extract the ~30 postings shown on
   the first page (520 total exist across the full category — only the first page is in scope,
   see Out of Scope).

6. **Client-side filter** — scan titles/summaries for matches against the rotation keywords (or
   the single custom query term if `$ARGUMENTS` was non-empty). Most results will be unrelated
   (BA, PM, Data Engineer, Salesforce, etc.) — this is a broad "Technologies" category, not
   DevOps-specific, similar noise profile to Job Bank's NOC-code matching. Keep only titles/
   summaries that plausibly match DevOps/Cloud/Platform/SRE/Infrastructure work.

7. **Read `profile.md`** in full.

8. **No eligibility gate** — `randstad.ca` (not `.com`/`randstaddigital.com`) is the Canadian
   site; postings shown are Canada-scoped by construction.

9. **Open each candidate posting** (the filtered subset from step 6) — click through to the job
   detail page. Extract title, company (often "Our client" — normal for a staffing agency, not a
   red flag), full description, pay rate, job type, and location.

   - CAPTCHA or blocking page appears → stop the entire run immediately, tell the user which
     posting triggered it, do not attempt to solve it.
   - Posting fails to load → mark "couldn't fetch," continue with the rest.
   - Never click Apply or any other write-side button.

10. **Score each candidate posting 0–10**, skill/domain-first, same philosophy as the other
    `/check-*` commands. **Job Type is a first-class signal** — Contract roles align with the
    consulting-engagement preference; flag Permanent roles as FTE but don't auto-exclude given
    the current lowered scoring bar.

11. **Present a single results table**, sorted highest score first:

    | Role — Company | Score | Job Type | Why | Flags |
    |---|---|---|---|---|

    No files are written at this step.

12. **Offer to go deeper** — same pattern as the other commands: duplicate check via
    `grep -ril`, reuse content already fetched in step 9, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the company is anonymized, use
    `randstad` as the company slug unless the full posting reveals the real client name.

    Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
    only.

13. **Close the tab** at the end of the run.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-randstad` (no arguments) — confirm the Technologies category page loads with real
  listings and the client-side filter correctly narrows to DevOps/Cloud/SRE-relevant titles.
- Confirm `?query=` is NOT used anywhere in the command (would silently return 0 results per
  testing).
- Confirm both Contract and Permanent postings are surfaced and correctly labeled.
- Confirm no Apply button is ever clicked during a run.

## Out of Scope

Same as spec: pagination beyond page one, trusting `?query=`, `randstaddigital.com`'s broken
flow, auto-filing without confirmation.
