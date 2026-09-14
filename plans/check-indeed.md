# Plan: `/check-indeed` — Indeed Search & Bulk Quick-Score

Implements `specs/check-indeed.md`.

## Deliverable

`.claude/commands/check-indeed.md` — a slash command definition, prompt-driven like `/addjob`.
**Revised 2026-09-13**: no longer uses WebFetch — Indeed started returning HTTP 403 to plain
WebFetch as of 2026-09-08, confirmed again 2026-09-13 (two consecutive runs, no longer
transient). Now drives a real Chrome browser (`mcp__claude-in-chrome__*` tools) for the search
page and each posting, same workaround already used for RemoteOK/WWR/LinkedIn/S.i. Systems. Read
for `profile.md`, and reuses `/addjob`'s file-writing logic for any posting the user chooses to
file afterward.

## Command Steps

1. **Load Chrome tools** — one `ToolSearch` call for `tabs_context_mcp`, `navigate`, `computer`,
   `read_page`, `tabs_create_mcp`, `tabs_close_mcp`, `get_page_text`, `find`. Open a tab via
   `tabs_context_mcp` then `tabs_create_mcp`. No login required.

2. **Parse input** — `$ARGUMENTS` is optional. Location is always `Remote`, not a user-supplied
   argument.
   - Non-empty → single custom query, same as the original behavior.
   - Empty → run the **default role rotation** (DevOps Engineer, Platform Engineer, Site
     Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer), one
     search per keyword.

3. **Navigate to the search URL(s)** — `https://ca.indeed.com/jobs?q=<keyword>&l=Remote`
   (URL-encode spaces as `+`) for each keyword in play this run. `wait` ~2s for lazy-loaded
   content, then `get_page_text` for title/company/location/snippet; use `find` on each result's
   title to get a link/element ref for job-posting URLs (`pagead/clk`, `/viewjob?jk=`, `/rc/clk`)
   not present in the plain text output. Prefer `/viewjob?jk=` or `/rc/clk?jk=` links over bare
   `pagead/clk` links with no `jk=` param (these rotate and can resolve to an unrelated job later
   — see the data-quality bug noted in `job_sources.md`); if only a bare link is available,
   follow the redirect and record the resolved URL. Cap at 15 links for a single custom query, or
   8 links per keyword in rotation mode (6 keywords × 8 ≈ manageable total batch size).

4. **Dedupe** (rotation mode only) — collapse the combined link list by company + title
   (case-insensitive) before opening full postings, since the same posting commonly surfaces
   under more than one keyword.

5. **Read `profile.md`** in full before scoring anything.

6. **Open each deduped posting** via Chrome (click the `find` ref, or `navigate` directly if the
   resolved URL is already known), extracting: title, company, location, remote/hybrid/onsite,
   salary/rate if stated, engagement type, and enough of the responsibilities/requirements to
   score against `profile.md`. A CAPTCHA or blocking page stops the entire run immediately —
   report it, don't attempt to solve it. Never click Apply or any other write-side button.

7. **Score each 0–10**, skill/domain-first, same philosophy as `/addjob` (Azure depth, platform
   engineering/CI-CD/IaC scope, financial/energy relevance, autonomy vs. ticket-taking; logistics
   flagged, not scored down). One-sentence rationale per posting — this is a scan, not a full
   writeup.

8. **Present a sorted table** (highest score first): Role — Company | Score | one-line why | key
   flags. No files written at this step.

9. **Ask the user** which postings (if any) should get the full `/addjob` treatment. For each one
   picked:
   - Run the duplicate check (`grep -ril` across `jobs/new/`, `jobs/applied/`, `jobs/rejected/`).
   - Reuse the posting content already fetched in step 6 — no need to re-navigate.
   - Produce the full resume delta + cover letter + job file exactly as `/addjob` does, using the
     same schema (including the `Flags` field).

10. **Close the tab** at the end of the run — success, empty-result, or early-stop path alike.

## Edge Cases (carried from spec)

- A single keyword's search returns no job links (rotation mode) → skip it, continue with the
  rest of the rotation.
- No parseable job links at all (every keyword, or the single custom query) → report it, suggest
  a different query or direct `/addjob <url>`.
- A single posting fails to fetch → mark it "couldn't fetch" in the table, don't drop it
  silently, don't abort the rest of the batch.
- Results exceed the per-mode cap → truncate and say so.
- User picks a posting that's already in `jobs/` → same duplicate warning `/addjob` gives, ask
  before proceeding.

## Testing

Manual:
- Run `/check-indeed` (no arguments) and confirm all 6 rotation keywords get searched, results
  are deduped (no obvious repeats), and the table covers a reasonable spread of companies.
- Run `/check-indeed devops engineer` and confirm single-query mode still works as before.
- A results table appears covering the fetched postings, sorted by score, in both modes.
- Picking a posting to file produces a `jobs/new/` file matching the `/addjob` schema.
- A narrow/nonsense single-query search degrades gracefully (no results found message, not a
  crash).

No automated test suite for this repo; verification is manual, same as `/addjob`.

## Out of Scope

Same as spec: other job boards, auto-filing every result, pagination past page one.
