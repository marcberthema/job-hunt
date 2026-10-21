# Intact — DevOps Specialist, Shared Services (R155688) — call prep

Applied 2026-10-06. Intact phoned 2026-10-19. Montréal hybrid (also Saint-Hyacinthe, Laval), CAD $118.7–145.1k + 15% bonus target. Bilingual required.
Tailored resume: `resume/tailored/2026-10-05-intact-devops-specialist-shared-services-en.md`.
Only claim what is in `profile.md`. Where you lack experience, say so, then show the adjacent proof.

## 1. Ask first (the call decides what matters)
- Which team and who is the hiring manager? Is the lead a Java engineer or a platform person?
- Office days per week? Is Ottawa an option, or only Montréal / Saint-Hyacinthe / Laval?
- Process and timeline: how many interviews, technical test, and in what language?
- Pay: where in the range do they expect to land? Is the 15% bonus real in practice? (Range is based on a 35-hour week.)

## 2. 60-second pitch
"I'm a senior DevOps engineer with nearly 18 years in the field. At Énergir I standardized CI/CD across 12 application teams and 70+ apps, and I got adoption without any reporting line, through recurring enablement sessions with each team. The point wasn't the tooling, it was teams actually using it. Before that I centralized Jenkins pipelines for 80+ apps at Tink. I work in French and English every day. Your squad advises product squads and builds the tools they use, which is what I've been doing."

## 3. Likely questions and answers

**Tell me about enabling product squads.**
Énergir: pipelines delivered, then about six enablement sessions a year with each of the 12 teams. Pipeline failures were made self-diagnosing by separating application-code errors from platform errors, so squads knew who owned a failure. Result: a team doesn't need me to read its logs.

**How do you lead without authority?**
Same Énergir story. Add the Salesforce delivery rebuild: no prior Salesforce experience, replaced legacy ANT scripts, added a validation pipeline, and it gave the team a dependable every-other-Tuesday release cadence. Say there was one missed window after launch, over a problem identified days earlier that stayed unowned. Do not call "no missed windows" or "one missed release" a measured improvement.

**Our stack is Java/Spring Boot on OpenShift. Your experience?** (the main gap)
Be direct: "I haven't built Spring Boot services, and I haven't run OpenShift specifically. I've delivered Java applications through pipelines for years, and I used Kubernetes at the application level at Desjardins, where the validation suite was deployed through ArgoCD. I haven't owned a cluster. I'd expect OpenShift's differences (routes, security constraints, operators) to be a learning curve of weeks, not months." Don't oversell it. Énergir Kubernetes use is limited, not primary ownership.

**Kafka / IBM MQ?**
Say you have not owned either. Name only messaging you have actually operated. Offer what transfers: observing and alerting on event-driven systems through Dynatrace.

**Testing: WireMock, TestContainers, Playwright, Cucumber?**
Not on your resume. Talk about the automated quality gates you built into the pipelines, and say you'd learn their test stack from the squads.

**Observability: Dynatrace, Grafana, Elastic?**
- Dynatrace: Desjardins service publishing scheduled health signals for about 250 Artifactory repos (say scheduled; the interval is not reconfirmed). Énergir: Salesforce logging moved from Logstash to direct Dynatrace ingestion, parsing extended to DML errors, dashboards for Salesforce. It ran in production for several weeks before you left; do not say the old path was retired. Logstash still served two other teams.
- Elastic: centralized ELK at Tink.
- Grafana: say it is not on your resume, and that dashboard and alerting design carry over.
- Do not claim SLOs. You built groundwork for them, not measured compliance.

**Where do you see software delivery heading?** ("vision" is in the posting)
AI-assisted engineering with controls. At Énergir you introduced AI-assisted practices over 6–9 months with hard scope gates and human validation before anything reaches production, and you told leadership the organization lacked safeguards (not acted on). Do not name personal projects.

**Why Intact / why leaving Énergir?**
Énergir ended September 30. Keep it factual. Say you want a long-term team that modernizes delivery in a regulated environment, and that you're available immediately.

**Salary expectations?**
Montréal floor is $120k and the range starts at $118.7k. Ask where the role is leveled before naming a number, then aim for the upper half given nearly 18 years. Don't state your $160k+ ideal against this range unless you're willing to lose it.

**Questions in French?**
The role is bilingual. Be ready to run the pitch and the Énergir story in French.

## 4. Do not say
- Spring Boot, OpenShift, Kafka, MQ, Playwright or Cucumber expertise.
- Any figure not in `profile.md`.
- That the Logstash path was fully retired, or that SLOs were implemented.
- Your birth date, or anything about personal projects.

## 5. After the call
Tell Claude: the recruiter's name, the role confirmed, next step and date, office days, pay signal. It goes on the R155688 row in `applications.md`.
