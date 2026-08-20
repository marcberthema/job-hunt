---
description: Search Braintrust via Claude in Chrome, gate out region-ineligible postings before scoring, then quick-score the rest — no files written until you pick which postings to file
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-braintrust.md` / `plans/check-braintrust.md`. Follow these steps in order.

This command drives your real Chrome browser (`mcp__claude-in-chrome__*` tools) because Braintrust
is client-side rendered and `WebFetch` sees an empty page shell. **No login is required to
browse** — confirmed 2026-08-20, the earlier "needs a logged-in session" note was based on the
JS-rendering issue, not an actual auth wall.

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

Same rotation list as `/check-indeed`, `/check-dice`, `/check-jobbank`, `/check-builtin`,
`/check-wwr`, `/check-remoteok`.

## 4. Search Braintrust (per keyword)

Braintrust filters via URL query parameters, not free text. `navigate` to:
```
https://app.usebraintrust.com/jobs/?role=5%2C16&skills=<skill-id>
```
- `role=5,16` restricts to Engineering + IT & System Admin — confirmed correct for this rotation.
- `skills=<id>` filters by skill chip. Confirmed **`1338` = DevOps**. For any keyword without a
  confirmed ID below, look it up once: click the **Skills** filter pill, type the keyword into
  its search box, click the matching chip, click **Apply**, and read the `skills=` value the URL
  updates to. Update `specs/check-braintrust.md`'s Skill ID Table with newly confirmed IDs so
  future runs don't need to repeat this lookup.

  | Keyword | Skill ID | Notes (2026-08-20) |
  |---|---|---|
  | DevOps Engineer | `1338` | Only keyword that reliably returns results (3, as of 2026-08-20) |
  | Platform Engineer | none — no matching skill chip | "Skill not found" when searched; fall back to unfiltered `role=5,16` + title-skim |
  | Site Reliability Engineer | `8473` | Chip exists but returned 0 open postings as of 2026-08-20 — re-check next run, may just be a quiet period |
  | Cloud Engineer | `10001` (Cloud Engineering) | Chip exists but returned 0 open postings as of 2026-08-20 |
  | DevSecOps Engineer | `6831` | Chip exists but returned 0 open postings as of 2026-08-20 |
  | Forward Deployed Engineer | not confirmed | Also appears as a literal role title in postings (e.g. Turing) — may not need its own skill chip; re-test lookup next run |

  **Never combine multiple `skills=` IDs in one URL** — confirmed during testing that
  `skills=8473,6831` (two IDs together) ANDs them and returned 0 even though each alone also
  returned 0. Run each keyword as a fully separate navigation.

  If a keyword has no matching skill chip at all, fall back to the unfiltered `role=5,16` results
  and title-skim (same triage pattern used for Indeed's noisy default rotation).

`get_page_text` on the results page returns clean, complete data directly: title, company,
engagement type (Freelance/Employee), rate, hours/week, and — importantly — the **Location
column** on each card (e.g. "United States only," "Work from anywhere," "North America + 1
more," "United States | Canada"). Get the job link (`/jobs/<numeric-id>` pattern) via `find` on
the job title if it's not directly visible in the `get_page_text` output.

- **Single custom query**: cap at first 15 results.
- **Default rotation**: cap at first **8** results per keyword.

If a keyword returns no results, skip it and move to the next keyword. If every keyword (or the
single custom query) comes back empty, tell the user and stop.

## 5. Dedupe (rotation mode only)

Collapse the combined result list by company + **exact** title (not fuzzy).

## 6. Read profile.md

Read `profile.md` in full before scoring or gating anything.

## 7. Location-eligibility gate, using the Location column captured in step 4

- **"Work from anywhere," an explicit "Canada" mention, or "North America"** → **eligible**,
  proceed to step 8.
- **"United States only," or a region list that excludes Canada** → **ineligible** — do not open
  the full posting. Log title, company, and the reason.
- **A specific US city/state shown with no "only" qualifier** (Braintrust's on-site convention) →
  **ineligible** unless the full posting says otherwise.

## 8. Open each eligible posting

`navigate` to `https://app.usebraintrust.com/jobs/<id>`. Confirmed during testing:
`get_page_text` returns the full, correct job description directly — no `find`+`read_page`
workaround needed. Extract title, company, full description, rate, skills, and the "Preferred
location" field in the body.

- **Skim the body for anything that contradicts the card's Location column** — no mismatch was
  found in initial testing, but apply the same caution learned from RemoteOK, where a
  "Worldwide"-tagged card sometimes hid a real location restriction in the body text.
- **Posting fails to load** → mark "couldn't fetch," continue with the rest — skip the gate for
  it too.
- **Never click Apply** — read-only navigation and text extraction only, at every step of this
  command.

## 9. Quick-score each eligible posting (0–10)

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking. Logistics don't drag the score down — flag them instead. **Freelance/contract
postings are a strong engagement-type match here, not a flag** — Braintrust is fundamentally a
contractor marketplace, which aligns directly with the consulting-engagement preference. One
sentence rationale per posting.

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

Close the Braintrust tab at the end of the run — success, empty-result, or early-stop path alike.
