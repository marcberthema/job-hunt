# Airudi — Lead Platform Engineer / Ingénieur plateforme principal — call prep

Applied 2026-10-07. Phone screening Wed 2026-10-21, 1:30–2:00pm, with Jonathan Deguire, CRHA, Senior Talent & Culture Advisor (HR, not technical).
Montréal hybrid, 2 days/week at the Mile-Ex office. Full-time. Salary not published ("on en parlera dès notre premier appel"). French and English mastery mandatory.
Resume sent: `resume/tailored/2026-10-07-airudi-lead-platform-engineer-fr.md` (French). Cover letter: `resume/cover-letters/lettre-presentation-airudi-lead-platform-engineer.md`.
Posting: https://www.linkedin.com/jobs/view/4475875037/
Only claim what is in `profile.md`. Where you lack experience, say so, then show the adjacent proof.

## What this call is
An HR screen, 30 minutes. Expect: motivation, your story, language level, pay, office days, availability. Deep technical questions come later. Your goals: get the pay range, settle the office-days question, and learn the process.

## 1. Ask first
- **Pay:** what is the salary range for this level? Is there a bonus? (Don't name a number before they do.)
- **Office days:** 2 days/week in Mile-Ex. Is that firm? Is it every week, or can it be flexible/less for someone based outside Montréal? You live in Smiths Falls, so this decides whether the role works at all.
- **Employment type:** it's listed as full-time. Is a contract/consulting arrangement possible? (You prefer consulting; ask lightly, don't push.)
- **Process:** how many interviews, who are they (platform architect? CTO?), any technical exercise, which language?
- **Team and stage:** how big is the platform team today, and who would you work next to (the platform architect)? Is this a new role or a backfill?
- **Timeline:** when do they want someone to start?

## 2. 60-second pitch (say it in French, keep the English ready)
**FR:** « Je suis ingénieur DevOps et plateforme depuis près de 18 ans. Chez Énergir, j'ai standardisé le CI/CD pour 12 équipes applicatives et plus de 70 applications, sur neuf technologies différentes, sans lien hiérarchique : l'adoption est venue de séances de formation régulières avec chaque équipe. Chez Desjardins, j'ai construit un service Python/FastAPI qui valide environ 250 dépôts Artifactory et publie les résultats dans Dynatrace. Votre poste est de bâtir la plateforme sur laquelle les autres équipes vont s'appuyer, et c'est le type de travail que je fais : transformer des demandes récurrentes en pipelines et en garde-fous standardisés. »

**EN:** "I'm a DevOps and platform engineer with nearly 18 years in the field. At Énergir I standardized CI/CD across 12 application teams and 70+ apps on nine technologies, with no reporting line; adoption came from recurring enablement sessions with each team. At Desjardins I built a Python/FastAPI service that validates about 250 Artifactory repositories and reports to Dynatrace. This role builds the platform other teams depend on, which is the work I do: turning recurring requests into standard pipelines and guardrails."

## 3. Likely questions and answers

**Why Airudi / why this role?**
You want to build a shared platform that product teams depend on, in a company that is scaling. You are drawn to the point that AI agents in production need guardrails, permissions and traceability. Énergir ended September 30; you're available immediately. Keep it factual.

**Walk me through your background.**
Use the pitch. Then: Tink (Jenkins pipelines for 80+ apps, monitoring a 600+ server fleet, ELK, the inventory platform), Énergir (five years, CI/CD across nine stacks), Desjardins (Artifactory validation, ArgoCD/GitOps).

**The posting asks for 7+ years including 2+ at lead/staff level. How do you fit?**
You have nearly 18 years. You have no formal lead title: say it plainly. What you did is technical ownership: you initiated the shared Jenkins pipelines, were the primary developer contact when the ecosystem broke, and onboarded new DevOps engineers and developers. Don't claim a lead or staff title.

**Have you technically led a capability used by several teams?**
Yes: the shared Jenkins pipeline templates at Énergir, used by 12 teams and 70+ applications, with mandatory quality checks such as SonarQube that developers can't skip. Do not say every application used them: some manual-deployment teams were still being integrated.

**Leading cross-cutting change without authority?**
Énergir: about six enablement sessions a year with each team. Also the Salesforce delivery rebuild: no prior Salesforce experience, replaced legacy ANT scripts, built a validation pipeline for every candidate merge. And the Oracle deployment change: Jenkins automated releases, so normal deployments no longer needed the firefighter account.

**Reliability: SLIs, SLOs, error budgets, post-incident?**
Be direct: you have not implemented SLOs. You built the groundwork: Salesforce logging moved to direct Dynatrace ingestion, DML error parsing and dashboards. You have done root cause analysis on critical incidents. Do not claim error budgets or measured SLO compliance.

**Progressive delivery and tested rollbacks?**
MuleSoft: releases prepared and QA-tested days ahead, selected by version at the production window, and rollback redeploys a previous artifact. Build once, deploy many: the same QA-tested artifact promoted to production. You haven't run canary or blue/green in production: say so if asked.

**Kubernetes, Terraform, OpenTelemetry?**
- Kubernetes: application-level. You used it at work and at home; you have never owned a production cluster. At Desjardins the Artifactory validation suite was deployed through ArgoCD/GitOps.
- Terraform: you were a user of automation owned by another team, not its author. You helped migrate Nexus, Jenkins and Vault from manual Azure to Terraform and Ansible, and introduced Azure Storage for Terraform state and Key Vault.
- OpenTelemetry: not on your resume. Your observability is Dynatrace, Splunk and ELK. Say that, and that the concepts carry over.

**Multi-tenant SaaS, API design, distributed systems, workflow orchestration?** (the biggest gap)
Say you haven't designed multi-tenant SaaS architecture or built a production distributed system as the owner. What you bring is the delivery, reliability and tooling side. Don't stretch it. Expect them to probe here later with the architect.

**Policy-as-code, approval gates, traceability, LLM gateway, MCP?**
You have not built an LLM gateway or agent runtime. Adjacent proof only:
- Approval gates: Oracle releases without manual steps no longer needed emergency-access approval; releases with manual steps still did.
- Traceability: the Tink inventory showed CVEs from artifact reports, Jira references from Git logs and release details per application.
- Guardrails: mandatory pipeline quality checks that developers can't skip.
- AI: at Énergir you introduced AI-assisted practices over 6–9 months with hard scope gates and human validation before anything reaches production, and told leadership the organization lacked safeguards. This is about people using AI to build, not running AI agents in production: be precise.

**Security: IAM, secrets, ISO 27001, SOC 2?**
Secrets: Vault, then Azure Key Vault. No SOC 2 or ISO 27001 certification work on your record: don't claim it.

**Azure?** (nice-to-have)
Your strongest cloud: Azure DevOps, Azure delivery, and the Azure IaC migration at Énergir. Don't inflate it into deep Azure platform ownership.

**Regulated or sensitive-data environments?**
Energy (Énergir) and financial services (Desjardins). Don't claim Law 25 work.

**Mentoring?**
You onboarded new DevOps engineers and developers at Énergir and directed a junior engineer on the Bitbucket governance tooling. No formal management title.

**What went wrong / what didn't land?** (if asked)
The Bitbucket governance initiative was discontinued before broader adoption when the DevOps lead declined ownership; Backstage was declined. Say it neutrally.

**Why are you leaving / not working at Énergir?**
The contract ended September 30. Don't speculate about colleagues.

**Salary expectations?**
Ask for their range first. If pushed: your aspirational target is $160–175k base. The role is full-time with 2 office days in Montréal, which you live outside of, so you'd want it to be worth the commute. Your hard floor for Montréal hybrid is $120k, and a lead-level platform role should sit well above that. Don't reveal the floor.

## 4. Assessment (read before the call)
- **Fit:** score 6. The match is real on CI/CD standardization, enablement without authority, and delivery tooling. The gaps are real too: formal lead scope, multi-tenant SaaS and distributed-systems design, SLOs, OpenTelemetry, and any agentic or LLM-gateway work. 74 applicants.
- **Practical:** Compromise at best. Two days a week in Montréal from Smiths Falls is a long commute, and your profile flags 2 days/week as borderline. Unknown pay. If the answer on office days is "firm, every week" and the range tops out below about $140k, I would not spend more time on this one.
- **On this call, the good outcome is** a range, a clear office-days answer, and an interview with the platform architect.

## 5. Do not say
- A lead or staff title, a formal roadmap, or that every application used the shared pipelines.
- SLOs, error budgets, canary or blue/green in production, OpenTelemetry, multi-tenant design, LLM gateway or MCP experience.
- Kubernetes cluster ownership, or Terraform module authorship.
- Any figure not in `profile.md`, including a Desjardins check interval ("scheduled" is enough).
- Anything about Brayd or Canopy, your birth date, or that references are available (none are identified).

## 6. After the call
Tell Claude: the recruiter's confirmation of the role, pay range, office days (and whether they flex), next step and date, and who the next interviewer is. It goes on the Airudi row in `applications.md`.
