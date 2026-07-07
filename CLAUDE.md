# Job Hunt

> This repo automates the consulting job search pipeline: find → score → draft → review → apply.
> All specs and plans follow a conversational workflow — no slash commands for the spec/plan phase.
> Dedicated commands exist for the job flow only (`/findjobs`, `/review`).

---

## Repository Structure

```
job-hunt/
  CLAUDE.md               ← This file — project conventions and workflow
  profile.md              ← Source of truth: background, skills, rate, preferences, what "real consulting" looks like
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
| `/review`    | Walk through `jobs/new/` one by one — approve (move to `applied/`) or reject (move to `rejected/`) |

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
