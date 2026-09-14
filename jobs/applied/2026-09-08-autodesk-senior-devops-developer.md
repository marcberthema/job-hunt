# Senior DevOps Developer — Autodesk

- **Source:** https://www.linkedin.com/jobs/view/4451945559/
- **Found:** 2026-09-08
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $107,000–$157,300 CAD/year
- **Location/Remote:** Canada — Remote (distributed engineering team)
- **Days in Office:** 0 (Remote), though posting notes onboarding/ID verification may require
  an in-person step
- **Flags:** Salary tops out just under the $160K target and the bottom sits well below the $130K
  employment floor; requires MongoDB Atlas/DynamoDB/Redshift experience Marc doesn't have; lists
  specific AWS services (Step Functions, IAM, CloudWatch, Lambda) beyond Marc's actual AWS depth
  (EC2/S3/VPC/Route 53 from the Tink build) — kept honest in the resume/cover letter rather than
  claimed

## Fit Score: 6/10

Solid general platform/DevOps and SRE overlap: Terraform/Ansible IaC, Jenkins/GitHub Actions CI/CD,
Kubernetes/Docker via Desjardins ArgoCD work, Python/Bash scripting, and a real on-call/incident
response/RCA track record (Tink 24/7 rotation, Énergir MTTR reduction) against their SLO/SLI and
incident-postmortem practices. Cloud requirement reads as "AWS preferred" rather than a hard AWS
depth gate, and the posting's named AWS services (EC2, S3) overlap directly with the Tink build,
so this falls in the "apply" tier of the cloud-platform rule rather than the hard gate — Azure
depth carries the general "5+ years large-scale cloud production" requirement. Real gaps: no
MongoDB Atlas/DynamoDB/Redshift experience, and the posting's specific AWS service list (Step
Functions, IAM, CloudWatch, Lambda) goes beyond what the Tink build covered — both kept out of the
resume/cover letter rather than overclaimed.

## Resume Delta

- Lead with Azure production depth (Énergir, Desjardins) to satisfy "5+ years large-scale cloud
  infrastructure," then name the Tink AWS build (EC2, S3, VPC, Route 53) honestly, with the
  by-hand/pre-production caveat, to cover the AWS-preferred and EC2/S3 keyword requirements.
- Highlight Kubernetes/ArgoCD provisioning automation from Desjardins against container
  orchestration requirements.
- Emphasize Jenkins (Tink) and GitHub Actions (Desjardins) CI/CD experience directly.
- Lead with RCA/MTTR-reduction and Dynatrace/Splunk observability work from Énergir against the
  SLO/SLI, incident-response, and postmortem responsibilities — this is the strongest lever since
  "chaos testing" itself isn't part of the background.
- Note the Tink 24/7 on-call rotation directly against the on-call requirement.
- Do not list MongoDB Atlas, DynamoDB, Redshift, Step Functions, Lambda, or CloudWatow as skills —
  not part of the real skill set; be upfront if asked in interview.

## Draft Cover Letter

Hi Autodesk team,

I'm applying for the Senior DevOps Developer / SRE role on the Bidding team within Autodesk
Construction Solutions. Your focus on service reliability, operational excellence, and CI/CD
automation for cloud-native services lines up closely with the platform work I've done throughout
my career.

At Énergir, I standardized CI/CD and Terraform/Ansible Infrastructure as Code across nine runtimes
for 12 application teams and 70+ applications, and drove root cause analysis and proactive
monitoring (Dynatrace, Splunk) to reduce MTTR on critical production incidents — directly relevant
to your SLO/SLI and incident-response practices. At Desjardins, I automated on-demand environment
provisioning using Kubernetes and ArgoCD as part of hardening the enterprise JFrog Artifactory
platform, and built GitHub Actions-based CI/CD pipelines.

My cloud depth is primarily Microsoft Azure at production scale; I've also built hands-on AWS
infrastructure (EC2, S3, VPC, Route 53) for a client migration target environment, though that work
was pre-production and provisioned manually rather than through Terraform. I carried 24/7 on-call
responsibility for production systems earlier in my career and am comfortable with that
expectation here.

I'm incorporated in Canada, fully bilingual (French/English), and available immediately.

Best regards,
Marc Berthelette

## Application Note

**2026-09-08:** Applied directly via LinkedIn.
