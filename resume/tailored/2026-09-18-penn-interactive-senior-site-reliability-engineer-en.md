# Marc Berthelette

**Senior Site Reliability Engineer · Regulated Infrastructure · Platform Automation**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual French and English · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior site reliability and infrastructure engineer with 18 years of experience owning production infrastructure in regulated environments — financial services and energy. Led Azure cloud modernization and Terraform/Ansible IaC standardization across 12 application teams at Énergir; automated Kubernetes/ArgoCD environment provisioning at Desjardins. Drives root-cause analysis and toil reduction through automation — cut on-call paging frequency roughly in half at Tink and built self-healing remediation for a recurring production failure. Leads cross-team infrastructure work with high autonomy, outside any formal reporting line.

## Technical Skills

| Category | Technologies and Practices |
|---|---|
| **Site Reliability Engineering** | Root-cause analysis, MTTR reduction, incident response, automated remediation, self-healing automation, on-call rotation |
| **Containers & Orchestration** | Kubernetes, Docker, ArgoCD, Helm |
| **Cloud Platforms** | Microsoft Azure (production, 5–10 service migrations led), AWS (hands-on build, non-production, see Work Experience) |
| **Infrastructure as Code & CI/CD** | Terraform, Ansible, Azure DevOps, GitHub Actions, Jenkins Pipeline as Code |
| **Observability** | Dynatrace, Splunk, ELK Stack, dashboards, alerting |
| **Regulated Environments** | Financial services (Desjardins), energy utility (Énergir) — audit-driven configuration governance and compliance |
| **Programming & Automation** | Python, FastAPI, Bash, Java, SQL, NoSQL |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Led cloud modernization migrating several mission-critical services to Microsoft Azure, implementing Terraform and Ansible IaC practices that standardized environment provisioning and eliminated configuration drift across dev, staging, and production.
- Drove root-cause analysis on critical production incidents and built proactive monitoring, dashboards, alerts, and automated remediation that reduced MTTR across 12 application teams and 70+ applications, in a regulated energy-sector environment.
- Drove CI/CD and platform-engineering adoption across 12 teams outside any reporting line, leading cross-team infrastructure initiatives with high autonomy.
- Cut false-positive pipeline failures by separating application-code errors from platform-pipeline errors in reporting, reducing diagnostic toil.

**Key technologies:** Microsoft Azure, Terraform, Ansible, Python, Dynatrace, Splunk, Azure DevOps, GitHub Actions

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement alongside the Énergir role, financial services sector*

- Automated provisioning of on-demand Artifactory environments using Kubernetes and ArgoCD, giving administrators repeatable, isolated environments for safely testing configuration changes and upgrades.
- Built Splunk alerting to detect manual configuration changes made outside the CI/CD pipeline, improving auditability in a regulated environment.
- Designed and built a Python/FastAPI service that tested the health of ~250 enterprise Artifactory repositories every 4 hours, publishing telemetry to Dynatrace.

**Key technologies:** Kubernetes, ArgoCD, Helm, Python, FastAPI, Dynatrace, Splunk, GitHub Actions

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Drove down 24/7 on-call frequency via root-cause analysis and prevention — from roughly one page every 2 rotations to one every 4–5 by the end.
- Built a self-healing response for a recurring, unstable Elasticsearch cluster — monitoring detected when the service became unresponsive and automatically triggered a Bash remediation script to restart it, eliminating a recurring human page.
- Built the compute, caching, and database layers of a client's full AWS migration target environment — EC2, S3, Route 53, self-managed memcached, serverless relational database — with no prior AWS experience; the client cancelled the migration before cutover, resources provisioned by hand rather than through Terraform or CloudFormation.
- Centralized Jenkins Pipeline as Code across 10–15 developers maintaining 80+ applications for 20+ clients.
- Managed fleet configuration as code via Puppet and Spacewalk across 600+ servers.

**Key technologies:** AWS (EC2, S3, Route 53, VPC), ELK Stack, Bash, Jenkins, Puppet, Spacewalk

### SOVO Technologies — Lead Technician to Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned company IT infrastructure, delivered a zero-downtime server relocation, and introduced redundancy that eliminated single points of failure.
- Wrote production software for approximately seven years before the title formalized it.

**Key technologies:** C++, Java, SQL, Windows Server, VMware vSphere

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure, Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
