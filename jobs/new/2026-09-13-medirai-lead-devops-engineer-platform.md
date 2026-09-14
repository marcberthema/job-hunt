# Lead DevOps Engineer, Platform — MedirAI

- **Source:** https://ca.indeed.com/jobs?q=DevOps+Engineer&l=Remote&vjk=38b0681a67c10383
- **Found:** 2026-09-13
- **Engagement type:** Full-time employee (Permanent)
- **Rate/Salary (stated):** $115,000–$160,000 CAD/year
- **Location/Remote:** Canada, Remote (10-person team building a European clinical AI platform, operated from Canada under a European data-residency boundary)
- **Days in Office:** 0 (Remote)

## Fit Score: 6

**Correction (2026-09-13, post-filing):** the original version of this score overstated Marc's
Kubernetes depth — he has used Kubernetes/ArgoCD for automation/provisioning (Desjardins'
Artifactory environment spin-up), but has never personally owned a cluster at the node-pool/
capacity/upgrade/restore-drill level this posting explicitly wants ("not 'has deployed to
Kubernetes' — you ran a cluster other people depended on"). That's a real, acknowledged gap, not
just an AWS-vs-Azure cloud mismatch.

What genuinely does transfer: 15+ years of critical-path infrastructure ownership on VMware
vSphere at SOVO (zero-downtime server relocation, eliminating single points of failure) — the
same conceptual muscle (capacity planning, host/node maintenance without dropping workloads, being
the one paged when it breaks) that this role wants, just on Kubernetes' conceptual ancestor rather
than Kubernetes itself. Combined with the established pattern across 18 years of entering
unfamiliar systems with zero prior experience and making them production-solid (Oracle/Salesforce/
Databricks at Énergir, AWS at Tink), this is a legitimate case to make — but it's a bet on ramp
speed, not an existing checkbox match. The posting's own tone ("there is no team beneath you
initially") signals they're not staffed for a learning curve, so this should be pitched as "here's
the gap, here's why I still think I close it fast" — not as a request for onboarding runway.

Other flags unchanged: their cloud is **AWS at account level** (IAM, KMS, networking) — Marc's
deepest cloud is Azure, and his only AWS experience is the ~6-month Tink migration (no prior AWS
background, built by hand without Terraform, cancelled before cutover). Company-risk flag: 10-
person startup with a first clinical pilot this autumn — no bench pay, no safety net, solo
2-person on-call rotation — worth weighing against the family-stability goal behind the current
search, even though the role itself is an excellent values/ownership-style match.

## Resume Delta

- Lead with the vSphere-era critical-infrastructure ownership at SOVO (zero-downtime server
  relocation, eliminating single points of failure across the fleet) as the honest analogue to
  "ran a cluster other people depended on" — not a Kubernetes claim, a critical-path-ownership
  claim.
- State plainly that Kubernetes/ArgoCD experience (Desjardins' Artifactory provisioning) is real
  but automation/provisioning-level, not node-pool/capacity/upgrade ownership — don't blur this
  line, MedirAI's posting specifically screens for people who overstate "deployed to Kubernetes"
  as "ran a cluster."
- Use the pattern across 18 years of entering unfamiliar systems with zero prior experience and
  making them production-solid (Oracle/Salesforce/Databricks at Énergir, AWS at Tink) as the case
  for ramp speed — this is the actual argument being made, not a claim of existing K8s depth.
- Cite the Tink on-call rotation (24/7, all production systems) and the self-healing Elasticsearch
  remediation script as direct evidence of "carried a production pager, can walk an incident end
  to end."
- Mention Terraform/Ansible IaC practice from Énergir for the "plan-review-apply discipline"
  requirement, and note AWS depth is lighter than Azure — don't overstate it.
- Do not claim formal production-database backup/restore drills or Kubernetes-specific cluster
  ownership anywhere in the application — both are real gaps, acknowledged directly in the cover
  letter below rather than glossed over.

## Draft Cover Letter

Their stated application process bypasses forms entirely — they want a direct email to
tech@medirai.com with "a few lines on one cluster you were responsible for: what it ran, who
depended on it, and the worst night you had with it." Marc's confirmed direction (2026-09-13):
lead with the honest gap, not a request for learning runway — their own posting explicitly screens
out that framing ("there is no team beneath you initially"). Final version:

Hi MedirAI team,

I haven't owned a Kubernetes cluster directly — I've used Kubernetes/ArgoCD for automation and
provisioning (built the system that spins up on-demand Artifactory environments for Desjardins),
but not at the node-pool/capacity/upgrade level you're describing. What I have owned, for over 15
years, is critical-path infrastructure where I was the one paged when it broke: at SOVO, I ran a
zero-downtime server relocation and eliminated single points of failure across the fleet running
on VMware vSphere — Kubernetes' conceptual ancestor for a lot of what you're describing (resource
scheduling, host maintenance without dropping the workload, capacity planning under real
constraints).

The pattern across my 18 years is entering unfamiliar systems with no prior experience and making
them production-solid — Oracle, Salesforce, and Databricks pipelines at Énergir, AWS
infrastructure at Tink, all with zero background going in. I'd rather tell you the
Kubernetes-specific gap directly than pretend it isn't there, and let that track record speak to
whether I can close it fast enough to be useful.

Best,
Marc Berthelette
