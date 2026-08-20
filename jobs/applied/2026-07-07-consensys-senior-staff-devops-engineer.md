# Senior Staff DevOps Engineer - MetaMask — Consensys

- **Source:** pasted text (no URL provided)
- **Found:** 2026-07-07
- **Engagement type:** Full-time (background checks required, standard employment language — no contract mentioned)
- **Rate/Salary (stated):** US-based candidates: $164,000–$218,000 USD base; explicitly states compensation for Canada-based candidates "will be determined based on location, experience, and skills" and may differ from the US range
- **Location/Remote:** Fully remote, globally distributed team
- **Flags:** Full-time only, no contract path; salary figure quoted is US-only — actual Canada-based compensation unstated and could land anywhere; web3/blockchain domain has no direct precedent in Marc's work history, though the infrastructure work itself is domain-agnostic; "DORA metrics" / high-security (ISO/SOC2) environment implies a mature, process-heavy org

## Fit Score: 7/10 (skill/domain fit — logistics noted separately above)

Strong technical overlap: the role explicitly lists both AWS *and* Azure (not an AWS-only or GCP-heavy stack like several recent postings), Kubernetes/Helm/containerization, Terraform IaC, and CI/CD pipeline ownership — all core to Marc's Desjardins and Énergir work. Python is listed among acceptable languages, and the security-first, ISO/SOC2, no-single-point-of-failure/HA/DR framing lines up well with the governance and compliance-oriented work built at Desjardins (Splunk alerting for out-of-pipeline changes, artifact lifecycle governance). The main gaps are monitoring tooling (LGTM/Prometheus vs. Marc's Dynatrace/Splunk/ELK background — related discipline, different tools) and the web3/blockchain product domain, which has no precedent in the profile, though the posting's infrastructure scope doesn't require blockchain-specific expertise to execute well.

## Resume Delta

- Lead with Kubernetes/ArgoCD environment automation and JFrog Artifactory governance from Desjardins to match container orchestration and secure infrastructure requirements
- Emphasize the Splunk alerting work catching out-of-pipeline configuration changes as direct evidence of the "security first mindset" and compliance-oriented (ISO/SOC2-adjacent) practices this role wants
- Highlight Terraform/Ansible IaC standardization from Énergir against the Infrastructure as Code requirement
- Surface Azure cloud modernization and Azure DevOps CI/CD architecture from Énergir — one of the two named cloud platforms
- Note Python/FastAPI from Desjardins against the language requirement
- Be candid that observability tooling experience is Dynatrace/Splunk/ELK rather than Prometheus/LGTM, and that AWS depth is lighter than Azure — frame as transferable platform-engineering discipline rather than tool-for-tool experience

## Draft Cover Letter

Dear Consensys / MetaMask Hiring Team,

I'm a Senior DevOps Engineer with nearly 20 years of experience delivering secure, compliant infrastructure for regulated enterprise environments — most recently a 6-month engagement with Desjardins hardening the JFrog Artifactory platform, where I built Kubernetes/ArgoCD-driven environment automation, governance tooling, and Splunk alerting to enforce pipeline-only configuration changes and improve auditability. That security-first, compliance-oriented approach to infrastructure is directly relevant to running high-cybersecurity-standard (ISO/SOC2) production environments for MetaMask.

At Énergir, I architected enterprise CI/CD pipelines on Azure DevOps and standardized infrastructure provisioning with Terraform and Ansible, while driving RCA and observability practices to reduce MTTR — the same discipline your team needs to improve DORA metrics across products. While my direct blockchain/web3 exposure is limited, the underlying platform engineering fundamentals — multi-cloud infrastructure (Azure, with growing AWS exposure), Kubernetes, IaC, and CI/CD — transfer directly, and I'm energized by the chance to apply that experience to a new domain.

I'm based remotely in Canada, incorporated, fully bilingual (French/English), and open to discussing compensation and engagement structure that fits both sides.

Best regards,
Marc Berthelette
