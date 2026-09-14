---
name: check-linkedin
description: Search LinkedIn and employer career sites for recent Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate accessible postings, score them against this repository's candidate profile, and return a deduplicated comparison table. Use when the user asks to run, check, or search LinkedIn for jobs.
---

# Check LinkedIn

Discover recent LinkedIn-listed jobs through public web access, validate them using accessible LinkedIn pages or employer career sites, and compare every eligible posting with Marc's current profile. This workflow is read-only: do not sign in, use private cookies, evade access controls, solve CAPTCHAs, create job files, change pipeline state, or submit applications.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and prior run notes. Never invent or strengthen experience.

## Search scope

If the user supplies a query, search that query only. Otherwise run the following LinkedIn-oriented phrase rotation:

- `DevOps Consultant Remote`
- `Senior DevOps Engineer Remote` 
- `Staff DevOps Engineer Remote`
- `Senior Site Reliability Engineer Remote`
- `Platform Engineer Remote` 
- `Senior Platform Engineer Remote`
- `Cloud Engineer Remote` 
- `Infrastructure Engineer SRE Remote`
- `DevSecOps Engineer Remote` 
- `Deployment Engineer Remote` 
- `Professional Services DevOps Engineer Remote`
- `Forward Deployed Engineer Remote`

Search for jobs posted in the past two days when the source exposes reliable dates. Target remote work explicitly open to Canada or Ontario and hybrid work in Ottawa, Kingston, Cornwall, and Montréal. For Montréal, exclude confirmed requirements above two office days weekly. Retain undisclosed hybrid cadence as `Hybrid — days not stated; confirm <=2`. Exclude fully on-site roles and remote roles restricted to an ineligible region.

Run additional remote-only discovery passes using Canada's major employment hubs as the LinkedIn location: Toronto/GTA, Vancouver, Montréal, Calgary, Ottawa, Edmonton, Waterloo/Kitchener, Halifax, Winnipeg, Québec City, and Victoria. LinkedIn frequently indexes a Canada-remote position under an employer office or recruiting hub instead of labeling it Remote. These passes are discovery mechanisms, not permission to retain local on-site or hybrid roles outside Marc's reachable cities.

Do not exclude a result based on LinkedIn's location label alone. Open the full description and retain it only when the posting itself explicitly permits remote work from Canada or Ontario, worldwide remote work compatible with a Canadian worker, or an equivalent eligible arrangement. Apply this validation to postings indexed under any Canadian city.

Treat timezone language as a remote-eligibility signal worth validating. Phrases such as `USA or Canada (Eastern timezone)`, `Canada - Eastern time`, or `remote within Canada` qualify when the full posting does not impose an incompatible office requirement.

Use public LinkedIn job pages and web searches targeting `linkedin.com/jobs/view/`. Because LinkedIn may restrict automated or logged-out access, supplement discovery with distinctive title/company searches and employer career sites. For a custom query, review up to 20 plausible results. For the default rotation, review up to 12 plausible results per phrase before deduplication. State the actual boundary when access or result volume prevents this.

## Access and validation

Never request or reuse the user's LinkedIn credentials, browser session, private cookies, or authentication tokens. Never evade bot protection or attempt CAPTCHA or verification bypass. If a LinkedIn page is blocked or login-gated, use it only as a discovery lead and look for the same role on the employer's official career site.

For every candidate, establish from an accessible full description the exact title/company, current availability, eligible location/arrangement, office cadence, stated compensation, and requirements needed for scoring. Do not score a search snippet or LinkedIn summary alone. Prefer the employer posting as the canonical URL and evidence source. If no current full description is accessible, omit the role from the scored table and list it under `Could not validate` with the reason.

Deduplicate by employer canonical URL, then LinkedIn job ID, then company plus exact title. Check `jobs/new/`, `jobs/applied/`, and `jobs/rejected/` for URL and company/title matches. Keep known roles in the table but label their pipeline status beside the company.

## Classification and scoring

Classify each retained role by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location out of the score. Apply the profile's honesty rules, particularly for AWS, GCP, Kubernetes cluster administration, languages, and people management. Under `Biggest gap`, name the single most consequential requirement mismatch; use `None material` only when justified.

## Output

Lead with search phrases completed, unique postings validated, exclusions, employer-site recoveries, inaccessible postings, and known pipeline matches. Sort every validated role by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps`. Link directly to the accessible full posting, preferring the employer page. Preserve currency and pay period; use `Not stated` for unknown facts. Include low scores.

After the table, list `Could not validate` entries and material search limitations. Explicitly distinguish employer-validated roles from LinkedIn pages that were inaccessible. Ask which roles the user wants investigated or added to `jobs/new/`. Do not draft or write applications during discovery.

## Follow-up filing

For a selected posting, refresh it, re-check duplicates, and follow `specs/addjob.md`. Write only to `jobs/new/`; do not apply or change pipeline status without explicit confirmation.
