---
name: check-builtin
description: Search Built In broadly for Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; score every fetched posting against this repository's candidate profile and return a deduplicated comparison table. Use when the user asks to run, check, or search Built In for jobs.
---

# Check Built In

Search Built In, validate the full postings, and compare every eligible result with Marc's current profile. This is a read-only discovery workflow: do not create job files, change pipeline state, or submit applications unless the user subsequently asks.

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

Use the broad Forward Deployed Engineer query so discovery does not miss infrastructure-oriented roles whose titles omit an infrastructure qualifier. Evaluate the full description: retain roles with meaningful infrastructure, platform, reliability, cloud, or DevOps responsibilities, including weak fits with low scores; exclude roles that are purely application development or otherwise unrelated to the three target families.

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

Search Built In's current filtered pages first. Because its URL taxonomy and filters can change, inspect the live site rather than assuming an old route remains valid. Supplement weak or empty internal results with domain-restricted web searches targeting `builtin.com/job/` and the same role/geography. Do not use search-result snippets as the final evidence when the posting itself is accessible.

Review the complete first results page for every search pass; do not stop after the first few attractive jobs. If pagination or a large result set would materially expand the run, state the boundary used instead of silently truncating it.

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

Check `jobs/new/`, `jobs/applied/`, and `jobs/rejected/` for the direct URL and company/title. This does not remove the result from the table: label prior pipeline status beside the company name in parentheses, such as `already applied` or `already in new`, so reruns remain complete without disguising duplicates as new opportunities.

## Skill score and biggest gap

Give every validated, geographically eligible posting a `Skill score` from 0–10. Score technical experience, domain relevance, seniority/scope, and demonstrated leadership/autonomy against `profile.md` and the resume.

Keep logistics out of the skill score because location and pay have their own columns. Do not increase a score merely because compensation is high or work is remote. Do not lower it merely because salary is missing.

Apply the profile's honesty rules to AWS, GCP, Kubernetes, people management, programming languages, and other depth requirements. A hard technical mismatch can produce a 0–4 skill score even when adjacent skills are strong.

For `Biggest gap`, name the single requirement most likely to prevent an interview or successful performance. Be specific, for example `Requires 5+ years operating EKS; Marc's AWS work was a dated, non-production build`, rather than `AWS`. If there is no material gap, write `None material`.

## Output

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

After the table, report `Could not validate` and material search limitations, if any. End by asking which postings the user wants to investigate or add to `jobs/new/`. Do not draft cover letters or write files during this discovery run.

## Follow-up filing

When the user selects a posting, reuse the already fetched description when still current, re-check for duplicates, and follow the schema in `specs/addjob.md`. Write only to `jobs/new/`; never submit an application or move it to `applied` or `rejected` without the user's explicit confirmation.
