# Senior DevOps/Platform Engineer — Jitsu

- **Source:** https://builtin.com/job/senior-devops-platform-engineer/10895885
- **Found:** 2026-08-31
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $120K–$147K annually
- **Location/Remote:** 31 locations listed; Emeryville, CA (HQ) — In-office or remote
- **Days in Office:** 0 (Remote option available)

## Fit Score: 5

Good technical overlap — Terraform, Kubernetes, ArgoCD/GitOps, CI/CD ownership, and SLI/SLO
definition all track Marc's Desjardins and Énergir work directly. Two flags pull it down from a
stronger score: GCP is listed as "preferred" (venue-level mismatch, not a hard gate, but Marc has
zero GCP exposure so it's a real gap if GCP work is central day-to-day), and the stated salary
($120K–$147K) sits below the $160K CAD employment target — likely USD given the California HQ,
which narrows or erases the gap, but that needs confirming before pursuing. Remote option and
genuine platform-engineering scope (not ticket execution) keep it in the "apply" range under the
lowered bar.

## Resume Delta

- Lead with ArgoCD/Kubernetes/GitHub Actions depth from the Desjardins contract — directly
  matches their GitOps + Kubernetes production requirement.
- Emphasize Terraform IaC ownership at Énergir (environment provisioning, drift reduction) for
  their "strong Terraform and Kubernetes production experience" line.
- Use the Desjardins RCA/MTTR and observability story (Dynatrace/Splunk) to answer their
  "SLI/SLO definition and incident management" requirement — frame in SRE vocabulary.
- On GCP: do not claim any experience. If asked, use the learn-cold argument (Salesforce,
  MuleSoft, Databricks, Spark, CloudFoundry, Oracle at Énergir; AWS at Tink) rather than
  implying GCP exposure.
- Confirm currency on the stated salary range before any interview — it likely reads low in CAD
  terms only if misread as CAD.

## Draft Cover Letter

Hi Jitsu team,

Your Senior DevOps/Platform Engineer role — owning CI/CD, GitOps, and Kubernetes operations for
a high-volume logistics platform — lines up closely with what I did at Desjardins over the past
six months: I designed a Python/FastAPI service that continuously validated ~250 Artifactory
repositories and, using Kubernetes and ArgoCD, automated on-demand environment provisioning for
safe testing of platform upgrades.

The habit that differentiates my work is delivering more than the literal ask when it's the
right call for the client. Asked at Desjardins simply to verify repository configuration, I built
the validation logic tool-agnostic and configurable rather than JFrog-specific — the same harness
then became the regression-safety net for their enterprise Artifactory version upgrade. I bring
that same "what's actually best here" instinct to infrastructure reliability work.

I don't have production GCP experience — my cloud depth is in Azure, with hands-on AWS build
experience from an earlier engagement — but I've repeatedly picked up unfamiliar platforms cold
under a delivery clock (Salesforce, MuleSoft, Databricks, Spark, Kubernetes, ArgoCD among them),
and I'd expect the same here if that's part of the role.

Happy to walk through the Desjardins and Énergir work in more detail.

Best,
Marc Berthelette
