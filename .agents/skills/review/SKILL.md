---
name: review
description: Walk applications.md rows with Status New, highest score first, presenting a fresh company/role summary for each and letting the user apply or skip — drafting materials and marking the row InProcess on Apply, then Applied only after confirmed submission. Use when the user asks to review the job backlog, walk new postings, or start a review session.
---

# Review

Walk every `New` row in `applications.md` one posting at a time, highest `Score` first, and help decide: apply or skip. The normal pursued path is `New → InProcess → Applied`: `InProcess` means the application materials are ready but Marc has not yet confirmed submission. (`Rejected` is a separate, later transition — see step 7 — and never happens directly from `New` or `InProcess`.)

## 1. Read the source of truth

Read `profile.md` in full before anything else, so any judgment calls made during review (e.g. urgency-mode scoring bar, red flags) are grounded in current preferences.

## 2. Build the queue

Read `applications.md`. Filter to rows where `Status = New`, sort by `Score` descending, tie-broken by `Date Found` ascending, so the single most-promising posting comes up first.

If no `New` rows exist, tell the user the backlog is clear and stop.

## 3. Present one posting

Pop the top of the queue and present a fresh company/role summary:

- **Role — Company**
- **Source:** the URL, on its own line
- **Board** and **Score** from the row
- Fetch the live posting (unless it was already fetched earlier this same session) and summarize: what the company does, the role's actual responsibilities, required/nice-to-have skills, compensation, location/remote policy, and any notable flags (sponsorship, on-site cadence, salary vs. the profile's floors, employer rating, etc.) — not just the row's stored `Notes` field, which may be thin or stale.
- If the posting can't be fetched (dead link, login wall), fall back to the row's `Notes` and say plainly that the summary is from stored data, not a live check.
- Queue position, e.g. "Posting 1 of 9 remaining"

Do not surface or read any existing cover letter / tailored resume file at this stage — drafting only happens after the user says Apply (step 4).

## 4. Ask for a decision

Ask: **Apply**, **Skip**, or **Stop**. One posting at a time — no batch/quick-approve shortcut.

- **Skip**: this is Marc's own decision not to pursue the posting — a skill gap, duplicate, expired listing, bad rate, wrong domain, anything. If the user gives a reason, add it to the row's `Notes`. Don't prompt for a reason if they don't offer one. Update the row: `Status → Skipped`, `Status Date → today`. Advance to the next posting.

- **Stop**: break out of the loop and go to step 5.

- **Apply**: immediately draft (or refresh, if a draft already exists) the cover letter and tailored resume, grounded in `profile.md` and `resume/marc-berthelette-resume-en.md` — never invent experience that isn't documented there:
  - Cover letter → `resume/cover-letters/cover-letter-<company-slug>-<role-slug>.md`
  - Tailored resume delta → `resume/tailored/<YYYY-MM-DD>-<company-slug>-<role-slug>-en.md`
  - After both drafts are successfully saved, update the row: `Status → InProcess`, `Status Date → today`. Do not mark it `InProcess` if drafting failed or remains incomplete.
  - Mirror `InProcess` to every matching row in `reports/data/*.json`, matching by canonical URL first and company + exact role second, then rebuild each affected static report with `reports/build_report.py`. This makes pending external submissions visible on the static boards. Do not create a report row when no match exists.
  - Do **not** paste the cover letter (or resume delta) into the chat, ask how they plan to apply, or wait for submission confirmation. Confirm in one line that the drafts are saved (file paths only, not contents) and immediately advance to the next posting's summary. If the user wants to see or revise a draft, they'll ask for it by name.

## 5. End-of-run summary

Report: how many were marked `InProcess` / skipped this session, how many `New` rows remain, and the total number of `InProcess` rows still awaiting submission. Remind the user to commit, per `CLAUDE.md`'s "commit after each review session" convention — don't commit automatically, only if asked.

## 6. Later submission confirmation

Whenever the user says they submitted an application to a specific posting — in this session, later in the same review run, or in an entirely different conversation — find the matching `applications.md` row (by source URL first, then company + role) and update it from `InProcess` to `Applied`, with `Status Date → today`. Mirror `Applied` to matching rows in `reports/data/*.json` and rebuild affected reports as in step 4. This can happen well after drafting and does not require re-entering the review loop. If the row is still `New`, verify that the user truly submitted it before recording the direct correction to `Applied`; never interpret merely wanting to apply as submission confirmation.

## 7. Employer outcome (Applied → Rejected)

Whenever the user reports that an employer passed on him for a posting that's currently `Status: Applied`, update that row: `Status → Rejected`, `Status Date → today`, and record any reason given in `Notes`. Mirror the status to matching report JSON rows and rebuild affected reports. This is the only path to `Rejected` — it always starts from `Applied`, never directly from `New`, `InProcess`, or `Skipped`. Like step 6, this can happen at any time, in any session, independent of an active review loop.

## Out of scope

- Never submits an application on the user's behalf — only the user does that; this skill records `InProcess` when drafts are ready, `Applied` only once the user separately confirms submission, and `Rejected` only once the user reports the employer's outcome.
- No re-scoring — scoring already happened when the row was filed via the `addjob` skill or a `check-*` skill. Re-fetching the live posting for a fresh summary (step 3) is expected, though.
