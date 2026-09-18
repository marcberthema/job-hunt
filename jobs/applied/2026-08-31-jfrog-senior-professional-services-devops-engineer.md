# Senior Professional Services DevOps Engineer — JFrog

- **Source:** https://join.jfrog.com/job/?job=8157049 (via https://ca.indeed.com/rc/clk?jk=6d4602ce18cff5ee)
- **Found:** 2026-08-31
- **Status:** Applied
- **Applied:** September 15, 2026
- **Tailored resume:** `resume/tailored/2026-09-15-jfrog-senior-professional-services-devops-engineer-en.pdf`
- **Cover letter:** `resume/export/cover-letters/cover-letter-jfrog-senior-professional-services-devops-engineer.pdf`
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $130,000–$150,000 CAD base + bonus/commission + RSU equity
- **Location/Remote:** Remote, Canada — **posting says "East Coast only"**; ambiguous whether this means Atlantic Canada specifically or Eastern Canada broadly (Ontario/Quebec) — confirm before applying, since Smiths Falls, ON reads as Eastern Canada but not literally the East Coast
- **Days in Office:** 0 (Remote)
- **Flags:** Customer-facing Professional Services role (implementation/training for JFrog customers), not an internal platform-engineering seat — different flavor of DevOps work than Marc's usual target, but directly domain-relevant; salary meets target; "East Coast only" geography needs confirmation

## Fit Score: 8

Exceptional domain fit — this is a JFrog Artifactory-focused DevOps role, and Marc just closed a 6-month Desjardins contract doing exactly this: hardening and operationalizing enterprise JFrog Artifactory (observability, environment automation, governance, the validation harness that de-risked JFrog's own version upgrade). CI/CD tooling (Jenkins, Docker, Artifactory), cloud infrastructure (AWS/Azure/GCP), and Kubernetes/Ansible/Puppet all line up directly. Held at 8 rather than higher pending confirmation of the "East Coast only" location restriction and the customer-facing (vs. internal platform) nature of the role.

## Resume Delta

- Lead hard with the Desjardins JFrog Artifactory engagement — this is the single most directly relevant story in Marc's history for this specific posting: the Python/FastAPI health-monitoring service across 250 repositories, the tool-agnostic validation harness that became the regression-safety net for JFrog's own enterprise version upgrade, and the Kubernetes/ArgoCD on-demand Artifactory provisioning.
- Frame the Desjardins engagement using the signature-pattern story: asked to verify repository configuration, delivered a validation harness that also de-risked the enterprise JFrog version upgrade — exactly the kind of "goes beyond the ticket" evidence a customer-facing Professional Services role values.
- Highlight the Énergir Terraform/Ansible IaC standardization and GitHub Actions CI/CD ownership (12 teams, 70+ apps) against the CI/CD pipeline design and customer-enablement requirements.
- Note the recurring team-enablement sessions at Énergir (~6/year) directly against this posting's "training community members and clients on JFrog technologies" responsibility.
- Cloud platform is listed as "AWS, Azure, or GCP" — no penalty; lead with Azure depth, mention the Tink AWS build if pressed.

## Draft Cover Letter

Hi JFrog team,

I'm applying for the Senior Professional Services DevOps Engineer role. I just closed a 6-month Desjardins contract doing exactly this kind of work on your own platform: hardening and operationalizing their enterprise JFrog Artifactory environment. Asked to verify that ~250 repositories were correctly configured, I built a Python/FastAPI health-monitoring service testing them every 4 hours against Dynatrace dashboards — then extended it well past the original ask by making the validation logic tool-agnostic and the test set configurable, so the same harness became the regression-safety net for Desjardins' own enterprise JFrog version upgrade. I also automated on-demand Artifactory instance provisioning using Kubernetes and ArgoCD, and built Splunk alerting to catch configuration changes made outside CI/CD.

Beyond JFrog specifically, I standardized CI/CD and Infrastructure as Code (Terraform, Ansible) across nine runtimes for 70+ applications at Énergir, and ran recurring enablement sessions (~6/year) to turn delivered tooling into actual team adoption — directly relevant to this role's customer-training component.

I'm incorporated in Canada, fully bilingual (French/English), and available immediately. I'd want to confirm the "East Coast only" geography requirement against my location (Smiths Falls, ON) before going further — happy to discuss.

Best regards,
Marc Berthelette
