---
description: Search Dice, gate out postings you're ineligible for (clearance/US-work-authorization) BEFORE scoring, then quick-score the rest
argument-hint: [search terms — optional, defaults to the full role rotation]
---

Implements `specs/check-dice.md` / `plans/check-dice.md`. Follow these steps in order.

If `WebSearch` is deferred (not yet in your active tool list), load it via one `ToolSearch` call
(`select:WebSearch`) before step 5 — it's used there to recover a canonical employer-page URL
when a posting fails to fetch or looks stale.

## 1. Parse input

`$ARGUMENTS` is optional. Location/sponsorship filters are fixed — not user-supplied arguments.

- If `$ARGUMENTS` is non-empty, treat it as a single search-terms query and run step 2 once for
  it, same as before.
- If `$ARGUMENTS` is empty, run step 2 once per keyword in the **default role rotation** below,
  then dedupe (step 3) before continuing to the eligibility gate.

### Default role rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

Same rotation as `/check-indeed` — keep both files' lists in sync if Marc's positioning changes.
Update this list directly in this file; no need to touch the spec/plan for a wording tweak.

## 2. Search Dice (per keyword)

For each keyword being searched this run, build:
```
https://www.dice.com/jobs?filters.postedDate=SEVEN&filters.employmentType=FULLTIME%7CCONTRACTS&filters.workplaceTypes=Remote&filters.willingToSponsor=true&q=<keyword, spaces as +>&countryCode2=CA&language=en
```
Fetch with WebFetch, asking for every `/job-detail/<id>` link with title, company, location, and
rate/salary as shown on the results page.

- **Single custom query** (arguments given): cap at the first 15-20 links.
- **Default rotation** (no arguments): cap at the first **8** links per keyword, to keep the
  total batch size reasonable across 6 keywords.

**Revised 2026-09-13**: `filters.workplaceTypes=Remote` and `filters.willingToSponsor=true`
replace the old `location=Remote` text param, which produced noisy US-onsite-heavy results.
`filters.employmentType` now includes both `FULLTIME` and `CONTRACTS` — Marc is now open to
TN-visa-sponsored US roles (Canadian citizens get fast/cheap sponsorship under USMCA), so
sponsor-willing full-time US positions are in scope, not just contracts.

If a keyword's search returns no job links, skip it and move to the next keyword — don't abort
the whole rotation over one empty search. If every keyword comes back empty (or the single custom
query does), tell the user and stop.

## 3. Dedupe (rotation mode only)

Postings often show up under more than one keyword. Before running the eligibility gate, dedupe
the combined link list by company + title (case-insensitive, ignore minor punctuation
differences) so each unique posting is only fetched once, even if it matched multiple keywords.

## 4. Read profile.md

Read `profile.md` in full before doing anything else.

## 5. Eligibility gate — run this BEFORE scoring, for every posting

Fetch each deduped posting. **If a posting fails to fetch or looks stale**, try a quick web
search for the exact title + company before giving up — if the posting names a direct employer
(not an anonymized staffing-agency client) and their own careers page turns up, prefer that as
the canonical URL and confirm the details still match. Dice listings, like other aggregators,
rotate and expire. Before extracting full requirements or scoring, check in this order:

1. **Security clearance mentioned** (TS/SCI, Secret, Public Trust, etc.) → **INELIGIBLE**:
   clearance required — this requires US citizenship in practice even when not stated
   explicitly, and TN status doesn't change this.
2. **Work authorization restricted to US statuses, WITH sponsorship mentioned** ("will sponsor,"
   "able to sponsor," H-1B/TN/visa language) → **ELIGIBLE (revised 2026-09-13)**. Marc is a
   Canadian citizen and TN-visa eligible under USMCA — fast, cheap sponsorship relative to other
   nationalities. **Flag prominently: "TN-sponsorship path — likely W2 employment via the posting
   company or a staffing intermediary, no corp-to-corp; confirm with the recruiter whether
   sponsorship means a work visa (TN) or something else — do not assume green card."** This
   distinction matters: "willing to sponsor" on a contract/FTE posting essentially always means a
   work visa, not permanent residency sponsorship, which is a separate, far larger, rarely-offered
   commitment.
3. **Work authorization restricted to US statuses, NO sponsorship mentioned** (e.g. "must be
   authorized to work in the US without sponsorship") → **INELIGIBLE**: hard closed door.
4. **On-site (not hybrid/remote) at a US location with no remote option** → **INELIGIBLE**: TN
   doesn't solve relocation — this is a separate logistics fail from work authorization.
5. Otherwise → **ELIGIBLE**. If work-authorization language is simply absent (neither open nor
   restricted), still mark eligible but add the flag "confirm work authorization with recruiter
   before applying."

**For postings that fail the gate, stop there** — record only title, company, and the one-line
ineligibility reason. Do not extract full responsibilities/requirements or spend effort scoring
against `profile.md`. This is the entire point of running the gate first: don't burn tokens
matching a profile against a job that can't legally be taken.

## 6. Score only ELIGIBLE postings (0–10)

Same skill/domain-first philosophy as `/addjob` and `/check-indeed`: Azure depth, platform
engineering/CI-CD/IaC scope, financial/energy relevance, autonomy vs. ticket-taking. Logistics
(not eligibility — eligibility already gated) are flagged, not scored down. One sentence
rationale per posting.

## 7. Report two sections

**Eligible** (sorted highest score first):

| Role — Company | Score | Why | Flags |
|---|---|---|---|

**Ineligible** (no scoring spent):

| Role — Company | Reason |
|---|---|

## 8. Offer to go deeper

Ask which **eligible** posting(s) should get the full `/addjob` treatment. For each one picked:

- Duplicate check: `grep -ril "<company/role>" jobs/new/ jobs/applied/ jobs/rejected/`. Warn and
  confirm before proceeding if a match is found.
- Reuse the posting content already fetched in step 5 — don't re-fetch.
- Produce the full resume delta, cover letter, and job file exactly per `/addjob`'s schema
  (`specs/addjob.md`), written to `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.
- Report back: score, one-line summary, flags, and the file path.

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.
