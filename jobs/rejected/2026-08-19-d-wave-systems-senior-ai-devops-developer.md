# Senior AI DevOps Developer [584] — D-Wave Systems

- **Source:** https://builtin.com/job/senior-ai-devops-developer-584/10601570
- **Found:** 2026-08-19
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $150,000–$206,000 CAD annually
- **Location/Remote:** Remote, Canada
- **Days in Office:** 0 (Remote)
- **Flags:** Full-time only (no contract path stated); no explicit Azure mentioned

## Fit Score: 7

Strong tooling overlap: Kubernetes, Terraform, ArgoCD, JFrog Artifactory, and Jenkins are named directly — an almost one-to-one match with the Artifactory/Kubernetes/ArgoCD platform work delivered at Desjardins. Salary is above Marc's $160K target. The AI/LLM platform framing (deployment pipelines for models/prompts) is a layer on top of standard DevOps fundamentals rather than a replacement for them, so the core skill fit is high even though it's a full-time role rather than a contract.

## Resume Delta

- Lead with the Desjardins JFrog Artifactory bullet almost verbatim — this posting names Artifactory explicitly as part of their pipeline/artifact management stack.
- Emphasize the Kubernetes/ArgoCD on-demand provisioning work from Desjardins — directly matches their "containerized deployments using Kubernetes, Terraform, ArgoCD" requirement.
- Highlight Jenkins pipeline experience from Tink to cover their Jenkins mention.
- Note Python scripting depth (FastAPI health-monitoring service at Desjardins) against their Python/Go/Groovy automation requirement.
- Mention Dynatrace/Splunk observability work as a parallel to their Grafana/OpenSearch/Prometheus monitoring ask.

## Draft Cover Letter

Hi D-Wave Systems team,

I'm applying for the Senior AI DevOps Developer role. My most recent contract at Desjardins is a close match for this position's core stack: I hardened and operationalized their enterprise JFrog Artifactory platform, automated on-demand environment provisioning using Kubernetes and ArgoCD, and built a Python/FastAPI service that tested ~250 Artifactory repositories every 4 hours, publishing results to Dynatrace dashboards — directly relevant to the artifact management, containerized deployment, and observability responsibilities in this role.

I bring nearly 18 years of DevOps and platform engineering experience across financial services and energy, with deep CI/CD, Terraform, and Kubernetes/ArgoCD expertise, plus Python scripting for automation and internal tooling. I'm comfortable extending that foundation into AI/LLM platform operations given the strong overlap in deployment pipeline and observability fundamentals.

I'm incorporated in Canada, fully bilingual (French/English), and available to start quickly.

Best regards,
Marc Berthelette

## Rejection Note

**2026-08-23:** Original scoring undersold the AI/LLM requirements as "a layer on top of standard DevOps fundamentals." Re-checked the full posting — required qualifications include hands-on production LLM application experience, RAG/embeddings/vector search, and AWS Bedrock/AgentCore/MCP/ACP. This is genuine, deep AI-engineering depth Marc doesn't have (his AI exposure is using AI-assisted tooling in his own workflow, not building production LLM/RAG systems) — a real gap, not a soft skill mismatch.
