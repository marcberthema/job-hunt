# Site Reliability Engineer — Joblet-AI

- **Source:** https://www.linkedin.com/jobs/view/4466788286/
- **Found:** 2026-09-13
- **Engagement type:** Full-time employee
- **Rate/Salary (stated):** $130,000–$200,000 (stated as "USD equivalent") + benefits
- **Location/Remote:** Remote (listing geo-tagged Greater Toronto Area, but role is fully remote)
- **Days in Office:** 0 (Remote)

## Fit Score: 7

Direct SRE/DevOps skill match: 4+ years in SRE/DevOps/infrastructure, cloud platforms (AWS/GCP/
Azure), Kubernetes, Terraform, observability tooling, SLOs/SLIs/error budgets, incident response
and post-mortems — all core to Marc's practice at Énergir/Desjardins/Tink (on-call rotation,
Dynatrace/Splunk/ELK observability, Terraform IaC). **Correction (2026-09-13, post-filing): Marc's
Kubernetes experience is using it via ArgoCD-driven GitOps automation, not owning/operating
clusters** — this posting's "hands-on with Kubernetes" is less demanding than MedirAI's explicit
cluster-ownership bar, so it's a reasonable fit, but don't oversell it as deep cluster
administration if asked directly. Fully remote removes any
location gate entirely. Compensation is unusually high ($130-200K "USD equivalent") for a Canada-
geo search — worth confirming directly whether the actual offer would be paid/leveled as a
Canadian hire or if the range is a US band applied loosely, before treating the top of it as real.
Joblet-AI is a real company (recruiting-tech startup, ~11-50 employees) hiring for their own
internal SRE seat, not a staffing pass-through — direct employer relationship, which is generally
a cleaner process than an agency-anonymized client.

## Resume Delta

- Lead with on-call/incident-response ownership: Tink's 24/7 production on-call rotation and the
  self-healing Elasticsearch remediation script are direct evidence of "lead incident response and
  post-mortem reviews" and "automate operational toil through tooling."
- Emphasize observability practice: Dynatrace/Splunk/ELK Stack work at Énergir and the Desjardins
  JFrog health-monitoring service (continuous signal across 250+ repositories every 4 hours) as
  the closest concrete analogue to "define and track SLOs, SLIs, and error budgets" — be honest
  that formal SLO/error-budget frameworks weren't explicitly named in those roles, but the
  underlying practice (continuous health signal, proactive detection) is the same discipline.
- Cite Kubernetes/ArgoCD (Desjardins) and Terraform/Ansible IaC (Énergir) for the "hands-on with
  Kubernetes, Terraform" requirement — state precisely that Kubernetes experience is via GitOps
  automation (ArgoCD), not cluster ownership/administration.
- Mention Python/FastAPI development experience (Desjardins) for the "strong scripting and
  software engineering skills (Python, Go, or similar)" line — Go itself isn't a language Marc has
  used; don't claim it.
- Frame the 18-year pattern of ramping fast on unfamiliar systems as evidence of the "curiosity to
  dig into systems and turn findings into shipped improvements" trait they're asking for.

## Draft Cover Letter

Hi Joblet-AI team,

I've spent the last several years treating reliability as a first-class engineering problem —
building the Python/FastAPI monitoring service that gave Desjardins' enterprise JFrog Artifactory
platform its first continuous health signal across 250+ repositories, and running a 24/7 on-call
rotation at an earlier role where I built a self-healing remediation script that eliminated a
recurring Elasticsearch failure from ever needing a human page again.

Your Site Reliability Engineer role — combining software engineering with operations, SLOs,
incident response, and automating away toil — matches how I've actually worked. I bring real
Kubernetes experience via ArgoCD-driven GitOps automation (not cluster ownership/administration),
deep Terraform practice, and strong observability chops (Dynatrace, Splunk, ELK) from senior
DevOps roles in regulated industries (energy, financial services), and I'm comfortable moving fast
and working asynchronously.

I'd welcome the chance to talk about what reliability looks like for your platform today, and
where the biggest toil is currently hiding.

Best,
Marc Berthelette
