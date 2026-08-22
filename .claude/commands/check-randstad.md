---
description: Browse Randstad Canada's Technologies job category via Claude in Chrome (keyword search is broken on this site, so this filters client-side), no eligibility gate needed (Canada-only by construction), then quick-score matches in a table — no files written until you pick which postings to file
argument-hint: [filter term — optional, defaults to the full role rotation used as filter terms]
---

Implements `specs/check-randstad.md` / `plans/check-randstad.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools). **Unlike the
other `/check-*` commands, this one cannot drive a site-side keyword search** — `randstad.ca`'s
own `?query=` free-text search returns 0 results even for common terms like "devops" (confirmed
2026-08-20). Instead, it browses the Technologies category page and filters client-side.

`randstaddigital.com`'s own careers flow is broken (dead-ends at a country-picker link that
doesn't navigate) — **always use `randstad.ca/jobs/s-technologies/` directly**.

## 1. Load Chrome tools

One `ToolSearch` call, before anything else:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

## 2. Open a tab

Call `tabs_context_mcp`, then `tabs_create_mcp` a new tab. No login check needed.

## 3. Parse input

`$ARGUMENTS` is optional and used as a **client-side filter term**, not a search query.

- Non-empty → filter the browsed category listing for this term only.
- Empty → filter using the full default rotation as match terms.

### Default role rotation (filter terms)

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

## 4. Navigate once to the Technologies category

```
https://www.randstad.ca/jobs/s-technologies/
```

Confirmed during testing: loads directly with real listings (title, location, job type
Contract/Permanent, pay rate when disclosed, posted-date). **Do not attempt `?query=` free-text
search on this domain** — confirmed 0 results even for "devops." The category-browse page is the
only reliable path.

## 5. Enumerate results

Use `get_page_text` or `read_page` to extract the ~30 postings shown on the first page (520 total
exist across the full category — only the first page is in scope for this command).

## 6. Client-side filter

Scan titles/summaries for matches against the filter term(s) from step 3. Most results will be
unrelated (BA, PM, Data Engineer, Salesforce, etc.) — this is a broad "Technologies" category,
not DevOps-specific, similar noise profile to Job Bank's NOC-code matching. Keep only titles/
summaries that plausibly match DevOps/Cloud/Platform/SRE/Infrastructure work.

## 7. Read profile.md

Read `profile.md` in full before scoring anything.

## 8. No eligibility gate

`randstad.ca` (not `.com`/`randstaddigital.com`) is the Canadian-market site — postings shown are
Canada-scoped by construction.

## 9. Open each candidate posting

Click through to the job detail page for each result kept in step 6. Extract title, company
(often "Our client" — normal for a staffing agency, not a red flag), full description, pay rate,
job type, and location.

- **CAPTCHA or a blocking page appears instead of job content** → stop the entire run
  immediately. Tell the user exactly what happened and which posting triggered it. Do not
  continue, do not attempt to solve it.
- **Posting fails to load** → mark "couldn't fetch," continue with the rest.
- **Never click Apply or any other write-side button** — read-only navigation and text
  extraction only, at every step of this command.

## 10. Quick-score each candidate posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. **Job Type is a first-class signal** — Contract roles align with the
consulting-engagement preference; flag Permanent roles as FTE but don't auto-exclude given the
current lowered scoring bar. One sentence rationale per posting.

## 11. Present one results table

No eligible/ineligible split needed (no gate ran). Sort highest score first:

| Role — Company | Score | Job Type | Why | Flags |
|---|---|---|---|---|

No files are written at this step.

## 12. Offer to go deeper

Ask the user which posting(s), if any, should get the full `/addjob` treatment. For each one
picked:

- Run the duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`.
  Warn and confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 9 — don't re-navigate.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), including the `Flags` field, written to
  `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`. When the company is anonymized, use
  `randstad` as the company slug unless the full posting reveals the real client name.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 13. Close the tab

Close the Randstad tab at the end of the run — success, empty-result, or early-stop path alike.
