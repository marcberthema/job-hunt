# Spec: `/check-jobbank` — Job Bank (Canada) Search & Bulk Quick-Score

## Problem

Job Bank (jobbank.gc.ca), the Government of Canada's official job board, is fetchable directly
via WebFetch — both search-result pages and individual postings return real content, unlike
Eluta.ca (whose job links are JavaScript-generated fragments with no real URL) or Braintrust
(client-side rendered, empty on fetch). It's a legitimate additional Canadian-specific source
worth adding alongside `/check-indeed` and `/check-dice`.

## Capability

Same shape as `/check-indeed`: optional search query (defaults to the shared role rotation),
searches Job Bank, fetches each result, and reports a quick-score table. No eligibility gate is
needed here (unlike `/check-dice`) — Job Bank is Canada-specific by nature, so the US
work-authorization failure pattern doesn't apply.

## Usage

```
/check-jobbank [search terms]
```

- `/check-jobbank` (no arguments) — runs the default role rotation (same list as `/check-indeed`
  and `/check-dice`: DevOps Engineer, Platform Engineer, Site Reliability Engineer, Cloud
  Engineer, DevSecOps Engineer, Forward Deployed Engineer).
- `/check-jobbank devops engineer` — runs that single query only.

## Behavior

1. **Determine query mode**: single custom query or full rotation.
2. **Build and fetch the search URL(s)**:
   `https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=<keyword>&locationstring=Remote`
   for each keyword in play. Extract every `/jobsearch/jobposting/<id>` link with title, company,
   location, and salary as shown on the results page.
   Note: Job Bank's `locationstring` filter doesn't reliably restrict to remote-only postings —
   during testing, `locationstring=Canada` returned a mix of on-site, hybrid, and remote roles
   across Ontario/BC. This is fine: on-site/hybrid status gets surfaced as a **flag** during
   scoring (same philosophy as `/addjob` and `/check-indeed`), not filtered out.
3. **Dedupe** (rotation mode only) — collapse by company + title.
4. **Read `profile.md` first**.
5. **Fetch each posting**, extract title, company, location, remote/hybrid/onsite,
   salary/rate, engagement type, requirements.
6. **Quick-score each** 0–10, same skill/domain-first philosophy as `/check-indeed`.
7. **Report a table**, sorted highest score first. No files written.
8. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Known Overlap with `/check-indeed`

Job Bank aggregates postings from multiple sources, **including Indeed** (confirmed during
testing — one fetched posting explicitly stated "sourced from Indeed.com"). This means
`/check-jobbank` and `/check-indeed` will likely surface some of the same underlying postings
under different URLs. This isn't a bug to fix within either command — the existing duplicate
check at filing time (`grep -ril` across `jobs/new/`, `jobs/applied/`, `jobs/rejected/` by
company/role) already catches this when the user picks a posting for the full `/addjob`
treatment. No special de-duplication between commands is needed.

## Edge Cases

- A single keyword's search returns no job links → skip it, continue the rotation.
- Every keyword (or the single custom query) returns no job links → report it, stop.
- Individual posting fetch fails → mark "couldn't fetch," don't drop it or abort the batch.
- Large result count → cap at 15 for single query, 8 per keyword in rotation mode (same limits
  as `/check-indeed`).

## Out of Scope

- Eluta.ca and Braintrust — confirmed unusable this session (JS-rendered links / empty content).
- An eligibility gate like `/check-dice`'s — not needed since Job Bank results are Canada-native.
- Pagination beyond the first results page.
