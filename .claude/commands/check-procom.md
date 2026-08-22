---
description: Search Procom (Canadian IT staffing agency) via Claude in Chrome, run a lightweight US-location eligibility gate before scoring, then quick-score the rest — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-procom.md` / `plans/check-procom.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools). Procom's public
marketing site (`procom.ca/find-jobs/`) is a dead end — it redirects to a broken client-portal
shell that never resolves to real content. **The real jobs portal is a different subdomain**,
confirmed 2026-08-20, no login required to browse:
```
https://myprocom-portal.procomservices.com/jobs?loginType=contractor&lang=en
```

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

## 4. Search Procom (per keyword)

`navigate` to:
```
https://myprocom-portal.procomservices.com/jobs?keyword=<keyword, spaces as +>
```

Confirmed during testing: this works and returns relevant results ("devops" → 24 results
including real "DevOps Engineer" and "Senior Cloud DevOps Engineer" titles). Each result card
shows a **remote/hybrid/onsite tag** directly, plus title, location, posted-date, and pay rate
when disclosed (`$X-$Y/hr CAD` format).

**`get_page_text` only returns the first visible card's content, not the full list** — confirmed
during testing. Use `read_page` (filter: `interactive`) to get job title/link elements for all
visible results, or repeated `find` calls, before deciding which to open.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no relevant results, skip it and move to the next keyword. If every keyword
(or the single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring or gating anything.

## 7. Lightweight eligibility gate

Procom is a Canadian staffing agency, but **some US postings mix in** — confirmed during testing
(Colorado Springs, Raleigh NC postings turned up in a plain "devops" search). Use the location
field shown per result:

- **Canadian city/province**, or **"Remote"** with no US-specific qualifier → **eligible**,
  proceed to step 8.
- **US city/state shown** → open the posting first (step 8) to check for an explicit "open to
  Canada-based remote candidates" line before excluding. If silent or explicitly US-only →
  **ineligible** — log title, company, and reason ("US-based posting, no stated Canada
  eligibility").

## 8. Open each eligible posting

Click the job title/link element found via `read_page`/`find` in step 4. Extract title, company
(often just "Procom" — client name may or may not be disclosed, normal for a staffing agency, not
a red flag), full description, pay rate, job type (remote/hybrid/onsite), and location.

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
ticket-taking. One sentence rationale per posting.

## 10. Present two tables

**Eligible**, sorted highest score first:

| Role — Company | Score | Job Type | Why | Flags |
|---|---|---|---|---|

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
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the client is anonymized, use
  `procom` as the company slug unless the full posting reveals the real client name.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 12. Close the tab

Close the Procom tab at the end of the run — success, empty-result, or early-stop path alike.
