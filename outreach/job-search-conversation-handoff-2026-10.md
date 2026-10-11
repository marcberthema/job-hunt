# Job search and consulting — conversation handoff

Saved 2026-10-11 for Marc Berthelette. This is a consolidated conversation summary, not a verbatim transcript. It includes decisions, factual corrections, sites, and unfinished work. Website features/prices mentioned below are historical snapshots, not live verification.

## Instructions for the next chat

Read this document before suggesting a new strategy. In this repository, also read `profile.md`, applicable repository instructions, and any skill required for the task. Use current files for current application status. Do not assume old drafts, generated PDFs, or LinkedIn copy reflect the latest edits.

Do not restart the discovery interview or ask questions already answered here. Prioritize actionable income opportunities and accurate positioning. Do not invent metrics, infrastructure ownership, production adoption, or technical depth. Distinguish completed work from proposed work and submitted applications from drafts.

No authorization is implied to register accounts, send messages, submit proposals/applications, buy subscriptions/credits, accept contracts, or commit/push changes.

## Situation and priorities

- Marc lives in Smiths Falls, Ontario; bilingual French/English; incorporated in Canada.
- Énergir mandate ended September 30, 2026. Available immediately; income is urgent.
- Hundreds of applications produced about three interviews in the period discussed. Elastic was the only interview that matched the ideal well; other opportunities had major compromises such as Montréal office attendance or lower salary.
- Elastic declined after interviewing: insufficient experience at the scale they needed, despite liking Marc. Follow-up is already done. Do not recommend following up again as an outstanding task.
- Marc finds the search demoralizing. More job-board volume alone has not solved the problem.
- **Consulting is preferred over permanent employment.** Prioritize full-time remote contracts and relevant project/part-time consulting. FTE remains an income-stability fallback.
- Ideal employment: growth, fully remote, CAD $160k base or more. Existing profile contains broader geographic and compensation compromises; use its current rules rather than treating the ideal as a universal rejection gate.
- Household bills are approximately CAD $6k/month excluding food; wife's part-time work/government income and Marc's partial second job can help with food. CAD $7k/month clear was discussed as a planning need. That is $84k annual net, not $100k annual gross; do not reuse unverified tax estimates as guarantees.

### Keep the income tracks separate

| Track | Decision |
|---|---|
| Normal full-time consulting | Profile target CAD $110–130/hr. Profile discusses roughly $80/hr as a survival floor only for a long, reliably billable contract; its take-home estimates are not independently verified here. |
| Employment | Ideal CAD $160k+ base; consult current profile for compromise floors and geography. |
| Temporary remote IT bridge work | **CAD $35/hr after platform fees, before tax.** Explicitly approved while searching for stable work. |
| Longer-term fractional business | Still an aspiration; distinguish deliberate retainer-business development from immediate bridge gigs. |

The bridge floor supersedes older $90/hr part-time restrictions only for temporary bridge gigs. It is a private acceptance minimum, not a public advertised rate or normal consulting price. Marc would rather earn money doing IT than work retail. Do not reject bridge gigs just because their scope is junior or lacks cloud work.

Check currency, actual platform fees, realistic delivery/meeting/revision hours, proposal costs, payment timing, and Ontario eligibility. For fixed-price projects, calculate effective hourly proceeds. Do not assume enough hours will exist to cover household bills.

## Positioning and résumé strategy

Two core English résumés were created:

- `resume/platform/marc-berthelette-resume-en.md` and corresponding PDF: primary track, delivery automation, platform/DevOps, developer enablement, hands-on implementation.
- `resume/sre/marc-berthelette-resume-en.md` and corresponding PDF: reliability/operations-oriented SRE opportunities grounded in actual experience.

Both PDFs were previously checked as two-page selectable-text documents. Subsequent Markdown edits may mean they need regeneration. `resume/md_to_pdf.py` gained an optional `--core-resume` layout; normal defaults were retained.

Marc's strongest differentiator is learning unfamiliar systems quickly, understanding workflows and real problems, proposing a workable plan, and delivering it. Lead with that evidence, not a giant tool list or unsupported expert-level claims.

Nearly 18 years spans software, infrastructure, and operations; do not label all of it DevOps/platform engineering. Strong practical delivery ownership does not imply Kubernetes cluster administration or Terraform module ownership.

## Career evidence and corrections — preserve these distinctions

### Énergir — September 2021–September 2026

- Delivery ecosystem served about 50 developers, 12 teams, and 70+ applications. Prior material describes nine runtimes: Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks. ArcGIS was a later addition.
- Owned centralized Jenkins pipeline templates used across technology stacks. Developers could not arbitrarily skip stages such as SonarQube.
- Unofficial delivery/collaboration owner during the first three years: created a roadmap, was the primary developer escalation contact, and onboarded developers and DevOps colleagues. This was not an official lead title.
- **Salesforce:** legacy ANT scripts hid problems and deployment windows were frequently missed. Replaced them with official Salesforce CLI tooling and candidate-merge validation in a sandbox. Missed windows fell to one since launch in the period Marc described; that remaining miss involved an issue flagged days earlier that the responsible team had not addressed. Do not claim bad deployments became literally impossible.
- **MuleSoft:** reduced a roughly 15-step manual deployment checklist to a few Jenkins jobs; some preparation could run before the release window.
- **Oracle:** automated normal deployments that previously needed a manually approved emergency/firefighter account. Tests caught recurring problems, notably file encoding. Do not imply all emergency access was removed.
- **Terraform/Ansible clarification:** primarily a user of another team's IaC, not its owner or primary module author. Helped with migration of Nexus dev/prod, Jenkins controllers dev/prod and two agents per environment, and HashiCorp Vault dev/prod. Vault was later decommissioned; Azure Key Vault and Azure Storage for Terraform state were introduced. Terraform provisioned resource groups/network/VMs; existing Ansible configured hosts, including Docker. Do not convert this into authored end-to-end IaC architecture.
- Marc proposed improvements to the owning team but often could not implement them himself. Describe scope honestly without blaming former colleagues in public materials.
- **Bitbucket governance tool:** after Backstage was rejected, directed a junior engineer on a tool reporting stale branches, branch protections, and peer-review configuration. This was repository governance health, not Bitbucket uptime. Marc was unofficial owner; the initiative was cancelled without business buy-in. Do not claim organization-wide rollout or measured adoption.
- **ArcGIS:** full ownership of the delivery pipeline; learned the APIs and delivered phase 1 at the end of the mandate. Map services and their properties became versioned and deployable to dev/test/prod through a service account rather than from individual laptops. Adoption was happening after departure. Restricting routine production-server access while preserving emergency access was a proposed later phase, not delivered.
- Examples of adaptability include quickly understanding a Dynatrace demo and learning Databricks, Oracle, and ArcGIS workflows sufficiently to implement useful automation. Present results rather than comparisons with slower-learning colleagues.

### Tink — January 2018–August 2021

- Jenkins delivery supported approximately 10–15 developers, 80+ applications, and 20+ clients.
- Fleet work covered 600+ servers; automated recurring patching and verification. Puppet/Spacewalk were configuration/patch-management evidence, not proof of infrastructure provisioning ownership.
- Proactively built a software inventory platform exposing CVE exposure, end-of-life risk, and operational information to product owners.
- **Elasticsearch incident:** a client declined an upgrade and the component repeatedly crashed. After two minutes down, a probe triggered a local Bash restart; if still down after five minutes, it paged the on-call person. This was mitigation of a known failure, not a root-cause fix or guaranteed elimination of pages.
- Operational background includes logging and 24/7 on-call.
- **AWS:** learned it during a roughly six-month greenfield target-environment build. Experience included EC2, S3, Route 53 and other environment components, primarily console-based. The project was cancelled before cutover. Do not imply production AWS operations, successful migration, or Terraform-built AWS infrastructure.

### Desjardins — October 2025–March 2026, concurrent contract

- Built a Python/FastAPI validation service checking roughly 250 remote Artifactory repositories every four hours across seven ecosystems, with Dynatrace visibility.
- Made the validation harness configurable/tool-agnostic so it also supported regression checks for an Artifactory version upgrade.
- Automated on-demand Artifactory application environments with Kubernetes/ArgoCD; this was not Kubernetes cluster ownership.
- Additional work included artifact retention and Splunk alerts for configuration changes outside the delivery pipeline.

### SOVO and general boundaries

- SOVO: November 2008–December 2017. Formal software-engineer title from May 2017; earlier lead-technician role included years of programming overlap. Do not erase earlier software work or invent an earlier formal title.
- Kubernetes: used it professionally, knows concepts, experimented at home, never owned/administered the clusters. Avoid “deep Kubernetes expertise.”
- References: former people in charge left or retired; no reference is presently arranged. Do not promise one or assume they are unreachable.

## LinkedIn work

English and French versions of the headline, About, and Énergir/Tink/Desjardins experience were discussed and supplied in the conversation. Marc reported making updates and requested the French versions. Do not assume every supplied paragraph is now live or that local drafts exactly match his final edits.

- Current saved draft: `outreach/linkedin-profile-2026-10.md`.
- Historical draft: `outreach/linkedin-profile.md`, marked superseded.
- Position consulting first, explain practical outcomes and adaptability, mention bilingual capability, Canadian incorporation, and immediate availability.
- Avoid the earlier About's overstatements: “18 years in DevOps,” “deep Kubernetes,” absolute production safety guarantees, or implying uncompleted AWS cutover.
- Do not just prepend another sales paragraph to an already long About. Use coherent positioning and selected evidence.

## Job-search automation work already performed

Earlier work updated 14 board-check skills plus `addjob` and `review`, with shared policy in `.agents/skills/_shared/candidate-matching.md`. They were validated at the time; no live board search was performed as part of that policy update. Inspect current files before assuming the inventory is unchanged.

- Separate technical fit from practical constraints: Target / Compromise / Confirm / Ineligible.
- Preserve special eligibility sentinel scores and distinguish unknown eligibility from confirmed eligibility.
- Prioritize Platform/DevOps fit without excluding credible SRE roles solely by title or company scale.
- Use the corrected evidence above; do not invent Kubernetes cluster ownership or IaC authorship.
- Select the appropriate core résumé and generate a complete tailored document, not just an edit list.
- Track recruiter/interview/offer outcomes and dates; silence is not automatic rejection.
- Elastic was recorded as rejected based on the reported outcome; follow-up is complete.
- Existing report metadata accommodates technical gaps, practical constraints, and recommended résumé without a new schema.
- Temporary bridge sourcing is explicitly permitted when requested, but not automatic submission or spending.

Model guidance discussed: Sol Medium for nuanced searching/scoring/tailoring; Sol Low for routine mechanical updates. Treat that as previous guidance, not a claim about current model availability or pricing.

Apify was discussed as an optional scraping tool, not a solution to low interview conversion. Consider only a bounded experiment for a source with worthwhile unique inventory and appropriate access/terms. Do not add scraping infrastructure or another skill without showing incremental value.

## Consulting sites — consolidated directory

These are discovery options, not a statement of current vacancies, guaranteed acceptance, Ontario eligibility, or current fee structures. Verify before applying or paying.

### Freelance marketplaces and talent networks

| Site | Intended use |
|---|---|
| [Upwork](https://www.upwork.com/freelance-jobs/devops/) | Immediate bridge projects: pipeline fixes, Linux, scripting, deployment automation. |
| [Gun.io](https://gun.io/find-work/) | Screened talent matching for part-time/full-time contracts; apply with Platform positioning. Not guaranteed immediate work. |
| [Braintrust](https://www.usebraintrust.com/for-talent) | Contract/freelance opportunities; an existing search skill covers it. |
| [Arc](https://arc.dev/talent) | Remote freelance contracts and engineering opportunities. |
| [Codementor](https://www.codementor.io/freelance) | Paid troubleshooting, mentoring, and projects; acceptance is not guaranteed. |
| [Guru](https://www.guru.com/how-it-works-freelancer/) | Hourly, fixed-price, and recurring work; inspect inventory before paying. |
| [Workhoppers](https://www.workhoppers.com/en/find-a-job) | Freelance, temporary, and part-time opportunities; check remote requirements. |
| [Toptal](https://www.toptal.com/freelance-jobs) | Selective network; secondary because screening takes time. |
| [Contra](https://contra.com/how-it-works/independents) | Project/ongoing freelance work; relevant DevOps demand not established. |
| [Fiverr](https://www.fiverr.com/) | Optional narrowly packaged technical services. |
| [Freelancer](https://www.freelancer.com/) | Secondary project source; scrutinize fees and scope. |
| [PeoplePerHour](https://www.peopleperhour.com/freelance-jobs/technology-programming) | Secondary scripting, integration, and project source. |

### Canadian contract agencies

- [Procom](https://procomservices.com/en-ca/)
- [S.i. Systems](https://www.sisystems.com/)
- [Randstad Digital](https://www.randstad.ca/jobs/s-technologies/remote/)
- [Robert Half Technology](https://www.roberthalf.com/ca/en/jobs/all/technology)
- [TEKsystems Canada](https://www.teksystems.com/en-ca/careers)
- [LeverageTek](https://leveragetek.ca/en/)
- [LRO Staffing](https://www.lrostaffing.com/services-technology/)

For every mandate, confirm remote/Ontario eligibility, corporation-to-corporation versus agency payroll, hours, term, rate, and payment timing. “Contract” does not automatically mean incorporated consulting.

Suggested focus: larger contracts through Procom, S.i. Systems, Randstad, and LeverageTek; profiles with Gun.io, Braintrust, and Arc; bridge work through Upwork, Codementor, and Guru. This is not a requirement to register on every site.

### Remote Rocketship — latest discussion

- [Canada listings](https://www.remoterocketship.com/ca/) and [pricing](https://www.remoterocketship.com/ca/pricing/).
- Job-discovery aggregator, not a freelance marketplace or matching agency. Employer applications are made directly.
- Canada, contract, and part-time discovery make it relevant as a supplementary source.
- Search DevOps, Platform, Cloud, SRE, and deployment automation. Confirm actual Ontario eligibility and incorporated-contract arrangements per posting.
- As checked October 10, 2026: free browsing; paid plans advertised CAD $39/month, $79/quarter, or $129/year, with broader access, alerts, and API/CLI/MCP access. Recheck all prices/features before using them.
- Recommendation: inspect free inventory first; pay only if it reveals relevant contracts missing from current sources. Do not buy an annual plan or build a new scanner before establishing incremental value.

### Other sources Marc raised — not all vetted

Preserve this original exploration list. Inclusion is not an endorsement or completed evaluation:

- Handshake
- Google Jobs
- CareerHound
- We Work Remotely — https://weworkremotely.com/
- Remotive — https://remotive.com/
- Remote4me — https://remote4me.com/
- Himalayas — https://himalayas.app/
- RemoteOK — https://remoteok.com/
- HiringCafe — https://hiring.cafe/
- “Wellhound” — name as supplied; confirm which service Marc meant rather than silently substituting Wellfound.
- Perplexity — research/search aid, not necessarily a consulting marketplace.
- LinkedIn — Marc suggested focusing on postings from the latest 24 hours.
- Wonsulting — clarify the intended service; do not assume it is a consulting job board.
- TechFetch — https://www.techfetch.com/

Existing repository sources also include Built In, Dice, Eluta, Glassdoor, Indeed, and Canada's Job Bank. Their existence does not mean all are equally useful for incorporated contracts.

Longer-term consulting/expert-network sources mentioned in the profile include Business Talent Group, Catalant, GLG, and Coleman Research. They are distinct from immediate DevOps bridge work; inspect `job_sources.md` before prioritizing them.

## Practical next steps — proposed, not completed

1. Keep a focused full-time consulting pipeline while pursuing a small number of near-term bridge opportunities.
2. Reuse the Platform résumé and corrected evidence for consulting profiles; tailor the offer to CI/CD fixes, deployment automation, Linux troubleshooting, Python/Bash, monitoring, and repository tooling.
3. Check useful inventory before spending significant time on screening, subscriptions, or new scraping integrations.
4. Track source, eligibility, rate/currency, estimated net after fees, hours, payment timing, and outcome. Evaluate interview/proposal conversion, not just application count.
5. Keep paid projects bounded so interviews and the main search remain feasible.

No consulting-platform signup, paid subscription, proposal, or engagement was confirmed as completed in this conversation. Do not infer that none happened outside it.

## Repository references

- `profile.md` — factual profile and current matching preferences; contains older sections overridden by newer dated clarifications.
- `consulting-profile.md` — existing consulting positioning; review against the corrections here before publishing claims.
- `outreach/consulting-sites.md` — earlier pinned consulting directory.
- `outreach/linkedin-profile-2026-10.md` — saved bilingual LinkedIn draft.
- `resume/platform/` and `resume/sre/` — core résumés.
- `.agents/skills/_shared/candidate-matching.md` — shared scoring/eligibility policy.
- `applications.md` — application ledger; read current status, not a historical summary.
- `job_sources.md` — source inventory.

## Prompt to start a new chat

> Read `outreach/job-search-conversation-handoff-2026-10.md` and `profile.md`. Continue from the decisions already made. My priority is remote consulting, with temporary remote IT bridge work acceptable at CAD $35/hr after platform fees, before tax. Keep that separate from my normal full-time consulting rates. Use the corrected career evidence, do not inflate my Kubernetes or IaC ownership, and help me take the next concrete step without restarting the discovery conversation.
