# Spec: `/addjob` — Manual Job Intake

## Problem

`/findjobs` (Gmail-based discovery) requires OAuth setup, platform sign-ups, and alert
configuration that isn't done yet (see `todo.md`). We want to exercise and validate the
scoring → drafting → review → apply pipeline now, without waiting on that integration.

## Capability

A command that takes a single job posting URL, fetches and reads it, and produces a fully
scored, drafted job file in `jobs/new/` — using the same output schema `/findjobs` will
eventually produce, so `/review` and everything downstream needs no changes.

## Usage

```
/addjob <url>
```

## Behavior

1. **Fetch** the posting at `<url>` (WebFetch). If the page can't be fetched or doesn't look
   like a job posting (e.g. login wall, generic homepage), tell the user and stop — don't
   guess.
2. **Read `profile.md` first** (per repo convention) — background, rate, preferences, red
   flags, scoring notes.
3. **Extract** from the posting: role title, company, engagement type (contract / fractional /
   FTE — infer from language), rate/salary if stated, location/remote policy, posting URL,
   today's date as "found" date.
4. **Score** 0–10 against `profile.md`'s scoring notes and red flags, with a short written
   rationale (2–4 sentences) referencing specific posting details. Should be mostly skill based.
   The pay and the remote vs hybrid vs on site will also be shown for each job. If I am a great fit but its a on site job, I want the score to high but mention its on site, same with pay.
5. **Draft**:
   - Resume delta — which existing experience/skills to emphasize for this posting (bullet
     list, references `resume/marc-berthelette-resume-en.md`, doesn't rewrite the resume file
     itself).
   - Cover letter — short, tailored draft in the job file.
6. **Write** the job file to `jobs/new/<YYYY-MM-DD>-<company>-<role-slug>.md` per the schema
   below. Never write directly to `jobs/applied/` or `jobs/rejected/` — those are `/review`'s
   job.
7. **No auto-apply** — this command only files the draft for review, consistent with the
   manual approval gate in CLAUDE.md.
8. Report back to the user: score, one-line summary, and the file path.

## Job File Schema

```markdown
# <Role Title> — <Company>

- **Source:** <url>
- **Found:** <YYYY-MM-DD>
- **Engagement type:** Contract | Fractional | Full-time | Unclear
- **Rate/Salary (stated):** <as posted, or "not stated">
- **Location/Remote:** <as posted>

## Fit Score: <0-10>

<rationale, 2-4 sentences>

## Resume Delta

- <what to emphasize>
- ...

## Draft Cover Letter

<tailored draft>
```

## Edge Cases

- **Duplicate posting** (same URL or same company+role already in `jobs/`): warn the user and
  ask whether to proceed, rather than silently creating a duplicate file.
- **Unfetchable URL** (paywall, JS-only rendering, 404): report the failure; ask the user to
  paste the posting text instead as a fallback.
- **Score 0–4**: still write the file (so there's a record and the user can see the reasoning)
  but flag clearly in the chat response that it's a low-fit posting.

## Out of Scope

- Gmail integration (separate story, see `todo.md` #4/#6).
- Auto-submitting applications.
- Editing `resume/` files directly.
