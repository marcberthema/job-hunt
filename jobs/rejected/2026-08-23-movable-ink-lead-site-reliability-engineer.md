# Lead Site Reliability Engineer — Movable Ink

- **Source:** https://www.linkedin.com/jobs/view/4372005660
- **Found:** 2026-08-23
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $154,000–$200,000 CAD/year, plus potential bonus and benefits
- **Location/Remote:** Toronto, ON, Canada — remote/hybrid/on-site policy not explicitly stated in the posting
- **Days in Office:** Not stated (Toronto listed as the location with no remote designation — could be on-site)
- **Flags:** **Remote policy unconfirmed and Toronto is outside the reachable-city list (Ottawa, Kingston, Brockville, Cornwall, Montréal) per profile.md** — if this turns out to be on-site/hybrid, that's a hard red flag that caps the score at 0-4 regardless of skill fit; confirm before investing further. Separately, the required stack (Apache Pulsar, Kafka, ScyllaDB/Cassandra, Chef, NodeJS/Golang/Ruby) has essentially no overlap with Marc's documented experience; no Azure mentioned (AWS/GCP only)

## Fit Score: 3/10 (skill/domain fit — logistics noted separately above, but see the location flag, which is serious)

This is a deep distributed-systems specialist role, not a platform/DevOps generalist one — core requirements name Apache Pulsar, Kafka, ScyllaDB/Cassandra, and Grafana Loki/Thanos/Tempo at an expert level, none of which appear in Marc's documented background (Azure/AWS, Terraform/Ansible, Docker/Kubernetes/ArgoCD, Dynatrace/Splunk/ELK). Programming languages named (NodeJS, Golang, Ruby) don't match his (Bash, Python, C++, Java). Kubernetes here means advanced EKS/GKE cluster architecture and multi-tenancy design — cluster ownership Marc doesn't have (his Kubernetes experience is from the automation/provisioning and application side, not cluster architecture, as clarified in a recent review session). No Azure at all. On top of the skill mismatch, the location risk is real: Toronto is outside the reachable-city range and the posting doesn't confirm remote eligibility — if it's on-site or hybrid, profile.md's rule caps this at 0-4 outright regardless of skill fit.

## Resume Delta

- Not recommended to build a tailored application around this one — the core technical requirements (Pulsar, Kafka, ScyllaDB, Chef, Go/Ruby/Node, advanced multi-tenant Kubernetes cluster architecture) don't have a credible bridge in the documented resume.
- If pursuing anyway, the only honest angle is general SRE/incident-response leadership and IaC discipline (Terraform, on-call, RCA/MTTR work at Énergir) as transferable fundamentals — but this would be a significant stretch application, not a strong-fit one.

## Draft Cover Letter

Given the scope of the tooling gap here (Kafka/Pulsar/ScyllaDB, Chef, Go/Ruby/Node, deep multi-tenant Kubernetes cluster architecture) and the unconfirmed Toronto location, I'd recommend clarifying remote eligibility and being candid about the stack gap before drafting a tailored letter — a generic "transferable SRE fundamentals" pitch is unlikely to be competitive against candidates with direct experience in this exact distributed-systems stack.
