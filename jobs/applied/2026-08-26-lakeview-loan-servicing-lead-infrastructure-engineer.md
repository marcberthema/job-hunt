# Lead Infrastructure Engineer — Lakeview Loan Servicing, LLC.

- **Source:** https://www.linkedin.com/jobs/view/4412403902/
- **Found:** 2026-08-26
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $220,000–$260,000 USD/year, plus annual bonus, medical from day one, company-matched 401(k)
- **Location/Remote:** North York, ON listed, but posting explicitly states "This is a fully remote position"
- **Days in Office:** 0 (Remote)
- **Sourced via:** Manually added by Marc via URL — came from a personal LinkedIn saved-search email alert, not `/check-linkedin`. **Not found by the 2026-08-25 `/check-linkedin` overnight run.** Likely cause: `/check-linkedin` searches live via a fixed keyword rotation (e.g. "DevOps Consultant Remote," "Senior Site Reliability Engineer Remote") against `geoId=101174742` (Canada) + `f_TPR=r172800` (past 2 days), then scrolls the results panel — this posting's title, "Lead Infrastructure Engineer," isn't one of the rotation keywords and LinkedIn's own relevance ranking/email-alert matching clearly surfaces it under a different signal than the skill's search terms reach. Worth adding "Infrastructure Engineer" and "Lead Infrastructure Engineer" to the keyword rotation in `specs/check-linkedin.md` — this is the second time a manually-added posting revealed a rotation-keyword gap.
- **Flags:** Requires "2+ years as a tech lead, staff-level project lead, TLM, or hands-on leader guiding projects and mentoring engineers" — Marc has led CI/CD/platform-engineering adoption across 12 teams outside any reporting line (no formal management title/tenure) — real gap worth acknowledging, not concealing; role is US-parent-company (Bayview) fintech/mortgage servicing, regulated domain — strong sector fit; "AI-native engineering environment" expectation (coding agents, rapid prototyping) is unremarkable for Marc's actual workflow but worth a line if asked; cloud platform is "AWS, GCP, or Azure" — no penalty per profile's cloud rule, Azure depth is a straight asset here

## Fit Score: 8

Very strong technical match: Terraform IaC, CI/CD, Docker/Kubernetes, observability, secrets management, and cost discipline in a regulated fintech environment map almost one-to-one onto the Énergir Azure modernization/IaC work and the Desjardins JFrog/Kubernetes/ArgoCD engagement. Fully remote, well above target compensation even before FX conversion, and the posting explicitly welcomes candidates without a fintech background ("if your background does not line up perfectly with every bullet... please apply"). The one real gap is the 2+ years formal tech-lead/TLM requirement — Marc's leadership is real (12 teams, no reporting line, ~6 enablement sessions/year) but not a management title, which is a known blocker pattern worth flagging honestly rather than talking around.

## Resume Delta

- Lead with the Énergir Azure cloud modernization + Terraform/Ansible IaC bullet — directly matches "Lead the design, build, and operation of cloud infrastructure... with a focus on reliability, scalability, security, and cost discipline" and "Lead and contribute hands-on to infrastructure as code."
- Pair the Desjardins Kubernetes/ArgoCD on-demand environment provisioning bullet with the posting's "containers and orchestration technologies such as Docker, Kubernetes, ECS" and "Automate repeatable operational workflows, environment provisioning" requirements.
- Use the Énergir RCA/observability bullet (MTTR reduction, proactive monitoring dashboards) against "Reliability, Observability & Production Operations" — Dynatrace/Splunk experience covers the "logs, metrics, traces, alerts, dashboards" list almost verbatim.
- Use the "Drove CI/CD and platform-engineering adoption across 12 teams outside any reporting line, running recurring enablement sessions" bullet directly against the Leadership/Mentorship section and the tech-lead requirement — frame honestly as leadership substance without the title, per Marc's own "leads without authority" positioning.
- Note the Desjardins/financial-services and Énergir/regulated-energy-sector bullets together against "Support compliance-aware engineering practices appropriate for a regulated fintech environment" — two different regulated sectors, same discipline.
- Mention Python/FastAPI scripting (Desjardins) against the "write scripts or production-quality automation in Python, Go, Rust, Bash, TypeScript" requirement.

## Draft Cover Letter

Hi [Hiring Manager],

I'm applying for the Lead Infrastructure Engineer role on the Mission Control team. The scope here — owning cloud infrastructure, IaC, CI/CD, and observability in a regulated environment while keeping a small team moving with urgency — is close to what I've spent the last several years doing, most recently in financial services.

At Énergir, I led cloud modernization initiatives migrating 5–10 mission-critical services to Microsoft Azure and standardized Infrastructure as Code with Terraform and Ansible across 12 application teams — eliminating configuration drift across dev, staging, and production. I also drove CI/CD and platform-engineering adoption across those same 12 teams without a formal reporting line, running enablement sessions roughly six times a year to turn delivered tooling into actual usage. That's the leadership substance the role asks for — I just haven't held the title yet, and I want to say that plainly rather than talk around it.

On the regulated-industry side, I most recently delivered a 6-month contract at Desjardins hardening their enterprise JFrog Artifactory platform: building a Python/FastAPI health-monitoring service, automating on-demand environment provisioning with Kubernetes and ArgoCD, and adding Splunk alerting to catch changes made outside the CI/CD pipeline — the same auditability concerns a mortgage-servicing environment would care about. What consistently sets my work apart, across employers, is being handed a narrow scope and delivering something structurally larger than what was asked — that's the pattern behind the Salesforce CLI migration and validation-sandbox gate at Énergir, and the tool-agnostic validation harness at Desjardins that ended up de-risking their entire Artifactory version upgrade.

I'm incorporated in Canada, bilingual (French/English), and available immediately. I'd welcome the chance to talk through the role.

Best regards,
Marc Berthelette
