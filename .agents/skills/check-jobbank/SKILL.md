---
name: check-jobbank
description: Search Canada's Job Bank for recent Canada-remote and selected Eastern Ontario/Montreal hybrid SRE, Platform, and DevOps jobs; validate and score accessible postings, and update the Job Bank HTML report. Use when the user asks to run, check, or search Job Bank for jobs.
---

# Check Job Bank

Search Job Bank, validate full postings, compare every eligible result with Marc's current profile, and update `reports/jobbank-job-search.html`. Job Bank access is strictly read-only: never apply, email, subscribe, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical notes. Never invent or strengthen experience.

## Search scope

If the user supplies a query, search that query only and review up to the first 15 results. Otherwise search separately for:

- `DevOps Engineer`
- `Cloud Engineer`
- `Site Reliability Engineer`

Do not include `Platform Engineer`, `Forward Deployed Engineer`, or `DevSecOps Engineer` in the default rotation. Job Bank's occupation-code matching has repeatedly returned unrelated application, industrial, agronomy, mechanical, and telecom roles for those terms. A user may still request any of them explicitly.

For each query, use:

`https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=<encoded query>&locationstring=Remote`

Review up to the first eight results per query in the default rotation. State when fewer were available. The `locationstring=Remote` parameter does not reliably restrict results to remote work, so treat it as discovery rather than proof of eligibility. Do not paginate unless the user requests a deeper search or the first page has too few plausible results to test the source meaningfully.

Retain roles whose actual responsibilities center on SRE, platform engineering, cloud infrastructure, DevOps, DevSecOps, release engineering, CI/CD, infrastructure as code, observability, or closely related automation. Exclude results that merely carry a matching occupation label while their title and description are unrelated.

Prefer postings from the past two days when Job Bank provides a reliable date, but include every matching current posting found within the stated review boundary and report its date.

## Geography and eligibility

Job Bank is Canada-specific, but that does not establish an acceptable work arrangement. Validate the full description and retain only:

- Remote roles explicitly open to workers anywhere in Canada or in Ontario.
- Hybrid roles in Ottawa, Kingston, Brockville, Cornwall, or Montreal.
- Remote roles tied to another city when the description permits work from Canada and any required travel is occasional.

Exclude fully on-site roles and hybrid roles outside those cities. For Montreal, exclude confirmed requirements above two office days weekly. When Montreal cadence is undisclosed, retain the role and write `Hybrid - days not stated; confirm <=2`. Check for explicit provincial or regional residence restrictions.

## Access, validation, and deduplication

Prefer direct HTTP retrieval of Job Bank result and detail pages. Use a browser only when direct retrieval no longer exposes complete current listings. Stop the affected retrieval path if Job Bank or an originating site presents a CAPTCHA, verification challenge, or access restriction; never bypass it.

Open every plausible result's direct `/jobsearch/jobposting/<id>` page. Establish from a full accessible description:

- Exact title, employer, Job Bank identifier, and current availability
- Date posted and closing date when stated
- Location, remote eligibility, office cadence, and required travel
- Salary or rate, currency, pay period, and engagement type
- Responsibilities and requirements needed for classification and scoring

Job Bank aggregates postings from other sources, including Indeed. Prefer the current originating employer posting as the canonical evidence and output URL when Job Bank links to it and it is accessible. If a full description cannot be validated, omit the role from the scored table and list it under `Could not validate` with the reason. Never score a search-result snippet.

Deduplicate first by Job Bank identifier or canonical URL, then by company plus exact title. Check `applications.md` for a matching `Source` URL, identifier, or `Company`+`Role` row. Keep known roles in the table and label their pipeline status from its `Status` column. Cross-source duplicates are expected; do not treat an Indeed-origin posting as new merely because Job Bank assigned it another URL.

## Classification and scoring

Classify each retained role by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible role a 0-10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay, contract type, location, and travel outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management.

Under `Biggest gap`, name the single most consequential mismatch. Use `None material` only when justified. Include weak fits with low scores rather than silently hiding them.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/jobbank.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py jobbank` to regenerate `reports/jobbank-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no validated jobs. Include all scored rows, direct posting URLs, pipeline status, run date, and counts for results reviewed, plausible matches, eligible validated jobs, geographic or role exclusions, inaccessible postings, and known pipeline matches.

Lead with the run totals and note that overlap with Indeed is expected. Sort validated roles by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link to the employer's canonical posting when available; otherwise link directly to the Job Bank detail page. Preserve currency and pay period and use `Not stated` for unknown facts.

After the table, list geographic and unrelated-role exclusions, `Could not validate` entries, and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/jobbank.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied` or `Rejected` without the user's explicit confirmation.
