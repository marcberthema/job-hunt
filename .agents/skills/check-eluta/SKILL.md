---
name: check-eluta
description: Search Eluta and Canadian employer career sites for recent Canada-remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate accessible postings, score them against this repository's candidate profile, and update the Eluta HTML report. Use when the user asks to run, check, or search Eluta for jobs.
---

# Check Eluta

Discover recent jobs indexed by Eluta, validate them through full Eluta cached copies or employer career pages, compare every eligible posting with Marc's current profile, and update `reports/eluta-job-search.html`. Eluta and employer-site access is strictly read-only: never apply, email, subscribe, create an account, sign in, upload information, or submit a form. Apart from the board-specific report refresh, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Search scope

If the user supplies a query, search that query only. Otherwise search separately for:

- `DevOps Engineer`
- `Senior DevOps Engineer`
- `Staff DevOps Engineer`
- `Site Reliability Engineer`
- `Senior Site Reliability Engineer`
- `Staff Site Reliability Engineer`
- `Cloud Engineer`
- `DevSecOps Engineer`
- `Infrastructure Engineer`
- `Senior Infrastructure Engineer`

Do not include `Forward Deployed Engineer` in the default rotation: Eluta's results for that phrase have consistently been AI implementation, telecom, industrial, or customer-deployment roles. Treat `Platform Engineer` as a custom-query term rather than a default because Eluta matches it very broadly and produces heavy unrelated noise.

For Canada-wide remote discovery, leave location blank and always enable Eluta's Remote filter. When constructing the confirmed search URL directly, use:

`https://www.eluta.ca/search?q=<encoded query>&filter-remote_jobs=only`

Do not add `l=Canada`; Eluta rejects it as an unknown location. Eluta indexes Canadian employer career pages, but the full posting must still confirm that its remote arrangement is compatible with Marc's location. Check for provincial residence restrictions and office requirements in the description.

Run additional hybrid discovery for Ottawa, Kingston, Brockville, Cornwall, and Montréal. Use Eluta's visible location field and confirm the site accepts the city value; do not guess location URL parameters. Do not enable the Remote-only filter for these city passes. Retain only genuinely hybrid target-family roles. For Montréal, exclude confirmed requirements above two office days weekly. Record an undisclosed cadence as `Hybrid — days not stated; confirm <=2`. Exclude fully on-site roles.

A posting ruled out for location/remote-eligibility (on-site, or hybrid outside the reachable cities) is still a scored row — give it `score: -1` and a specific `Ineligible — <short reason>` status pill per `reports/report_schema.md`, with `gap` stating the gate. A posting ruled out because its actual work is outside the target-family center of gravity gets `score: 0` and an `Out of scope — <short reason>` pill instead. Neither is dropped silently or moved to a footer list.

Prefer postings from the past two days using Eluta's displayed posted age or an authoritative employer date. When the source exposes no reliable date, retain the posting but mark freshness as unconfirmed. Review the first 10 results per query and state when fewer were available. Do not paginate unless the user requests a deeper search.

## Run completeness and pass audit

Unless the user narrows the request, every default role query and declared remote/hybrid geography pass is mandatory. Execute each pass separately, verify the rendered query, accepted city value, Remote-filter state, and visible result count, then record the exact pass, count, number reviewed, Eluta cache IDs or canonical URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Capture this audit before deduplication and retain repeated postings under every pass where they appeared.

A CAPTCHA, verification page, blocked cache path, login wall, persistent loading state, or other access failure makes the affected pass and overall run incomplete unless the same pass's rendered inventory was already captured and every candidate can be validated through employer pages. Never claim completion from snippets or a partial role/geography rotation.

## Browser access and validation

Use a browser for Eluta's client-rendered result links. No login is required. Run this source sequentially with other browser-driven job-board skills because shared browser sessions have previously caused tab collisions.

Eluta title links may be JavaScript fragments (`href="#!"`) and may not navigate reliably. Validate each plausible result in this order:

1. Open the employer's current canonical career posting when a stable URL is available.
2. Otherwise open that result's `See how this page looked when Eluta indexed it` link, which normally targets `https://www.eluta.ca/cache?u=<id>:<domain>`.
3. If the cached document says it cannot be displayed directly, use the corresponding `https://www.eluta.ca/cache_open?u=<id>:<domain>` representation. Workday postings may expose their full description there as structured data.
4. If no current full description is accessible, omit the role from the scored table and list it under `Could not validate`. A result snippet can guide discovery but is not sufficient for scoring.

Close temporary cache and employer tabs after extracting the information. Stop using the affected path if Eluta or an employer site presents a CAPTCHA, verification challenge, or access restriction; never attempt to bypass it. Never click `APPLY FOR THIS JOB`, `Email`, or any control whose effect could transmit information.

For every candidate, establish from an accessible full description the exact title and company, current availability, remote eligibility or hybrid cadence, location, stated compensation, and requirements needed for scoring. Treat removed employer pages and materially conflicting dates as stale.

Deduplicate by employer canonical URL, then Eluta cache identity, then company plus exact title. Check `applications.md` for a matching `Source` URL or `Company`+`Role` row. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each retained job by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location out of the skill score while reporting both plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output

Before returning results, write this run's data to `reports/data/eluta.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py eluta` to regenerate `reports/eluta-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no validated postings. Include all scored rows, current pipeline-status labels, direct accessible posting URLs, the run date, and search, validation, exclusion, employer-recovery, and inaccessible totals.

Put the pass audit in `notes_sections`, summarize it in `method`, and report passes attempted separately from passes completed. Reconcile it before `latest_update`; all mandatory passes must be `Complete` or `Zero results` before claiming a complete run. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with searches completed, unique postings reviewed, validated jobs, exclusions, employer-site recoveries, inaccessible postings, and known pipeline matches. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps`. Prefer the employer's canonical URL; otherwise link the accessible Eluta cached copy. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores, and include full-review exclusions as `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) rows in this same table, per `reports/report_schema.md`.

After the table, list `Could not validate` entries and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft applications or write files other than `reports/data/eluta.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application, send an email, or change a row's status to `Applied`, `Skipped`, or `Rejected` through this skill.
