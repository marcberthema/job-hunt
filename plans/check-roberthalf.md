# Plan: `/check-roberthalf` — Robert Half Technology Search & Bulk Quick-Score (via WebFetch)

Implements `specs/check-roberthalf.md`.

## Deliverable

`.claude/commands/check-roberthalf.md` — a slash command definition using plain `WebFetch`, same
shape as `/check-indeed`/`/check-builtin`. This is the only staffing-agency source in this repo
that doesn't need the Claude in Chrome workaround.

## Command Steps

1. **No Chrome tools needed** — this command uses `WebFetch` only.

2. **Parse input** — `$ARGUMENTS` optional.

   ### Default role rotation
   ```
   DevOps Engineer
   Platform Engineer
   Site Reliability Engineer
   Cloud Engineer
   DevSecOps Engineer
   Forward Deployed Engineer
   ```

3. **Search per keyword** — `WebFetch`:
   ```
   https://www.roberthalf.com/ca/en/jobs?jobType=CONTRACT&specialty=TECHNOLOGY&keywords=<keyword, spaces as +>
   ```
   Confirmed during testing: this returns clean, real, Canada-scoped Contract tech postings
   directly (e.g. $123.50-$143/hr Senior Director Engineering, Toronto; $35-$45/hr Software
   Engineer II, Mississauga). Extract title, location, job type, pay rate, and each posting's
   individual URL from the fetched content.

   - Single custom query: cap at first 15 results.
   - Default rotation: cap at first 8 results per keyword.

   If a keyword returns no relevant results, skip it and continue. If everything comes back
   empty, report and stop.

4. **Dedupe** (rotation mode only) — collapse by company + exact title.

5. **Read `profile.md`** in full.

6. **No eligibility gate** — the `ca.` region path plus `TECHNOLOGY` specialty filter keep
   results Canada/tech-scoped by construction.

7. **Fetch each candidate posting's individual page** via `WebFetch`. Extract full description,
   confirm pay rate and job type match what was shown on the results page.

8. **Score each posting 0–10**, skill/domain-first, same philosophy as the other `/check-*`
   commands. Robert Half is a general staffing firm — expect some non-DevOps noise even within
   `specialty=TECHNOLOGY` (SAP, plain developer, QA roles); skim titles before full-fetching each
   one, same discipline as `/check-indeed`.

9. **Present a single results table**, sorted highest score first:

   | Role — Company | Score | Rate | Why | Flags |
   |---|---|---|---|---|

   No files are written at this step.

10. **Offer to go deeper** — same pattern as the other commands: duplicate check via
    `grep -ril`, reuse content already fetched in step 7, full `/addjob` schema output to
    `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`.

    Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
    only.

## Testing

Manual (no automated test suite in this repo):

- Run `/check-roberthalf devops engineer` — confirm `WebFetch` alone (no Chrome) returns real,
  Canada-scoped Contract results with rates.
- Confirm the `jobType=CONTRACT&specialty=TECHNOLOGY` filter combo is used on every request —
  never drop it silently.
- Confirm low-volume keywords are reported honestly rather than padded with irrelevant results.

## Out of Scope

Same as spec: removing `jobType=CONTRACT`, pagination, auto-filing without confirmation.
