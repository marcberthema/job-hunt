---
name: check-roberthalf
description: Search Robert Half Technology (Canada, Contract listings) for recent SRE, Platform, DevOps, Cloud, and DevSecOps contract jobs; score every accessible posting against this repository's candidate profile, and update the Robert Half HTML report. Use when the user asks to run, check, or search Robert Half for jobs.
---

# Check Robert Half

Search Robert Half Technology, validate current postings, compare every result with Marc's profile, and update `reports/roberthalf-job-search.html`. All external activity is strictly read-only: never apply, save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Access

Robert Half Technology is the one staffing-agency source in this repository confirmed fetchable via direct HTTP — no browser workaround is needed. Use direct HTTP retrieval by default; fall back to a browser only if direct retrieval stops exposing complete current listings.

Search via:

`https://www.roberthalf.com/ca/en/jobs?jobType=CONTRACT&specialty=TECHNOLOGY&keywords=<keyword, spaces as +>`

Always keep `jobType=CONTRACT&specialty=TECHNOLOGY` on every request — dropping `jobType=` pulls in Permanent/FTE listings against the consulting-engagement preference; only broaden this if the user explicitly asks. This has returned clean, real, Canada-scoped Contract tech postings directly, including pay rate, location, and job type.

## Search scope

If the user supplies a query, use it alone and review the first 15 results. Otherwise run separately:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

Review up to eight results per keyword in the default rotation. If a keyword returns no relevant results, continue to the next; if every keyword is empty, report that outcome.

Deduplicate by company plus exact title.

## Geography and eligibility

The `ca.` region path plus `specialty=TECHNOLOGY` keep results Canada/tech-scoped by construction — no eligibility gate is needed.

## Validate and extract

Fetch each candidate posting's own page. Extract full description and confirm pay rate and job type match what the results page showed. Robert Half is a general staffing firm — expect some non-DevOps noise even within `specialty=TECHNOLOGY` (SAP, plain developer, QA roles); skim titles before full-fetching each one. If a posting fails to load, mark it "Could not validate" and continue.

Check `applications.md` for a matching company/title row. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every posting a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/roberthalf.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py roberthalf` to regenerate `reports/roberthalf-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no validated jobs. Include every scored row, direct posting URLs, pipeline status, run date, and counts for searches completed, results reviewed, validated jobs, inaccessible postings, and known pipeline matches.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the Robert Half job page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

After the table, list `Could not validate` entries and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/roberthalf.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
