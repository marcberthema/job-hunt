# Read-in-full policy for check skills

Added 2026-10-05 at Marc's direction: **open more postings, not fewer.** This policy applies to
every `check-*` skill and is written to be tool-neutral — it works the same from Claude Code,
ChatGPT/Codex, or a person following the steps by hand. It supplements each skill's own scope and
eligibility rules; it never relaxes a hard gate in `profile.md`.

## The rule

Score postings from their **full description**, not from a title, a search snippet, or the
employer's name. Every result that could plausibly be SRE, Platform, or DevOps work in substance
is opened and read before it is scored.

### Never filter on company

- Do not drop a result because the employer already appears in `applications.md`. A different
  role at a known employer is a new posting.
- Deduplicate **only** by posting identity: canonical URL or requisition/job ID first, then exact
  employer + exact role title. A cross-board copy of a role already in the ledger (same
  employer, same title or same requisition) keeps its existing row and status — do not append or
  reset it — but it still counts as reviewed.
- Employer aliases and staffing-agency copies of the same requisition are duplicates; different
  requisitions at one employer (for example, a Senior role and a Level II role on the same team)
  are separate postings.

### Do not skip on title alone

Marc's example: a "Staff Software Engineer, Electricity Markets" at an energy-software company
could still be the person who ships and monitors that software. Titles outside the usual DevOps
vocabulary are opened when the employer runs production software and the description may include
deployment, infrastructure, release, or reliability scope. After reading, a role whose actual work
is outside the three target families is scored `0` with an `Out of scope — <reason>` status and
stays in the report (see `reports/report_schema.md`); it is not dropped silently.

Safe to skip without opening: clearly unrelated occupations (sales, recruiting, HR, retail,
healthcare, trades, finance/accounting) and internships/co-ops. Record the count, not each row.

### Report what you did not open

Anything left unopened for a real reason — an empty cached shell, a blocked page, a rate limit —
goes under `could_not_validate` with the reason and a link. Never imply a list was fully read when
it was triaged. In the run notes, state how many results were collected, how many had their full
text read, how many were opened for a closer look, and how many were set aside and why.

## Procedure

1. **Collect** every result for each mandatory pass (first page per the skill's own boundary).
   Keep the posting ID, title, company, and location label.
2. **Remove only the obvious non-engineering titles** listed above.
3. **Fetch the full description of every remaining result** using the best retrieval method the
   skill documents (employer page first; otherwise the board's public description endpoint or
   cached copy). Record the date the copy was indexed when the source shows one — cached copies
   can be stale.
4. **Extract features from the text**: required cloud platform(s), Kubernetes/IaC/CI-CD/observability
   scope, years required, stated pay, remote/hybrid/on-site wording, residency or clearance
   requirements, and what the day-to-day duties actually are.
5. **Read the workplace label on the posting itself** when the board's search filter does not
   enforce it (LinkedIn's public listing endpoint ignores the Remote filter).
6. **Read in detail** every posting that is remote/eligible-hybrid and has meaningful DevOps, SRE,
   platform, cloud, or CI/CD content. Open the duties and requirements sections, not just the
   summary.
7. **Score** per the skill, then apply the automatic-filing policy
   (`automatic-filing.md`). A role that fails a hard gate (AWS/GCP depth, Kubernetes
   administration, clearance, residency, pay floor, off-range on-site) is still a scored row.

## Pacing and blocks

Space requests (several seconds between fetches), run sequentially, and stop a pass on HTTP 429,
a verification page, or a CAPTCHA. Do not retry in a loop, rotate identities, or click through a
human-verification page — mark the pass `Incomplete` and, if appropriate, ask Marc to clear the
check himself. See each skill for its source-specific limits.
