---
name: review
description: Walk applications.md rows with Status New, highest score first, and either reject/skip each one or help apply — cover letter refinement and application-question support — updating the row's Status to Applied only once the user confirms submission. Use when the user asks to review the job backlog, walk new postings, or start a review session.
---

# Review

Walk every `New` row in `applications.md` one posting at a time, highest `Score` first, and help decide: apply, reject, or skip. This is the only place a row's `Status` changes to `Applied` or `Rejected` — no other skill sets those values.

## 1. Read the source of truth

Read `profile.md` in full before anything else, so any judgment calls made during review (e.g. urgency-mode scoring bar, red flags) are grounded in current preferences.

## 2. Build the queue

Read `applications.md`. Filter to rows where `Status = New`, sort by `Score` descending, tie-broken by `Date Found` ascending, so the single most-promising posting comes up first.

If no `New` rows exist, tell the user the backlog is clear and stop.

## 3. Present one posting

Pop the top of the queue and show a detailed view:

- **Role — Company**
- **Source:** the URL, on its own line
- **Board**, **Score**, and **Notes** (logistics flags) from the row
- The cover letter draft, read from `resume/cover-letters/cover-letter-<company-slug>-<role-slug>.md`, in full
- The tailored resume delta, read from `resume/tailored/<date>-<company-slug>-<role-slug>-en.md`, in full
- If either file is missing (posting was filed before this convention, or filed through a path that skipped drafting), say so plainly rather than erroring
- Queue position, e.g. "Posting 1 of 9 remaining"

## 4. Ask for a decision

Ask: **Apply**, **Reject**, **Skip**, or **Stop**. One posting at a time — no batch/quick-approve shortcut.

- **Reject**: if the user gives a reason, add it to the row's `Notes`. Don't prompt for a reason if they don't offer one. Update the row: `Status → Rejected`, `Status Date → today`. Advance to the next posting.

- **Skip**: no row changes. Advance to the next posting.

- **Stop**: break out of the loop and go to step 5.

- **Apply**: do not update the row yet. Open an application-assistance exchange scoped to this posting:
  - Ask (if not already clear) how they're applying — a portal, email, LinkedIn Easy Apply, etc.
  - Refine the cover letter draft on request, grounded in `profile.md` and `resume/marc-berthelette-resume-en.md` — don't invent experience that isn't documented there. Save refinements back to the same `resume/cover-letters/` file.
  - Answer any application-form questions the user pastes in, the same way.
  - This can span several turns. Stay on this posting until one of:
    - The user **confirms they submitted** the application → update the row: `Status → Applied`, `Status Date → today`. Advance to the next posting.
    - The user decides not to submit after all → treat as Reject or Skip per their call, then advance.

## 5. End-of-run summary

Report: how many were applied / rejected / skipped this session, and how many `New` rows remain. Remind the user to commit, per `CLAUDE.md`'s "commit after each review session" convention — don't commit automatically, only if asked.

## Out of scope

- Never submits an application on the user's behalf — only the user does that; this skill helps draft/refine and then records the outcome once they confirm.
- No re-scoring or re-fetching — scoring already happened when the row was filed via the `addjob` skill or a `check-*` skill.
