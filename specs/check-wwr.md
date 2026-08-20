# Spec: `/check-wwr` — We Work Remotely Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

We Work Remotely returns HTTP 403 via `WebFetch` (active bot-blocking — see `job_sources.md`,
"Not usable" table). Tested via Claude in Chrome (2026-08-20): the site loads cleanly with a real
browser session, no login required, no CAPTCHA encountered. It's a curated remote-only board —
worth adding as the second Chrome-driven source after `/check-linkedin`.

Second finding from testing: WWR is a **worldwide** remote board, not Canada-specific. Postings
commonly restrict eligibility to a named region/country list (e.g. a European-countries flag list)
or say "Anywhere in the World." A large share of raw results are **structurally ineligible**
regardless of skill fit — same problem `/check-dice` solved for US-work-authorization postings.

## Capability

Same overall shape as `/check-dice`: optional search query (defaults to the shared role rotation),
searches We Work Remotely, and runs a **region-eligibility gate before scoring** — ineligible
postings are listed with the reason and not scored, not silently dropped. Drives Chrome
(`mcp__claude-in-chrome__*`) instead of `WebFetch` since the site blocks direct fetches.

## Usage

```
/check-wwr [search terms]
```

- `/check-wwr` (no arguments) — runs the default role rotation (same list as the other `/check-*`
  commands: DevOps Engineer, Platform Engineer, Site Reliability Engineer, Cloud Engineer,
  DevSecOps Engineer, Forward Deployed Engineer — bare titles, not LinkedIn-style phrases; WWR's
  search is plain keyword matching, not semantic).
- `/check-wwr platform engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login check needed (WWR requires no account to browse).
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://weworkremotely.com/remote-jobs/search?term=<keyword, spaces as +>`
   This loads cleanly and completely — confirmed no scrolling or lazy-load workaround needed on
   the search-results page (unlike LinkedIn). `get_page_text` works directly here, but **only
   returns the generic "Anywhere in the World" tag, not the specific location line** — that line
   only shows up via `find` + `read_page` on the individual result card (see the correction
   below). Extract each result's title, company, posted-date, engagement type, and salary (if
   shown) from `get_page_text`; extract the **specific location line** per candidate result via
   `find`/`read_page` before deciding eligibility (step 6).
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **Region-eligibility gate BEFORE scoring** — **correction from real-run testing (2026-08-20):
   `/check-wwr`'s first live run found that WWR shows the generic "Anywhere in the World" tag on
   nearly every posting regardless of actual eligibility — it is decorative, not a real signal,
   and must not be used to decide eligibility.** Sample: 8/8 DevOps/Platform-titled postings
   checked all carried that tag while also showing a specific non-Canada location (Bengaluru,
   India; Paris, France; Remote/Teleworker US-only; Ahmedabad, India; Romania; Malta) — every one
   of them was actually region-restricted despite the tag.

   The real signal is the **specific location line** shown per result card (e.g. "Remote India,
   IN", "Paris, France", "6314 Remote/Teleworker US") — get to it via `find` (e.g. "job link at
   \<company\>") then `read_page` on that ref, not `get_page_text` (which only surfaces the
   generic tag). For each deduped result:
   - **Specific location line names Canada, "Worldwide," or is absent/blank** → treat as
     provisionally eligible, but if blank/absent still open the full posting (step 8) to look for
     an explicit region statement before finalizing.
   - **Specific location line names a single non-Canada country/city, or a region list that
     excludes Canada** (India, a European country, "US-only," etc.) → **ineligible** — skip, no
     need to open the full posting. Do not let the "Anywhere in the World" tag override this.
   - **Specific location line names a broad multi-country descriptor that plausibly includes
     Canada** (e.g. "North America Only," a flag-emoji list that includes Canada) → eligible,
     proceed.
7. **For eligible postings only**, open each one — navigate directly to
   `https://weworkremotely.com/remote-jobs/<slug>` (from the results list link, pattern
   `/remote-jobs/<company-slug>-<role-slug>`). **`get_page_text` picks the wrong content on job
   detail pages** — confirmed during testing: it grabs a sidebar/related-jobs `<article>` instead
   of the actual description. Use `find` with a query like "job description main content
   container" to locate the real description region, then `read_page` on that ref_id. Extract
   title, company, full description, salary if shown, and engagement type (Full-Time/Contract).
8. **Quick-score each eligible posting** 0–10, same skill/domain-first philosophy as the other
   `/check-*` commands.
9. **Present a table**: eligible postings sorted highest score first, ineligible postings listed
   separately below with just the reason (not scored) — same reporting shape as `/check-dice`.
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **A single keyword's search returns no job links** → skip it, continue the rotation.
- **Every keyword (or the single custom query) returns nothing** → report it, stop.
- **Individual posting fetch fails** → mark "couldn't fetch," don't drop it or abort the batch,
  don't run it through the gate (nothing to check).
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it (same rule as `/check-linkedin`).
- **Never click Apply / "AI Auto-Apply" / Save job** — read-only browsing only, same as
  `/check-linkedin`.

## Region-Eligibility Gate — Design Note

Same rationale as `/check-dice`'s eligibility gate (see that spec) but for a different failure
mode: WWR postings restrict by *region*, not work authorization or clearance. Keep this gate local
to `/check-wwr` rather than generalizing — the disqualifying condition is source-specific.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode (pre-gate; the gate then
narrows this further before any scoring effort is spent).

## Out of Scope

- Pagination beyond the first results page.
- Extending the eligibility gate to other sources.
- Auto-filing eligible+high-scoring results without user confirmation.
