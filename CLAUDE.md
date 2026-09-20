# Job Hunt

> This repo automates the consulting job search pipeline: find → score → draft → review → apply.
> All specs and plans follow a conversational workflow — no slash commands for the spec/plan phase.
> The job flow itself runs on portable skills in `.agents/skills/`, invoked in plain language
> ("check builtin for jobs," "walk the review queue") — usable identically from Claude Code or
> ChatGPT/Codex, so the search isn't locked into one agent's token budget.

---

## Feedback Style — Brutal Honesty Requested

Marc wants direct, unsugarcoated assessments — no pipe dreams, only achievable goals. If a job,
career path, certification plan, or strategy has a bad outlook, say so plainly and explain why,
even if it's not what he wants to hear. This applies to scoring rationale, career/cert advice,
and any strategic recommendation in this repo — don't soften a weak assessment to be encouraging.

---

## Current Situation (as of 2026-08-19) — URGENT

Marc's long-term consulting contract at Énergir will not be renewed — it ends in **just over 5
weeks**. He is the main financial provider for his family and cannot afford a long gap between
engagements. This changes priorities across the whole repo until he lands a new role:

1. **First — external presence.** LinkedIn profile and resumes must be fully in sync with
   `profile.md` and read well to a recruiter (headline, About, experience entries, skills). This
   comes before any new outreach — a recruiter who clicks through from an application to a stale
   or mismatched LinkedIn profile is a lost opportunity.
2. **Then — active, high-frequency search.** Once the profile/resume sync is done, run the
   `check-*` skills aggressively (daily/every-other-day, not weekly) across all working sources in
   `job_sources.md`, clear the `applications.md` `New` backlog quickly, and apply broadly.
3. **Scoring bar is temporarily lower.** Per the scoring notes in `profile.md`, treat 5+ (not just
   8–10) as "apply" — urgency now outweighs strict selectivity. Do not relax the remote-only /
   on-site red flag without asking first.

Revisit this section once Marc lands a new role or the timeline changes.

---

## Repository Structure

```
job-hunt/
  CLAUDE.md               ← This file — project conventions and workflow
  profile.md              ← Source of truth: background, skills, rate, preferences, what "real consulting" looks like
  job_sources.md          ← Every job board evaluated: working/blocked/manual, last-checked date per source
  applications.md         ← The ledger: one row per posting, Status = New | Applied | Skipped | Rejected
  specs/
    INDEX.md              ← Progress tracker for all automation stories
    <story>.md            ← Feature specs (written conversationally, one per automation capability)
  plans/
    <story>.md            ← Implementation plans derived from specs
  .agents/skills/
    check-<board>/SKILL.md ← One per job board — discover, validate, score, refresh that board's report
    addjob/SKILL.md        ← Shared filing step: fetch a URL, score it, draft, append a New row
    review/SKILL.md        ← Walk New rows, apply/skip/decline, update Status
  reports/
    build_report.py        ← Deterministic renderer: data/<board>.json → <board>-job-search.html (no AI-authored HTML)
    report_schema.md        ← The JSON schema every check-* skill writes to
    data/<board>.json       ← Structured scoring output per board, written by its check-* skill
    index.html             ← Nav hub across every board's report
    <board>-job-search.html ← Rendered from data/<board>.json, refreshed on every check-* run
  resume/
    cover-letters/          ← One cover letter per posting pursued
    tailored/                ← One tailored resume delta per posting pursued
```

---

## Job Sources

`job_sources.md` tracks every job board evaluated for this search — which ones are automatable
via a `check-*` skill, which are blocked/broken, and which need manual checking. Each row has a
`Last Checked` date. When the user asks for a status (e.g. "give me a status" any morning), read
this file and recommend the oldest-checked source first. After running any `check-*` skill,
update that row's date to today.

## Profile

`profile.md` is the single source of truth for everything about you as a consultant. All LLM steps
(scoring, resume tailoring, letter writing) read this file first. Keep it up to date — it is the
most important file in this repo.

It should contain:
- Your background, skills, and domain expertise
- Preferred engagement types (contract, fractional, advisory — not FTE)
- Target rate and engagement length
- Red flags that signal "FTE in disguise" (benefits emphasis, single client, 40h/week mandatory, etc.)
- Geographic and remote preferences
- What a great match looks like

---

## Job Lifecycle

Every posting is one row in `applications.md`, moving through one `Status` column:

```
New  →  Applied   (you confirmed submission)
     →  Skipped   (you decided not to pursue it — skill gap, duplicate, expired, etc.)

Applied  →  Rejected  (the employer passed on you — only reachable from Applied)
```

`Skipped` and `Rejected` look similar but mean opposite things: `Skipped` is Marc's own call, made
before ever applying; `Rejected` means he applied and the employer said no. Never set `Rejected`
directly from `New` — that transition always passes through `Applied` first.

A row carries: date found, score, company, role, the board it came from, its source URL, and any
flags in `Notes`. Full scoring detail and rationale live in that board's
`reports/<board>-job-search.html`; the cover letter and tailored resume for a pursued posting live
in `resume/cover-letters/` and `resume/tailored/`. Nothing moves between folders — a row's
`Status` and `Status Date` just update in place.

The `review` skill walks every `New` row, highest score first, and helps you decide.

---

## Spec / Plan Workflow (conversational)

No `/newspec` command — specs are written through conversation:

1. **Describe the capability** you want to automate in a Claude Code session
2. **Claude writes the spec** to `specs/<story>.md` and adds it to `specs/INDEX.md`
3. **Review and confirm** the spec looks right
4. **Claude writes the plan** to `plans/<story>.md`
5. **Confirm the plan**, then Claude implements it

This mirrors the Brayd workflow but without GitHub Projects or slash commands for the spec/plan phase.

---

## Skills

All in `.agents/skills/`, portable across Claude Code and ChatGPT/Codex — invoke by asking in
plain language, not a slash command. Every `check-*` skill is discovery-only: it scores results
into that board's `reports/<board>-job-search.html` and never files anything on its own. `addjob`
and `review` are the only two that touch `applications.md`.

| Skill | Purpose |
|---|---|
| `addjob` | Shared filing step: fetch/score/draft a single posting by URL, append a `New` row to `applications.md` |
| `review` | Walk `applications.md`'s `New` rows (highest score first), pay/days-in-office/contract-type highlighted — reject/skip, or apply (cover letter + application-question help), updating `Status` to `Applied` once you confirm submission |
| `check-indeed` | Search Indeed for Canada-eligible remote and reachable-city hybrid roles, score every result, file picks via `addjob` |
| `check-dice` | Search Dice, gate out clearance/US-work-authorization-only postings before scoring |
| `check-jobbank` | Search Job Bank (Canada), score every result |
| `check-builtin` | Search BuiltIn, score every result |
| `check-linkedin` | Search LinkedIn Jobs via your logged-in session, score every result |
| `check-wwr` | Search We Work Remotely, gate out region-ineligible postings before scoring |
| `check-remoteok` | Search RemoteOK, gate out region-ineligible postings using its flag-emoji tags |
| `check-braintrust` | Search Braintrust, gate out region-ineligible postings before scoring |
| `check-eluta` | Search Eluta.ca, work around its JS-fragment links via cached copies (no eligibility gate needed — Canada-only by construction) |
| `check-sisystems` | Search S.i. Systems (Canada's largest IT staffing agency) — no eligibility gate needed |
| `check-procom` | Search Procom's real jobs portal, gate out US-only postings before scoring |
| `check-randstad` | Browse Randstad Canada's Technologies category (site-side keyword search is broken, filters client-side instead) — no eligibility gate needed |
| `check-roberthalf` | Search Robert Half Technology (Canada, Contract listings) — no eligibility gate needed |
| `check-glassdoor` | Search Glassdoor Canada, flag likely duplicates against other sources |

---

## Website (`site/`)

The site is a pure HTML/CSS personal consulting site with no build step. Deploy by pointing Cloudflare Pages (or Netlify/GitHub Pages) at the `site/` folder.

**Decisions made — do not revert without confirmation:**
- **No rate on the public site** — consulting rate stays out of all public-facing copy; discuss on first call instead
- **Bilingual site** — `site/index.html` (English) and `site/fr/index.html` (French); both pages link to each other via an EN/FR nav toggle
- Regenerate with `/buildsite` after updating `profile.md`

---

## Conventions

- **`profile.md` is always read first** by any skill before doing anything
- **One row per posting** in `applications.md` — never a file per job
- **No API tokens** — everything runs within your Claude subscription via Claude Code, or the equivalent on ChatGPT/Codex
- **Manual approval gate** — no skill ever submits an application without your explicit confirmation; only the `review` skill sets `Status: Applied`, and only once you confirm submission
- **Git tracks everything** — commit after each `check-*` run and after each review session
