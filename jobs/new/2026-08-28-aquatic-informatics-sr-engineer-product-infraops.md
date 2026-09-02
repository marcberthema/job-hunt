# Sr. Engineer, Product InfraOps (Remote) — Aquatic Informatics (Veralto / Hach)

- **Source:** https://www.linkedin.com/jobs/view/4444227143
- **Found:** 2026-08-28
- **Engagement type:** Full-time (employee — health benefits and RSP from day 1, 11 paid holidays, PPTO)
- **Rate/Salary (stated):** "$90,000 to 130,000 CAD/year" + bonus eligibility
- **Location/Remote:** "remote within Canada - PST working hours" (posting listed against Ontario, Canada; company HQ is Vancouver)
- **Days in Office:** 0 (Remote) — but a **30-day onsite immersion program** if selected, plus a mandatory **in-person final interview**; location not stated (HQ is Vancouver)
- **Flags:** FTE only, no consulting path; salary band tops out at Marc's $130k floor and midpoint (~$110k) is well below the $160k target; **PST working hours from Eastern Ontario** (roughly 12:00–20:00 ET); **30-day onsite immersion + in-person final interview**, likely Vancouver — travel/away-from-family cost not compensated in the posting; Kubernetes listed as a required qualification (known depth gap); on-call rotation

## Fit Score: 7

The requirement list is a close, honest match to what Marc actually does: Terraform *and* Ansible named explicitly (his exact IaC pairing at Énergir), CI/CD pipeline ownership, Python/Bash automation, observability ownership end-to-end, RCA on production incidents, and "ability to lead through influence" — which is almost a restatement of driving CI/CD adoption across 12 teams outside any reporting line. Cloud is explicitly platform-agnostic ("AWS, Azure, or GCP"), so Azure depth counts as a straight asset with no mismatch penalty. It falls short of an 8–9 on two counts: Kubernetes and container orchestration are a stated required qualification rather than a nice-to-have, which is Marc's acknowledged gap (the reason Sophos and Nango were rejected and CKA became priority #1), and the formal SRE vocabulary they lead with — SLIs, SLOs, SLAs as tracked objectives — is framing Marc hasn't used even though he's done the underlying work. Water/environmental SaaS also gives him none of the regulated-sector credibility that carries him at financial and energy shops.

**Read this one honestly before spending effort on it:** it is a salaried job at roughly $110–125k realistic, which is a large step down from $110–130/hr consulting, and it asks for a month onsite plus a permanent Pacific-hours schedule from Smiths Falls. The skill match is real; the package is the problem.

## Resume Delta

- **Lead with the Énergir IaC bullet** — Terraform and Ansible standardizing provisioning across dev/staging/prod is a literal match to their "Terraform and Ansible" requirement line; put it above the runtime-standardization bullet for this one.
- **Promote the RCA / MTTR bullet high** — their posting asks for incident response, root cause analysis, and "durable corrective and preventive actions," which is exactly how that bullet is already written.
- **Reframe the Desjardins health-monitoring service as SLI/SLO work** — a service testing ~250 repositories every 4 hours and publishing segmented health dashboards to Dynatrace *is* service-objective tracking; name it in their vocabulary (service health signal, operational metrics) rather than leaving it as "monitoring."
- **Surface Kubernetes/ArgoCD from the Desjardins bullet into the skills summary line**, since orchestration is a required qualification here — but keep it to what's true (on-demand Artifactory instance provisioning), and expect the depth question in interview.
- **Use the 12-teams-outside-any-reporting-line bullet against "lead through influence" and "mentor team members"** — this is the single strongest keyword-to-evidence match in the posting.
- **Do not lead with Azure as a differentiator** — the posting treats all three clouds as interchangeable, so Azure depth is table stakes here rather than an edge. Lead with delivery breadth instead.

## Draft Cover Letter

Hello Aquatic Informatics team,

I'm applying for the Sr. Engineer, Product InfraOps role. What caught my attention is that the posting asks for someone to own reliability and operational maturity across a platform — not to work a queue of infrastructure tickets. That distinction matters to me, and it's the kind of work I've spent the last several years doing.

At Énergir I was asked to standardize CI/CD for the application teams. Nine runtimes later — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks — I'd built pipelines for 12 teams and 70+ applications, entering most of those ecosystems with no prior experience and reverse-engineering each one before automating it. The part I'm proudest of wasn't the pipelines: it was recognizing that delivered tooling nobody adopts is shelfware, so I ran recurring enablement sessions with each team afterward, across 12 teams I had no authority over. Your "lead through influence" line is the thing I actually do.

A more recent example of the same instinct: at Desjardins I was brought in to verify that ~250 enterprise Artifactory repositories were configured correctly. I built a Python/FastAPI service that tested all of them every four hours and published segmented health dashboards to Dynatrace — but I built the validation logic tool-agnostic and the test set configurable, rather than hard-coding it to JFrog. That was more work than the ask, and it's why the same harness later became the safety net for the platform's version upgrade. My rule is to build what's best for the client, not necessarily what's cheapest.

On the technical requirements: Terraform and Ansible are my daily IaC tooling, I've built and run CI/CD across Azure DevOps, GitHub Actions, and Jenkins, and observability ownership — Dynatrace, Splunk, ELK — has been part of every role I've held, including the RCA and MTTR-reduction work at Énergir. I'm based in Smiths Falls, Ontario, and bilingual French/English.

I'd welcome a conversation.

Marc Berthelette
