---
description: Search RemoteOK via Claude in Chrome, gate out region-ineligible postings before scoring using its flag-emoji region tags, then quick-score the rest — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-remoteok.md` / `plans/check-remoteok.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) instead of
`WebFetch`, because RemoteOK returns HTTP 403 to direct fetches (bot-blocking) but loads fine
through a real browser session — confirmed 2026-08-20, no login required.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

## 2. Open a tab

Call `tabs_context_mcp`, then `tabs_create_mcp` a new tab. No login check needed.

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

Bare titles, same rotation as `/check-indeed`, `/check-dice`, `/check-jobbank`, `/check-builtin`,
`/check-wwr`.

## 4. Search RemoteOK (per keyword)

`navigate` to:
```
https://remoteok.com/remote-jobs?search=<keyword, spaces as +>
```

**Always use this search endpoint — never a category-browse URL** (e.g. `/remote-devops-jobs`).
Confirmed during testing: category pages mix in large amounts of unrelated non-tech postings
(retail, hospitality, logistics) despite the category tag. The `?search=` endpoint returns much
more relevant, keyword-matched results.

`get_page_text` on the search-results page returns clean, complete data directly: title, company,
posted-date, **flag-emoji region list** (or "Worldwide"/"Probably worldwide"), and salary if shown
(many show "Upgrade to Premium to see salary" — treat as "not stated"). For the job link
(`/remote-jobs/<slug>-<numeric-id>` pattern), use `find` on the job title if it's not directly
visible in the `get_page_text` output.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results, skip it and move to the next keyword. If every keyword
(or the single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring or gating anything.

## 7. Region-eligibility gate, using the flag list captured in step 4

RemoteOK's flag-emoji list is a **reliable, consistent signal** (cross-checked listing page vs.
individual job page during testing — they matched). This is different from We Work Remotely,
whose "Anywhere in the World" tag turned out to be decorative and untrustworthy — do not repeat
that mistake here; RemoteOK's flags can be trusted directly off the search-results page.

- **🇨🇦 Canada explicitly in the flag list**, or **"Worldwide"/"Probably worldwide"** →
  **eligible**, proceed to step 8.
- **A flag/region list present but excluding Canada** (US-only, Europe-only, a single other
  country) → **ineligible** — do not open the full posting. Log title, company, and the reason
  ("region-restricted to X, excludes Canada").
- **No region info shown at all** → open the posting in step 8 to check; if still silent, mark
  eligible with a flag: "confirm regional eligibility before applying."

## 8. Open each eligible posting

`navigate` to the job's URL. **`get_page_text` returns the full, correct job description
directly here** — confirmed during testing, no `find`+`read_page` workaround is needed (unlike
`/check-wwr`, where `get_page_text` grabbed the wrong sidebar content). Extract title, company,
full description, salary if shown, engagement type, and re-confirm the flag list.

**The flag tag is not always trustworthy even when it says "Worldwide"/"Probably worldwide"** —
confirmed via a full-rotation run (2026-08-20) that found 3 such-tagged postings with hidden bias
only visible in the body (Life360: "within the US"; MinIO: "US West" in the title itself;
Wikimedia Foundation: opened with "San Francisco, United States") and one (Cohere) requiring
Middle East residency and Arabic fluency despite the tag. **Always skim the opened body for a
contradicting location/citizenship/language requirement and downgrade to ineligible if found —
don't stop at the tag once the posting is open.**

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **Posting fails to load** → mark "couldn't fetch," continue with the rest — skip the gate for
  it too.
- **Never click Apply or any other write-side button** — read-only navigation and text
  extraction only, at every step of this command.

## 9. Quick-score each eligible posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics (below-target pay, unclear terms) don't drag the score down — flag them
instead. **Note staffing-marketplace postings (e.g. Lemon.io — a freelance developer marketplace,
not a direct employer) as a flag, not a disqualifier** — they can fit the contract/consulting
engagement preference well. One sentence rationale per posting.

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

Close the RemoteOK tab at the end of the run — success, empty-result, or early-stop path alike.
