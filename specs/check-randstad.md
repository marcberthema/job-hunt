# Spec: `/check-randstad` — Randstad Canada Technologies Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

`randstaddigital.com` (Randstad's specialized tech-staffing brand) has a broken careers flow — its
"current opportunities" page dead-ends at a country-picker link ("canada") that doesn't actually
navigate anywhere via Chrome. **The working path is the general `randstad.ca` domain's
Technologies category**: `randstad.ca/jobs/s-technologies/`, confirmed 2026-08-20 — 520 real
Technologies jobs at test time, mostly Contract, real Canadian rates shown per posting, regional
breakdown by province. Free-text `?query=` search on `randstad.ca` returned **0 results** for
"devops" — the category-browse page is the reliable path, not keyword search (same
"keyword-search-broken, category-browse-works" pattern seen on S.i. Systems).

## Capability

Same overall shape as `/check-sisystems`: browses the Technologies category via Chrome (no
reliable keyword search available), filters client-side by scanning titles/skills for DevOps/
Cloud/SRE relevance, then quick-scores matches. **No eligibility gate needed** — `randstad.ca` is
the Canadian-market site (as opposed to `randstaddigital.com`'s global one), so postings are
Canada-scoped by construction.

## Usage

```
/check-randstad [search terms]
```

- `/check-randstad` (no arguments) — browses the Technologies category and filters for the
  default role rotation's keywords across titles/descriptions.
- `/check-randstad platform engineer` — same category browse, filtered to that term only.

Unlike the other `/check-*` commands, **the search term filters client-side against the browsed
category listing rather than driving a site search** — Randstad's own keyword search doesn't
work reliably.

## Behavior

1. **Load Chrome tools, open a tab** — no login required.
2. **Navigate to the Technologies category**:
   `https://www.randstad.ca/jobs/s-technologies/`
   Confirmed during testing: this loads directly, no wait needed beyond normal page load, and
   shows real listings with title, location, job type (Contract/Permanent), pay rate (when
   disclosed), and posted-date directly on the results page.
3. **Do NOT rely on `?query=` free-text search** — confirmed during testing it returns 0 results
   even for common terms like "devops" on this domain. Browse the category page(s) directly
   instead.
4. **Client-side filter** — scan the ~30 results shown per page (520 total exist; only the first
   page is in scope for this command, see Out of Scope) for titles/summaries matching the
   rotation keywords or the custom query term. Most results will be unrelated (BA, PM, Data
   Engineer, Salesforce, etc. — this is a broad "Technologies" category, not DevOps-specific) —
   this is expected noise, similar to Job Bank's NOC-code noise.
5. **Read `profile.md` first**.
6. **No eligibility gate** — `randstad.ca` (not `.com` or `randstaddigital.com`) is the Canadian
   site; postings shown are Canada-scoped.
7. **Open each candidate posting** — click through to the job detail page. Extract title, company
   (often "Our client" — normal for a staffing agency), full description, pay rate, job type
   (Contract/Permanent), and location.
8. **Quick-score each candidate posting** 0–10, same skill/domain-first philosophy as the other
   `/check-*` commands. Flag (don't penalize) Contract-type postings positively per the
   consulting-engagement preference; flag Permanent postings as FTE per the usual pattern.
9. **Present a single table** sorted highest score first, including a Job Type column.
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **The Technologies category page returns mostly noise** (expected — it's a broad category, not
  DevOps-specific) → don't over-open irrelevant postings; skim titles first before opening detail
  pages.
- **A posting's company is anonymized** ("Our client") → normal, not a red flag.
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it.
- **Never click Apply or any write-side button** — read-only browsing only.

## Limits

Scan the first page of Technologies results (~30 postings); open and score up to 15 that match
the query/rotation keywords by title/summary skim.

## Out of Scope

- Pagination beyond the first Technologies results page (520 total exist; revisit if first-page
  yield is consistently low).
- Trusting `?query=` free-text search (confirmed broken on `randstad.ca`).
- `randstaddigital.com`'s own broken careers flow.
- Auto-filing high-scoring results without user confirmation.
