# Principal DevOps Engineer — Veeva

- **Source:** https://builtin.com/job/principal-devops-engineer/10570857
- **Found:** 2026-08-28
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $150,000–$200,000 CAD/year
- **Location/Remote:** Toronto, ON — In-office or remote (flexible)
- **Days in Office:** 0 (Remote option available)
- **Flags:** AWS is the primary cloud platform named — venue, not deliverable (general automation/distributed-systems scope, not EKS multi-tenancy or cluster-architecture-as-the-job), so no hard-gate concern per the AWS three-tier rule; full-time only, no contract path mentioned

## Fit Score: 7

Strong seniority and scope match: 5+ years DevOps with architectural leadership, mentoring, and cloud-native infrastructure design for an AI-driven life sciences platform — squarely in Marc's "signature pattern" territory of taking ownership beyond the assigned scope. Terraform/Ansible IaC and Kubernetes/OpenShift orchestration line up directly with Énergir's IaC standardization and Desjardins' ArgoCD/Kubernetes work. AWS is the named cloud platform rather than Azure, but the posting frames it as the operating environment rather than deep AWS-native architecture ownership, so the Tink AWS build experience answers it directly without needing the hard-gate caveat.

## Resume Delta

- Lead with the signature pattern — Tink's unprompted software inventory platform, Énergir's Salesforce CLI + validation-sandbox delivery, and Desjardins' JFrog validation harness — to match "lead design and implementation," not just execute tickets.
- Answer the AWS requirement directly with the Tink build (EC2, S3, Route 53, VPC, self-managed memcached, serverless relational DB), honestly bounded (6 months, by-hand, cancelled before cutover) rather than an analogy.
- Emphasize Terraform/Ansible IaC standardization from Énergir against the posting's IaC + Kubernetes/OpenShift requirement.
- Highlight the 18 years of breadth (~7 years writing production code at SOVO) against the posting's programming-language requirement (Python, Java/Scala/Go).
- Note the recurring team-enablement sessions at Énergir as evidence of the mentoring/architectural-leadership expectation.

## Draft Cover Letter

Hi Veeva team,

I'm applying for the Principal DevOps Engineer role. My career has a consistent pattern: given a narrow scope, I deliver something structurally larger. At Desjardins, asked to verify Artifactory repository configuration, I built a tool-agnostic validation harness that also de-risked the enterprise JFrog version upgrade. At Tink, unprompted, I built a fleet-wide software inventory platform surfacing CVE exposure and EoL risk to product owners who had no such visibility. At Énergir, I standardized CI/CD and IaC (Terraform, Ansible) across nine runtimes for 70+ applications, entering most with no prior experience.

On AWS specifically: I built a client's full AWS migration target environment at Tink — EC2, S3, Route 53, VPC, self-managed memcached, a serverless relational database — over roughly six months, with no prior AWS experience. The client cancelled before cutover, and the work was provisioned by hand rather than through Terraform, but it's direct, defensible experience across the core AWS service surface. I also bring hands-on Kubernetes and ArgoCD experience from Desjardins.

I'm incorporated in Canada, fully bilingual, and comfortable leading without formal authority — I drove platform-engineering adoption across 12 teams outside any reporting line at Énergir. I'd welcome a conversation.

Best regards,
Marc Berthelette

## Rejection Note

**2026-08-28:** Requires deep Kubernetes expertise and is functionally an AWS developer role — mismatch against Marc's actual depth (Azure-primary, operational/provisioning-level Kubernetes rather than deep cluster-architecture expertise).
