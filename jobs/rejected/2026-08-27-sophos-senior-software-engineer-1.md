# Senior Software Engineer 1 — Sophos

- **Rejected:** 2026-08-27 — Marc could live with the AWS gap, but not the required production Kubernetes/EKS depth

- **Source:** https://www.linkedin.com/jobs/view/4449026460
- **Found:** 2026-08-27
- **Engagement type:** Full-time
- **Rate/Salary (stated):** CAD $105,000 – $175,000 base (Canada)
- **Location/Remote:** Smiths Falls, ON, Canada — remote-first, potential hybrid for some roles
- **Days in Office:** Not stated (remote-first)
- **Flags:** AWS cloud-platform hard gate (see rationale) — profile's AWS/GCP hard-gate rule applies; no Azure mentioned anywhere in the posting; salary at/above target and location is Marc's own city, so purely a skill-stack mismatch, not a logistics issue

## Fit Score: 3 (skill/domain fit — AWS hard gate caps this despite excellent salary/location)

The role's core stack is AWS-only: "Advanced AWS cloud services knowledge (IAM, EC2, EKS, VPC, S3)" and "Terraform Infrastructure as Code expertise" are both listed as required qualifications, alongside production Kubernetes on Amazon EKS. This is Infrastructure-as-Code ownership *on AWS*, plus EKS cluster maintenance — exactly the combination the profile's cloud-platform hard gate flags as "cloud-native architecture ownership at scale is the deliverable," not a venue detail. Marc's real AWS experience (Tink, ~6 months, EC2/S3/Route 53/VPC provisioned by hand, no Terraform, no Kubernetes, cancelled before cutover) does not clear a role that requires advanced, production-grade AWS + Terraform + EKS as day-one competence — and he has never used Terraform against AWS, only Azure. No Azure appears anywhere in the posting, so his strongest asset doesn't transfer. Location (Smiths Falls — his home city) and salary ($105k–175k, above his $160k target) are ideal, but per the profile's scoring rule the cloud mismatch caps this regardless of how well the rest fits.

## Resume Delta

- If applying anyway, lead with the Tink AWS build (EC2, S3, Route 53, VPC) up front rather than buried — it's the only AWS keyword match, and this ATS will likely filter on "AWS," "Terraform," "EKS."
- Emphasize the Terraform/Ansible IaC work at Énergir, but be prepared to state clearly in interview that it was Azure, not AWS — don't let the resume imply otherwise.
- Highlight the Kubernetes/ArgoCD work at Desjardins to show real (if non-EKS) production Kubernetes operation.
- Lead the summary with "18 years making unfamiliar systems deliverable" and the learn-cold pattern (Salesforce, MuleSoft, Databricks) as the argument for ramping on EKS/AWS specifics fast — this is the honest angle per profile guidance, not a claim of existing AWS depth.
- Given the hard-gate flag, recommend against applying unless Marc wants to make an explicit case in a cover letter that his learn-cold track record offsets the gap — this is a stretch application, not a strong match.

## Draft Cover Letter

Dear Sophos Hiring Team,

I'm applying for the Senior Software Engineer 1 role. Eighteen years of my career have followed the same pattern: given a narrow ask, I end up delivering something structurally larger, and I get there by reverse-engineering how a system actually works before I automate it. At Énergir I was asked to help port a struggling Salesforce deployment; I ended up replacing the legacy ANT scripts with the official Salesforce CLI and adding a validation-sandbox gate that made a broken merge structurally unable to reach production — taking the team from dreading their deployment window to a dependable every-other-Tuesday release. I'd never touched Salesforce before that project.

I want to be direct about where I stand on your stack: my Terraform and Infrastructure-as-Code depth is on Microsoft Azure, not AWS. My hands-on AWS experience is real but dated — about six months at Tink building a client's full AWS migration target environment (EC2, S3, Route 53, VPC, self-managed memcached, a serverless relational database) from a standing start with no prior AWS exposure, though that environment was provisioned by hand rather than through Terraform, and the client cancelled the migration before cutover. I'm telling you this plainly because it's the same instinct that's made me effective everywhere I've worked: I'd rather give you an honest starting point than a resume that oversells itself.

What I can offer is the platform-engineering judgment underneath the tooling: standardizing CI/CD across nine runtimes at Énergir, running Kubernetes and ArgoCD in production at Desjardins, and a track record of learning unfamiliar platforms — Salesforce, MuleSoft, Databricks, Spark, CloudFoundry — cold, under a delivery clock, every time. If your team values that kind of ramp-up ability as much as existing AWS depth, I'd welcome the conversation.

Sincerely,
Marc Berthelette
