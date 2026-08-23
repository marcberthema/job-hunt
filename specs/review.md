# Spec: `/review` — Backlog Review

## Problem

`jobs/new/` accumulates postings from `/addjob` and the `/check-*` sources. CLAUDE.md's job
lifecycle says these move to `jobs/applied/` (approved) or `jobs/rejected/` (rejected) after
review, and the commands table has documented `/review` for this since the repo's early commits
— but the command was never actually built. The backlog has been cleared manually so far (e.g.
commit `1dbc771`, "file 19 applications, reject 28 postings").

`jobs/new/review-dashboard.html` already gives a compact, sortable table view (company, score,
salary, flags) for scanning the whole backlog. `/review` is the deeper, one-job-at-a-time
companion to that — where the dashboard is for triage, `/review` is for actually reading a
posting closely enough to decide, and then working through applying to it.

## Goal

A `/review` slash command that surfaces the single highest-priority posting in `jobs/new/` at a
time, shows a full, detailed view of it (more than the dashboard table), and lets the user
decide: reject it, skip it, or apply — where "apply" hands off into an interactive
cover-letter-finalizing / application-question-answering session, with the file staying in
`jobs/new/` until the user confirms they actually submitted.

## Behavior

1. **Read `profile.md` first** — same hard requirement as every other command, so judgment calls
   during review (e.g. "is this rate acceptable given the urgent-search lower bar?") are grounded
   in current preferences, not stale assumptions.

2. **Build the queue** — every `.md` file directly in `jobs/new/` (skip `review-dashboard.html`
   and any non-`.md` file). Sort by `Fit Score` descending, tie-broken by `Found` date ascending,
   so the single most-promising posting comes up first.

3. **One posting at a time.** No batch/quick-approve shortcut — every posting gets the full
   detailed treatment below before the next one comes up.

4. **Detailed summary per posting** — longer and more prominent than the dashboard row:
   - Role — Company, and the **Source URL** (so the user can open the real posting immediately).
   - Three logistics facts pulled to the top and called out clearly, not buried in prose:
     **Pay** (Rate/Salary as stated), **Days in office** (see field addition below), and
     **Contract vs. full-time** (Engagement type).
   - Full Fit Score and its written rationale (not a one-line gist).
   - Location/Remote and Flags.
   - Resume Delta and the drafted Cover Letter, shown in full so the user can judge them, not
     just referenced.

5. **Decision per posting**: Apply / Reject / Skip / Stop.
   - **Reject** → move the file to `jobs/rejected/` unchanged (matches the existing convention —
     files in `applied/`/`rejected/` today carry no added annotation beyond a location change).
     If the user volunteers a reason, append it as a `## Rejection Note` section first; don't
     prompt for one if they don't offer it.
   - **Skip** → leave in `jobs/new/`, move to the next posting in the queue.
   - **Stop** → end the session; report a tally of what happened so far.
   - **Apply** → do **not** move the file yet. Enter an application-assistance exchange for this
     posting: refine/finalize the cover letter for the actual application (portal, email, Easy
     Apply, whatever the user describes), and answer any application-form questions the user
     pastes in, grounded in `profile.md` and the resume. This can span several back-and-forth
     turns. Only once the user explicitly confirms they submitted the application does the file
     move to `jobs/applied/`. If the user decides mid-flow not to submit after all, treat it as a
     reject or a skip per their call, not an automatic move.

6. **End-of-run summary** — counts of applied/rejected/skipped, and a reminder to run
   `/update-dashboard` (since it regenerates from the `jobs/new/` backlog, which just changed)
   and to commit, per CLAUDE.md's "commit after each review session" convention.

## Schema addition: Days in Office

Pay and contract-vs-FTE already exist as fields (`Rate/Salary (stated)`, `Engagement type`), but
"how many days in the office per week" doesn't have a dedicated field today — it's inconsistently
buried in `Location/Remote` or `Flags` text. Add a **`Days in Office`** field to the job file
schema (defined in `specs/addjob.md` / `.claude/commands/addjob.md`, inherited by every
`/check-*` skill since they file through `/addjob`'s schema):

- Infer from the posting's stated remote/hybrid/on-site policy: `0 (Remote)`, an explicit count
  like `2/week (Hybrid)` when the posting states one, `5/week (On-site)` for fully on-site, or
  `Not stated` when it's labeled "Hybrid" without a day count.
- This is populated going forward by `/addjob` and, transitively, every `/check-*` skill — not
  backfilled onto existing `jobs/new/` files. `/review` should show `Not stated` gracefully for
  older files that predate this field rather than erroring.

## Non-goals

- Never submits an actual application on the user's behalf — I help draft/refine material and
  answer questions; the user does the actual submitting, then confirms so the file can move.
- Doesn't re-score postings — scoring already happened in `/addjob` or the `/check-*` flow that
  filed the posting. If the user's read of the posting during `/review` surfaces something that
  changes the picture, that's a conversation, not an automatic re-score.
