# Automatic filing for check skills

After validation, scoring, deduplication, and report-data refresh, automatically append each qualifying discovery to `applications.md` with `Status: New`.

This policy supersedes older Output wording in a board skill that says discovery may write only its report JSON or asks the user to select every posting manually. The board JSON/HTML refresh plus qualifying `applications.md` appends are the permitted local writes; all external sites remain read-only.

A posting qualifies only when all of these are true:

- `score >= 5`.
- The complete description was accessible and used for scoring; snippets, summaries, and unvalidated listings do not qualify.
- It is current and actionable. Do not file `Expired`, `Likely expired`, `Freshness unconfirmed`, or `Could not validate` postings.
- It is geographically and legally eligible. Do not file `Ineligible` or `Out of scope` rows.
- Compensation does not violate a hard floor documented in `profile.md` when compensation is stated.

Before every append, deduplicate against `applications.md` in this order: canonical source URL or requisition identity, then employer plus exact role. Treat known employer aliases and cross-board copies as duplicates. If any matching row exists, preserve it exactly regardless of whether its status is `New`, `InProcess`, `Applied`, `Skipped`, or `Rejected`; never append another row or reset a decision.

Append one standard `applications.md` row per new qualifying posting using today's date, `Status: New`, its score, company, exact role, originating board, canonical posting URL, and concise decision-relevant notes. Do not invoke `addjob`, draft a cover letter, create a tailored resume, or create per-job files during automatic filing. Those actions belong to `/review` after the user chooses `Apply`.

The board run remains complete even when zero rows qualify. Report `auto-filed`, `already present`, and `below-threshold/not-filed` counts separately. A manually selected sub-5 posting may still be filed later through `addjob`.
