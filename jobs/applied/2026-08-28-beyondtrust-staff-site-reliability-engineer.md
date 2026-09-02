# Staff Site Reliability Engineer- Remote — BeyondTrust

- **Source:** https://www.linkedin.com/jobs/view/4449482118/
- **Found:** 2026-08-28
- **Engagement type:** Full-time
- **Rate/Salary (stated):** Not stated
- **Location/Remote:** Canada — Remote
- **Days in Office:** 0 (Remote)
- **Flags:** Salary not disclosed; full-time only, no contract path mentioned; cybersecurity SaaS platform (Password Safe) — dual-cloud AWS/Azure environment, cloud platform is the venue, not the deliverable, so no hard-gate concern

## Fit Score: 7

Strong platform-engineering and reliability alignment: the role centers on "Everything as Code" (GitOps, Terraform/OpenTofu/Ansible), CI/CD standardization, and SLO/SLI definition across cloud and on-prem — directly matching the Terraform/Ansible IaC practice and CI/CD standardization work at Énergir, plus the RCA/MTTR-reduction discipline built there. The observability stack named (Grafana Cloud, Datadog, OpenTelemetry) overlaps with Marc's Dynatrace/Splunk/ELK background, though not an exact tool match. Dual AWS/Azure requirement keeps this from an even higher score since Azure isn't clearly primary, but the venue-not-deliverable framing means no cloud-platform red flag applies.

## Resume Delta

- Lead with the Desjardins JFrog Artifactory health-monitoring service (Python/FastAPI, ~250 repositories tested every 4 hours) as direct evidence of platform-as-a-product thinking and CI/CD-adjacent tooling ownership.
- Emphasize Terraform/Ansible IaC standardization from Énergir against the "Everything as Code" / GitOps requirement.
- Highlight the ArgoCD/Kubernetes provisioning work at Desjardins for the containerization and cluster-administration requirement.
- Use the Énergir RCA and MTTR-reduction practice as direct precedent for defining and enforcing SLOs/SLIs.
- Lead with the signature pattern (Desjardins: asked to verify repo configuration, delivered a tool-agnostic validation harness that also de-risked the JFrog version upgrade) — matches this role's emphasis on reducing engineer cognitive load through platform initiatives.

## Draft Cover Letter

Hi BeyondTrust team,

I'm applying for the Staff Site Reliability Engineer role supporting the Password Safe platform. At Desjardins, I was asked to verify Artifactory repository configuration — I delivered a tool-agnostic, configurable validation harness that also became the regression-safety net for the enterprise JFrog version upgrade, the same "platform as a product" instinct your posting describes. I built that service in Python/FastAPI with Terraform-driven environment automation and ArgoCD/Kubernetes provisioning, and at Énergir I standardized Terraform and Ansible IaC across nine runtimes while driving RCA practices that measurably reduced MTTR.

Your emphasis on "Everything as Code," GitOps workflows, and SLO/SLI definition maps closely to that work. I'm comfortable operating across both cloud and on-prem environments, having led Azure modernization migrations at Énergir alongside earlier hands-on AWS build experience.

I'm incorporated in Canada, fully bilingual, and available to start immediately. I'd welcome a conversation about the role.

Best regards,
Marc Berthelette
