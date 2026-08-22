# Spec: `/check-sisystems` — S.i. Systems Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

S.i. Systems ("Canada's largest IT staffing agency") returns a blocked/WAF page via `WebFetch`
("The requested URL was rejected. Please consult with your administrator.") on both
`/jobs` and `/find-jobs/`. Tested via Claude in Chrome (2026-08-20): the homepage and the real
search page load cleanly, no login required — the WebFetch block looks like bot-defense
false-positive, not a real wall. Confirmed **1,093 open jobs, 114 new this week** at test time.

## Capability

Same overall shape as `/check-remoteok`/`/check-braintrust`: optional search query (defaults to
the shared role rotation), searches S.i. Systems via Chrome, and quick-scores results. **No
eligibility gate needed** — S.i. Systems is a Canadian staffing agency; every posting is
Canada-scoped by construction (unlike the worldwide remote boards).

## Usage

```
/check-sisystems [search terms]
```

- `/check-sisystems` (no arguments) — runs the default role rotation (same list as the other
  `/check-*` commands: DevOps Engineer, Platform Engineer, Site Reliability Engineer, Cloud
  Engineer, DevSecOps Engineer, Forward Deployed Engineer).
- `/check-sisystems site reliability engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required.
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://www.sisystems.com/search-it-jobs/?q=<keyword, spaces as +>`

   **Confirmed during testing: the `?q=` free-text param does NOT reliably filter by keyword** —
   searching "devops" returned 151 results dominated by unrelated Business Analyst, QA, and
   Salesforce postings alongside the few genuinely relevant ones. Client-side rendered — needs a
   short wait (~2s) after navigation before `get_page_text` returns real results instead of a
   loading placeholder.

   **The reliable filter is the "All Specializations" dropdown**, which maps to an `expertise=<N>`
   URL param (discovered via UI interaction: `expertise=3` = "Networks and Infrastructure", the
   closest category to DevOps/Cloud/SRE work — confirmed 64 results at test time). Prefer
   `https://www.sisystems.com/search-it-jobs/?expertise=3` (optionally combined with `&q=<keyword>`
   for extra narrowing) over keyword-only search. The specialization list also includes other
   categories (Architecture, Cyber Security, ERP, etc.) worth a one-time lookup if "Networks and
   Infrastructure" alone under- or over-returns on a given run — see the Specialization ID Table
   below.
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **No eligibility gate** — S.i. Systems only lists Canadian-market roles.
7. **Open each candidate posting** — `navigate` to the job's URL (from the "DETAILS" link,
   pattern `/jobs/<slug>/<encoded-id>/`). Confirmed during testing: `get_page_text` returns the
   full job description directly and cleanly — **no `find`+`read_page` workaround needed**.
   Extract title, company (often anonymized as "Our client"), full description, pay rate (shown
   as "Pay Rate: Salary: Negotiable" for many Permanent roles, or an explicit `$X-$Y/hr` for many
   Contract roles), job type (Contract vs. Permanent), and location.
8. **Quick-score each posting** 0–10, same skill/domain-first philosophy as the other `/check-*`
   commands. **Job Type is a first-class signal here** — S.i. Systems lists both Contract and
   Permanent roles; Contract roles align directly with the consulting-engagement preference in
   `profile.md` and should not be penalized for being agency-sourced.
9. **Present a single table** (no eligibility split needed) sorted highest score first, including
   a Job Type column.
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Specialization ID Table (partial, from initial testing)

| Specialization | `expertise=` value |
|---|---|
| Networks and Infrastructure | 3 |

Other IDs (Architecture, Cyber Security, Data Analytics, Software Development, etc.) weren't
captured during initial testing — look them up via the dropdown UI (`find` + `read_page` on the
"All Specializations" control) if a future run needs a category beyond Networks and Infrastructure.

## Edge Cases

- **Keyword search returns mostly noise** → prefer the `expertise=` specialization filter over
  free-text `q=`, per the note above. Don't silently trust result counts as relevance.
- **A posting's company is anonymized** ("Our client") → normal for a staffing agency, not a red
  flag; note it but don't penalize the score.
- **Permanent roles mixed in with Contract** → both are valid; flag Permanent roles as "FTE, not
  contract" per `profile.md`'s engagement-type preference, don't auto-exclude given the current
  lowered scoring bar.
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it.
- **Never click Apply or any write-side button** — read-only browsing only.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode.

## Out of Scope

- Trusting the `?q=` free-text search alone (use `expertise=` specialization filtering).
- Pagination beyond the first results page.
- Building out the full Specialization ID Table beyond what's needed for the DevOps-adjacent
  categories.
- Auto-filing high-scoring results without user confirmation.
