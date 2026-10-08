# Candidate matching and resume selection

Effective 2026-10-08. Read this file and `profile.md` completely before matching, scoring, or drafting. This policy supersedes older skill/profile language that mixes compensation into technical scores, implies deep Kubernetes/Terraform ownership, or selects the old general resume. Preserve board-specific discovery passes, full-description review, eligibility checks, and external-action boundaries.

## Evidence and priorities

Prioritize demonstrated Platform/DevOps work: shared delivery platforms, CI/CD, developer productivity, release automation, internal tooling, and production reliability. Keep SRE discovery in scope; classify by duties, not title. Within existing searches include equivalent release-engineering/developer-enablement terminology where supported; do not remove mandatory passes or filter unfamiliar titles without reading.

- Strong evidence: Jenkins standards and mandatory SonarQube gates for approximately 50 developers, 12 teams, 70+ applications; Salesforce/Oracle/MuleSoft/ArcGIS delivery; Python monitoring; Linux operations, fleet automation, incident response, and technical direction without a formal lead title.
- Kubernetes: application/platform user, not production cluster owner. ArgoCD usage does not establish cluster upgrades, architecture, networking/storage administration, or deep Kubernetes operations.
- Terraform/Ansible: primarily used another team's provisioning/configuration workflows. Do not infer module authorship, IaC architecture ownership, or deep infrastructure engineering from tool names or years of exposure.
- Azure: ground claims in the documented Nexus/Jenkins/Vault VM environments and delivery work. Preserve the profile's bounded AWS experience and zero GCP experience.
- Distinguish tools used, work personally implemented, proposals, and adoption. ArcGIS phase one shipped; adoption followed departure; production-access removal remained proposed. Bitbucket governance tooling was discontinued before broader adoption.
- SRE: observability, automation, incident response, and operational tooling can fit. Explicit requirements for deep cluster ownership or large-scale distributed-system operations are material gaps. Evaluate required versus preferred experience and actual ownership/scale; do not reject all SRE jobs or infer scale solely from employer name. Elastic's reported rejection concerned operating scale, not a universal SRE disqualification.

## Score and practical assessment

For validated in-scope jobs, `score` is technical/domain/scope fit, 0–10: 8–10 strong evidence for the core deliverables; 5–7 plausible with explicit gaps; 1–4 substantial required-experience mismatch. Tool overlap cannot cancel a core ownership/scale gap. Retain schema conventions: `0` for out-of-scope and `-1` for hard eligibility/pay-floor exclusion. These sentinel values are exclusion codes, not technical ratings; never invent a technical rating when only metadata was reviewed.

Evaluate logistics separately. The ideal is CAD $160k+ **base**, fully remote from Ontario, with growth supported by concrete team/role evidence. Bonus/equity/OTE is not base. Income is urgent: below-ideal roles remain eligible when above the existing profile floors. CAD $115k–$120k is a planning range discussed for roughly $7k average monthly employee take-home before employer deductions, not a new hard floor or guaranteed net income. Do not convert that into a contract rate. Preserve existing contract floors and geographic constraints.

Label practical assessment:
- `Target`: Ontario-remote eligibility and CAD $160k+ base supported; state whether growth is evidenced or unconfirmed.
- `Compromise`: eligible but below ideal pay, hybrid, or another stated tradeoff; name the compromise. Do not call it financially sufficient without the relevant costs/deductions.
- `Confirm`: missing base pay, Ontario eligibility, cadence, or other decision-critical terms; list what must be confirmed. Unknown is not eligible by assumption.
- `Ineligible`: a confirmed hard gate; state its evidence.

Use existing output fields so all reports remain compatible: `gap` starts `Technical: ...; Practical: Target/Compromise/Confirm/Ineligible — ...; Resume: Platform/SRE.` Keep location/cadence and salary/currency/pay period in their existing columns. In `applications.md`, use the same concise labels in Notes. Never hide a practical blocker behind a high technical score. Salary unspecified can still auto-file if all other filing rules pass; unresolved geographic/legal eligibility cannot.

When otherwise equally suitable, recommend Platform/DevOps roles with direct evidence first, then suitable SRE. Do not manufacture a score bonus for a title or salary. Preserve report sorting; explain recommendation priority in the summary.

## Resume routing

- Default: `resume/platform/marc-berthelette-resume-en.md` for delivery platforms, CI/CD, developer productivity, release automation, and mixed DevOps.
- Use `resume/sre/marc-berthelette-resume-en.md` when production reliability, observability, incidents, and operational tooling dominate, regardless of title.
- Read the selected core resume completely when drafting. For discovery, read the Platform core and additionally the SRE core when evaluating SRE duties. These replace references to `resume/marc-berthelette-resume-en.md` in older instructions.
- Produce a complete standalone tailored resume, not instructions or a delta. Preserve documented roles and evidence; never fill a required gap with invented experience. Record the selected base in Notes.
- For French applications, translate the selected current core using Canadian French and the existing style guide. Older French resumes can guide terminology but cannot override current facts. Follow the established PDF exporter and verify selectable text and at most two pages.
- No cover letters/resumes during discovery auto-filing; draft through `addjob` or after Apply in `review`.

## Outcomes

Use `review`'s outcome workflow for user-reported progress even without a New queue. Keep the existing lifecycle statuses; record interview stages, dates, and reasons in Notes. Do not infer failure from silence or re-score historical applications without a new assessment. Measure confirmed recruiter screens/interviews by originating Board, acknowledging missing outcomes and recent applications rather than treating every Applied row as a rejection.
