# Senior DevSecOps Engineer — ComPsych Corporation

- **Source:** https://ca.indeed.com/viewjob?jk=f7352acd77c80189
- **Found:** 2026-09-01
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $150,000–$200,000 USD/year
- **Location/Remote:** Canada — Remote
- **Days in Office:** 0 (Remote)
- **Flags:** Full-time only, no contract path stated; heavy benefits emphasis (PTO, medical/dental/vision, 401(k) with match, EAP, wellness program) is a soft FTE signal per profile's red-flag list; domain is healthcare/behavioral-health data (HIPAA/HITRUST/SOC 2) rather than Marc's core financial/energy sector credibility, though the regulated-industry pattern still transfers; cloud is "AWS or Azure" at real production scale (not just venue) — no penalty since Azure is explicitly named as sufficient; salary well above the $160K target even before CAD conversion (stated in USD)

## Fit Score: 8/10 (skill/domain fit — logistics noted separately above)

Strong, close match: the role is explicitly CI/CD architecture ownership, IaC (Terraform/CloudFormation/ARM), Kubernetes/Helm for application workloads, and security-shift-left (SAST/DAST/SCA, secrets scanning, least-privilege IAM) — directly overlapping the Terraform/Ansible IaC standardization and Kubernetes/ArgoCD work at Énergir and Desjardins. The posting's "CloudSecOps team building shared standards across multiple application teams" framing matches Marc's Énergir pattern of driving platform-engineering adoption across 12 teams outside any reporting line. Most distinctively, this posting is explicitly AI-native — "agentic AI is your primary surface for planning and building CI/CD," directing AI-built pipelines and validating output before it ships — which is a near-literal description of the Claude-driven Python/FastAPI health-monitoring service Marc built at Desjardins, giving him a genuine, defensible answer rather than a generic "AI-curious" claim. Healthcare/behavioral-health compliance (HIPAA/HITRUST) isn't Marc's named sector (financial services/energy), but the regulated-data discipline and audit/compliance posture (Splunk alerting for out-of-band config changes at Desjardins) transfers directly.

## Resume Delta

- Lead with the Desjardins Python/FastAPI health-monitoring service and its AI-assisted build — this posting's "direct AI to build pipelines/automation and validate what it produces" requirement is the closest literal match anywhere in the job search so far; name it explicitly rather than folding it into a generic automation bullet.
- Emphasize the Énergir Terraform/Ansible IaC standardization and the Kubernetes/ArgoCD provisioning automation from Desjardins against the posting's "one or more IaC tools used in production" and "containers and Kubernetes for application workloads" requirements.
- Highlight the Desjardins Splunk alerting for out-of-band configuration changes and artifact lifecycle/retention policy work as direct evidence of "security and observability as designed-in requirements," not an afterthought.
- Lead the "drives standards across teams outside any reporting line" language from Énergir (12 application teams, ~6 enablement sessions/year) against the posting's "build shared standards with CloudSecOps, not one-off fixes per team" requirement.
- Note the Énergir RCA/observability/MTTR-reduction work as evidence for the "own application observability, unblock teams in production" responsibility.
- Since the posting accepts AWS or Azure at production scale, foreground Azure depth as the primary claim and don't over-index on the smaller, dated AWS build at Tink — this posting doesn't need the AWS caveat unless asked directly.

## Draft Cover Letter

Hi ComPsych team,

I'm applying for the Senior DevSecOps Engineer role on your CloudSecOps team. What caught my attention is how specifically the posting describes directing AI to build pipelines and infrastructure while staying accountable for validating what it produces — that's not a hypothetical for me. At Desjardins, I designed and built a Python/FastAPI health-monitoring service, using Claude-driven workflows, that automatically tested the configuration of ~250 remote Artifactory repositories every 4 hours and published results to Dynatrace. I wrote the specs, directed the AI-assisted build, and validated the output before it shipped — then extended the harness well past its original scope to de-risk an enterprise-wide platform upgrade. That's the exact operating model this role describes, not an analogy for it.

On the infrastructure side: at Énergir, I standardized CI/CD and Terraform/Ansible IaC across nine runtimes for 12 application teams and 70+ applications, and drove that adoption through recurring enablement sessions rather than one-off fixes — directly matching your goal of building shared CloudSecOps standards rather than solving the same problem differently per team. At Desjardins, I also built Splunk alerting to catch configuration changes made outside the CI/CD pipeline and implemented artifact lifecycle policies for audit and compliance — the same "security and observability designed in, not caught later" posture your posting describes, which matters given the behavioral-health data your systems carry.

I'm comfortable in both Azure and Kubernetes/container environments in production, and I've carried on-call responsibility for critical production systems throughout my career. I'm incorporated in Canada, fully bilingual (French/English), and available immediately. I'd welcome a conversation.

Best regards,
Marc Berthelette
