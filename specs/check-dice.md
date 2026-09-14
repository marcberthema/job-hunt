# Spec: `/check-dice` — Dice Search & Bulk Quick-Score

## Problem

Dice is a viable fetchable source (unlike We Work Remotely / RemoteOK, which return HTTP 403).
But Dice's default search skews heavily US-market, and a large share of its contract postings
explicitly restrict work authorization to US-based statuses (US Citizen, H-1B, OPT-EAD, GC-EAD)
or require security clearances (TS/SCI) that require US citizenship in practice. Marc is a
Canadian-incorporated consultant, not a US-authorized worker — so a large fraction of raw Dice
results are **structurally ineligible** regardless of skill fit. Scoring those against
`profile.md` in full before checking eligibility wastes effort on postings that were never
applicable.

## Capability

Same shape as `/check-indeed`, including the optional default role rotation (DevOps Engineer,
Platform Engineer, SRE, Cloud Engineer, DevSecOps Engineer, Forward Deployed Engineer) when no
search terms are given: search Dice, fetch each result, and produce a quick-score table — but
with an **eligibility gate** that runs first, before any skill/domain scoring. Postings that fail
the gate are marked ineligible with the reason and skipped for scoring, not silently dropped.

## Usage

```
/check-dice [search terms]
```

- `/check-dice` (no arguments) — runs the full default role rotation (same list as
  `/check-indeed`).
- `/check-dice devops engineer` — runs that single query only.

## Behavior

1. **Determine query mode**: single custom query (arguments given) or full rotation (no
   arguments) — same rotation list as `/check-indeed`.
2. **Build and fetch the search URL(s)** — **revised 2026-09-13**, given Marc is now open to
   TN-visa-sponsored US roles (Canadian citizens get fast/cheap TN sponsorship under USMCA):
   `https://www.dice.com/jobs?filters.postedDate=SEVEN&filters.employmentType=FULLTIME%7CCONTRACTS&filters.workplaceTypes=Remote&filters.willingToSponsor=true&q=<keyword>&countryCode2=CA&language=en`
   for each keyword in play this run. `filters.willingToSponsor=true` and
   `filters.workplaceTypes=Remote` replace the old `location=Remote` text param, which produced
   noisy US-onsite-heavy results (see prior note, now superseded). `filters.employmentType`
   includes both `FULLTIME` and `CONTRACTS` now, not just contracts — a sponsor-willing full-time
   US role is now in scope too.
   Extract every `/job-detail/<id>` link with its title, company, location, and any rate/salary
   shown on the results page. Cap at 15-20 links for a single custom query, or 8 per keyword in
   rotation mode.
3. **Dedupe** (rotation mode only) — collapse by company + title before running the eligibility
   gate, since the same posting commonly surfaces under more than one keyword.
4. **Read `profile.md` first**, same as `/addjob` and `/check-indeed`.
5. **For each deduped result, run the eligibility gate BEFORE scoring** — fetch the posting and
   check, in this order:
   - **Security clearance required** (TS/SCI, Secret, Public Trust, etc.) → ineligible. Clearance
     eligibility requires US citizenship in practice even when not stated explicitly, and TN
     status doesn't change this.
   - **Work authorization explicitly restricted to US statuses, WITH sponsorship mentioned**
     (e.g. "will sponsor," "able to sponsor," H-1B/TN/visa sponsorship language) → **revised
     2026-09-13: eligible**, not ineligible. Marc (Canadian citizen) is TN-visa eligible under
     USMCA — fast/cheap sponsorship relative to other nationalities. **Flag prominently:
     "TN-sponsorship path — likely W2 employment, no corp-to-corp; confirm sponsorship type
     (TN vs. green card) with recruiter before proceeding — see feedback memory on TN vs. green
     card distinction."** Do not silently treat "willing to sponsor" as a green-card offer.
   - **Work authorization explicitly restricted to US statuses, with NO sponsorship mentioned**
     (e.g. "must be authorized to work in the US without sponsorship") → still **ineligible** —
     this is a hard closed door regardless of Marc's TN eligibility.
   - **On-site (not hybrid/remote) at a US location** with no remote option → ineligible — TN
     doesn't solve the relocation/logistics problem, this is a separate practical fail.
   - If none of the above apply (posting is silent on work authorization, or explicitly open to
     corp-to-corp/international contractors, or is Canada-based) → **eligible**, proceed to
     scoring.
   - If eligibility is ambiguous (e.g. "remote" with no work-authorization language either way),
     mark as **eligible but flag "confirm work authorization with recruiter before applying."**
     Don't fail it outright — Dice postings are often copy-pasted boilerplate and silence isn't
     always a hard block.
6. **Only score postings that pass the gate** — same skill/domain-first scoring philosophy as
   `/check-indeed` (one-sentence rationale, logistics flagged not scored down). Ineligible
   postings get one line in the output (title, company, reason) with **no scoring effort spent
   on them** — this is the whole point of running the gate first.
7. **Report a table**, eligible postings sorted highest score first, ineligible postings listed
   separately below with just the reason (not scored).
8. **Offer to go deeper** — same as `/check-indeed`: ask which eligible postings should get the
   full `/addjob` treatment (resume delta, cover letter, filed to `jobs/new/`).

## Eligibility Gate — Design Note

This gate exists specifically because Dice's US-market bias makes eligibility failures common
and expensive to discover late. It is **not** meant to be added to `/check-indeed` or `/addjob`
generally — Indeed's Canada-market results don't have the same failure pattern. If a future
source shows the same pattern, replicate the gate there rather than centralizing it, since the
disqualifying conditions may differ per source (e.g. residency requirements vs. clearance vs.
visa status).

## Edge Cases

- **A single keyword's search returns no job links** (rotation mode): skip that keyword,
  continue with the rest of the rotation.
- **Every keyword (or the single custom query) returns no job links**: report it, suggest a
  different query.
- **Individual posting fetch fails**: skip it, note "couldn't fetch" — don't run it through the
  gate at all since there's nothing to check.
- **Duplicate of an existing `jobs/` entry**: checked only when the user picks a posting for the
  full `/addjob` treatment, same as `/check-indeed`.
- **Large result count**: cap per the limits in step 2 to keep the batch fetch reasonable.

## Out of Scope

- Extending the eligibility gate to other sources (see design note above).
- Pagination beyond the first results page.
- Auto-filing eligible+high-scoring results without user confirmation.
