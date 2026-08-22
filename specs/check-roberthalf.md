# Spec: `/check-roberthalf` — Robert Half Technology Search & Bulk Quick-Score (via WebFetch)

## Problem

Robert Half Technology (`roberthalf.com/ca/en/jobs`) is confirmed fetchable directly via plain
`WebFetch` — no Chrome workaround needed, unlike every other staffing-agency source in
`job_sources.md`. Tested 2026-08-20: `?jobType=CONTRACT&specialty=TECHNOLOGY` returned real
Canadian contract tech postings with rates shown directly (e.g. $123.50-$143/hr Senior Director
Engineering, Toronto; $35-$45/hr Software Engineer II, Mississauga).

## Capability

Same overall shape as `/check-indeed`: optional search query (defaults to the shared role
rotation), searches Robert Half via `WebFetch`, quick-scores results. **No eligibility gate
needed** — the `ca.` region-scoped path and `TECHNOLOGY` specialty filter keep results
Canada/tech-scoped by construction.

## Usage

```
/check-roberthalf [search terms]
```

- `/check-roberthalf` (no arguments) — runs the default role rotation (same list as the other
  `/check-*` commands).
- `/check-roberthalf platform engineer` — runs that single query only.

## Behavior

1. **Determine query mode**: single custom query or full rotation.
2. **Search per keyword** — `WebFetch`:
   `https://www.roberthalf.com/ca/en/jobs?jobType=CONTRACT&specialty=TECHNOLOGY&keywords=<keyword>`
   Confirmed during testing that `jobType=CONTRACT&specialty=TECHNOLOGY` returns clean,
   Canada-scoped, tech-specific results directly via plain `WebFetch` (no Chrome, no blocking).
   Extract title, location, job type, pay rate (shown directly per listing), and posting URL.
3. **Dedupe** (rotation mode only) — collapse by company + exact title.
4. **Read `profile.md` first**.
5. **No eligibility gate** — the `ca.` path plus `TECHNOLOGY` specialty filter keep results
   Canada/tech-scoped.
6. **Fetch each candidate posting's full detail** via `WebFetch` on its individual URL. Extract
   full description, confirm pay rate and job type.
7. **Quick-score each posting** 0–10, same skill/domain-first philosophy as the other `/check-*`
   commands. Note: Robert Half is a general staffing firm (not IT-exclusive like Dice), so expect
   some non-DevOps noise even within the TECHNOLOGY specialty (e.g. SAP, developer, QA roles) —
   skim titles before full-fetching each one, same discipline as `/check-indeed`.
8. **Present a single table** sorted highest score first.
9. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **Low volume on a given keyword** (only one test query run so far — the site may not have deep
  DevOps/SRE-specific inventory) → don't over-invest; report what's found and move on.
- **`jobType=CONTRACT` narrows out Permanent listings entirely** — this is intentional, matching
  the consulting-engagement preference; don't broaden to `jobType=` unset without asking first.
- **A posting's rate is shown as a wide band** (e.g. entry-to-senior spread) → note as-is, don't
  assume the top of the band applies.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode.

## Out of Scope

- Removing the `jobType=CONTRACT` filter (would pull in FTE listings against the consulting
  preference — only broaden if the user asks).
- Pagination beyond the first results page.
- Auto-filing high-scoring results without user confirmation.
