---
name: check-linkedin
description: Search LinkedIn and employer career sites for recent Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate accessible postings, score them against this repository's candidate profile, and return a deduplicated comparison table. Use when the user asks to run, check, or search LinkedIn for jobs.
---

# Check LinkedIn

Discover recent LinkedIn-listed jobs through Marc's authenticated LinkedIn session in the connected browser, validate them using full LinkedIn postings or employer career sites, compare every eligible posting with Marc's current profile, and update `reports/linkedin-job-search.html`. LinkedIn access is strictly read-only: never apply, save a job, follow, connect, react, comment, post, message, submit a form, change profile or account data, or perform any other action that writes to LinkedIn. Apart from the board-specific report refresh, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and prior run notes. Never invent or strengthen experience.

## Search scope

If the user supplies a query, search that query only. Otherwise run the following LinkedIn-oriented phrase rotation:

- `DevOps Consultant Remote`
- `DevOps Specialist Remote`
- `DevOps Engineer Remote`
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

A posting ruled out for location or remote-eligibility is still a scored row — give it `score: -1` and a specific `Ineligible — <short reason>` status pill per `reports/report_schema.md`, with `gap` stating the gate. A posting ruled out because its actual work is outside the target-family center of gravity gets `score: 0` and an `Out of scope — <short reason>` pill instead. Neither is dropped silently or moved to a footer list.

Run additional remote-only discovery passes using Canada's major employment hubs as the LinkedIn location: Toronto/GTA, Vancouver, Montréal, Calgary, Ottawa, Edmonton, Waterloo/Kitchener, Halifax, Winnipeg, Québec City, and Victoria. LinkedIn frequently indexes a Canada-remote position under an employer office or recruiting hub instead of labeling it Remote. These passes are discovery mechanisms, not permission to retain local on-site or hybrid roles outside Marc's reachable cities.

Run a separate hybrid discovery pass for each reachable city: Ottawa, Kingston, Cornwall, and Montréal. Do not include `Remote` in these searches; run `Cloud Platform Engineer`, `Platform Engineer`, `DevOps Engineer`, `Site Reliability Engineer`, and `Infrastructure Engineer` as separate searches, with LinkedIn's Hybrid workplace filter and past-two-days filter when available. LinkedIn's Hybrid filter can incorrectly return an empty set; when that happens, rerun the city/title search without a workplace filter and inspect each result's work-arrangement label manually. Review up to 12 plausible results per city after combining the title families. Open each posting to establish its actual office cadence. Retain Montréal roles when the cadence is two days weekly or less, or when it is undisclosed and recorded as `Hybrid — days not stated; confirm <=2`.

Do not exclude a result based on LinkedIn's location label alone. Open the full description and retain it only when the posting itself explicitly permits remote work from Canada or Ontario, worldwide remote work compatible with a Canadian worker, or an equivalent eligible arrangement. Apply this validation to postings indexed under any Canadian city.

Treat timezone language as a remote-eligibility signal worth validating. Phrases such as `USA or Canada (Eastern timezone)`, `Canada - Eastern time`, or `remote within Canada` qualify when the full posting does not impose an incompatible office requirement.

Use the connected browser's existing authenticated LinkedIn session as the primary discovery path. Navigate LinkedIn Jobs, enter searches and filters, open result pages, scroll, paginate, and read posting details as needed. These are the only permitted LinkedIn interactions. Supplement discovery and validation with public web searches, distinctive title/company searches, and employer career sites when they improve coverage or provide a more authoritative posting. For a custom query, review up to 20 plausible results. For the default rotation, review up to 12 plausible results per phrase before deduplication. State the actual boundary when access or result volume prevents this.

## Run completeness and pass audit

Unless the user narrows the request, every declared phrase, remote-hub, and reachable-city hybrid pass is mandatory. Execute each pass independently and verify the rendered query, location, workplace, and past-two-days state. For every pass, record its exact parameters, rendered result count, number reviewed, LinkedIn job IDs or canonical employer URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Capture the audit before deduplication and retain repeated postings under every pass where they appeared.

A CAPTCHA, security checkpoint, verification prompt, login/session loss, or other access block makes the affected pass and overall run incomplete. Employer pages may validate postings already discovered, but public snippets or employer searches cannot be used to pretend a mandatory LinkedIn pass ran successfully.

## Browser access and validation

Use only an already connected, authenticated browser session; never request, reveal, extract, copy, export, or otherwise handle credentials, cookies, authentication tokens, or session data. Do not sign in or sign out. Never evade bot protection or attempt CAPTCHA or verification bypass. If LinkedIn presents a CAPTCHA, verification prompt, security checkpoint, or access restriction, stop using that path and look for the role on the employer's official career site.

Treat every LinkedIn interaction as read-only. Permitted actions are navigating, searching, filtering, opening results, scrolling, paginating, and reading. Do not click any control that applies, saves, follows, connects, reacts, comments, posts, messages, shares, subscribes, changes preferences, edits account/profile data, uploads a file, or submits information. Avoid controls when their effect is unclear. Reading the inbox or unrelated private account data is outside scope.

For every candidate, establish from an accessible full description the exact title/company, current availability, eligible location/arrangement, office cadence, stated compensation, and requirements needed for scoring. Do not score a search snippet or LinkedIn summary alone. Prefer the employer posting as the canonical URL and evidence source. If no current full description is accessible, omit the role from the scored table and list it under `Could not validate` with the reason.

Deduplicate by employer canonical URL, then LinkedIn job ID, then company plus exact title. Check `applications.md` for a matching `Source` URL or `Company`+`Role` row. Keep known roles in the table but label their pipeline status beside the company from its `Status` column.

## Classification and scoring

Classify each retained role by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location out of the score. Apply the profile's honesty rules, particularly for AWS, GCP, Kubernetes cluster administration, languages, and people management. Under `Biggest gap`, name the single most consequential requirement mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output

Before returning the result, write this run's data to `reports/data/linkedin.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py linkedin` to regenerate `reports/linkedin-job-search.html` — never hand-author the HTML directly, so it reflects the current validated run. Include every scored row, current pipeline-status labels, direct posting URLs, the run date, and search/validation/exclusion totals. This data refresh is required on every invocation, including reruns with no new postings.

Put the pass audit in `notes_sections`, summarize it in `method`, and report passes attempted separately from passes completed. Reconcile it before `latest_update`; all mandatory passes must be `Complete` or `Zero results` before claiming completion. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with search phrases completed, unique postings validated, exclusions, employer-site recoveries, inaccessible postings, and known pipeline matches. Sort every validated role by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps`. Link directly to the accessible full posting, preferring the employer page. Preserve currency and pay period; use `Not stated` for unknown facts. Include low scores, and include full-review exclusions as `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) rows in this same table, per `reports/report_schema.md`.

After the table, list `Could not validate` entries and material search limitations. Explicitly distinguish employer-validated roles from LinkedIn pages that were inaccessible. Ask which roles the user wants investigated or added to `applications.md`. Do not draft applications or write files other than `reports/data/linkedin.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change LinkedIn state through this skill; application submission belongs to a separate, explicitly requested workflow.
