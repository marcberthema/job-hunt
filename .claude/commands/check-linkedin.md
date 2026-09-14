---
description: Search LinkedIn Jobs via Claude in Chrome (your logged-in session), fetch every result, and produce a quick-score table — no files written until you pick which postings to file
argument-hint: [search phrase, e.g. "platform engineer remote" — optional, defaults to the full phrase rotation]
---

Implements `specs/check-linkedin.md` / `plans/check-linkedin.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) instead of
`WebFetch`, because LinkedIn sits behind an auth wall that plain fetching can't clear.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,WebSearch
```
`WebSearch` is used later (step 7) to recover a canonical employer-page URL when a LinkedIn
posting fails to load or is expired.

## 2. Open a tab and confirm login

Call `tabs_context_mcp` for context, then `tabs_create_mcp` a new tab. `navigate` to
`https://www.linkedin.com/feed/`. Use `get_page_text` to check what loaded:

- Feed content (posts, "Start a post" box, etc.) → logged in, continue.
- A login/join page → **stop here**. Tell the user: "You're not logged into LinkedIn in Chrome —
  log in and re-run `/check-linkedin`." Close the tab and end the command. Do not attempt to log
  in on the user's behalf.

## 3. Parse input

`$ARGUMENTS` is optional.

- Non-empty → single custom query, run steps 4–5 once for it.
- Empty → run steps 4 once per keyword in the default rotation below, then dedupe (step 6) before
  continuing.

### Default phrase rotation

```
DevOps Consultant Remote
Senior Site Reliability Engineer Remote
Platform Engineer Remote
Cloud Engineer Remote
DevSecOps Engineer Remote
Forward Deployed Engineer Remote
```

**This is a full natural-language phrase rotation, not bare titles** — confirmed against Marc's
real LinkedIn alert emails (2026-08-20). The first two entries are verbatim from real alerts; the
rest follow the same `"<Role> Remote"` pattern. Do not shorten these to bare titles like the other
`/check-*` commands' rotations — the phrase form and "Remote" suffix are what make LinkedIn's
semantic search actually work (bare titles under-return badly; see `specs/check-linkedin.md` for
the comparison data).

## 4. Search LinkedIn (per keyword)

`navigate` to:
```
https://www.linkedin.com/jobs/search/?keywords=<phrase, spaces as %20>&geoId=101174742&f_TPR=r172800&sortBy=DD
```
- `geoId=101174742` — the broad "Canada" geo used by Marc's real alerts. Do not substitute
  `location=Canada` text or a city-specific `geoId`; the broad geoId returns equal-or-better
  results than city-anchored versions.
- `f_TPR=r172800` — postings from the **past 2 days** (confirmed preference, 2026-08-20).
- No `f_WT` (remote) filter param — "Remote" is already part of the keyword phrase itself.

**Scroll the results panel before reading it.** The unscrolled view shows the same handful of
"recently viewed/recommended" cards regardless of the keyword in the URL — genuinely
keyword-relevant results only appear after scrolling. Use `computer` (`action: scroll`) targeted
at the results-list column (the left panel, not the whole page) at least twice, ~10 ticks each.
Then use `read_page` (filter: `interactive`) to extract each result's title, company, location,
and job ID from the `/jobs/view/<id>/` links — `get_page_text` doesn't expose hrefs, so
`read_page` is required for this step.

- **Single custom query**: cap at first 20 results (post-scroll).
- **Default rotation**: cap at first **12** results per keyword (post-scroll).

Result volumes are much higher with phrase queries (42-99+ observed per keyword) — scroll enough
to comfortably clear the cap before extracting; a couple of extra scroll passes is cheap insurance.

Clicking to page 2+ via the numbered pager is still out of scope — scrolling within page 1's
results panel is enough.

If a keyword returns no job links, skip it and move to the next keyword. If every keyword (or the
single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy), same rule as
`/check-builtin`.

## 6. Read profile.md

Read `profile.md` in full before scoring anything.

## 7. Open each posting

For each deduped result, `navigate` directly to `https://www.linkedin.com/jobs/view/<job-id>/`
(not by clicking through the UI), then **scroll down a few ticks before calling
`get_page_text`** — the description body lazy-loads and stays as skeleton placeholders right
after navigation even with a multi-second wait; scrolling reliably triggers it to render. Extract:
title, company, location, remote/hybrid/onsite status, salary/rate if shown, engagement type, and
enough of the description to score.

- **Challenge/CAPTCHA/"verify it's you" page detected instead of job content** → stop the entire
  run immediately. Tell the user exactly what happened and which job ID triggered it. Do not
  continue to remaining postings, do not attempt to solve it.
- **"No longer accepting applications" or failed load** → before marking it expired, try a quick
  web search for the exact title + company to find the employer's own careers page — if found,
  prefer that as the canonical URL (LinkedIn listings frequently outlive their real application
  window) and confirm the details still match. Otherwise mark "couldn't fetch / expired" and
  continue with the rest.
- **Never click Easy Apply, Apply, Save, Follow, or any other write-side button** — read-only
  navigation and text extraction only, at every step of this command.

## 8. Quick-score each (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (on-site, below-target pay) don't drag the score down — flag them
instead. One sentence rationale per posting.

## 9. Present the table

Sorted highest score first:

| Role — Company | Score | Why | Flags |
|---|---|---|---|

No files are written at this step.

## 10. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 7 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 11. Close the tab

Close the LinkedIn tab at the end of the run — success, empty-result, or early-stop path alike.
