# Plan: `/check-builtin` — BuiltIn Search & Bulk Quick-Score

Implements `specs/check-builtin.md`.

## Deliverable

`.claude/commands/check-builtin.md` — a slash command definition, same pattern as
`/check-indeed` and `/check-jobbank` (no eligibility gate).

## Command Steps

1. **Parse input** — `$ARGUMENTS` is optional.
   - Non-empty → single custom query.
   - Empty → run the default role rotation (DevOps Engineer, Platform Engineer, Site
     Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer) — same
     list as the other three `/check-*` commands.

2. **Build and fetch the search URL(s)**, one per keyword in play:
   ```
   https://builtin.com/jobs/remote/dev-ops?search=<keyword, spaces as +>
   ```
   WebFetch each, extracting every `/job/<slug>/<id>` link with title, company, location, and
   remote status as shown. Cap at 15 links for a single custom query, or 8 per keyword in
   rotation mode.

3. **Dedupe** (rotation mode only) — collapse by company + *exact* title (not fuzzy) before
   fetching full details, since BuiltIn showed genuinely distinct postings at the same company
   with similar-but-different titles during testing (e.g. "DevOps Engineer Backend" vs "DevOps
   Engineer Mobile" at Air Apps) — over-aggressive fuzzy dedup would wrongly collapse these.

4. **Read `profile.md`** in full.

5. **Fetch each deduped posting** individually, extracting: title, company, location,
   remote/hybrid/onsite, salary/rate if stated, engagement type, and enough requirements to
   score.

6. **Score each 0–10**, skill/domain-first, same philosophy as `/addjob` and the other
   `/check-*` commands — logistics flagged, not scored down. One-sentence rationale.

7. **Present a sorted table** (highest score first). No files written.

8. **Offer to go deeper** — duplicate check, reuse fetched content, full `/addjob` treatment for
   picks.

## Testing

Manual:
- Run `/check-builtin` (no arguments) and confirm all 6 rotation keywords get searched.
- Run `/check-builtin devops engineer` and confirm single-query mode works.
- Confirm the URL requires both the `/jobs/remote/dev-ops` base path AND the `?search=` param —
  validated this session: base path alone returns noisy sales/tax/insurance results, search
  param combined with the base path returns clean DevOps/Platform results.
- Confirm near-duplicate same-company postings (e.g. Air Apps' Backend vs Mobile DevOps roles)
  are NOT incorrectly collapsed by the dedupe step.

No automated test suite for this repo; verification is manual, same as the other `/check-*`
commands.

## Out of Scope

Same as spec: no pagination, no eligibility gate.
