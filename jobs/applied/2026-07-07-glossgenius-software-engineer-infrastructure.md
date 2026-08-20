# Software Engineer, Infrastructure - All Levels — GlossGenius

- **Source:** pasted text (no URL provided)
- **Found:** 2026-07-07
- **Engagement type:** Full-time (health/dental with employer-covered premiums, parental leave, retirement savings plan, PTO — no contract language)
- **Rate/Salary (stated):** not stated
- **Location/Remote:** "Based remotely in or near the Greater Toronto Area" — remote but geographically restricted to GTA
- **Flags:** Full-time role with standard benefits emphasis (health/dental, parental leave, retirement plan) — FTE signal per profile red flags; salary not stated; remote is geo-restricted to near GTA rather than fully open; cloud platform in practice is AWS-primary ("scales its AWS cloud footprint efficiently"), despite listing AWS/GCP/Azure generically in requirements — real gap against Marc's Azure-only depth; on-call rotation required

## Fit Score: 5/10 (skill/domain fit — logistics noted separately above)

Good overlap on general platform/SRE fundamentals: Terraform-based Infrastructure as Code, Kubernetes/container orchestration, monitoring/alerting/observability ownership, and DevOps culture-building all map to Marc's Desjardins and Énergir experience, and Python is explicitly listed among acceptable languages. However, the actual operational cloud environment is AWS ("ensure GlossGenius scales its AWS cloud footprint efficiently"), not Azure — the requirements list AWS/GCP/Azure generically, but the role's day-to-day work is clearly AWS-centric, which is a real gap against Marc's Azure-exclusive cloud background, similar to the pattern seen in the Apptoza and GlobalLogic postings. The fintech/SMB-payments domain is a different flavor of "financial" than the large enterprise financial institutions (Desjardins) that anchor Marc's strongest domain credibility.

## Resume Delta

- Lead with Terraform/Ansible IaC standardization from Énergir against the "infrastructure-as-code frameworks" requirement
- Highlight Kubernetes/ArgoCD environment automation from Desjardins against container orchestration and EKS/GKE-equivalent experience
- Surface Dynatrace/Splunk observability and alerting work as direct evidence for "building and maintaining monitoring, logging, and alerting systems for large-scale, 24/7 platforms"
- Emphasize Python/FastAPI health-monitoring service from Desjardins to match the "high-quality code in a high-level language" requirement
- Note RCA/incident-response and MTTR-reduction work from Énergir against "drive operational excellence" and incident management practices
- Be candid that hands-on production cloud experience is Azure, not AWS — don't overstate AWS-specific service depth (EKS, etc.) that isn't on the resume

## Draft Cover Letter

Dear GlossGenius Hiring Team,

I'm a Senior DevOps Engineer with nearly 20 years of experience building reliable, secure, and scalable infrastructure for enterprise and financial-services clients — including a 6-month engagement with Desjardins building Kubernetes/ArgoCD-driven environment automation, a Python/FastAPI health-monitoring service with Dynatrace-based observability, and Splunk alerting to catch configuration drift outside the CI/CD pipeline. That focus on developer-facing tooling and platform reliability closely matches what you're looking for on the Infrastructure team.

At Énergir, I standardized Infrastructure as Code with Terraform and Ansible and drove incident response and root-cause-analysis practices to reduce MTTR — directly relevant to the operational-excellence and monitoring ownership this role calls for. My deepest cloud platform experience is Microsoft Azure rather than AWS, but the underlying IaC, container orchestration, and observability discipline transfers directly, and I'm confident ramping quickly on AWS specifics.

I'm based remotely in Canada and open to discussing fit for the Greater Toronto Area remote arrangement.

Best regards,
Marc Berthelette
