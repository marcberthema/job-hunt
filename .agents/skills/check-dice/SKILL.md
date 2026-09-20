---
name: check-dice
description: Search Dice for recent sponsor-willing remote DevOps, Platform, SRE, Cloud, DevSecOps, and Forward Deployed roles; gate US work authorization and clearance requirements before scoring eligible jobs. Use when the user asks to run, check, or search Dice for jobs.
---

# Check Dice

Search Dice, validate accessible postings, apply the eligibility gate before scoring, compare eligible jobs with Marc's profile, and update reports/dice-job-search.html. Apart from that report refresh, this is read-only discovery: do not create job files, change pipeline state, sign in, submit forms, or apply unless the user subsequently asks.

## Input and role rotation

If the user supplies search terms, use them as one query. Otherwise run:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

## Search filters

For each query, use Dice's current equivalent of:

    https://www.dice.com/jobs?filters.postedDate=SEVEN&filters.employmentType=FULLTIME%7CCONTRACTS&filters.workplaceTypes=Remote&filters.willingToSponsor=true&q=<URL-encoded-query>&countryCode2=CA&language=en

Required filters:

- Posted within the past seven days
- Full-time or contract
- Remote
- Willing to sponsor
- Canada country code
- English

Dice is US-market-heavy and may return US roles despite countryCode2=CA. Sponsor-willing remote US positions remain in scope because Marc is a Canadian citizen and may qualify for TN work authorization.

For a custom query, review the first 15–20 results. For the default rotation, review up to eight results per query. Do not paginate beyond the first page. If one query is empty, continue; if all are empty, report that outcome.

Deduplicate rotation results by company plus exact title before fetching descriptions and applying the eligibility gate.

## Source of truth

Read profile.md completely before eligibility assessment or scoring. Its current contents override older commands, specifications, plans, job files, and run notes. Never invent or strengthen experience.

## Validate and recover postings

Open every deduplicated candidate. If a Dice posting is stale, inaccessible, or incomplete, search for the exact title and company on the employer's official career site. Prefer a matching current employer page as the canonical URL. If neither source exposes a complete current description, list the posting under Could not validate and do not score it.

## Eligibility gate

Apply these rules in order before detailed extraction or scoring:

1. Required US security clearance, including TS/SCI, Secret, or Public Trust: ineligible. TN status does not satisfy citizenship-based clearance requirements.
2. US work-status restriction with explicit sponsorship language such as will sponsor, able to sponsor, H-1B, TN, or visa sponsorship: eligible. Flag: TN-sponsorship path — likely W-2 employment with no corporation-to-corporation arrangement; confirm support for TN and whether sponsorship concerns a work visa rather than permanent residence.
3. Current US authorization required without sponsorship: ineligible.
4. Fully on-site US role without a remote option: ineligible.
5. Otherwise: eligible. If authorization language is absent, flag: Confirm work authorization with recruiter before applying.

For an ineligible posting, stop detailed review and record only title, company, direct URL, and one-line reason. Do not score it.

## Score eligible postings

Score each eligible posting from 0–10 against profile.md using technical and domain fit, seniority, autonomy, and demonstrated leadership. Give appropriate weight to Azure, platform engineering, CI/CD, infrastructure as code, and financial or energy experience. Treat logistics and authorization as flags rather than skill-score inputs.

Apply the profile's honesty rules for AWS, GCP, Kubernetes cluster administration, programming languages, people management, and other depth requirements. Give one concise rationale and identify the single biggest skill gap.

Check `applications.md` for a matching `Source` URL or `Company`+`Role` row. Keep known eligible roles and label their pipeline status from its `Status` column.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output

Before responding, write this run's data to `reports/data/dice.json` per `reports/report_schema.md` — run date, queries completed, search boundary, unique results reviewed, eligible/ineligible/inaccessible totals, employer recoveries, pipeline matches, every scored eligible posting, every ineligible posting and reason, canonical links — then run `python3 reports/build_report.py dice` to regenerate `reports/dice-job-search.html`. Never hand-author the HTML directly.

Refresh the data file on every invocation, including runs with no eligible results.

Return two sections.

### Eligible

Sort by score descending:

| Role — Company | Score | Why | Flags |
|---|---:|---|---|

### Ineligible

Do not score these:

| Role — Company | Reason |
|---|---|

Then list Could not validate postings and material limitations. Ask which eligible postings the user wants investigated or added to `applications.md`. Do not draft applications or write files other than `reports/data/dice.json` during discovery.

## Follow-up filing

For a selected eligible posting, reuse its fetched description when current, check duplicates again, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without explicit confirmation.
