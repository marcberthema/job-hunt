# Software Developer & DevOps Engineer (Elite FinTech Firm, via Hunter Bond) — Hunter Bond

- **Source:** https://www.linkedin.com/jobs/view/4464755557/
- **Found:** 2026-09-13
- **Engagement type:** Full-time employee
- **Rate/Salary (stated):** $140,000–$180,000 CAD/year + Bonus
- **Location/Remote:** Montreal, QC — Hybrid (days/week not stated in posting)
- **Days in Office:** Not stated (Hybrid) — confirm before proceeding far, since profile.md's
  onsite-frequency rule can't be applied without this

## Fit Score: 7

Strong direct skill match against an anonymized "Elite FinTech Firm" client (posted via
staffing/recruitment firm Hunter Bond): Python, Terraform/Ansible/Puppet, CI/CD, Docker,
Prometheus, and specifically "strong Kubernetes (ideally Rancher)." **Correction (2026-09-13,
post-filing): Marc's Kubernetes experience is using it — via ArgoCD-driven GitOps automation at
Desjardins/Énergir — not owning or operating clusters (no node-pool/capacity/upgrade ownership).**
The posting's "strong Kubernetes" bar is somewhat ambiguous on which depth it means; don't assume
it's satisfied without being upfront about the use-vs-own distinction. Rancher itself is not owned
either — Rancher bundles its own GitOps tool (Fleet) that covers similar ground to ArgoCD, so the
GitOps half of Rancher is a reasonable analogy, but Rancher's broader multi-cluster management/UI
layer is unfamiliar. Montreal is fully within the reachable on-site/hybrid radius. Pay ($140-180K +
bonus) clears the on-site FTE floor comfortably. Posting language ("no red tape," "personal
projects on Fridays," "unlimited tech budget") reads as a genuine high-autonomy engineering culture
pitch rather than corporate boilerplate — matches the kind of ownership-heavy environment Marc
does well in. Main unknown: hybrid days/week aren't stated — worth clarifying with the recruiter
(Robin Wells, Team Leader - Infrastructure at Hunter Bond) before going deep on this one.

## Resume Delta

- Lead with CI/CD ownership (unambiguous strength): Énergir's CI/CD standardization across nine
  runtimes for 12 teams maps directly onto "building CI/CD pipelines for a scale rarely seen
  elsewhere."
- State Kubernetes experience precisely: used via ArgoCD-driven GitOps automation at Desjardins/
  Énergir — real, but automation/provisioning-level, not cluster ownership/operation. Don't let
  "working heavily with Kubernetes" in the posting imply more than that.
- Emphasize Terraform/Ansible IaC practice from Énergir for the Terraform/Ansible/Puppet
  requirement — Puppet itself is a real match too (Tink's fleet configuration management).
- Cite Python scripting from the Desjardins FastAPI monitoring service for the "knowledge of
  programming (ideally Python)" line.
- Mention observability/monitoring practice (Dynatrace, Splunk, ELK at Énergir) as adjacent to
  Prometheus even though Prometheus itself isn't a direct tool match — be honest that the specific
  tool is new but the observability discipline isn't.
- Don't claim Rancher experience or deep Kubernetes ownership — if it comes up, state plainly:
  real GitOps/CI-CD experience with Kubernetes as the deployment target, no cluster
  administration, no Rancher.

## Draft Cover Letter

Hi Robin,

I have real hands-on Kubernetes experience — using it via ArgoCD-driven GitOps automation at
Desjardins and Énergir — though I haven't owned or operated clusters directly. I do have deep
Terraform, Ansible, and CI/CD practice from those same roles, including standardizing CI/CD
delivery across nine runtimes for a dozen application teams at Énergir. I haven't used Rancher
specifically, though ArgoCD covers similar GitOps ground to Rancher's Fleet.

The Software Developer & DevOps Engineer role for your FinTech client caught my attention — a
zero-downtime, low-latency infrastructure problem with real ownership and no red tape is exactly
the kind of work I look for. I'm based close enough to Montreal for the hybrid schedule and
available to start immediately.

I'd welcome the chance to discuss the role in more detail, including the on-site cadence.

Best,
Marc Berthelette
