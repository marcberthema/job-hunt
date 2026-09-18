# Spec: `addjob` — Manual Job Intake

## Problem

Every `check-*` skill discovers and scores postings but never files anything on its own — filing
only happens once the user picks a posting to pursue. We need one shared, portable capability
that any of those skills (or the user, with a bare URL) can hand off to, producing a scored,
drafted record without duplicating the fetch/score/draft logic in every board-specific skill.

## Capability

A skill that takes a single job posting URL (or pasted text), fetches and reads it, scores it,
drafts a cover letter and tailored resume, and appends one row to `applications.md` — the shared
output every `check-*` skill's "Follow-up filing" section points to, and the same schema the
`review` skill reads from.

## Usage

Invoked directly with a URL, or by any `check-*` skill once the user selects a posting from its
results table.

## Behavior

1. **Duplicate check.** Before fetching, scan `applications.md` for this `Source` URL or an
   obvious `Company`+`Role` match. If found, tell the user what's on record (its `Status`) and
   ask whether to proceed before continuing.
2. **Fetch** the posting. If it can't be fetched or doesn't look like a job posting (e.g. login
   wall, generic homepage), tell the user and stop — don't guess.
3. **Read `profile.md` and `resume/marc-berthelette-resume-en.md` first** — background, rate,
   preferences, red flags, scoring notes, and existing experience to draw from.
4. **Extract** from the posting: role title, company, engagement type (contract / fractional /
   FTE — infer from language), rate/salary if stated, location/remote policy, days in office per
   week (`0` remote, stated count for hybrid, `5` on-site, "Not stated" if hybrid with no count
   given), posting URL, and the board it came from (Indeed, LinkedIn, BuiltIn, Dice, Job Bank,
   RemoteOK, Eluta, S.i. Systems, Randstad, We Work Remotely, Braintrust, Procom, Robert Half,
   Glassdoor, or `Manual` when the user supplied it directly).
5. **Score** 0–10 against `profile.md`'s scoring notes and red flags, mostly skill-based. Logistics
   (on-site, below-target pay) don't drag the score down — surface them as flags instead, so a
   great skill match on an on-site role still reads as a high score with a clear caveat.
6. **Draft**:
   - **Cover letter** — a short, tailored draft, written to
     `resume/cover-letters/cover-letter-<company-slug>-<role-slug>.md`.
   - **Tailored resume** — a resume delta naming which existing experience to lead with for this
     posting, written to `resume/tailored/<YYYY-MM-DD>-<company-slug>-<role-slug>-en.md`.
   Never rewrite the base resume file itself; only produce these per-posting derivatives. Follow
   the naming convention already established by existing files in those two folders.
7. **Append one row** to `applications.md` with `Status: New` per the schema below. Never write
   `Status: Applied` or `Status: Rejected` — those transitions belong to the `review` skill only.
8. **No auto-apply** — this skill only files the draft for review, consistent with the manual
   approval gate in `CLAUDE.md`.
9. Report back to the user: score, one-line summary, any flags, and the two file paths written.

## `applications.md` Row Schema

`applications.md` is one markdown table at the repo root. Appending a job means adding one row:

| Date Found | Status | Status Date | Score | Company | Role | Board | Source | Notes |
|---|---|---|---:|---|---|---|---|---|
| `<YYYY-MM-DD>` | `New` | `<YYYY-MM-DD>` | `<0-10>` | `<Company>` | `<Role Title>` | `<Board>` | `<url>` | `<flags, or blank>` |

- `Date Found` and `Status Date` are both today's date at creation time.
- `Notes` carries logistics flags (on-site, below-target rate, unstated details) surfaced during
  scoring — pipe characters (`|`) inside any field must be escaped as `\|` so the table doesn't
  break.

## Edge Cases

- **Duplicate posting** (same URL or same company+role already in `applications.md`): warn the
  user and ask whether to proceed, rather than silently creating a duplicate row.
- **Unfetchable URL** (paywall, JS-only rendering, 404): report the failure; ask the user to
  paste the posting text instead as a fallback.
- **Score 0–4**: still append the row and write the drafts (keeps a record of the reasoning) but
  flag clearly in the chat response that it's a low-fit posting.

## Out of Scope

- Auto-submitting applications.
- Editing `resume/marc-berthelette-resume-en.md` directly.
- Changing a row's `Status` to `Applied` or `Rejected` — that's the `review` skill's job.
