# Spec: `/check-remoteok` — RemoteOK Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

RemoteOK returns HTTP 403 via `WebFetch` (bot-blocking — see `job_sources.md`, "Not usable"
table). Tested via Claude in Chrome (2026-08-20): loads cleanly, no login required, no CAPTCHA.
Same worldwide-remote-board shape as We Work Remotely, so the same region-eligibility problem
applies — but RemoteOK's region tagging turned out far more reliable during testing: every
listing (both on the results list and the individual job page) shows a consistent flag-emoji
country list or "Worldwide"/"Probably worldwide," and this list is the *actual* eligibility
signal (unlike WWR's decorative "Anywhere in the World" tag — see `specs/check-wwr.md`'s
correction). A genuinely Canada-eligible DevOps posting (Lemon.io, flags including 🇨🇦) and a
Canadian company's own posting (Shakepay, 🇨🇦) both turned up in initial testing.

## Capability

Same shape as `/check-wwr`: optional search query (defaults to the shared role rotation), searches
RemoteOK, runs a region-eligibility gate before scoring using the flag-emoji list, and reports
eligible postings scored plus ineligible ones logged with reason. Drives Chrome instead of
`WebFetch`.

## Usage

```
/check-remoteok [search terms]
```

- `/check-remoteok` (no arguments) — runs the default role rotation (bare titles, same list as
  `/check-indeed`/`/check-dice`/`/check-wwr`: DevOps Engineer, Platform Engineer, Site Reliability
  Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer).
- `/check-remoteok platform engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required.
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://remoteok.com/remote-jobs?search=<keyword, spaces as +>`
   Confirmed during testing this is far cleaner than browsing a category page directly (e.g.
   `/remote-devops-jobs`) — category pages are heavily polluted with unrelated non-tech listings
   (retail, hospitality, logistics jobs mixed in with "DevOps" tag). Always use the `?search=`
   query, not category browsing. `get_page_text` on the search-results page returns clean,
   complete listing data directly, including each result's flag-emoji region list and salary (if
   shown — many are "Upgrade to Premium to see salary," treat as "not stated").
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **Region-eligibility gate BEFORE scoring**, using the flag-emoji list already visible in the
   search results (confirmed reliable and consistent — no need to open the posting first, unlike
   WWR):
   - **🇨🇦 Canada explicitly listed**, or **"Worldwide"/"Probably worldwide"** → eligible.
   - **A flag/region list that excludes Canada** (e.g. only 🇺🇸 US, only European flags, a single
     non-Canada country) → **ineligible** — skip, no need to open the full posting.
   - **No region info at all shown** (rare — some postings show only a city or nothing) → open
     the posting to check; if still silent, mark eligible with a flag: "confirm regional
     eligibility before applying."
7. **Open each eligible posting** — `navigate` to the job's URL (from the results list link,
   pattern `/remote-jobs/<slug>-<numeric-id>`). Confirmed during testing: `get_page_text` returns
   the full job description directly and cleanly — **no `find`+`read_page` workaround needed
   here**, unlike WWR. Extract title, company, full description, salary if shown, and the flag
   list again for a final confirmation.

   **Correction from a full-rotation live run (2026-08-20): the flag tag alone is not always
   trustworthy, even though it's far better than WWR's.** Three "Worldwide"/"Probably worldwide"
   -tagged postings turned out to have hidden bias only visible in the body: Life360 said
   "within the US" explicitly, MinIO's own title said "US West," and Wikimedia Foundation's
   listing opened with "San Francisco, United States." Cohere's "Probably worldwide"-tagged
   Forward Deployed Engineer posting required Middle East residency and Arabic fluency. **Always
   skim the opened body for a contradicting location/citizenship/language line, even when the tag
   said eligible** — downgrade to ineligible if found, same as any other gate failure.
8. **Quick-score each eligible posting** 0–10, same skill/domain-first philosophy as the other
   `/check-*` commands. Note staffing-marketplace postings (e.g. Lemon.io — a freelance developer
   marketplace, not a direct employer) as a flag, not a disqualifier — they can fit the
   contract/consulting engagement preference well.
9. **Present two tables**: eligible sorted highest score first, ineligible listed separately with
   reason only (not scored).
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **A single keyword's search returns no relevant results** → skip it, continue the rotation.
- **Every keyword (or the single custom query) returns nothing** → report it, stop.
- **Old postings** (some results were 7-10 months old during testing) → don't auto-exclude by
  age, but note the posted-date in the table so the user can judge staleness; very old postings
  (6+ months) are worth flagging as "may be filled/stale, verify before applying."
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it.
- **Never click Apply or any write-side button** — read-only browsing only.

## Region-Eligibility Gate — Design Note

Same rationale as `/check-wwr`'s gate, but RemoteOK's flag-emoji list is trustworthy where WWR's
tag wasn't — confirmed by cross-checking listing-page flags against individual job-page flags for
multiple postings during testing; they matched consistently. Still keep this gate local to
`/check-remoteok` rather than generalizing, per the same reasoning as the other gated sources.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode (pre-gate).

## Out of Scope

- Category-page browsing (use `?search=` only — confirmed cleaner).
- Pagination beyond the first results page.
- Extending the eligibility gate to other sources.
- Auto-filing eligible+high-scoring results without user confirmation.
