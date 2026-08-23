# Plan: `/review` — Backlog Review

Implements `specs/review.md`.

## Deliverable

`.claude/commands/review.md` — a slash command definition, no arguments. Prompt-driven, using
existing tools only (Read, Glob, Bash `git mv`, Edit for the rare rejection-note append). Also a
small schema addition to `.claude/commands/addjob.md` / `specs/addjob.md` (the `Days in Office`
field), which every `/check-*` skill inherits automatically since they file through `/addjob`'s
schema — no need to touch those 14 files individually.

## Part 1: Add `Days in Office` to the `/addjob` schema

In `.claude/commands/addjob.md`:
- Step 5 ("Extract fields from the posting"): add a bullet — infer days-in-office per week from
  the posting's stated policy (`0` for fully remote, an explicit count for hybrid when stated,
  `5` for fully on-site, `Not stated` when "hybrid" appears with no count).
- Step 8 (schema block): add `- **Days in Office:** <as inferred, or "Not stated">` under
  `Location/Remote`.

Mirror the same two changes in `specs/addjob.md` (extract list + schema block) so the spec stays
accurate. No changes needed to `plans/addjob.md` (implementation detail, not a design decision)
or to any `check-*.md` file — they file through `/addjob`'s schema by reference.

## Part 2: `.claude/commands/review.md`

1. **Read `profile.md`** in full before anything else.

2. **Build the queue**: `Glob jobs/new/*.md`. Read each file's `Fit Score` and `Found` date.
   Sort descending by score, ascending by date as tiebreak. Empty queue → report and stop.

3. **Per posting** (top of queue):
   - Render the detailed view: Role — Company, Source URL up top; a highlighted three-line block
     for Pay / Days in Office / Contract-vs-FTE; full Fit Score + rationale; Location/Remote;
     Flags; Resume Delta; full Draft Cover Letter. For files predating the `Days in Office`
     field, show `Not stated` rather than erroring on a missing line.
   - Ask for a decision: Apply / Reject / Skip / Stop (AskUserQuestion or free text, either is
     fine since this is single-item, not batch).
   - **Reject**: if the reply included a reason, append a `## Rejection Note` section (today's
     date + the reason) before moving. `git mv jobs/new/<file> jobs/rejected/<file>`.
   - **Skip**: no file operation, advance to the next item in the queue.
   - **Stop**: break out of the loop, go to step 4.
   - **Apply**: switch into an open-ended sub-exchange scoped to this posting — refine the cover
     letter on request, answer pasted application-form questions using `profile.md` and
     `resume/marc-berthelette-resume-en.md` as grounding. Stay in this sub-exchange (don't
     advance the queue) until the user either confirms submission (then
     `git mv jobs/new/<file> jobs/applied/<file>` and advance to the next posting) or says to
     reject/skip it instead (handle per those branches, then advance).

4. **Summary**: counts (applied/rejected/skipped/remaining in queue), reminder to run
   `/update-dashboard` and to commit — do not commit automatically.

## Out of scope

- No re-scoring, no re-fetching.
- No automatic git commit, no automatic application submission.
- No changes to `/check-*` command files.
