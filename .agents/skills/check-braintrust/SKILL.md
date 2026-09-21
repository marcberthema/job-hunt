---
name: check-braintrust
description: Search Braintrust for recent Canada-eligible remote SRE, Platform, DevOps, Cloud, and DevSecOps contract/freelance jobs; gate regional eligibility before scoring, and update the Braintrust HTML report. Use when the user asks to run, check, or search Braintrust for jobs.
---

# Check Braintrust

Search Braintrust, validate current postings, gate regional eligibility before scoring, compare every eligible result with Marc's profile, and update `reports/braintrust-job-search.html`. All external activity is strictly read-only: never apply, save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before gating or scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Browser access

Braintrust (`app.usebraintrust.com`) is client-side rendered — a direct HTTP fetch returns an empty page shell. Use a real browser. No login is required to browse.

Braintrust filters via URL query parameters, not free text:

`https://app.usebraintrust.com/jobs/?role=5,16&skills=<skill-id>`

`role=5,16` restricts to Engineering plus IT & System Admin. `skills=<id>` filters by skill chip. Confirmed IDs: DevOps Engineer `1338` (the only keyword that reliably returns results), Site Reliability Engineer `8473`, Cloud Engineer `10001` (Cloud Engineering), DevSecOps Engineer `6831`. Platform Engineer and Forward Deployed Engineer have no confirmed skill chip; fall back to the unfiltered `role=5,16` listing and title-skim. Never combine multiple `skills=` IDs in one URL — that ANDs them rather than ORing them, which has returned 0 even when each ID alone also returns 0. Run each keyword as a fully separate navigation.

If the site presents a CAPTCHA, verification prompt, or blocking page, stop the run and report it. Never attempt to solve or bypass a challenge. Close temporary Braintrust tabs when finished.

## Search scope

If the user supplies a query, use it as one query against the unfiltered `role=5,16` listing and review the first 15 results. Otherwise search separately with the confirmed or looked-up skill ID for:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

Review up to eight results per keyword in the default rotation. If a keyword returns no results, continue to the next; if every keyword is empty, report that outcome.

Deduplicate by company plus exact title.

## Run completeness and query audit

For the default rotation, all six queries are mandatory and independent. Navigate each query separately and verify the rendered filter or title-skim state. For every query, record the exact term, filter/URL, rendered result count, number reviewed, posting IDs or canonical URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Deduplicate only after capturing this audit, retaining a repeated posting under every query where it appeared.

A CAPTCHA, verification page, login wall, persistent loading state, or other block makes the affected query and overall run incomplete. Never claim all searches completed from snippets, cached pages, or a partial rotation.

## Eligibility gate

Each result card shows a Location column directly (e.g. "United States only," "Work from anywhere," "North America + 1 more," "United States | Canada"). Apply this gate using that column before opening the full posting:

- "Work from anywhere," an explicit Canada mention, or "North America": eligible.
- "United States only," or a region list that excludes Canada: ineligible. Do not open the full posting; add a `score: -1` row with a specific `Ineligible — <short reason>` status pill and the evidence in `gap`.
- A specific US city/state with no "only" qualifier (Braintrust's on-site convention): ineligible unless the full posting states otherwise.

Whether the card location or the full description reveals the restriction, keep the posting in `rows` as `score: -1` with an explanatory status pill. Never create a separate ineligible collection or footer list.

## Validate and extract

Open each eligible posting's direct page. Skim the full description for anything that contradicts the card's Location column — the same caution warranted on RemoteOK, where a card tag has hidden a real restriction in the body. Extract exact title, company, full description, rate, skills required, and the "Preferred location" field. If a posting fails to load, mark it "Could not validate" and continue.

Treat contract/freelance status as a strong engagement-type match — Braintrust is fundamentally a contractor marketplace, aligned with the consulting-engagement preference, not a flag against it.

Check `applications.md` for a matching company/title row. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each eligible posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay, contract type, and location outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

An eligible posting whose actual work is outside the SRE/Platform/DevOps center of gravity still gets a row — score it `0` with `status: "Out of scope"` per `reports/report_schema.md`, with the gap stating what the role actually is, rather than dropping it from the results.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/braintrust.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py braintrust` to regenerate `reports/braintrust-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no eligible jobs. Include every result and exclusion in `rows`, direct posting URLs, pipeline or exclusion status pills, run date, and counts for searches completed, results reviewed, eligible, ineligible, inaccessible, and known pipeline matches.

Put the per-query audit in `notes_sections`, summarize it in `method`, and report searches attempted separately from searches completed. Reconcile the audit before `latest_update`; a run is complete only when every mandatory query is `Complete` or `Zero results`. Preserve any matching `Applied`, `Skipped`, or `Rejected` pipeline status exactly and never reset a reviewed posting to `New`.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the Braintrust job detail page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches, and include full-review exclusions as `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) rows in this same table, per `reports/report_schema.md`.

Put every ineligible entry in the same table as a `score: -1` row; never repeat it in a footer list. After the table, list only `Could not validate` entries and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/braintrust.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
