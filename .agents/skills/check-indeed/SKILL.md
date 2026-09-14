---
name: check-indeed
description: Search Indeed and employer career sites for Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate freshness, score every accessible posting against this repository's candidate profile, and return a deduplicated comparison table. Use when the user asks to run, check, or search Indeed for jobs.
---

# Check Indeed

Discover Indeed jobs through public search access, validate them against authoritative postings, and compare every eligible result with Marc's current profile. This is read-only: do not create job files, change pipeline state, apply, sign in, solve CAPTCHAs, or attempt to bypass access controls.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, plans, job files, and prior run notes. Never invent or strengthen experience.

## Search scope

Unless narrowed by the user, search separately for `Site Reliability Engineer`, `Reliability Engineer`, `Platform Engineer`, `Infrastructure Engineer`, `Cloud Engineer`, `DevOps Engineer`, `DevSecOps Engineer`, `Azure DevOps Engineer`, and `Forward Deployed Engineer`.

Use the broad Forward Deployed Engineer query so discovery does not miss infrastructure-oriented roles whose titles omit an infrastructure qualifier. Evaluate the full description: retain roles with meaningful infrastructure, platform, reliability, cloud, or DevOps responsibilities, including weak fits with low scores; exclude roles that are purely application development or otherwise unrelated to the three target families.

Run geography passes for remote work explicitly open to Canada or Ontario, plus hybrid work in Ottawa, Kingston, Cornwall, and Montréal. For Montréal, exclude confirmed requirements above two office days weekly. Retain undisclosed hybrid cadence as `Hybrid — days not stated; confirm <=2`. Exclude fully on-site roles and remote roles restricted to an ineligible region.

Search Indeed's public pages when accessible and supplement them with web searches targeting Indeed, distinctive title/company combinations, and employer career sites. Review a reasonable first page for each pass and state any boundary.

## Access and validation

Never evade bot protection, rotate identities, disguise automation, reuse private browser cookies, or attempt CAPTCHA bypass. When Indeed blocks a page, use it only for discovery and seek the same job on the employer's official career site. Prefer the employer posting as the canonical URL and evidence source.

For every candidate, establish from an accessible full description the exact title/company, current availability, eligible location/arrangement, office cadence, stated compensation, and requirements needed for scoring. Do not score a search snippet. If no current full description is accessible, omit it from the table and list it under `Could not validate` with the reason. Treat conflicting dates or removed employer pages as stale.

Deduplicate by employer canonical URL, then Indeed identity, then company plus exact title. Check `jobs/new/`, `jobs/applied/`, and `jobs/rejected/` for URL and company/title matches. Keep known roles in the table but label pipeline status beside the company.

## Classification and scoring

Classify each retained job by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location out of the score. Apply the profile's honesty rules, particularly for AWS, GCP, Kubernetes cluster administration, languages, and people management. Under `Biggest gap`, name the single most consequential requirement mismatch; use `None material` only when justified.

## Output

Lead with searches completed, unique postings validated, exclusions, employer-site recoveries, inaccessible postings, and known pipeline matches. Sort every validated job by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps`. Link directly to the accessible full posting, preferring the employer page. Preserve currency and pay period; use `Not stated` for unknown facts. Include low scores.

After the table, list `Could not validate` entries and search limitations. Ask which roles the user wants investigated or added to `jobs/new/`. Do not draft or write applications during discovery.

## Follow-up filing

For a selected posting, refresh it, re-check duplicates, and follow `specs/addjob.md`. Write only to `jobs/new/`; do not apply or change pipeline status without explicit confirmation.
