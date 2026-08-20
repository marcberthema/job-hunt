# Spec: `/check-builtin` — BuiltIn Search & Bulk Quick-Score

## Problem

BuiltIn is fetchable directly via WebFetch (confirmed this session — both the search-results page
and individual `/job/<slug>/<id>` postings return real content). It's a tech-company-direct job
board with a decent Canada/remote section, worth adding alongside `/check-indeed`, `/check-dice`,
and `/check-jobbank` as a fourth source.

## Capability

Same shape as `/check-indeed`: optional search query (defaults to the shared role rotation),
searches BuiltIn, fetches each result, and reports a quick-score table. No eligibility gate
needed (like `/check-jobbank`) — BuiltIn results are already location-labeled (Remote/Hybrid/
In-Office, with country/city), so on-site/hybrid gets flagged during scoring like usual, not
gated out.

## Usage

```
/check-builtin [search terms]
```

- `/check-builtin` (no arguments) — runs the default role rotation (same list as the other three
  `/check-*` commands: DevOps Engineer, Platform Engineer, Site Reliability Engineer, Cloud
  Engineer, DevSecOps Engineer, Forward Deployed Engineer).
- `/check-builtin devops engineer` — runs that single query only.

## Behavior

1. **Determine query mode**: single custom query or full rotation.
2. **Build and fetch the search URL(s)**:
   `https://builtin.com/jobs/remote/dev-ops?search=<keyword>` for each keyword in play.
   Discovered during testing: the bare job-function URL (`/jobs/remote/dev-ops-engineer` with no
   `search` param) returns noisy, largely irrelevant results (sales, tax, insurance roles mixed
   in). Adding `?search=<keyword>` on top of the `/jobs/remote/dev-ops` base path produces clean,
   relevant results — this combination (fixed base path + search param) is required, not either
   piece alone.
3. **Dedupe** (rotation mode only) — collapse by company + title. BuiltIn results showed several
   near-duplicate postings during testing (e.g. "DevOps Engineer Backend" and "DevOps Engineer
   Mobile" at the same company, or the same title reposted under different IDs) — dedupe by
   company + *exact* title, not a fuzzy match, so genuinely distinct postings at the same company
   aren't accidentally collapsed.
4. **Read `profile.md` first**.
5. **Fetch each posting**, extract title, company, location, remote/hybrid/onsite,
   salary/rate if stated, engagement type, requirements.
6. **Quick-score each** 0–10, same skill/domain-first philosophy as `/check-indeed`.
7. **Report a table**, sorted highest score first. No files written.
8. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- A single keyword's search returns no job links → skip it, continue the rotation.
- Every keyword (or the single custom query) returns no job links → report it, stop.
- Individual posting fetch fails → mark "couldn't fetch," don't drop it or abort the batch.
- Large result count → cap at 15 for single query, 8 per keyword in rotation mode (same limits
  as the other `/check-*` commands).

## Out of Scope

- Pagination beyond the first results page (BuiltIn showed pagination up to page 813 for some
  categories — no attempt to go past page one).
- An eligibility gate — not needed, BuiltIn isn't showing the Dice-style US-work-authorization
  failure pattern.
