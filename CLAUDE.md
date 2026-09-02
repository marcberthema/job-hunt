# Job Hunt

> This repo automates the consulting job search pipeline: find → score → draft → review → apply.
> All specs and plans follow a conversational workflow — no slash commands for the spec/plan phase.
> Dedicated commands exist for the job flow only (`/findjobs`, `/review`).

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
   `/check-*` skills and `/findjobs` aggressively (daily/every-other-day, not weekly) across all
   working sources in `job_sources.md`, clear the `jobs/new/` review backlog quickly, and apply
   broadly.
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
  specs/
    INDEX.md              ← Progress tracker for all automation stories
    <story>.md            ← Feature specs (written conversationally, one per automation capability)
  plans/
    <story>.md            ← Implementation plans derived from specs
  jobs/
    new/                  ← Postings found and scored, awaiting your review
    applied/              ← Applications you approved and submitted
    rejected/             ← Postings you rejected or that rejected you
  .claude/commands/
    findjobs.md           ← /findjobs — find, score, and draft applications
    review.md             ← /review — walk the new/ queue for approval
```

---

## Job Sources

`job_sources.md` tracks every job board evaluated for this search — which ones are automatable
via a `/check-*` skill, which are blocked/broken, and which need manual checking. Each row has a
`Last Checked` date. When the user asks for a status (e.g. "give me a status" any morning), read
this file and recommend the oldest-checked source first. After running any `/check-*` command,
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

```
Found (jobs/new/)  →  Reviewed & approved  →  Applied (jobs/applied/)
                   →  Rejected             →  Rejected (jobs/rejected/)
```

Each job file is a markdown document with:
- Source URL and posting date
- Role title, company, and engagement type
- Fit score (0–10) and reasoning
- Tailored resume delta (what to emphasize)
- Draft cover letter

You move files between folders manually after review. `/review` walks you through `jobs/new/` and
helps you decide.

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

## Commands

| Command      | Purpose                                                                  |
|--------------|--------------------------------------------------------------------------|
| `/findjobs`  | Scrape/read sources, score postings against profile, draft letters, save to `jobs/new/` |
| `/review`    | Walk `jobs/new/` one posting at a time (highest score first), pay/days-in-office/contract-type highlighted — reject/skip, or apply (cover letter + application-question help), moving to `applied/` once you confirm submission |
| `/addjob`    | Manual intake: fetch/score/draft a single posting by URL into `jobs/new/` |
| `/check-indeed` | Search Indeed, quick-score every result in a table, then file picks via `/addjob`'s logic |
| `/check-dice`   | Search Dice, gate out clearance/US-work-authorization-only postings before scoring, then quick-score the rest |
| `/check-jobbank` | Search Job Bank (Canada), quick-score every result in a table, then file picks via `/addjob`'s logic |
| `/check-builtin` | Search BuiltIn, quick-score every result in a table, then file picks via `/addjob`'s logic |
| `/check-linkedin` | Search LinkedIn Jobs via Claude in Chrome (your logged-in session, clears the auth wall), quick-score every result in a table, then file picks via `/addjob`'s logic |
| `/check-wwr` | Search We Work Remotely via Claude in Chrome (clears the bot-block), gate out region-ineligible postings before scoring, then file picks via `/addjob`'s logic |
| `/check-remoteok` | Search RemoteOK via Claude in Chrome (clears the bot-block), gate out region-ineligible postings before scoring using its reliable flag-emoji tags, then file picks via `/addjob`'s logic |
| `/check-braintrust` | Search Braintrust via Claude in Chrome (clears the client-side-rendering block, no login needed), gate out region-ineligible postings before scoring, then file picks via `/addjob`'s logic |
| `/check-eluta` | Search Eluta.ca via Claude in Chrome, open each posting's cached copy to work around JS-fragment links (no eligibility gate needed — Canada-only by construction), then file picks via `/addjob`'s logic |
| `/check-sisystems` | Search S.i. Systems (Canada's largest IT staffing agency) via Claude in Chrome (WAF-block workaround), no eligibility gate needed (Canada-only by construction), then file picks via `/addjob`'s logic |
| `/check-procom` | Search Procom's real jobs portal via Claude in Chrome, gate out US-only postings before scoring, then file picks via `/addjob`'s logic |
| `/check-randstad` | Browse Randstad Canada's Technologies category via Claude in Chrome (site-side keyword search is broken, filters client-side instead), no eligibility gate needed, then file picks via `/addjob`'s logic |
| `/check-roberthalf` | Search Robert Half Technology (Canada, Contract listings) via plain WebFetch — no Chrome workaround needed — then file picks via `/addjob`'s logic |
| `/check-glassdoor` | Search Glassdoor Canada via Claude in Chrome, flag likely duplicates against other sources, then file picks via `/addjob`'s logic |

---

## Website (`site/`)

The site is a pure HTML/CSS personal consulting site with no build step. Deploy by pointing Cloudflare Pages (or Netlify/GitHub Pages) at the `site/` folder.

**Decisions made — do not revert without confirmation:**
- **No rate on the public site** — consulting rate stays out of all public-facing copy; discuss on first call instead
- **Bilingual site** — `site/index.html` (English) and `site/fr/index.html` (French); both pages link to each other via an EN/FR nav toggle
- Regenerate with `/buildsite` after updating `profile.md`

---

## Conventions

- **`profile.md` is always read first** by any command before doing anything
- **One file per job** in `jobs/` — filename: `<YYYY-MM-DD>-<company>-<role-slug>.md`
- **No API tokens** — everything runs within your Claude subscription via Claude Code
- **Manual approval gate** — no command ever submits an application without your explicit confirmation
- **Git tracks everything** — commit after each `/findjobs` run and after each review session
