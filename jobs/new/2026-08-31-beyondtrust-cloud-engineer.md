# Cloud Engineer — BeyondTrust

- **Source:** https://builtin.com/job/cloud-engineer/10915515
- **Found:** 2026-08-31
- **Engagement type:** Full-time
- **Rate/Salary (stated):** Not stated
- **Location/Remote:** Remote (2 locations listed)
- **Days in Office:** 0 (Remote)

## Fit Score: 6

Strong multi-cloud infrastructure fit — AWS networking (VPC, Transit Gateway), Terraform IaC,
GitHub Actions CI/CD with self-hosted runners, and identity/access governance all map onto Marc's
Énergir and Tink experience. Note: Marc already applied to a different BeyondTrust posting (Staff
Site Reliability Engineer, filed 2026-08-28) — this is a distinct, more junior-scoped role
("Mid-level," 2+ years minimum) at the same company, not a duplicate, but applying to two roles at
one employer simultaneously is worth flagging before submitting. One real gap: the posting states
"AWS cloud certification required" as a core requirement — Marc has no AWS certification, only
hands-on build experience from Tink (~6 months, by-hand provisioning, cancelled before cutover).
That's a genuine screening risk on a mid-level role where a named cert is explicitly required, not
just preferred.

## Resume Delta

- Lead with the Tink AWS build (EC2, S3, Route 53, VPC, memcached, serverless relational DB) —
  answer the AWS networking/VPC requirement honestly, stating the by-hand caveat and cancellation
  per profile guidance. Do not claim AWS certification.
- Emphasize Terraform IaC and GitHub Actions CI/CD depth from Énergir and the Desjardins contract.
- Use the identity/governance angle from the Salesforce CLI migration and validation-sandbox gate
  at Énergir as evidence of access-control and compliance-minded delivery.
- Flag in the cover letter or application notes that Marc doesn't hold an AWS certification —
  offer the SAA (Solutions Architect Associate) as a parked but planned cert goal if asked, per
  the certification roadmap in profile.md — don't overclaim readiness.
- Surface the "already applied to a different BeyondTrust role" fact to Marc before submitting —
  his call whether to pursue both.

## Draft Cover Letter

Hi BeyondTrust team,

Your Cloud Engineer role — multi-account AWS/Azure/GCP infrastructure, Terraform-driven IaC, and
GitHub Actions CI/CD with self-hosted runners — lines up closely with the modernization work I led
at Énergir, where I migrated 5–10 mission-critical services to Azure and standardized Terraform/
Ansible provisioning across environments to cut configuration drift.

On the AWS side specifically: I built a client's full AWS migration target environment at Tink —
EC2, S3, Route 53, VPC, self-managed memcached, and a serverless relational database — over about
six months, with no prior AWS experience going in. That engagement was cancelled by the client
before cutover, and the resources were provisioned by hand rather than through Terraform, so I
want to be direct about that scope rather than overstate it. I don't currently hold an AWS
certification, though it's on my near-term roadmap.

I'd welcome a conversation about where the role's governance and CI/CD priorities sit today.

Best,
Marc Berthelette
