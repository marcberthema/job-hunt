# Marc Berthelette

**Senior Engineer · Python Pipelines & Validation Tooling · Infrastructure Automation**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual: French (native) · English (fluent) · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior engineer with 18 years of experience, including roughly seven years writing production software before moving into DevOps and platform engineering. Builds and maintains the Python pipelines and infrastructure that other teams depend on, and is known for judgment about quality: separating real failures from noise, building validation harnesses that tell a team whether something is actually correct, and explaining why a result is good or needs improvement. At Desjardins, designed a Python/FastAPI service that validated roughly 250 enterprise repositories every four hours across seven package ecosystems, with a configurable test set that became the regression safety net for a major platform upgrade. At Énergir, introduced AI-assisted engineering with scope gates and human-validation checkpoints before generated code ships. Works well in ambiguous, fast-moving environments with a strong bias toward shipping, and communicates clearly in writing and in conversation.

## Technical Skills

| Category | Technologies |
|---|---|
| **Programming and Pipelines** | Python, FastAPI, Bash, Java, C++, SQL, NoSQL, REST services, data and validation pipelines, operational automation |
| **Quality and Validation** | Automated validation harnesses, configurable test sets, regression safety nets, pipeline quality gates, failure triage (application vs. platform), root-cause analysis |
| **AI-Assisted Engineering** | Scoped AI-assisted development, human-validation checkpoints, review criteria for generated code before promotion |
| **CI/CD and Developer Tooling** | GitHub Actions, Azure DevOps, Jenkins Pipeline as Code, Git, reusable pipelines |
| **Infrastructure and Cloud** | Microsoft Azure, Terraform, Ansible, Kubernetes, ArgoCD, Docker, Linux |
| **Observability** | Dynatrace, Splunk, ELK Stack, incident response, automated remediation |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Owned CI/CD for 12 application teams and 70+ applications across nine runtimes, entering most of those ecosystems with no prior experience and reverse-engineering each before automating it.
- Cut false-positive pipeline failures by separating application-code errors from platform errors in reporting, so each team could tell at a glance whether a failure was theirs to fix.
- Built a Salesforce validation pipeline that deploys every candidate merge into a sandbox and runs the full test suite, reducing missed deployment windows from a recurring problem to a single miss since launch.
- Introduced AI-assisted engineering practices with researched scope gates and human-validation checkpoints before any AI-generated code reaches production, and raised the absence of equivalent organizational safeguards with leadership.
- Drove adoption of the delivered tooling across 12 teams outside any reporting line through recurring enablement sessions.

**Key technologies:** Python, Microsoft Azure, Azure DevOps, GitHub Actions, Terraform, Ansible, Java, Node.js, Spark, Databricks, Salesforce

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement, delivered alongside the Énergir role*

- Designed and built a Python/FastAPI service that tested the configuration of about 250 remote repositories across Docker, Helm, Node.js, Maven, Python, NuGet, and Debian every four hours and published the results to Dynatrace dashboards.
- Extended the request well past its original scope by making the validation logic tool-agnostic and the test set configurable, so administrators could add their own cases; the same harness then served as the regression safety net for an enterprise platform upgrade.
- Automated on-demand test environments with Kubernetes and ArgoCD so changes could be validated safely before reaching production.
- Built Splunk alerting for configuration changes made outside the approved pipeline and implemented lifecycle policies that reduced storage overhead.

**Key technologies:** Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk, Docker, Helm

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Conceived and built, unprompted, a software inventory platform cataloguing every application and version across a 600+ server fleet, surfacing CVE exposure, end-of-life software, and SSL/TLS risk to product owners who previously had no visibility.
- Centralized Jenkins Pipeline as Code for 80+ applications serving 20+ clients, standardizing pipeline steps across technology stacks.
- Automated OS patching and kernel-update reboots across the fleet, reducing the process to a monthly verification check with near-zero downtime.
- Built a self-healing response for an unstable Elasticsearch cluster: monitoring detected the failure and triggered an automatic restart instead of paging a person.

**Key technologies:** Python, Bash, Jenkins, Puppet, ELK Stack, Linux, Jira

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Wrote production software for roughly seven years alongside infrastructure work, including a production scheduling system, a voice recognition evaluation system, and multi-language dictionary infrastructure.
- Served as the final QA gate before any software release reached production.
- Owned company IT infrastructure, including a zero-downtime server relocation and redundant architecture that removed single points of failure.

**Key technologies:** C++, Java, SQL, Linux, Windows Server

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
