---
description: Search We Work Remotely via Claude in Chrome, gate out region-ineligible postings before scoring, then quick-score the rest — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-wwr.md` / `plans/check-wwr.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) instead of
`WebFetch`, because We Work Remotely returns HTTP 403 to direct fetches (bot-blocking) but loads
fine through a real browser session — confirmed 2026-08-20, no login required.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

## 2. Open a tab

Call `tabs_context_mcp`, then `tabs_create_mcp` a new tab. No login check needed — We Work
Remotely is fully browsable without an account.

## 3. Parse input

`$ARGUMENTS` is optional.

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

Bare titles — **not** the LinkedIn-style natural-phrase rotation. WWR's search is plain keyword
matching, not semantic search, so bare titles are correct here. Same rotation list as
`/check-indeed`, `/check-dice`, `/check-jobbank`, `/check-builtin`.

## 4. Search We Work Remotely (per keyword)

`navigate` to:
```
https://weworkremotely.com/remote-jobs/search?term=<keyword, spaces as +>
```
This loads fully rendered with no scroll or lazy-load workaround needed — `get_page_text` on the
search-results page returns clean, complete data directly (confirmed during testing; unlike
LinkedIn, no scrolling trick is required here).

Extract per result via `get_page_text`: title, company, posted-date, engagement type
(Full-Time/Contract), salary if shown. **`get_page_text` only surfaces the generic "Anywhere in
the World" tag, not the real per-posting location** — for the job link and the actual **specific
location line** (e.g. "Remote India, IN", "Paris, France", "6314 Remote/Teleworker US"), call
`find` with a query like "\<title\> job link at \<company\>" for each candidate result, then
`read_page` on the matched ref. Do this for every result you keep after an initial title skim —
it's required for the gate in step 7, since the generic tag alone is not trustworthy (see below).

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no results, skip it and move to the next keyword. If every keyword (or the
single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring or gating anything.

## 7. Region-eligibility gate — BEFORE opening/scoring each posting

**Corrected 2026-08-20 after the first live run:** WWR shows the generic "Anywhere in the World"
tag on nearly every posting regardless of actual eligibility — confirmed by sampling 8
DevOps/Platform-titled postings, all 8 carried that tag while each was *also* restricted to a
single non-Canada location (Bengaluru India, Paris France, US-only, Ahmedabad India, Romania,
Malta, etc.). **Never treat "Anywhere in the World" as an eligibility signal.**

Use the **specific location line** you extracted per-result in step 4 instead:

- **Names Canada, "Worldwide," or is blank/absent** → provisionally eligible. If blank, still
  open the full posting in step 8 and look for an explicit region statement before finalizing.
- **Names a single non-Canada country/city, or a region list that excludes Canada** (India, a
  European country, "US-only," etc.) → **ineligible** — do not open the full posting. Log title,
  company, and the reason ("region-restricted to X, excludes Canada"). No scoring effort spent on
  it, and the generic tag does not override this call.
- **Names a broad multi-country descriptor that plausibly includes Canada** (e.g. "North America
  Only," a flag-emoji list containing Canada) → eligible, proceed to step 8.

## 8. Open each eligible posting

`navigate` to `https://weworkremotely.com/remote-jobs/<slug>`.

**Do not rely on `get_page_text` here** — confirmed during testing that it grabs the wrong
`<article>` element (a related-jobs sidebar, not the real description). Instead:

1. Call `find` with a query like "job description main content container."
2. Call `read_page` with that result's `ref_id` to extract the actual description (Role Purpose /
   Responsibilities / Qualifications sections), salary, and engagement type.

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **Posting fails to load / 404s** → mark "couldn't fetch," continue with the rest — skip the
  gate for it too, since there's nothing to check.
- **Never click Apply, "AI Auto-Apply," or Save job** — read-only navigation and text extraction
  only, at every step of this command.

## 9. Quick-score each eligible posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (below-target pay, unclear hybrid terms) don't drag the score down —
flag them instead. One sentence rationale per posting.

## 10. Present two tables

**Eligible**, sorted highest score first:

| Role — Company | Score | Why | Flags |
|---|---|---|---|

**Ineligible** (not scored), listed separately below:

| Role — Company | Reason |
|---|---|

No files are written at this step.

## 11. Offer to go deeper

Ask the user which eligible posting(s), if any, should get the full `/addjob` treatment. For each
one picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 8 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 12. Close the tab

Close the We Work Remotely tab at the end of the run — success, empty-result, or early-stop path
alike.
