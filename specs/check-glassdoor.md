# Spec: `/check-glassdoor` — Glassdoor Canada Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

Glassdoor (`glassdoor.ca`) loads cleanly via Chrome with no login wall to browse listings or full
postings (sign-in only gates reviews/salary-negotiation community content). Confirmed 2026-08-20:
126 results for "devops engineer" in Canada, rich per-listing data (salary, skill tags, Easy Apply
flag, remote/city). **Partial overlap with other sources confirmed** — one result (Deloitte's
"Cloud Engineer (Azure, az cli, Powershell)") was the exact same posting already filed from
Indeed — but it also surfaced titles not seen elsewhere in this search (Cerebras DevOps Engineer,
ZoomInfo Senior DevOps Engineer, Teknion DevOps Solutions Architect $110-130K). Worth running for
its unique inventory despite the overlap.

## Capability

Same overall shape as `/check-indeed`: optional search query (defaults to the shared role
rotation), searches Glassdoor via Chrome, quick-scores results, and runs the duplicate check at
filing time (same as every other command) to avoid re-filing the same posting found via a
different source.

## Usage

```
/check-glassdoor [search terms]
```

- `/check-glassdoor` (no arguments) — runs the default role rotation (same list as the other
  `/check-*` commands).
- `/check-glassdoor platform engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required to browse.
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://www.glassdoor.ca/Job/canada-<keyword-slug>-jobs-SRCH_IL.0,6_IN3_KO7,<N>.htm`

   **Fragile URL structure, confirmed during testing**: the trailing `<N>` in `KO7,<N>` must
   roughly match the keyword's character count (not including "canada-" or "-jobs") or the search
   silently returns **0 results** with no error — `,21` broke a "devops engineer" search, `,20`
   worked. **After navigating, check the page title/result count before treating a query as
   exhausted** — if it shows 0 results, retry with `<N>` adjusted by ±1-2 before concluding the
   keyword has no matches. As a more robust alternative, consider using Glassdoor's on-page search
   box (type + submit) rather than constructing the URL directly, since the box handles the
   `KO7,<N>` encoding internally — verify which approach is more reliable during implementation.

   `get_page_text` returns the full results list with title, company, location, salary (when
   employer-provided or Glassdoor-estimated), skill tags, and an Easy Apply flag.
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **No eligibility gate** — the `canada-` URL prefix scopes results to Canada by construction (a
   `Remote` location tag on an individual posting may still warrant a body-text skim for hidden
   US-only bias, same caution as RemoteOK/WWR, but this hasn't been confirmed as a widespread
   problem on Glassdoor yet — treat as a soft caution, not a hard gate).
7. **Open each candidate posting** — click through from the results list (title link). Extract
   full description, salary, skill tags, remote/hybrid/onsite, and company.
8. **Duplicate-aware scoring** — before presenting the final table, run the same duplicate check
   used at filing time (`grep -ril` against `jobs/new/`, `jobs/applied/`, `jobs/rejected/`) on
   each candidate's company+title. **Flag likely-duplicate postings inline in the results table**
   (e.g. "already filed via Indeed, 2026-08-19") rather than silently excluding them — this
   source's value is partly in cross-confirming postings and partly in finding new ones, so
   surfacing the overlap is useful information, not just noise to filter.
9. **Quick-score each posting** 0–10, same skill/domain-first philosophy as the other `/check-*`
   commands.
10. **Present a single table** sorted highest score first, with a "Possible duplicate" column
    per step 8.
11. **Offer to go deeper** — same `/addjob`-reuse pattern, skipping confirmed duplicates
    automatically (don't re-offer to file something already in `jobs/`).

## Edge Cases

- **URL `<N>` mismatch silently returns 0 results** → always verify result count before
  concluding a keyword has no matches; retry with adjusted `<N>`.
- **Community/review content prompts a sign-in wall mid-scroll** (e.g. "Sign in to see salary
  insights" on a Conversations/Bowls widget) → this is expected on some pages; ignore that widget,
  the core listing and full job description remain readable without signing in.
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it.
- **Never click Apply, Easy Apply, or Sign In** — read-only browsing only.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode.

## Out of Scope

- Building a robust general solution to the `KO7,<N>` encoding beyond a retry-on-zero-results
  heuristic (revisit if it proves unreliable across many keywords).
- Pagination beyond the first results page.
- Signing in for reviews/salary-community features — out of scope entirely, not needed for job
  search.
- Auto-filing high-scoring results without user confirmation.
