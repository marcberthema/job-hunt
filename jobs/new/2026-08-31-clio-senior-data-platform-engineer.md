# Senior Data Platform Engineer — Clio

- **Source:** https://builtin.com/job/senior-data-platform-engineer/10836218
- **Found:** 2026-08-31
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $157,300–$212,800 CAD annually
- **Location/Remote:** Canada (Burnaby, Calgary, or Toronto hubs; 3 locations) — In-office or
  remote (minimum 2 days/week on-site stated for local candidates at hub offices)
- **Days in Office:** Not stated for remote hires; 2/week (Hybrid) for local hub candidates

## Fit Score: 7

Strong pay match ($157K–$213K CAD, right at Marc's $160K target) and real infrastructure-platform
overlap — ELK/OpenSearch, Kafka/Kinesis streaming, Terraform, Kubernetes, and multi-cloud storage
(AWS S3, Azure Data Lake, GCS) all track Marc's observability and IaC background closely, even
though the role leans more data-platform/logging-infrastructure than classic CI/CD DevOps. None of
Clio's three hub cities (Burnaby, Calgary, Toronto) are in Marc's reachable-city list, so this
only scores well because the remote option appears open to non-local hires — if it turns out
Vancouver/Calgary/Toronto residency is actually required, this drops into the hard-gate on-site
range regardless of skill fit. Worth filing to confirm remote eligibility, not a slam-dunk yet.

## Resume Delta

- Lead with the ELK Stack build at Tink (centralized log aggregation, proactive anomaly
  detection) — direct precedent for their "architecting ELK and OpenSearch environments" ask.
- Emphasize Terraform/Kubernetes and multi-cloud exposure (Azure primary, AWS build experience at
  Tink) against their AWS S3 / Azure Data Lake / GCS storage requirement — note GCS/GCP is listed
  alongside AWS/Azure as one option among several, not GCP-primary, so no hard-gate applies.
  Never imply GCP experience beyond "one of several supported backends."
- Highlight the Desjardins Artifactory monitoring service (Dynatrace dashboards, 4-hour health
  checks across 250 repos) as evidence of building production observability/data-pipeline
  tooling, not just consuming it.
- Flag clearly in any application: confirm whether remote candidates are truly exempt from the
  2-day/week hub requirement before assuming full remote eligibility.

## Draft Cover Letter

Hi Clio team,

Your Senior Data Platform Engineer role — building out ELK/OpenSearch logging infrastructure,
streaming data pipelines, and the IaC underneath them — overlaps closely with work I've done at
two different employers: I built centralized ELK-based log aggregation at Tink for a 600+ server
fleet, and more recently designed and shipped a Python/FastAPI monitoring service at Desjardins
that gave 250 enterprise Artifactory repositories their first continuous, dashboarded health
signal.

A pattern shows up across my last three roles: given a narrow, specific ask, I tend to deliver
something structurally larger because it's the right call for the client, not just the cheapest
path to close the ticket. At Tink, nobody asked for a fleet-wide software inventory platform — I
built one anyway, because product owners had no visibility into their CVE exposure or EoL
software risk. I'd bring that same instinct to Clio's data platform.

I'd also want to confirm early how the 2-day/week hub-office expectation applies to remote hires
outside Burnaby, Calgary, and Toronto, since I'm based in Smiths Falls, ON.

Best,
Marc Berthelette
