# Plan: `/check-dice` — Dice Search & Bulk Quick-Score

Implements `specs/check-dice.md`.

## Deliverable

`.claude/commands/check-dice.md` — a slash command definition, same pattern as
`/check-indeed`, but with an eligibility gate inserted before scoring.

## Command Steps

1. **Parse input** — `$ARGUMENTS` is optional. Location is always `Remote`, not a user-supplied
   argument.
   - Non-empty → single custom query, same as the original behavior.
   - Empty → run the **default role rotation**, same list as `/check-indeed` (DevOps Engineer,
     Platform Engineer, Site Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward
     Deployed Engineer).

2. **Build and fetch the search URL(s)**, one per keyword in play this run (**revised
   2026-09-13**):
   ```
   https://www.dice.com/jobs?filters.postedDate=SEVEN&filters.employmentType=FULLTIME%7CCONTRACTS&filters.workplaceTypes=Remote&filters.willingToSponsor=true&q=<keyword, spaces as +>&countryCode2=CA&language=en
   ```
   WebFetch each, asking for every `/job-detail/<id>` link with title, company, location, and
   rate/salary as shown on the results page. Cap at 15-20 links for a single custom query, or 8
   per keyword in rotation mode. `filters.workplaceTypes=Remote` + `filters.willingToSponsor=true`
   replace the old noisy `location=Remote` text param; `employmentType` now includes both
   `FULLTIME` and `CONTRACTS` since Marc is open to TN-sponsored US full-time roles too.

3. **Dedupe** (rotation mode only) — collapse the combined link list by company + title
   (case-insensitive) before running the eligibility gate, since the same posting commonly
   surfaces under more than one keyword.

4. **Read `profile.md`** in full before doing anything else.

5. **For each deduped posting, fetch it and run the eligibility gate first** (before extracting
   full details for scoring) — **revised 2026-09-13**:
   - Security clearance mentioned (TS/SCI, Secret, Public Trust) → **INELIGIBLE: clearance
     required (requires US citizenship in practice; TN status doesn't change this)**.
   - Work authorization restricted to US statuses **with sponsorship mentioned** ("will sponsor,"
     H-1B/TN/visa language) → **ELIGIBLE**. Marc is a Canadian citizen, TN-visa eligible under
     USMCA. Flag prominently: "TN-sponsorship path — likely W2 employment, no corp-to-corp;
     confirm with recruiter whether sponsorship means a work visa (TN) vs. green card — these are
     very different commitments and shouldn't be assumed."
   - Work authorization restricted to US statuses **with no sponsorship mentioned** (e.g. "must
     be authorized to work in the US without sponsorship") → **INELIGIBLE**: hard closed door.
   - On-site (not hybrid/remote) at a US location, no remote option → **INELIGIBLE**: TN doesn't
     solve relocation logistics.
   - Otherwise → **ELIGIBLE** (if work-authorization language is simply absent, mark eligible
     but add a flag: "confirm work authorization with recruiter before applying").
   - **Do not extract full requirements/responsibilities or attempt scoring for INELIGIBLE
     postings** — record title, company, and the one-line reason only. This is the token-saving
     point of the gate.

6. **Score only ELIGIBLE postings**, 0-10, same skill/domain-first philosophy as `/check-indeed`
   — one-sentence rationale, logistics (not eligibility) flagged rather than scored down.

7. **Report two sections**:
   - Eligible postings, table sorted highest score first: Role — Company | Score | Why | Flags.
   - Ineligible postings, simple list: Role — Company | Reason (no score column).

8. **Offer to go deeper** on eligible postings only — same `/addjob`-reuse pattern as
   `/check-indeed`: duplicate check, reuse already-fetched content, full resume delta + cover
   letter + file to `jobs/new/` for whichever ones the user picks.

## Testing

Manual:
- Run `/check-dice` (no arguments) and confirm all 6 rotation keywords get searched and deduped.
- Run `/check-dice devops engineer` and confirm single-query mode still works as before.
- The ineligible list correctly catches clearance-required and US-work-authorization-only
  postings (validate against the Booz Allen Hamilton / SAIC / Quantum Technologies examples
  found this session).
- Montreal/Canada-based or explicitly open postings land in the eligible, scored table.
- Ineligible entries show no scoring effort (no resume-delta-style detail), just the reason.

No automated test suite for this repo; verification is manual, same as `/addjob` and
`/check-indeed`.

## Out of Scope

Same as spec: gate not added to other commands, no pagination, no auto-filing.
