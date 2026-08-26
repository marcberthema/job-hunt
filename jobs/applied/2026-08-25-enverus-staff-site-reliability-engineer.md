# Staff Site Reliability Engineer (26248) — Enverus

- **Source:** https://ca.indeed.com/rc/clk?jk=13d4e80d91c8a2cd
- **Found:** 2026-08-25
- **Engagement type:** Full-time (implied permanent)
- **Rate/Salary (stated):** Not stated
- **Location/Remote:** Calgary, AB — Remote
- **Days in Office:** 0 (Remote)
- **Flags:** Salary not disclosed; full-time only, no contract path mentioned; AWS is the primary cloud (no Azure mentioned) — falls under the "venue" tier of the cloud-platform rule (general cloud/infra competence, not a hard-gate deep-years requirement), so scores normally with the mismatch flagged

## Fit Score: 7

Strong platform-engineering and SRE overlap: CI/CD framework implementation, Kubernetes, Infrastructure as Code (Terraform/CloudFormation), and 24/7 on-call operational rigor all map directly to the CI/CD standardization at Énergir and the Kubernetes/ArgoCD provisioning automation at Desjardins. Cloud platform is AWS rather than Azure — the requirement reads as general cloud/infrastructure competence (3+ years AWS administration) rather than deep AWS-native architecture ownership, so this clears as a straightforward apply per the profile's cloud-platform rule, backed by the Tink AWS build (EC2, S3, Route 53, VPC) as a concrete, honest answer if AWS depth comes up.

## Resume Delta

- Lead with the Desjardins Kubernetes/ArgoCD automated-provisioning work — direct match to the posting's Kubernetes and CI/CD framework requirements.
- Emphasize the Terraform/Ansible IaC standardization from Énergir against the posting's Terraform/CloudFormation requirement.
- Answer the AWS requirement with the Tink build (EC2, S3, Route 53, VPC, self-managed memcached, serverless relational database) — ~6 months building a client's full AWS target environment with no prior AWS experience, cancelled before cutover, provisioned by hand rather than via IaC. State both facts plainly.
- Note the Desjardins Splunk/Dynatrace observability and on-call/incident-response practice from Énergir against the posting's 24/7 operational-excellence emphasis.

## Draft Cover Letter

Hello Enverus team,

I'm applying for the Staff Site Reliability Engineer role. Your emphasis on CI/CD automation, Kubernetes, and Infrastructure as Code for a global cloud footprint is the core of what I've been doing across my last two engagements.

At Desjardins, I automated the provisioning of on-demand Artifactory environments using Kubernetes and ArgoCD, giving administrators self-service, fully configured environments for safe testing. At Énergir, I standardized Terraform and Ansible IaC practices across nine runtimes and 70+ applications, and built the observability and incident-response practice (Splunk alerting, Dynatrace dashboards, RCA) that a 24/7 operational environment depends on.

On AWS specifically: I spent roughly six months at Tink building a client's entire AWS migration target environment — EC2, S3, Route 53, VPC, self-managed memcached, and a serverless relational database — with no prior AWS experience going in. The client ultimately cancelled the migration before cutover, and the environment was provisioned by hand in the console rather than through Terraform or CloudFormation, but the hands-on build experience across that core service surface is real and I can speak to it in detail.

I'm incorporated in Canada, fully bilingual (French/English), and available to start quickly.

Best regards,
Marc Berthelette
