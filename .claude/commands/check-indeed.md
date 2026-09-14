---
description: Search Indeed via Claude in Chrome, fetch every result, and produce a quick-score table — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-indeed.md` / `plans/check-indeed.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) instead of
`WebFetch`, because Indeed started returning HTTP 403 to direct fetches as of 2026-09-08
(confirmed again 2026-09-13, two consecutive runs — no longer a transient blip) but loads fine
through a real browser session, same pattern as RemoteOK/WWR/LinkedIn/S.i. Systems. No login
required.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,WebSearch
```
`WebSearch` is used later (step 8) to recover a canonical employer-page URL when an Indeed
posting fails to load or looks stale.

## 2. Open a tab

Call `tabs_context_mcp`, then `tabs_create_mcp` a new tab. No login check needed.

## 3. Parse input

`$ARGUMENTS` is optional. Location is always `Remote` — not a user-supplied argument.

- Non-empty → single custom query, run steps 4–5 once for it.
- Empty → run step 4 once per keyword in the default rotation below, then dedupe (step 5).

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

Bare titles, same rotation as `/check-dice`, `/check-jobbank`, `/check-builtin`, `/check-wwr`,
`/check-remoteok`. Update this list directly in this file if Marc's positioning changes — no need
to touch the spec/plan for a wording tweak.

## 4. Search Indeed (per keyword)

`navigate` to:
```
https://ca.indeed.com/jobs?q=<keyword, spaces as +>&l=Remote
```

Client-side elements may lazy-load — after `navigate`, `wait` ~2 seconds before calling
`get_page_text`, or you may get a partial/placeholder render.

`get_page_text` should return each result's title, company, location, and snippet directly.
Job-posting links (`/viewjob?jk=`, `/rc/clk`, or `pagead/clk` — treat bare `pagead/clk` links
with no `jk=` param as unstable per the caveat below) are **not always present in the plain text
output** — use `find` on each result's title to get a clickable element ref/URL for step 8.
Discard non-job links (ads for courses, employer resource pages, etc.).

**Prefer links containing `/viewjob?jk=` or `/rc/clk?jk=` over bare `pagead/clk` links (no `jk=`
param)** — a prior run found a filed posting's `Source` was an ad-tracking link that had already
rotated to a completely unrelated job by review time. If only a bare `pagead/clk` link is
available for a result, still open it via `find`-then-click to reach the real content (`navigate`
follows the redirect to the actual posting), but record the final resolved URL in the table, not
the ad-tracking one.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results, skip it and move to the next keyword. If every keyword
(or the single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Postings often show up under more than one keyword (e.g. a "Platform Engineer" posting also
surfaces under "DevOps Engineer"). Before opening full postings, dedupe the combined result list
by company + title (case-insensitive, ignore minor punctuation differences) so each unique
posting is only opened and scored once.

## 6. Read profile.md

Read `profile.md` in full before scoring anything — same hard requirement as `/addjob`.

## 7. No eligibility gate

Indeed's `l=Remote` param is scoped to `ca.indeed.com`, so results are Canada-market by
construction — same reasoning as `/check-eluta`. Skip straight to opening postings and scoring,
but stay alert for explicit provincial/regional residency requirements buried in posting body text
(a hard-gate red flag in `profile.md`) — flag these when found rather than silently scoring past
them.

## 8. Open each candidate posting

Click the result (via the `find` ref from step 4) or `navigate` directly if you already have the
resolved URL. Extract title, company, location, remote/hybrid/onsite status, salary/rate if
stated, engagement type, and enough of the responsibilities/requirements to score.

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **Posting fails to load, looks stale, or is a sponsored/expired listing** → before giving up,
  try a quick web search for the exact title + company to find the employer's own careers page.
  If found, treat the employer's page as the canonical source (use its URL in the results table
  and any filed job, not the Indeed link) — employer pages don't rotate/expire the way aggregator
  listings do, and confirm the same role/details still match before treating it as validated. If
  no employer page turns up, mark "couldn't fetch" and continue with the rest.
- **Never click Apply or any other write-side button** — read-only navigation and text
  extraction only, at every step of this command.

## 9. Quick-score each (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (on-site, below-target pay) don't drag the score down — flag them
instead. Keep the rationale to **one sentence** per posting — this is a scan, not the full
`/addjob` writeup.

## 10. Present the table

Sorted highest score first. In rotation mode, note in the intro line how many keywords were
searched and how many unique postings came back — no need to repeat which keyword(s) surfaced
each posting, the dedupe in step 5 already collapsed that.

| Role — Company | Score | Why | Flags |
|---|---|---|---|

No files are written at this step.

## 11. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 8 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path — same as `/addjob`.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 12. Close the tab

Close the Indeed tab at the end of the run — success, empty-result, or early-stop path alike.
