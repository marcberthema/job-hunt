# Lead DevOps Engineer — Litmus Automation Canada

- **Source:** pasted text (no URL provided)
- **Found:** 2026-07-14
- **Engagement type:** Full-time (benefits, equity participation, professional development allowance — standard FTE package)
- **Rate/Salary (stated):** CA$145,000 – CA$185,000 — exceeds the $160k CAD target
- **Location/Remote:** Toronto, ON — Remote full-time
- **Flags:** Full-time only; this is a **technical leadership role with explicit people-management scope** — "lead and mentor a distributed DevOps team spanning North America and India" — same management-scope pattern flagged on Empire Life, Vancity, Servus, and GoTo; primary stack is AWS + self-hosted GitLab administration, not Azure — Azure only satisfies a secondary "at least one of GCP/Azure" requirement via Azure AD/Entra ID identity federation, which is a narrower slice than Marc's broader Azure DevOps/infrastructure experience; deep, specialized tooling requirements (self-hosted GitLab platform administration, EKS day-2 operations, VMware/vCenter SSO federation, Qualys, 1Password/Vault, SBOM/CVE pipelines) with limited overlap to the documented background

## Fit Score: 5/10 (skill/domain fit — logistics noted separately above)

Genuine overlap exists on Terraform (module design, remote state, drift detection, CI/CD-driven plan/apply — all direct matches to the Énergir IaC work) and on the "AI-Enabled DevOps Transformation" pillar, which is unusually well-aligned with the spec-driven AI development approach already in practice — the posting explicitly wants "a clear point of view on where it creates genuine leverage vs. hype," which is a natural fit for the Claude Code/markdown-continuity workflow discussed earlier. However, the role's technical core is deep and specific in ways that don't overlap cleanly with Marc's background: self-hosted GitLab platform administration (not Azure DevOps/GitHub Actions/Jenkins, which is the documented CI/CD experience), EKS specifically as the primary Kubernetes target, AWS as the primary cloud with GCP as secondary (Azure only appears via a narrower Entra ID identity-federation angle), and a specialized security/identity tooling stack (Qualys, 1Password, VMware vCenter federation) with no precedent in the resume. Combined with the explicit people-leadership mandate (mentoring a distributed team across two continents), this is a role where the surface-level "DevOps/platform engineering" match is real but the specific tooling depth required is a meaningfully different profile than Marc's Azure-centric background.

## Resume Delta

- Lead with Terraform module design, drift management, and CI/CD-driven plan/apply workflows from Énergir against the core IaC requirement
- Bring the spec-driven AI development philosophy (product overview → stories → markdown continuity → coding-standard configs → CI/CD quality gates) directly into the resume delta and cover letter — this is a strong, specific match to the "AI-Enabled DevOps Transformation" pillar and the "demonstrated experience using AI tooling" requirement
- Surface CI/CD pipeline architecture from Azure DevOps/GitHub Actions/Jenkins as transferable platform-engineering discipline, while being transparent that self-hosted GitLab administration specifically isn't part of the documented experience
- Note Kubernetes/ArgoCD/Docker experience from Desjardins as general container-orchestration evidence, while being clear that EKS-specific day-2 operations aren't part of the background
- Be candid that AWS, GCP, VMware/vCenter federation, Qualys, and 1Password/Vault aren't part of the documented skill set — Azure and Splunk are the closer analogs
- Bring forward SOVO Technologies team-management experience as the only — dated — evidence toward the people-leadership requirement

## Draft Cover Letter

Dear Litmus Hiring Team,

I'm a Senior DevOps Engineer with nearly 18 years of experience building automated, secure infrastructure for enterprise clients — most recently a 6-month engagement with Desjardins where I automated environment provisioning with Kubernetes and ArgoCD and built Splunk-based alerting for configuration governance, and prior to that standardizing Terraform-based Infrastructure as Code at Énergir with drift-free provisioning across dev, staging, and production.

I want to speak directly to the AI-Enabled DevOps Transformation pillar of this role, since it's an area I already practice deliberately: I build with AI using a spec-driven development approach — starting with a product overview, breaking it into stories that get planned and implemented one at a time, with markdown files giving tools like Claude Code real continuity across a project, backed by coding-standard configuration files and CI/CD quality gates to maintain the same stability and trust a human-reviewed pipeline would carry. I have a clear point of view on where AI tooling creates genuine leverage versus where it's hype, grounded in hands-on use rather than theory.

My deepest cloud and CI/CD experience is Microsoft Azure and Azure DevOps rather than AWS and self-hosted GitLab, and I don't have hands-on EKS, VMware/vCenter federation, or the specific security tooling (Qualys, 1Password) named in this role. I want to be upfront about that gap rather than overstate it — the underlying platform engineering discipline transfers, but the specific tooling depth here is different from my recent work.

I'm based remotely in Canada, incorporated, and available to discuss whether my background is the right fit despite the tooling differences.

Best regards,
Marc Berthelette
