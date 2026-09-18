---
name: check-randstad
description: Search Randstad Canada's Technologies inventory for recent Canada-remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate and score matching postings, and update the Randstad HTML report. Use when the user asks to run, check, or search Randstad for jobs.
---

# Check Randstad

Search Randstad Canada, validate current postings, compare every eligible result with Marc's profile, and update `reports/randstad-job-search.html`. Randstad access is strictly read-only: never apply, email a recruiter, subscribe, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical notes. Never invent or strengthen experience.

## Retrieval

Use Randstad Canada's Technologies category, not Randstad Digital's careers flow:

`https://www.randstad.ca/jobs/s-technologies/`

Prefer direct HTTP retrieval because the category and job descriptions are present in static HTML and structured `JobPosting` data. Use a normal browser user-agent and follow redirects. A browser is a fallback only when direct retrieval stops exposing complete current listings.

Do not use Randstad's `?query=` parameter: it has returned zero results for ordinary terms such as `devops`. Fetch the Technologies category and filter its contents locally.

On a normal run, review every posting on the first category page, currently about 30 results. Record when fewer were available. Do not paginate unless the user requests a deeper search or the first page contains no postings recent enough to test the source meaningfully.

Stop the affected retrieval path if Randstad presents a CAPTCHA, verification challenge, or access restriction. Never bypass it. A failed posting should be listed under `Could not validate` without aborting other directly accessible postings.

## Search scope

If the user provides a filter term, use it alone. Otherwise retain titles or summaries plausibly centered on:

- DevOps engineering or consulting
- Site reliability engineering
- Platform engineering and developer platforms
- Cloud engineering
- DevSecOps
- Infrastructure engineering
- Release engineering, CI/CD, infrastructure as code, cloud foundations, or closely related automation

Do not require a literal title match. Exclude unrelated business analysis, project management, data engineering, QA, Salesforce administration, application development, and support roles unless the description's actual center of gravity is SRE, Platform, or DevOps.

Prefer postings from the past two days using Randstad's `datePosted` or displayed date, but include every matching current posting found on the reviewed page and report its date. Daily reruns depend on repository deduplication rather than silently omitting older live roles.

## Geography and eligibility

Randstad Canada listings are Canadian-market postings, but that alone does not establish an acceptable work arrangement. Validate the full description and retain only:

- Remote roles that explicitly allow residence anywhere in Canada or in Ontario.
- Hybrid roles in Ottawa, Kingston, Brockville, Cornwall, or Montréal.
- A remote role tied to another city when the description permits work from Canada and any required travel is occasional; state the travel requirement plainly.

Exclude fully on-site roles and hybrid roles outside those cities. For Montréal, exclude confirmed requirements above two office days weekly. When Montréal cadence is undisclosed, retain the role and write `Hybrid — days not stated; confirm <=2`.

Do not trust a title containing `REMOTE` or a location field alone. Confirm the arrangement in the description or structured posting data. For example, a posting may be indexed under Toronto while explicitly allowing remote work anywhere in Canada.

## Validation and deduplication

Open each retained posting's direct Randstad detail URL. Establish from the full description or structured `JobPosting` data:

- Exact title and disclosed client/company
- Current availability and expiration date
- Date posted
- Location, remote eligibility, office cadence, and required travel
- Contract or permanent status and duration
- Salary/rate and currency exactly as stated
- Responsibilities and requirements needed for scoring

When the client remains anonymous, use `Randstad client` as the company label. This is normal for an agency posting.

Deduplicate by Randstad job identifier or canonical URL, then by disclosed company plus exact title. Check `jobs/new/`, `jobs/applied/`, and `jobs/rejected/` for URL, Randstad identifier, and company/title matches. Keep known roles in the result table and label their pipeline status.

## Classification and scoring

Classify each retained role by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible role a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay, contract type, location, and travel outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management.

Under `Biggest gap`, name the single most consequential mismatch. Use `None material` only when justified. Treat contract work as a useful engagement signal, but do not inflate its skill score.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, update only `reports/randstad-job-search.html`. Refresh it on every invocation, including runs with no validated jobs. Include all scored rows, direct posting URLs, pipeline status, run date, and counts for category postings reviewed, plausible matches, eligible validated jobs, geographic exclusions, inaccessible postings, and known pipeline matches. Preserve useful filtering and sorting. Do not update `jobs/new/review-dashboard.html`.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the Randstad job detail page. Preserve currency and pay period and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

After the table, list geographic exclusions, `Could not validate` entries, and material search limitations. Ask which roles the user wants investigated or added to `jobs/new/`. Do not draft application material or write files other than the Randstad report during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow `specs/addjob.md`. Write only to `jobs/new/`. When the client is anonymous, use `randstad` as the company slug unless the description reveals it. Never submit an application or move a job to `applied` or `rejected` without the user's explicit confirmation.
