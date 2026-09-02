# Lead DevOps Engineer — Broadridge

- **Source:** https://builtin.com/job/lead-devops-engineer/10582710
- **Found:** 2026-08-31
- **Engagement type:** Full-time
- **Rate/Salary (stated):** Not disclosed
- **Location/Remote:** St-Arthur, NB — Hybrid Flexible (remote option available)
- **Days in Office:** Not stated; posting frames it as hybrid-flexible with a remote option
- **Flags:** Full-time only, no contract path stated; AWS-focused (EC2, ALB, S3, RDS/Aurora, EFS), no Azure mentioned; St-Arthur, NB is outside Marc's reachable-city list (Ottawa, Kingston, Brockville, Cornwall, Montréal) — if the remote option is genuine this is moot, but confirm before proceeding since a NB-based hybrid requirement would hard-gate this; financial services / low-latency trading infrastructure domain is a strong sector match

## Fit Score: 6

Strong domain and leadership-scope fit: Broadridge is financial services infrastructure (trading platforms), directly parallel to Marc's Énergir (energy, regulated) and Desjardins (financial services) background. The role explicitly combines hands-on IaC/CI/CD/Kubernetes work with mentoring — matching Marc's "leads without authority" pattern (Competitive Advantage #3) even though this role does carry formal lead scope. AWS-only stack (no Azure) and the unreachable New Brunswick location (mitigated only if the remote option is real) keep this below the 8-10 band. Rate/salary undisclosed is a real gap to confirm early.

## Resume Delta

- Lead with the Desjardins financial-services contract (JFrog Artifactory hardening for a large financial institution) to answer Broadridge's fintech/trading-infrastructure domain directly.
- Emphasize the Terraform/Ansible IaC standardization at Énergir against this role's "infrastructure provisioning through code-based tools and configuration management" requirement.
- Highlight the Kubernetes/ArgoCD work at Desjardins for the "containerization and orchestration initiatives" requirement.
- Note the recurring team-enablement sessions at Énergir (~6/year) as direct evidence for the mentoring/technical-leadership expectation, paired with Competitive Advantage #3 (led adoption across 12 teams outside any reporting line).
- Foreground the Tink AWS build (EC2, S3, Route 53, VPC, memcached, serverless DB) to answer the AWS requirement plainly, with the by-hand/cancellation caveats stated per the profile's AWS rule.

## Draft Cover Letter

Hi Broadridge team,

I'm applying for the Lead DevOps Engineer role supporting your trading infrastructure. Financial services is where I've done my most recent and most demanding work: at Desjardins, I hardened and operationalized the enterprise JFrog Artifactory platform for a major financial institution, building automated environment provisioning with Kubernetes and ArgoCD and Splunk-based governance alerting. At Énergir, I standardized Infrastructure as Code with Terraform and Ansible across nine runtimes for 70+ applications, and ran recurring enablement sessions to turn delivered tooling into adopted practice across 12 teams — the same hands-on-plus-mentoring balance this role calls for.

On AWS specifically: I built a client's full AWS target environment at Tink — EC2, S3, Route 53, VPC, self-managed memcached, a serverless relational database — over about six months with no prior AWS experience, provisioned by hand rather than through IaC, before the client cancelled ahead of cutover. It's real, defensible experience across the core AWS service surface I can speak to directly in interview.

I'm incorporated in Canada, fully bilingual (French/English), and available to start quickly. I'd want to confirm the remote/hybrid arrangement given my location, but wanted to get this in front of you. I'd welcome a conversation.

Best regards,
Marc Berthelette
