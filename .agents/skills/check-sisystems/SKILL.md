---
name: check-sisystems
description: Search S.i. Systems for recent Canada-remote and selected Eastern Ontario/Montréal contract or permanent SRE, Platform, Infrastructure, and DevOps jobs; validate and score accessible postings, and update the S.i. Systems HTML report. Use when the user asks to run, check, or search S.i. Systems for jobs.
---

# Check S.i. Systems

Search S.i. Systems, validate current postings, compare every eligible result with Marc's profile, and update `reports/sisystems-job-search.html`. All external activity is strictly read-only: never apply, email, save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Browser access

Use a real browser for this source. Direct HTTP requests receive S.i. Systems' WAF rejection page, while normal browser navigation loads the public listings without login.

Start at:

`https://www.sisystems.com/search-it-jobs/?expertise=3`

`expertise=3` selects `Networks and Infrastructure`, the closest specialization to DevOps, cloud, platform, SRE, and infrastructure work. Results are client-rendered; wait for the real listings to replace any `Loading...` state before reading the page.

If the site presents a CAPTCHA, verification prompt, or blocking page, stop the run and report it. Never attempt to solve or bypass a challenge. Close temporary S.i. Systems tabs when finished.

## Search scope

If the user supplies a query, add it as an encoded `q=` value and review the first 15 displayed results. Treat `q=` only as a soft ranking signal: it has historically returned unrelated roles even for ordinary terms such as `devops`.

For a default run, search these terms separately with `expertise=3`, reviewing the first eight displayed results per term before deduplication:

- `DevOps Engineer`
- `Senior DevOps Engineer`
- `Site Reliability Engineer`
- `Platform Engineer`
- `Cloud Engineer`
- `DevSecOps Engineer`
- `Infrastructure Engineer`
- `Senior Infrastructure Engineer`

Use URLs shaped as:

`https://www.sisystems.com/search-it-jobs/?expertise=3&q=<encoded query>`

Do not include `Forward Deployed Engineer` by default because current market results for that title are usually AI implementation or application-engineering roles. It remains available as a custom query.

Because keyword filtering is unreliable, inspect titles and summaries rather than trusting the result count. Retain roles plausibly centered on production reliability, observability, cloud foundations, CI/CD, deployment automation, infrastructure as code, platform enablement, systems infrastructure, or DevSecOps. Exclude unrelated business analysis, project management, application development, QA, data engineering, and support work unless the description's actual center of gravity belongs to one of the target families.

Prefer postings from the past two days using the displayed age or authoritative detail-page date. Include every matching current posting found within the stated result boundary and report its date or `Freshness unconfirmed`.

## Geography and eligibility

S.i. Systems serves the Canadian market, but each posting still needs work-arrangement validation. Retain only:

- Remote roles that explicitly permit residence anywhere in Canada or Ontario.
- Hybrid roles in Ottawa, Kingston, Brockville, Cornwall, or Montréal.
- Roles tied to another city when they offer a genuinely remote Canada-wide track and any office attendance is optional or only occasional; state the travel requirement plainly.

Exclude fully on-site roles and hybrid roles outside those cities. For Montréal, exclude confirmed requirements above two office days weekly. When Montréal cadence is undisclosed, retain it as `Hybrid — days not stated; confirm <=2`.

Do not infer remote eligibility merely because S.i. Systems is Canadian or a listing names multiple cities. Confirm it in the full description. A Toronto posting requiring only occasional attendance may be materially different from weekly hybrid work; retain it only when the burden is genuinely occasional and flag it for confirmation.

## Validate and deduplicate

Open every plausible result through its `DETAILS` link. Detail URLs usually follow `/jobs/<slug>/<encoded-id>/`. Extract from the complete posting:

- Exact title, requisition identity, and direct URL
- Disclosed client/company, or `S.i. Systems client` when anonymous
- Posted date and evidence the role remains available
- Location, remote eligibility, office cadence, and travel
- Contract or permanent status, duration, and extension language
- Pay rate/salary and currency exactly as stated
- Responsibilities and requirements needed for scoring
- Citizenship, residency, language, and security-clearance requirements

An anonymous client is normal for this agency and is not a negative signal. If a posting fails to load, list it under `Could not validate` and continue unless the failure is a site-wide challenge.

Deduplicate by canonical S.i. Systems URL or encoded requisition identity, then by disclosed client plus exact title. Check `applications.md` for a matching `Source` URL, requisition identity, or `Company`+`Role` row. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each eligible posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, DevSecOps, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep compensation, contract type, location, and office cadence outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, clearance, and people management.

Treat contract status as useful engagement information without inflating the skill score. For `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/sisystems.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py sisystems` to regenerate `reports/sisystems-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no validated jobs. Include every scored row, direct posting URLs, pipeline status, run date, and counts for searches completed, unique results reviewed, plausible candidates, eligible validated jobs, geographic or eligibility exclusions, inaccessible postings, and known pipeline matches.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the S.i. Systems detail page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

After the table, list eligibility/geographic exclusions, `Could not validate` entries, and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/sisystems.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. When the client remains anonymous, use `sisystems` as the company slug. Never submit an application or change a row's status to `Applied` or `Rejected` without the user's explicit confirmation.
