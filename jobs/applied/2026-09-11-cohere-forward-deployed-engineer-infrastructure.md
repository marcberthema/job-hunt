# Forward Deployed Engineer, Infrastructure Specialist (North America) — Cohere

- **Source:** https://www.linkedin.com/jobs/view/4301372605
- **Found:** 2026-09-11
- **Engagement type:** Full-time
- **Rate/Salary (stated):** CA$175,000 – CA$385,000/yr. Extremely wide band (likely spans multiple levels within the same posting) — realistic landing spot for Marc is probably toward the lower-to-mid end given the individual-contributor "Forward Deployed Engineer" title rather than Staff/Principal, but even the floor of the range clears the FTE target outright.
- **Location/Remote:** Ottawa, ON listed, but role is remote-friendly (co-working stipend + travel budget for those not near an office) — effectively no on-site requirement.
- **Days in Office:** N/A (remote-friendly, no stated in-office requirement)
- **Flags:** Fast-growing AI startup (42% employee growth over the past year) — higher upside but also more volatility than an established enterprise; role is customer-facing infrastructure deployment (private cloud/on-prem rollouts for enterprise clients like RBC, Dell, LG CNS) rather than internal platform-engineering ownership — a different flavor of the work than Marc's recent engagements, closer to a delivery-consulting role. Cloud requirement is explicitly "Azure, AWS, or GCP" (cloud-agnostic) — no cloud-mismatch penalty.

## Fit Score: 8

Strong match on substance and comp, with a real shift in role shape worth being clear-eyed about. The posting explicitly lists cloud infrastructure across "Azure, AWS, or GCP" with no platform singled out as the deliverable — Azure depth counts fully here, no cloud-mismatch flag. Production Kubernetes administration with Helm is named directly, matching the Desjardins engagement. DevOps practices, CI/CD, and Git are core strengths. The posting explicitly invites imperfect-fit applicants ("If any of the above doesn't line up exactly with your experience, we still encourage you to apply").

What's different here versus Marc's recent roles: this is a **forward-deployed** engineer role — embedding directly with enterprise clients to deploy Cohere's "North" AI platform into their private cloud/on-prem environments, troubleshooting live with client IT teams. That's much closer to consulting delivery than platform-engineering ownership, and leans hard on customer-facing skill rather than internal-standards leadership. It plays to Marc's consulting instincts and comfort working across unfamiliar systems under a delivery clock, but it is not the "recommends the fix, not the patch" platform-ownership story that is his strongest pitch — the resume angle needs to shift toward "learns unfamiliar systems fast, under pressure, in front of the client" instead.

## Resume Delta

- Reframe the "learns unfamiliar platforms cold" competitive advantage (Salesforce, MuleSoft, Databricks, Spark, CloudFoundry, Oracle at Énergir; the full AWS build at Tink with no prior AWS experience) as the headline story — this posting is fundamentally about being dropped into unfamiliar client environments and delivering fast, which is exactly this pattern.
- Lead with the Desjardins Kubernetes/ArgoCD/Helm bullet — direct, checkable match to "administering production Kubernetes clusters and expertise with Helm."
- Since the cloud requirement is genuinely cloud-agnostic here, it's safe to mention the Tink AWS build plainly (with its honest caveats — cancelled, by-hand, dated) as evidence of cross-cloud adaptability, not just an Azure specialist.
- Emphasize any client-facing/stakeholder-facing experience explicitly — the CI/CD enablement sessions at Énergir (running sessions with 12 application teams) is the closest existing evidence of working directly with people outside his own team to drive adoption; frame it as "customer enablement," not just internal training.
- Do not oversell general "AI experience" beyond the AI-assisted engineering governance practice — this posting is about deploying an AI *product*, not about AI-assisted software delivery. Keep those two things clearly separate in interview; conflating them would read as reaching.

## Draft Cover Letter

Dear Hiring Team,

I'm writing to express interest in the Forward Deployed Engineer, Infrastructure Specialist role at Cohere. Across 18 years in DevOps and platform engineering, the pattern that has defined my career is getting dropped into systems I didn't know, under a real delivery deadline, and figuring out how they actually work before automating or deploying against them — which is close to the core of what this role asks for.

At Desjardins, I used Kubernetes and ArgoCD to automate on-demand provisioning of fully configured corporate environments, giving administrators a safe way to test configuration changes and upgrades — directly relevant to deploying North into client private-cloud and on-prem environments. Earlier, at Tink, I built a client's entire AWS target environment — compute, caching, and database layers — having never used AWS before that project; the migration was ultimately cancelled by the client before cutover, but the six months of hands-on build gave me real, checkable experience working across a cloud platform I didn't start out knowing. I bring the same approach to Azure, where I've led 5–10 mission-critical service migrations and built the Terraform/Ansible automation behind them.

I also have real experience driving adoption of new practices across teams I had no formal authority over — running recurring enablement sessions with 12 application teams at Énergir to turn delivered tooling into actual usage. I'd bring that same instinct to working directly with your enterprise clients' engineering teams.

I'd welcome the opportunity to discuss how this experience applies to deploying North for Cohere's clients. Thank you for your consideration.

Best regards,
Marc Berthelette
