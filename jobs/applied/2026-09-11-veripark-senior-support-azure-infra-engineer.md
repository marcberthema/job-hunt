# Senior Support and Azure Infra Engineer — VeriPark

- **Source:** https://www.linkedin.com/jobs/view/4464569717
- **Found:** 2026-09-11
- **Engagement type:** Full-time
- **Rate/Salary (stated):** Not posted — unconfirmed whether it clears the $100k+ remote-FTE floor. Verify early (Glassdoor/recruiter) before investing heavily in the application.
- **Location/Remote:** Canada, 100% Remote
- **Days in Office:** N/A (fully remote)
- **Flags:** No salary posted; benefits-forward listing (birthday leave, wellbeing program, "Together Culture," reward programs) signals FTE-culture emphasis — not disqualifying under the current three-track strategy, just a tell about the environment; Azure certs (Solutions Architect Expert / Administrator Associate) "highly preferred" but not required — Marc doesn't hold these yet (roadmap intentionally parked); role reads more "Azure administration/support" than platform-engineering/strategic ownership — real but narrower leadership content (mentoring junior staff, troubleshooting, backup/DR) than Marc's strongest pitch. 90 applicants already at time of scoring.

## Fit Score: 7

Azure depth is a near-exact match: Virtual Machines, Storage, VNets, Azure AD, RBAC, Azure Monitor/Log Analytics/Application Insights, PowerShell — all things Marc already carries — and AKS/Kubernetes (listed as "a plus") is a real strength from the Desjardins and Énergir engagements. VeriPark builds banking/insurance software on the Microsoft stack, so the financial-services domain credibility from Desjardins plays well. Fully remote with no location or residency gate. FTE-only is no longer a scoring penalty under the three-track strategy (2026-09-11 update), but comp is entirely unstated, which caps this below 8 until verified. The role itself skews administration/support (break-fix, backup/DR, junior mentoring) rather than the "recommends the fix, not the patch" platform-engineering framing that is Marc's strongest differentiator — still a legitimate match, just not the sharpest one.

## Resume Delta

- Lead with Azure depth: RBAC/ABAC/Policy, Firewall, VNets, NSG, Private Link — directly answers "Azure Active Directory," "RBAC," and "role-based access control" in the posting.
- Surface PowerShell explicitly (already on the Desjardins-flavored resume skills list) — the posting names it three times as the primary automation tool. Terraform/Ansible is Marc's real IaC depth; be upfront that it's Terraform/Ansible rather than ARM templates specifically if asked — same category of skill (declarative infra), different tool.
- Use the Desjardins Kubernetes/ArgoCD bullet to answer the AKS requirement — provisioning on-demand instances is a concrete, checkable AKS story.
- Use the Énergir RCA/MTTR bullet (proactive monitoring, observability dashboards, automated remediation) to answer "proactive monitoring... Azure Monitor, Log Analytics, Application Insights" — Marc's tools were Dynatrace/Splunk, not Azure-native, so frame it as "the same discipline, different toolchain" rather than claiming direct Azure Monitor experience he doesn't have.
- Use the "leads without authority" / enablement pattern (12 teams, ~6 sessions/year) to answer "mentor and guide junior Azure support staff" — real evidence of teaching/enablement, even without a formal reports-to relationship.
- Do not claim or imply Azure Solutions Architect Expert / Administrator Associate certification — Marc doesn't hold either. If asked, be direct: certs are on a roadmap, not yet started, and the resume-backed hands-on depth (5-10 service migrations led, years of IaC) is the stronger evidence anyway.

## Draft Cover Letter

Dear Hiring Team,

I'm writing to express interest in the Senior Support and Azure Infra Engineer role at VeriPark. Over 18 years in DevOps and platform engineering — most recently leading Azure modernization at Énergir and a JFrog Artifactory reliability engagement at Desjardins, a Canadian financial institution — I've built deep, hands-on Azure expertise across compute, networking, RBAC, and IaC, plus the habit of fixing root causes instead of patching around them.

At Énergir, I configured RBAC, Azure Firewall, VNets, NSG, and Private Link while migrating 5–10 mission-critical services to Azure, and built the proactive monitoring, dashboards, and automated remediation that reduced Mean Time to Recovery across the application estate — the same discipline your posting asks for around Azure Monitor and Log Analytics, applied with a different observability toolchain (Dynatrace/Splunk). At Desjardins, I used Kubernetes and ArgoCD to automate on-demand provisioning of fully configured environments, directly relevant to your AKS-based infrastructure.

I also bring real experience guiding others without a formal reporting line: at Énergir I ran recurring enablement sessions with 12 application teams to turn delivered tooling into actual practice — the same instinct your posting asks for in mentoring junior Azure support staff.

One thing I'll be upfront about: I don't currently hold the Azure Solutions Architect Expert or Administrator Associate certifications your posting lists as preferred. My Azure depth comes from years of hands-on production work rather than certification, and I'm glad to speak to specific scenarios in interview to demonstrate it directly.

I'd welcome the chance to discuss how this background fits VeriPark's Azure environment. Thank you for your consideration.

Best regards,
Marc Berthelette
