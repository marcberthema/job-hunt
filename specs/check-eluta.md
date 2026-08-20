# Spec: `/check-eluta` — Eluta.ca Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

Eluta.ca's search results are visible via `WebFetch` (title/company/salary/snippet all present),
but every job title link is a JavaScript fragment (`href="#!"`) with no real URL — `WebFetch`
can't drill into individual postings. Tested via Claude in Chrome (2026-08-20): the search page
works cleanly with no login required, and — critically — **each result also carries a "See how
this page looked when Eluta indexed it" link that opens a genuinely fetchable cached copy of the
full posting** in a new tab (`https://www.eluta.ca/cache?u=<id>:<domain>`), served by Eluta
itself. This sidesteps both the `#!` fragment problem and any bot-blocking the original employer
site might have. The direct job-title link was tested and does **not** reliably open anything on
a synthetic click — use the cache link instead, every time.

Eluta.ca aggregates from Canadian employer career pages, so unlike LinkedIn/WWR/RemoteOK/
Braintrust, **results are inherently Canada-scoped already — no region-eligibility gate is
needed** for this source.

## Capability

Same shape as the other Chrome-driven `/check-*` commands: optional search query (defaults to the
shared role rotation), searches Eluta, opens each result's cached copy, and reports a quick-score
table. No eligibility gate (see above) — every result is presumed Canada-relevant by construction,
though on-site/hybrid location still needs the usual `profile.md` reachable-range check during
scoring, same as any other source.

## Usage

```
/check-eluta [search terms]
```

- `/check-eluta` (no arguments) — runs the default role rotation (bare titles, same list as
  `/check-indeed`/`/check-dice`/`/check-wwr`/`/check-remoteok`/`/check-braintrust`).
- `/check-eluta devops engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required.
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://www.eluta.ca/search?q=<keyword, spaces as +>&filter-remote_jobs=only`
   Do **not** add a `l=Canada` location param — confirmed during testing that `l=Canada` breaks
   the search ("The location you entered does not exist in our database"). Leave location blank;
   results are already Canada-only by the site's nature. **Always add `filter-remote_jobs=only`**
   — confirmed during testing this is a real, working filter (found via the site's own "Remote"
   dropdown) that cuts a noisy 1,700+-result unfiltered search down to a focused, genuinely
   remote-only set (191 for "devops engineer") without losing relevant results — a clear win over
   scoring on-site postings that fail the reachable-range check anyway. `get_page_text` on the
   results page returns clean, complete listing data directly: title, company, city/province
   (or "Work Remotely"), salary if shown, a snippet, and posted-time. Cap at the first page (10
   results) per keyword in rotation mode, first page for a single custom query too (page 2+ is
   out of scope, same as the other sources).
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **Open each posting's cached copy** — for each result, locate the **"See how this page looked
   when Eluta indexed it" link** (via `find`, since it's not distinguishable by plain text scan —
   query something like "cached page link for <job title> at <company>"), then click it. This
   opens a **new tab** at `https://www.eluta.ca/cache?u=<id>:<domain>` — call `tabs_context_mcp`
   after the click to discover the new tab's ID, then `get_page_text` on that tab for the full,
   clean posting content. **Do not click the job title link itself** — confirmed during testing
   it doesn't reliably fire on a synthetic click and produces no navigation.

   **Two corrections from a full live run (2026-08-20):**
   - **Not every result has a cache link.** Confirmed several results in a row (5th+ position)
     simply had no "See how this page looked..." link in the accessibility tree at all — only
     "Email." When this happens, don't force it — score from the search-results snippet alone and
     flag "full posting not fetchable, scored from listing summary."
   - **Some cache pages refuse to render** ("This cached document can not be displayed directly" —
     seen for Workday-hosted postings specifically). When that happens, `find` the "here" link in
     that message (or construct it directly) and navigate to
     `https://www.eluta.ca/cache_open?u=<same id>:<same domain>` instead of `cache?u=...` — this
     returns the raw underlying data (confirmed: a JSON payload for the Workday case, fully
     readable via `get_page_text` including the full job description field) even when the pretty
     rendered view fails.
7. **Quick-score each posting** 0–10, same skill/domain-first philosophy as the other `/check-*`
   commands. Since there's no eligibility gate, apply `profile.md`'s on-site/hybrid
   reachable-range check here as part of normal scoring (same as any Indeed/BuiltIn result).
8. **Close each cache tab** after extracting its content, before moving to the next posting —
   don't accumulate open tabs across the run.
9. **Present a table**, sorted highest score first. No files written.
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **A single keyword's search returns no results** → skip it, continue the rotation.
- **Every keyword (or the single custom query) returns nothing** → report it, stop.
- **A cache link fails to open a new tab, or the new tab shows an error/empty page** → mark
  "couldn't fetch," close the tab if it opened, continue with the rest.
- **reCAPTCHA or a blocking page appears** → stop the run, tell the user, don't attempt to solve.
- **Never click "APPLY FOR THIS JOB"** (visible on the cached copy) or the "Email" link — those
  are the read-only boundary here, same as every other Chrome-driven source.

## Out of Scope

- Pagination beyond the first results page.
- A region-eligibility gate (not needed — see Problem section).
- Auto-filing high-scoring results without user confirmation.
