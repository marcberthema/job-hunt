# Plan: `/check-jobbank` — Job Bank (Canada) Search & Bulk Quick-Score

Implements `specs/check-jobbank.md`.

## Deliverable

`.claude/commands/check-jobbank.md` — a slash command definition, same pattern as
`/check-indeed` (no eligibility gate needed, unlike `/check-dice`).

## Command Steps

1. **Parse input** — `$ARGUMENTS` is optional.
   - Non-empty → single custom query.
   - Empty → run the default role rotation (DevOps Engineer, Platform Engineer, Site
     Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer) — same
     list as `/check-indeed` and `/check-dice`.

2. **Build and fetch the search URL(s)**, one per keyword in play:
   ```
   https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=<keyword, spaces as +>&locationstring=Remote
   ```
   WebFetch each, extracting every `/jobsearch/jobposting/<id>` link with title, company,
   location, and salary as shown. Cap at 15 links for a single custom query, or 8 per keyword in
   rotation mode.

3. **Dedupe** (rotation mode only) — collapse by company + title before fetching full details.

4. **Read `profile.md`** in full.

5. **Fetch each deduped posting** individually, extracting: title, company, location,
   remote/hybrid/onsite, salary/rate, engagement type, and enough requirements to score.

6. **Score each 0–10**, skill/domain-first, same philosophy as `/addjob` and `/check-indeed` —
   logistics (on-site/hybrid, below-target pay) flagged, not scored down. One-sentence rationale.

7. **Present a sorted table** (highest score first). No files written.

8. **Offer to go deeper** — duplicate check, reuse fetched content, full `/addjob` treatment for
   picks.

## Testing

Manual:
- Run `/check-jobbank` (no arguments) and confirm all 6 rotation keywords get searched.
- Run `/check-jobbank devops engineer` and confirm single-query mode works.
- Confirm individual posting fetches return full detail (validated this session against
  `jobsearch/jobposting/49730307` — Sign In Solutions Inc., Senior DevOps/Cloud Engineer).
- Note (don't need to "fix") overlap with `/check-indeed` results — expected given Job Bank
  aggregates from Indeed among other sources.

No automated test suite for this repo; verification is manual, same as the other `/check-*`
commands.

## Out of Scope

Same as spec: no Eluta/Braintrust support, no eligibility gate, no pagination.
