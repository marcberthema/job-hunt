---
description: Walk jobs/new/ one posting at a time (highest fit score first), show a detailed view with pay/days-in-office/contract-type highlighted, and either reject/skip it or help apply — cover letter + application-question support — moving the file to jobs/applied/ only once you confirm submission
---

Implements `specs/review.md` / `plans/review.md`. Follow these steps in order.

## 1. Read profile.md

Read `profile.md` in full before anything else — same hard requirement as every other command in
this repo, so any judgment calls made during review (e.g. urgency-mode scoring bar, red flags)
are grounded in current preferences.

## 2. Build the queue

`Glob jobs/new/*.md` (ignore `review-dashboard.html` and any non-`.md` file). Read each file's
`Fit Score` and `Found` date from its header. Sort the queue by `Fit Score` descending, tie-broken
by `Found` date ascending, so the single most-promising posting comes up first.

If the queue is empty, tell the user `jobs/new/` is clear and stop.

## 3. Present one posting

Pop the top of the queue and show a **detailed** view — this is deliberately longer and more
prominent than `jobs/new/review-dashboard.html`'s compact table, since the point here is to
actually read the posting closely enough to decide:

- **Role — Company**
- **Source:** the URL, on its own line, so it can be opened directly
- A highlighted logistics block, pulled to the top rather than buried in prose:
  - **Pay:** Rate/Salary as stated
  - **Days in office:** the `Days in Office` field. If the file predates this field (filed before
    it existed), say `Not stated (filed before this field existed)` rather than erroring.
  - **Contract vs. full-time:** Engagement type
- **Fit Score** and its full written rationale (not a one-line gist)
- Location/Remote and Flags
- Resume Delta (full list)
- Draft Cover Letter (in full)
- Queue position, e.g. "Posting 1 of 9 remaining"

## 4. Ask for a decision

Ask: **Apply**, **Reject**, **Skip**, or **Stop**. One posting at a time — no batch/quick-approve
shortcut.

- **Reject**: if the user's reply includes a reason, append a `## Rejection Note` section (today's
  date + the reason) to the file before moving it. Don't prompt for a reason if they don't offer
  one — a quiet reject doesn't need justification. `git mv jobs/new/<file> jobs/rejected/<file>`.
  Advance to the next posting.

- **Skip**: no file operation. Advance to the next posting.

- **Stop**: break out of the loop and go to step 5.

- **Apply**: do **not** move the file yet. Open an application-assistance exchange scoped to this
  posting:
  - Ask (if not already clear) how they're applying — a portal, email, LinkedIn Easy Apply, etc.
    — since that shapes how the cover letter should be formatted/delivered.
  - Refine or finalize the draft cover letter on request, grounded in `profile.md` and
    `resume/marc-berthelette-resume-en.md` — don't invent experience that isn't documented there.
  - Answer any application-form questions the user pastes in, the same way.
  - This can span several conversation turns. Stay on this posting — don't advance the queue —
    until one of:
    - The user **confirms they submitted** the application → `git mv jobs/new/<file>
      jobs/applied/<file>`, then advance to the next posting.
    - The user decides not to submit after all → treat as Reject or Skip per their call, then
      advance.

## 5. End-of-run summary

Report: how many were applied / rejected / skipped this session, and how many remain in
`jobs/new/`. Remind the user to:
- Run `/update-dashboard` (it regenerates from the `jobs/new/` backlog, which just changed).
- Commit, per CLAUDE.md's "commit after each review session" convention — don't commit
  automatically, only if asked.

## Out of scope

- Never submits an application on the user's behalf — only the user does that; this command helps
  draft/refine and then records the outcome once they confirm.
- No re-scoring or re-fetching — scoring already happened when the posting was filed.
