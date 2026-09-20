---
name: check-wwr
description: Search We Work Remotely for recent Canada-eligible remote SRE, Platform, DevOps, Cloud, and DevSecOps jobs; gate region-restricted postings before scoring, and update the We Work Remotely HTML report. Use when the user asks to run, check, or search We Work Remotely for jobs.
---

# Check We Work Remotely

Search We Work Remotely, validate current postings, gate region eligibility before scoring, compare every eligible result with Marc's profile, and update `reports/wwr-job-search.html`. All external activity is strictly read-only: never apply, use "AI Auto-Apply," save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before gating or scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Browser access

We Work Remotely returns HTTP 403 to a direct fetch (bot-blocking) but loads cleanly through a real browser session with no login required. Use a browser rather than direct HTTP for this source.

Search via:

`https://weworkremotely.com/remote-jobs/search?term=<keyword, spaces as +>`

The results page renders fully with no scroll or lazy-load workaround needed. It surfaces title, company, posted date, engagement type, and salary when shown, but only the generic "Anywhere in the World" tag, not the real per-posting location. For every candidate kept after a title skim, open the actual result link to read the specific location line (e.g. "Remote India, IN," "Paris, France," "6314 Remote/Teleworker US") — required before the eligibility gate below, since the generic tag is not trustworthy on its own.

If the site presents a CAPTCHA, verification prompt, or blocking page, stop the run and report it immediately, naming the posting that triggered it. Never attempt to solve or bypass a challenge. Close temporary tabs when finished.

## Search scope

Use bare titles, not natural-language phrases — this site does plain keyword matching, not semantic search. If the user supplies a query, use it alone and review the first 15 results. Otherwise run separately:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

Review up to eight results per keyword in the default rotation. If a keyword returns no results, continue to the next; if every keyword is empty, report that outcome.

Deduplicate by company plus exact title.

## Eligibility gate

We Work Remotely shows "Anywhere in the World" on nearly every posting regardless of actual eligibility — confirmed by sampling: postings tagged that way have still been restricted to a single non-Canada location (India, France, US-only, Romania, Malta). Never treat that tag as an eligibility signal. Use the specific location line extracted per result instead:

- Names Canada, "Worldwide," or is blank/absent: provisionally eligible. If blank, confirm with an explicit region statement in the full posting before finalizing.
- Names a single non-Canada country/city, or a region list that excludes Canada: ineligible. Do not open the full posting; record title, company, and reason (e.g. "region-restricted to India, excludes Canada").
- Names a broad multi-country descriptor that plausibly includes Canada (e.g. "North America Only," a flag list containing Canada): eligible.

## Validate and extract

Open each eligible posting's own page. The generic page-text extraction on this site's detail pages can grab the wrong `<article>` element (a related-jobs sidebar rather than the real description) — confirm you're reading the actual Role Purpose/Responsibilities/Qualifications sections, not sidebar content, before extracting salary, engagement type, and requirements needed for scoring. If a posting fails to load, mark it "Could not validate" and continue.

Check `applications.md` for a matching company/title row. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each eligible posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/wwr.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py wwr` to regenerate `reports/wwr-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no eligible jobs. Include every scored row, ineligible entries and reasons, direct posting URLs, pipeline status, run date, and counts for searches completed, results reviewed, eligible, ineligible, inaccessible, and known pipeline matches.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Engagement | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the We Work Remotely job page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

After the table, list ineligible entries with reasons, `Could not validate` entries, and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/wwr.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
