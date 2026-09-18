---
name: check-glassdoor
description: Search Glassdoor Canada for recent SRE, Platform, DevOps, Cloud, and DevSecOps jobs; flag likely cross-source duplicates, score every accessible posting against this repository's candidate profile, and update the Glassdoor HTML report. Use when the user asks to run, check, or search Glassdoor for jobs.
---

# Check Glassdoor

Search Glassdoor Canada, validate current postings, compare every result with Marc's profile, and update `reports/glassdoor-job-search.html`. All external activity is strictly read-only: never apply, use Easy Apply, save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Browser access

Glassdoor Canada (`glassdoor.ca`) loads cleanly with no login wall to browse listings or full postings — sign-in is only needed for reviews/salary-community content, which this skill never touches. Use a browser for this source.

Expect partial overlap with other sources: Glassdoor pools listings that also surface via Indeed and other boards, alongside titles unique to this site.

Search via:

`https://www.glassdoor.ca/Job/canada-<keyword-slug>-jobs-SRCH_IL.0,6_IN3_KO7,<N>.htm`

`<keyword-slug>` is the keyword lowercased with spaces as hyphens. `<N>` is approximately the keyword's character count including spaces, but the exact formula is not fully pinned down — always verify the result count in the page title (`"<count> ... jobs in Canada, <month> <year> | Glassdoor"`) before treating a query as exhausted, and retry with `<N>` adjusted by 1-2 if the count is 0. Using the on-page search box instead of constructing the URL directly is a reasonable alternative when the URL encoding proves unreliable.

If the site presents a CAPTCHA, verification prompt, or blocking page, stop the run and report it immediately, naming the posting that triggered it. A "sign in to see salary insights" or similar community-content prompt can be ignored — the core job description remains readable without signing in; never click Sign In. Never bypass a real challenge. Close temporary tabs when finished.

## Search scope

If the user supplies a query, use it alone and review the first 15 results. Otherwise run separately:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

Review up to eight results per keyword in the default rotation. If a keyword returns no relevant results after the retry above, continue to the next; if every keyword is empty, report that outcome.

Deduplicate by company plus exact title.

## Geography and eligibility

The `canada-` URL prefix scopes results to Canada by construction — no hard eligibility gate is needed. A "Remote" tag on an individual posting could theoretically hide non-Canada bias (the same caution warranted on RemoteOK/We Work Remotely), but this is not confirmed as a widespread issue here; treat it as a soft skim-the-body caution rather than a gate.

## Validate and extract

Open each candidate posting. Extract full description, salary (employer-provided or Glassdoor-estimated), skill tags, remote/hybrid/onsite status, and company. If a posting fails to load, mark it "Could not validate" and continue.

Check `applications.md` for a matching company/title row before final scoring — note it as a likely duplicate with its status rather than silently excluding it; overlap is useful confirmation, not noise to filter out.

## Classification and scoring

Classify each posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every posting a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay and location outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/glassdoor.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py glassdoor` to regenerate `reports/glassdoor-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no validated jobs. Include every scored row, direct posting URLs, pipeline status, run date, and counts for searches completed, results reviewed, validated jobs, inaccessible postings, and known pipeline matches.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Location / office cadence | Salary / rate | Biggest gap | Possible duplicate | Posting |
|---:|---|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the Glassdoor job page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

After the table, list `Could not validate` entries and material search limitations. Ask which roles the user wants investigated or added to `applications.md` — skip re-offering any posting already flagged as a duplicate. Do not draft application material or write files other than `reports/data/glassdoor.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates as a final safety net, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied` or `Rejected` without the user's explicit confirmation.
