# Senior Site Reliability Engineer — Penn Interactive (Penn Entertainment)

- **Source:** https://job-boards.greenhouse.io/penninteractive/jobs/6131766004 (via https://ca.indeed.com/rc/clk?jk=33a60aac95f0b636)
- **Found:** 2026-08-31
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $145,000–$193,000 CAD/year
- **Location/Remote:** Remote, Canada
- **Days in Office:** 0 (Remote)
- **Flags:** Full-time only, no contract path stated; salary well above the $160K target across most of the range; AWS/GCP named (no Azure), but "and/or on-premise infrastructure expertise" keeps this a venue-not-deliverable posting rather than a hard AWS/GCP-ownership gate — general infra migration/automation scope, not EKS/GKE multi-tenancy ownership; sports-betting/gambling industry — flag for Marc's own values check, not a skill/eligibility issue

## Fit Score: 7

Strong platform-engineering fit: infrastructure migration ownership, ArgoCD/Helm/GitHub Actions platform automation tooling, Kubernetes in production, Terraform/Helm IaC, and Datadog observability — closely tracks the Desjardins Kubernetes/ArgoCD provisioning work and the Énergir Terraform/CI-CD standardization. Salary clears target comfortably. AWS/GCP-primary with no Azure keeps this below 8, but the posting reads as general infrastructure competence (migrations, automation, consulting to dev teams) rather than deep cloud-native architecture ownership, so no hard gate applies.

## Resume Delta

- Lead with the Desjardins Kubernetes/ArgoCD automated-provisioning work — direct match to "production Kubernetes experience" and the GitOps/Helm/ArgoCD stack named in the posting.
- Highlight the Énergir Terraform/Ansible IaC standardization and the "complex infrastructure migrations — scoping, planning, execution, validation" language, mirroring Marc's nine-runtime CI/CD migration story.
- Note the GitHub Actions CI/CD ownership from Énergir (12 teams, 70+ apps) against the platform-automation-tooling requirement.
- Emphasize the Dynatrace/Splunk observability and RCA/incident-response practice against the Datadog observability and on-call requirements.
- Answer the AWS requirement with the Tink build (EC2, S3, Route 53, VPC, memcached, serverless DB), honestly bounded per profile.md's cloud-platform rule — this is a "venue" posting, not a hard-gate one, so the Azure-primary framing plus the Tink AWS build both apply normally.

## Draft Cover Letter

Hi Penn Interactive team,

I'm applying for the Senior Site Reliability Engineer role. My career has a consistent pattern: given a narrow scope, I deliver something structurally larger. At Desjardins, asked to verify Artifactory repository configuration, I built a tool-agnostic validation harness that also de-risked the enterprise JFrog version upgrade — and separately automated the provisioning of on-demand Kubernetes environments using ArgoCD, giving system administrators safe, self-service testing environments. At Énergir, I standardized CI/CD and IaC (Terraform, Ansible, GitHub Actions) across nine runtimes for 70+ applications, and drove Dynatrace observability and Splunk alerting that cut MTTR on critical production incidents.

Your focus on infrastructure migrations, platform automation tooling (ArgoCD, Helm, GitHub Actions), and cross-team infrastructure consulting maps directly onto that background. On the cloud side, my deepest experience is Microsoft Azure, but I also built a client's full AWS migration target environment at Tink (EC2, S3, Route 53, VPC, memcached, serverless relational database) over roughly six months with no prior AWS experience — direct, defensible experience across the core AWS surface, honestly bounded (the client cancelled before cutover, and provisioning was manual rather than IaC).

I'm incorporated in Canada, fully bilingual (French/English), and comfortable operating in a fast-paced, regulated, high-availability environment. I'd welcome a conversation.

Best regards,
Marc Berthelette
