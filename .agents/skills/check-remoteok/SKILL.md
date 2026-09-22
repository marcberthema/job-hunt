---
name: check-remoteok
description: Search RemoteOK for recent Canada-eligible remote SRE, Platform, DevOps, Cloud, DevSecOps, and infrastructure jobs; validate regional eligibility, score accessible postings against this repository's candidate profile, and update the RemoteOK HTML report. Use when the user asks to run, check, or search RemoteOK for jobs.
---

# Check RemoteOK

Search RemoteOK, validate current postings, gate regional eligibility, compare every eligible result with Marc's profile, update `reports/remoteok-job-search.html`, and auto-file qualifying jobs under the policy below. External activity is read-only: never apply, save, create an account, sign in, upload information, or submit a form. Do not create per-job artifact files or alter existing pipeline decisions.

## Source of truth

Before gating or scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Direct HTTP access

Use direct HTTP rather than a browser by default. RemoteOK's public JSON endpoint currently exposes the latest inventory, complete descriptions, dates, tags, locations, salary fields, and canonical posting URLs:

    https://remoteok.com/api

Fetch it once with `curl.exe -L -sS --max-time 45 -A "Mozilla/5.0"`. The first JSON object is API metadata, not a job; ignore it. Do not send profile data, contact information, or other user information to RemoteOK.

Use the canonical `url` from each API job for validation. Direct HTML detail pages currently load without authentication. If a relevant description in the API is complete and current, it is sufficient; open the detail page when regional eligibility, freshness, compensation, or requirements remain ambiguous.

If the API returns a non-JSON response, a block page, or no real job objects, retry once. If it still fails, use a real browser on `https://remoteok.com/remote-jobs?search=<encoded query>`. Stop rather than bypassing any CAPTCHA or verification challenge. Close temporary browser tabs when finished.

## Search scope

If the user supplies a query, match it case-insensitively against `position`, `tags`, and the plain text of `description`, then review up to 15 plausible results.

For a default run, review the API inventory for these target families:

- DevOps Engineer
- Senior DevOps Engineer
- Site Reliability Engineer / SRE
- Platform Engineer
- Cloud Engineer
- DevSecOps Engineer
- Infrastructure Engineer

Prefer postings from the past 14 days. Review every plausible target-family posting within the latest 100 API jobs, not merely exact title matches. Retain roles centered on production reliability, observability, cloud foundations, CI/CD, deployment automation, infrastructure as code, platform enablement, systems infrastructure, or DevSecOps. Exclude application development, data engineering, sales/solutions architecture, QA, support, and unrelated operations unless the description's actual center of gravity belongs to a target family. A posting you open and read in full, then rule out for this reason, is still a scored row — give it `score: 0` and `status: "Out of scope"` per `reports/report_schema.md`, with `gap` stating what the role actually is.

Deduplicate by RemoteOK job `id` or canonical URL, then by company plus exact title.

## Run completeness and inventory audit

The latest-100 API inventory is the mandatory default discovery pass; the target families are independent classification buckets within that single fetch, not substitute queries. Record the endpoint, HTTP status, response type, total job objects after removing metadata, the 100-job boundary, number reviewed, every plausible RemoteOK ID, and a per-family match count including zero. Mark the inventory `Complete`, `Zero results`, or `Incomplete - <reason>` before deduplication.

If the API fails twice, the browser fallback is complete only when its rendered inventory and boundary are recorded. A CAPTCHA, verification page, malformed payload, metadata-only response, or partial browser load makes the run incomplete. Search snippets cannot substitute for the API or rendered fallback inventory.

## Regional eligibility gate

RemoteOK is worldwide and many postings are not open to Canadians. Apply this gate before scoring, using both `location` and the full description:

- Eligible: Canada is named; worldwide/global work is explicit; North America includes Canada; or the posting clearly accepts contractors internationally.
- Ineligible: US-only, US-person, US work authorization, a non-Canada country/region, mandatory residence outside Canada, or a location list that excludes Canada.
- Unclear: `location` is blank, says only `Remote`, or uses vague wording without confirming Canada. Inspect the full description and canonical page. If still unclear, retain it with `Confirm Canada eligibility` rather than presenting it as confirmed.

Never rely on `Remote`, `Worldwide`, tags, flag icons, or title text alone. The description may contain a narrower residency, citizenship, time-zone, or language requirement. Keep ineligible roles in the main table as `score: -1` rows with a specific `Ineligible — <short reason>` status pill.

Whether the location gate rules a posting out during a skim or the full validation pass, keep it in `rows` as `score: -1`, put the evidence in `gap`, and never create a separate ineligible collection or footer list.

## Validation and extraction

For every eligible or unclear plausible posting, capture:

- RemoteOK ID, exact title, company, and canonical URL
- API date and evidence the posting remains accessible
- Location, eligible countries/regions, time-zone constraints, and travel
- Employment or contract status when stated
- Salary/rate and currency exactly as stated; treat zero or missing API salary values as `Not stated`
- Responsibilities and requirements needed for scoring
- Citizenship, residency, language, and security-clearance requirements

If a canonical posting is inaccessible and the API description is insufficient, list it under `Could not validate` and do not score it.

Check `applications.md` for a matching RemoteOK canonical URL or `Company`+`Role` row. Keep known eligible roles in the results and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each eligible or unresolved posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, DevSecOps, or mixed cloud delivery.

Give every eligible or unresolved job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep compensation, employment type, location, and regional uncertainty outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, clearance, and people management.

Name the single most consequential mismatch under `Biggest gap`; use `None material` only when justified. Treat staffing or freelance marketplaces as an engagement flag, not an automatic rejection.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/remoteok.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py remoteok` to regenerate `reports/remoteok-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no eligible jobs. Include every scored row, direct posting URLs, pipeline status, run date, API inventory size, plausible candidates, eligible, unclear, ineligible, inaccessible, stale, and known-pipeline counts.

Put the inventory and family audit in `notes_sections`, summarize it in `method`, and report retrievals attempted separately from completed plus unique results reviewed. Reconcile it before `latest_update`; do not claim completion while the inventory is `Incomplete`. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Region / time zone | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the canonical RemoteOK detail page. Preserve currency and pay period, use `Not stated` for unknown facts, and include low scores rather than hiding weak matches. Include full-review exclusions as `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) rows in this same table, per `reports/report_schema.md`.

Regional exclusions belong in the same table as `score: -1` rows and are never repeated below it. After the table, list only unclear eligibility, `Could not validate` entries, stale postings, and material search limitations. Ask which eligible roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/remoteok.json` during discovery.

## Automatic filing

Read and follow [the shared automatic-filing policy](../_shared/automatic-filing.md). This is the only routine `applications.md` mutation authorized during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check regional eligibility and duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
