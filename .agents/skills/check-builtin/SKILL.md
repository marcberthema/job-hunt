---
name: check-builtin
description: Search Built In broadly for Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; score every fetched posting against this repository's candidate profile and return a deduplicated comparison table. Use when the user asks to run, check, or search Built In for jobs.
---

# Check Built In

Search Built In, validate full postings, compare every eligible result with Marc's profile, update `reports/builtin-job-search.html`, and auto-file qualifying jobs under the policy below. External discovery remains read-only: never submit applications or change third-party state. Do not create per-job artifact files or alter existing pipeline decisions.

## Source of truth

Before scoring, read these files completely:

1. `profile.md`
2. `resume/marc-berthelette-resume-en.md`

Use the current contents even when they conflict with older `.claude/commands`, `specs`, plans, job files, or prior run notes. Never invent or strengthen experience beyond those sources.

## Search scope

Run all search passes unless the user narrows the request.

### Role queries

Use these queries so discovery extends beyond literal matches to the three target families:

- `Site Reliability Engineer`
- `Reliability Engineer`
- `Platform Engineer`
- `Infrastructure Engineer`
- `Cloud Engineer`
- `DevOps Engineer`
- `DevSecOps Engineer`
- `Azure DevOps Engineer`
- `Forward Deployed Engineer`

Use the broad Forward Deployed Engineer query so discovery does not miss infrastructure-oriented roles whose titles omit an infrastructure qualifier. Evaluate the full description: retain roles with meaningful infrastructure, platform, reliability, cloud, or DevOps responsibilities, including weak fits with low scores; exclude roles that are purely application development or otherwise unrelated to the three target families. A posting you rule out for this reason is still a scored row — give it `score: 0` and a specific `Out of scope — <short reason>` status pill per `reports/report_schema.md`, with `gap` stating what the role actually is. Do not drop it silently or move it to a footer list.

Classify each retained posting into exactly one family based on its actual responsibilities, not merely its title:

- `SRE`: production reliability, incident response, observability, SLOs, availability, performance, or operational toil is the center of gravity.
- `Platform`: shared infrastructure/platforms, developer experience, cloud foundations, Kubernetes platforms, IaC, or internal tooling is the center of gravity.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud-delivery work is the center of gravity.

### Geography and work arrangement

Perform distinct discovery passes for:

1. Remote jobs that explicitly allow a worker based in Canada or Ontario.
2. Hybrid jobs based in Ottawa, Ontario.
3. Hybrid jobs based in Kingston, Ontario.
4. Hybrid jobs based in Cornwall, Ontario.
5. Hybrid jobs based in Montréal, Quebec.

For remote results, do not treat the word `remote` alone as proof of eligibility. Verify the full posting permits Canada/Ontario, worldwide workers, or cross-border employment/contracting that Marc can legally use. Exclude postings explicitly limited to the United States or another ineligible region.

For city passes, retain hybrid roles in the named city. Exclude roles in nearby but different cities and exclude fully on-site roles. For Montréal, exclude a posting when it requires more than two office days per week. If a Montréal posting says hybrid but does not disclose the cadence, retain it and show `Hybrid — days not stated; confirm <=2` in the Location column. Do not infer office cadence from generic terms such as flexible or remote-friendly.

Run additional remote-discovery passes using Canada's major employment hubs as the Built In location: Toronto/GTA, Vancouver, Montréal, Calgary, Ottawa, Edmonton, Waterloo/Kitchener, Halifax, Winnipeg, Québec City, and Victoria. Built In may index a Canada-remote position under an employer office or recruiting hub even when the worker can live elsewhere in Canada. Treat these city passes as discovery only: do not retain local on-site work or hybrid work outside Ottawa, Kingston, Cornwall, and Montréal.

Do not reject a posting from a remote-discovery pass merely because Built In labels it with a city. Open the full description and retain it only when the posting explicitly permits remote work from Canada or Ontario, worldwide remote work compatible with a Canadian worker, or an equivalent eligible arrangement. A bare `Remote` or `In-Office or Remote` label without supporting eligibility language is insufficient.

A posting you rule out for location or remote-eligibility (hybrid outside Ottawa/Kingston/Cornwall/Montréal, on-site, or a remote label that doesn't hold up) is still a scored row — give it `score: -1` and a specific `Ineligible — <short reason>` status pill per `reports/report_schema.md`, with `gap` stating the specific gate. Do not drop it silently or move it to a footer list.

Search Built In's current filtered pages first. Because its URL taxonomy and filters can change, inspect the live site rather than assuming an old route remains valid. Supplement weak or empty internal results with domain-restricted web searches targeting `builtin.com/job/` and the same role/geography. Do not use search-result snippets as the final evidence when the posting itself is accessible.

Review the complete first results page for every search pass; do not stop after the first few attractive jobs. If pagination or a large result set would materially expand the run, state the boundary used instead of silently truncating it.

## Run completeness and pass audit

Unless the user narrows the request, every declared role/geography discovery pass is mandatory. Execute each pass independently and verify the rendered query, location, workplace, and freshness filters before recording it. For every pass, record the exact role and geography, URL/filter state, rendered result count, number reviewed, posting IDs or canonical URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Capture the audit before deduplication and retain repeated postings under every pass where they appeared.

If Built In presents a CAPTCHA, verification page, login wall, persistent loading state, or other block, stop the affected path and mark the overall run incomplete. Supplemental web searches may recover an employer posting after Built In discovery, but cannot replace a mandatory Built In pass.

## Fetch, validate, and deduplicate

Open each candidate's direct `builtin.com/job/...` page. Extract the authoritative details from the full posting:

- Exact job title
- Company
- Direct posting URL
- Location and remote/hybrid status
- Required office days per week, or `Not stated`
- Salary/rate and currency exactly as posted, or `Not stated`
- Employment type when useful for eligibility
- Responsibilities and requirements needed for scoring

If a posting cannot be opened or no longer contains a real job description, omit it from the scored table and list it afterward under `Could not validate`, with its URL and the reason. Do not score snippets or guess missing facts.

Deduplicate across every search pass. Prefer canonical URL identity; also collapse the same company plus exact title when Built In exposes multiple URLs for the same posting. Preserve genuinely different roles at the same company.

Check `applications.md` for a matching `Source` URL or `Company`+`Role` row. This does not remove the result from the table: label prior pipeline status beside the company name in parentheses, such as `already applied` or `already new`, from that row's `Status` column, so reruns remain complete without disguising duplicates as new opportunities.

## Skill score and biggest gap

Give every validated, geographically eligible posting a `Skill score` from 0–10. Score technical experience, domain relevance, seniority/scope, and demonstrated leadership/autonomy against `profile.md` and the resume.

Keep logistics out of the skill score because location and pay have their own columns. Do not increase a score merely because compensation is high or work is remote. Do not lower it merely because salary is missing.

Apply the profile's honesty rules to AWS, GCP, Kubernetes, people management, programming languages, and other depth requirements. A hard technical mismatch can produce a 0–4 skill score even when adjacent skills are strong.

For `Biggest gap`, name the single requirement most likely to prevent an interview or successful performance. Be specific, for example `Requires 5+ years operating EKS; Marc's AWS work was a dated, non-production build`, rather than `AWS`. If there is no material gap, write `None material`.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output

Before returning the result, write this run's data to `reports/data/builtin.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py builtin` to regenerate `reports/builtin-job-search.html` — never hand-author the HTML directly, so it reflects the current validated run rather than a prior snapshot. Include every row from the scored table, current pipeline-status labels, direct posting URLs, the run date, and search/validation/exclusion totals. This data refresh is required on every invocation of this skill, including reruns with no new postings.

Put the pass audit in `notes_sections`, summarize the boundary in `method`, and report passes attempted separately from passes completed. Reconcile it before `latest_update`; all mandatory passes must be `Complete` or `Zero results` before claiming a complete run. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with the number of searches completed, unique postings validated, exclusions, and previously known pipeline matches. Then return one Markdown table sorted by skill score descending, using exactly these columns:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Requirements:

- One row per unique validated posting, regardless of score.
- Use only `SRE`, `Platform`, or `DevOps` in Family.
- Put a descriptive Markdown link to the direct job posting in `Posting`; never link to a results page.
- Preserve currencies and pay periods. Do not convert compensation unless the user asks.
- Use `Not stated` rather than guessing salary or office cadence.
- Keep table cells concise, but make `Biggest gap` decision-useful.
- Do not omit low-scoring jobs from the table.
- A posting opened and read in full, then ruled out for domain mismatch or ineligibility, belongs in this same table as a `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) row — never a separate list or prose note.

After the table, report `Could not validate` and material search limitations, if any. End by asking which postings the user wants to investigate or add to `applications.md`. Do not draft cover letters or write files other than `reports/data/builtin.json` during this discovery run.

## Automatic filing

Read and follow [the shared automatic-filing policy](../_shared/automatic-filing.md). This is the only routine `applications.md` mutation authorized during discovery.

## Follow-up filing

When the user selects a posting, reuse the already fetched description when still current, re-check for duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
