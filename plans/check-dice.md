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

2. **Build and fetch the search URL(s)**, one per keyword in play this run:
   ```
   https://www.dice.com/jobs?q=<keyword, spaces as +>&location=Remote&countryCode2=CA&filters.postedDate=SEVEN&filters.employmentType=CONTRACTS&language=en
   ```
   WebFetch each, asking for every `/job-detail/<id>` link with title, company, location, and
   rate/salary as shown on the results page. Cap at 15-20 links for a single custom query, or 8
   per keyword in rotation mode. Note: `location=Canada&radius=30&radiusUnit=mi` tested cleaner
   than plain `location=Remote` during development — revisit this combination first if results
   get noisy.

3. **Dedupe** (rotation mode only) — collapse the combined link list by company + title
   (case-insensitive) before running the eligibility gate, since the same posting commonly
   surfaces under more than one keyword.

4. **Read `profile.md`** in full before doing anything else.

5. **For each deduped posting, fetch it and run the eligibility gate first** (before extracting
   full details for scoring):
   - Security clearance mentioned (TS/SCI, Secret, Public Trust) → **INELIGIBLE: clearance
     required (requires US citizenship in practice)**.
   - Work authorization explicitly listed as US-only statuses (US Citizen / H-1B / OPT-EAD /
     GC-EAD, or "must be authorized to work in the US without sponsorship") with no
     corp-to-corp/international-contractor language → **INELIGIBLE: US work authorization
     required, not open to Canadian-incorporated contractors**.
   - On-site/hybrid at a US location, no remote option → **INELIGIBLE: on-site in the US**.
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
