# Plan: `/check-indeed` — Indeed Search & Bulk Quick-Score

Implements `specs/check-indeed.md`.

## Deliverable

`.claude/commands/check-indeed.md` — a slash command definition, prompt-driven like `/addjob`.
No new scripts; uses WebFetch for the search page and each posting, Read for `profile.md`, and
reuses `/addjob`'s file-writing logic for any posting the user chooses to file afterward.

## Command Steps

1. **Parse input** — `$ARGUMENTS` is optional. Location is always `Remote`, not a user-supplied
   argument.
   - Non-empty → single custom query, same as the original behavior.
   - Empty → run the **default role rotation** (DevOps Engineer, Platform Engineer, Site
     Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer), one
     search per keyword.

2. **Build and fetch the search URL(s)** — `https://ca.indeed.com/jobs?q=<keyword>&l=Remote`
   (URL-encode spaces as `+`) for each keyword in play this run. WebFetch each with a prompt that
   asks for every markdown hyperlink pointing at a job posting (`pagead/clk`, `/viewjob?jk=`,
   `/rc/clk`), each with the title and company as shown on the results page. Cap at 15 links for
   a single custom query, or 8 links per keyword in rotation mode (6 keywords × 8 ≈ manageable
   total batch size).

3. **Dedupe** (rotation mode only) — collapse the combined link list by company + title
   (case-insensitive) before fetching full posting details, since the same posting commonly
   surfaces under more than one keyword.

4. **Read `profile.md`** in full before scoring anything.

5. **Fetch each deduped posting** individually via WebFetch, extracting: title, company,
   location, remote/hybrid/onsite, salary/rate if stated, engagement type, and enough of the
   responsibilities/requirements to score against `profile.md`.

6. **Score each 0–10**, skill/domain-first, same philosophy as `/addjob` (Azure depth, platform
   engineering/CI-CD/IaC scope, financial/energy relevance, autonomy vs. ticket-taking; logistics
   flagged, not scored down). One-sentence rationale per posting — this is a scan, not a full
   writeup.

7. **Present a sorted table** (highest score first): Role — Company | Score | one-line why | key
   flags. No files written at this step.

8. **Ask the user** which postings (if any) should get the full `/addjob` treatment. For each one
   picked:
   - Run the duplicate check (`grep -ril` across `jobs/new/`, `jobs/applied/`, `jobs/rejected/`).
   - Reuse the posting content already fetched in step 5 — no need to re-fetch.
   - Produce the full resume delta + cover letter + job file exactly as `/addjob` does, using the
     same schema (including the `Flags` field).

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
