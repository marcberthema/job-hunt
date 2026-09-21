---
name: check-procom
description: Search Procom's contractor jobs portal for recent Canadian SRE, Platform, DevOps, Cloud, and DevSecOps contract jobs; run a lightweight US-location eligibility gate before scoring, and update the Procom HTML report. Use when the user asks to run, check, or search Procom for jobs.
---

# Check Procom

Search Procom, validate current postings, gate eligibility before scoring, compare every eligible result with Marc's profile, and update `reports/procom-job-search.html`. All external activity is strictly read-only: never apply, save a job, create an account, sign in, upload information, or submit a form. Apart from refreshing the board-specific report, do not create job files or change pipeline state.

## Source of truth

Before gating or scoring, read `profile.md` and `resume/marc-berthelette-resume-en.md` completely. Their current contents override older commands, specifications, plans, job files, and historical source notes. Never invent or strengthen experience.

## Browser access

Procom's public marketing site (`procom.ca/find-jobs/`) is a dead end — it redirects to a broken client-portal shell that never resolves to real content. The real jobs portal is a different subdomain, loading cleanly via browser with no login required to browse:

`https://myprocom-portal.procomservices.com/jobs?loginType=contractor&lang=en`

Search via `?keyword=<keyword, spaces as +>` on that same portal. Each result card shows a remote/hybrid/onsite tag directly, plus title, location, posted date, and pay rate when disclosed (`$X-$Y/hr CAD`). The results list may only render the first visible card's full content on a naive text extraction — confirm you're capturing all visible results, not just the first, before deciding which to open.

If the site presents a CAPTCHA, verification prompt, or blocking page, stop the run and report it immediately, naming the posting that triggered it. Never attempt to solve or bypass a challenge. Close temporary tabs when finished.

## Search scope

If the user supplies a query, use it alone and review the first 15 results. Otherwise run separately:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Cloud Engineer
- DevSecOps Engineer
- Forward Deployed Engineer

Review up to eight results per keyword in the default rotation. If a keyword returns no relevant results, continue to the next; if every keyword is empty, report that outcome.

Deduplicate by company plus exact title.

## Run completeness and query audit

All six default queries are mandatory and independent. Navigate each portal query separately, verify the rendered keyword and real results list, then record the result count, number reviewed, posting IDs or canonical URLs (or `none`), and `Complete`, `Zero results`, or `Incomplete - <reason>`. Deduplicate only after the audit, retaining repeated postings under every query where they appeared.

A CAPTCHA, verification page, login wall, persistent loading shell, or other block makes the affected query and overall rotation incomplete. Never infer completion from the marketing-site shell, snippets, or a single visible card.

## Eligibility gate

Procom is a Canadian staffing agency, but some US postings mix in. Use the location field shown per result:

- A Canadian city/province, or "Remote" with no US-specific qualifier: eligible.
- A US city/state shown: open the full posting first to check for an explicit "open to Canada-based remote candidates" line before excluding. If silent or explicitly US-only: add a `score: -1` row with status `Ineligible — US-only location` and the evidence in `gap`.

Whether a posting is ruled out during the quick location check or the full validation pass, keep it in `rows` as `score: -1` with a specific `Ineligible — <short reason>` status pill. Never create a separate ineligible collection or footer list.

## Validate and extract

Open each eligible posting. Extract exact title, disclosed client/company (often anonymized as "Procom" — the client name may or may not be disclosed; this is normal for a staffing agency, not a red flag), full description, pay rate, job type (remote/hybrid/onsite), and location. If a posting fails to load, mark it "Could not validate" and continue.

Check `applications.md` for a matching company/title row. When the client is anonymous, match on `procom` as the company slug unless a prior row reveals the real client. Keep known roles in the table and label their pipeline status from its `Status` column.

## Classification and scoring

Classify each eligible posting by its actual center of gravity:

- `SRE`: reliability, incidents, observability, SLOs, availability, performance, or operational toil.
- `Platform`: shared infrastructure, developer platforms, cloud foundations, Kubernetes platforms, IaC, or internal tooling.
- `DevOps`: CI/CD, release engineering, deployment automation, configuration management, or mixed cloud delivery.

Give every eligible job a 0–10 `Skill score` based only on technical/domain fit, seniority, autonomy, and demonstrated leadership. Keep pay, job type, and location outside the skill score while reporting them plainly. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, architecture ownership, and people management. Under `Biggest gap`, name the single most consequential mismatch; use `None material` only when justified.

An eligible posting whose actual work is outside the SRE/Platform/DevOps center of gravity still gets a row — score it `0` with `status: "Out of scope"` per `reports/report_schema.md`, with the gap stating what the role actually is, rather than dropping it from the results.

## Expiration status

Check freshness from the canonical employer page, explicit closed/expired notices, and stated closing dates. In the HTML report, preserve previously reported or newly discovered stale roles and label them visibly as `Expired` when confirmed, `Likely expired` when the evidence is indirect, or `Freshness unconfirmed` when no reliable date or current canonical page is available. Do not present expired roles as actionable or include them in eligible-current counts. Record the evidence and check date; never infer expiration solely from age.

## Output and report

Before returning results, write this run's data to `reports/data/procom.json` per `reports/report_schema.md`, then run `python3 reports/build_report.py procom` to regenerate `reports/procom-job-search.html` — never hand-author the HTML directly. Refresh the data file on every invocation, including runs with no eligible jobs. Include every result and exclusion in `rows`, direct posting URLs, pipeline or exclusion status pills, run date, and counts for searches completed, results reviewed, eligible, ineligible, inaccessible, and known pipeline matches.

Put the per-query audit in `notes_sections`, summarize it in `method`, and report searches attempted separately from searches completed plus unique results reviewed. Reconcile it before `latest_update`; all mandatory queries must be `Complete` or `Zero results` before the run is called complete. Preserve matching `Applied`, `Skipped`, and `Rejected` statuses exactly and never reset a reviewed posting to `New`.

Lead with the run totals. Sort validated jobs by score descending using exactly:

| Skill score | Family | Job title | Company | Job type | Salary / rate | Biggest gap | Posting |
|---:|---|---|---|---|---|---|---|

Use only `SRE`, `Platform`, or `DevOps` for Family. Link directly to the Procom job detail page. Preserve currency and pay period, and use `Not stated` for unknown facts. Include low scores rather than hiding weak matches.

Put location-gated and other ineligible entries in the same table as `score: -1` rows; never repeat them in a footer list. After the table, list only `Could not validate` entries and material search limitations. Ask which roles the user wants investigated or added to `applications.md`. Do not draft application material or write files other than `reports/data/procom.json` during discovery.

## Follow-up filing

For a selected posting, refresh it read-only, re-check duplicates, and follow the `addjob` skill: append one row to `applications.md` with `Status: New`. When the client is anonymous, use `procom` as the company slug unless the description reveals the real client. Never submit an application or change a row's status to `Applied`, `Skipped`, or `Rejected` without the user's explicit confirmation.
