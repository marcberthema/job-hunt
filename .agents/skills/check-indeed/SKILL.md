---
name: check-indeed
description: Search Indeed and employer career sites for Canada-eligible remote and selected Eastern Ontario/Montréal hybrid SRE, Platform, and DevOps jobs; validate freshness, score every accessible posting against this repository's candidate profile, and return a deduplicated comparison table. Use when the user asks to run, check, or search Indeed for jobs.
---

# Check Indeed

Discover Indeed jobs through public search access, validate them against authoritative postings, compare every eligible result with Marc's current profile, and update `reports/indeed-job-search.html`. Apart from that board-specific report refresh, this is read-only: do not create job files, change pipeline state, apply, sign in, solve CAPTCHAs, or attempt to bypass access controls.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, plans, job files, and prior run notes. Never invent or strengthen experience.

## Search scope

Unless narrowed by the user, search separately for `Site Reliability Engineer`, `Reliability Engineer`, `Platform Engineer`, `Infrastructure Engineer`, `Cloud Engineer`, `DevOps Engineer`, `DevSecOps Engineer`, `Azure DevOps Engineer`, and `Forward Deployed Engineer`.

Use the broad Forward Deployed Engineer query so discovery does not miss infrastructure-oriented roles whose titles omit an infrastructure qualifier. Evaluate the full description: retain roles with meaningful infrastructure, platform, reliability, cloud, or DevOps responsibilities, including weak fits with low scores; exclude roles that are purely application development or otherwise unrelated to the three target families. A posting you open and read in full, then rule out for this reason, is still a scored row — give it `score: 0` and `status: "Out of scope"` per `reports/report_schema.md`, with `gap` stating what the role actually is. Do not drop it silently or move it to a footer list.

Run geography passes for remote work explicitly open to Canada or Ontario, plus hybrid work in Ottawa, Kingston, Cornwall, and Montréal. For Montréal, exclude confirmed requirements above two office days weekly. Retain undisclosed hybrid cadence as `Hybrid — days not stated; confirm <=2`. Exclude fully on-site roles and remote roles restricted to an ineligible region.

A posting ruled out for location or remote-eligibility is still a scored row — give it `score: -1` and a specific `Ineligible — <short reason>` status pill per `reports/report_schema.md`, with `gap` stating the gate. Do not drop it silently or move it to a footer list.

Run additional remote-discovery passes using Canada's major employment hubs as the Indeed location: Toronto/GTA, Vancouver, Montréal, Calgary, Ottawa, Edmonton, Waterloo/Kitchener, Halifax, Winnipeg, Québec City, and Victoria. Indeed may index a Canada-remote position under an employer office or recruiting hub even when the worker can live elsewhere in Canada. Treat these city passes as discovery only: do not retain local on-site work or hybrid work outside Ottawa, Kingston, Cornwall, and Montréal.

Do not reject a posting from a remote-discovery pass merely because Indeed labels it with a city. Open the full description and retain it only when the posting explicitly permits remote work from Canada or Ontario, worldwide remote work compatible with a Canadian worker, or an equivalent eligible arrangement. A bare `Remote` label without supporting eligibility language is insufficient.

Search Indeed's public pages when accessible and supplement them with web searches targeting Indeed, distinctive title/company combinations, and employer career sites. Review a reasonable first page for each pass and state any boundary.

## Run completeness and pass audit

Unless the user narrows the request, every declared role/geography pass is mandatory and independent. For every pass, record the exact query and location, access method, result count when exposed, number reviewed, Indeed IDs or canonical employer URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Capture the audit before deduplication and retain repeated postings under every pass where they appeared.

If Indeed blocks a mandatory pass, attempt only the permitted employer-site recovery for postings already discovered and mark that Indeed pass incomplete; web or employer search results do not prove the Indeed inventory was exhausted. Never call a partial rotation complete.

## Access and validation

Never evade bot protection, rotate identities, disguise automation, reuse private browser cookies, or attempt CAPTCHA bypass. When Indeed blocks a page, use it only for discovery and seek the same job on the employer's official career site. Prefer the employer posting as the canonical URL and evidence source.

For every candidate, establish from an accessible full description the exact title/company, current availability, eligible location/arrangement, office cadence, stated compensation, and requirements needed for scoring. Do not score a search snippet. If no current full description is accessible, omit it from the table and list it under `Could not validate` with the reason. Treat conflicting dates or removed employer pages as stale.

Deduplicate by employer canonical URL, then Indeed identity, then company plus exact title. Check `applications.md` for a matching `Source` URL or `Company`+`Role` row. Keep known roles in the table but label pipeline status beside the company from its `Status` column.

## Classification and scoring

Classify each retained job by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location out of the score. Apply the profile's honesty rules, particularly for AWS, GCP, Kubernetes cluster administration, languages, and people management. Under `Biggest gap`, name the single most consequential requirement mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output

Before returning the result, write this run's data to `reports/data/indeed.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py indeed` to regenerate `reports/indeed-job-search.html` — never hand-author the HTML directly, so it reflects the current validated run. Include every scored row, current pipeline-status labels, direct posting URLs, the run date, and search/validation/exclusion totals. This data refresh is required on every invocation, including reruns with no new postings.

Put the pass audit in `notes_sections`, summarize it in `method`, and report passes attempted separately from passes completed. Reconcile it before `latest_update`; all mandatory passes must be `Complete` or `Zero results` before claiming completion. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with searches completed, unique postings validated, exclusions, employer-site recoveries, inaccessible postings, and known pipeline matches. Sort every validated job by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps`. Link directly to the accessible full posting, preferring the employer page. Preserve currency and pay period; use `Not stated` for unknown facts. Include low scores, and include full-review exclusions as `score: 0` (`Out of scope`) or `score: -1` (`Ineligible`) rows in this same table, per `reports/report_schema.md`.

After the table, list `Could not validate` entries and search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft applications or write files other than `reports/data/indeed.json` during discovery.

## Follow-up filing

For a selected posting, refresh it, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Do not apply or change a row's status without explicit confirmation.
