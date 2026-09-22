# Marc Berthelette

**Senior Platform Engineer · SRE · Linux Automation · Developer Infrastructure**

Smiths Falls, ON, Canada · Montréal Hybrid · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual: French (native) · English (fluent) · Available immediately

---

## Professional Summary

Senior platform and DevOps engineer with 18 years across infrastructure and software engineering. Built automation and internal platforms for 600+ Linux servers, standardized CI/CD across 80+ applications at Tink and 70+ applications at Énergir, and delivered Python platform tooling for 250 enterprise artifact repositories at Desjardins. Deep practice in Linux, Python, Bash, Puppet, Ansible, Terraform, CI/CD, observability, incident response, and automated remediation, with hands-on Kubernetes and ArgoCD infrastructure automation in financial services. Takes ownership of the whole operational problem and builds durable, self-service solutions rather than isolated scripts.

## Core Expertise

| Category | Focus |
|---|---|
| **Linux Platform Engineering** | Linux administration and troubleshooting, fleet lifecycle automation, Puppet, Spacewalk, Bash, automated patching and remediation |
| **Infrastructure Automation** | Terraform, Ansible, Puppet, Kubernetes, Docker, ArgoCD, Microsoft Azure, AWS |
| **Developer Infrastructure** | Internal platform tooling, Python/FastAPI APIs, CI/CD, pipeline-as-code, self-service workflows, artifact management |
| **Observability & Reliability** | Dynatrace, Splunk, ELK, metrics/logging/alerting, incident response, RCA, MTTR reduction, 24/7 on-call |
| **Programming & Systems** | Python, FastAPI, Bash, C++, Java, SQL, NoSQL, Red Hat Linux, CentOS, RockyOS, Ubuntu |

## Work Experience

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Automated OS-level patching and kernel-update reboots across 600+ Linux servers, reducing the process to a monthly verification check with near-zero downtime.
- Managed fleet configuration declaratively through Puppet and Spacewalk after VM provisioning, eliminating hand-tuned configuration and package state across the estate.
- Centralized Jenkins Pipeline as Code for 10–15 developers maintaining 80+ applications for 20+ clients, standardizing delivery across heterogeneous stacks and improving release visibility through Jira.
- Conceived and built an internal software-inventory platform cataloguing every installed application and version across the fleet, exposing CVE, end-of-life, and SSL/TLS risks directly to product owners.
- Built centralized ELK log aggregation and an automated self-healing response for a recurring Elasticsearch failure, removing the need for human intervention; participated in the 24/7 on-call rotation.
- Built the compute, caching, database, DNS, and network layers of an AWS migration target using EC2, S3, Route 53, VPC, self-managed memcached, and a serverless relational database; the client cancelled before production cutover.

**Key technologies:** Linux, Python, Bash, Puppet, Spacewalk, Jenkins, ELK Stack, PRTG, CentOS, RockyOS, VMware, AWS

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement, delivered alongside the Énergir role*

- Built a Python/FastAPI monitoring service that validated roughly 250 enterprise JFrog repositories across seven package ecosystems every four hours and published results to Dynatrace.
- Designed the validation logic and test set as reusable platform capabilities, allowing administrators to add their own cases and using the same harness to de-risk an enterprise JFrog upgrade.
- Automated provisioning of on-demand Artifactory environments with Kubernetes and ArgoCD, providing administrators with self-service infrastructure for safe testing.
- Implemented artifact lifecycle policies and Splunk alerting for configuration changes made outside the CI/CD pipeline.

**Key technologies:** Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, JFrog Artifactory, Dynatrace, Splunk, Docker, Helm

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Owned CI/CD standardization for 12 application teams and 70+ applications across nine distinct runtimes, replacing manual delivery with automated pipelines and quality gates.
- Led cloud modernization for 5–10 mission-critical services on Microsoft Azure and implemented Terraform and Ansible automation to standardize provisioning and reduce configuration drift.
- Drove RCA on critical incidents and implemented monitoring, observability dashboards, and automated remediation to reduce MTTR.
- Rebuilt Salesforce delivery with the official CLI and added a validation-sandbox merge gate, reducing a recurring missed-deployment problem to one miss since launch.
- Led adoption without reporting authority through recurring enablement sessions with all 12 application teams, turning delivered tooling into sustained developer workflows.

**Key technologies:** Microsoft Azure, Terraform, Ansible, Azure DevOps, GitHub Actions, Python, Bash, CloudFoundry, Databricks, Salesforce

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned company infrastructure, including a zero-downtime server relocation and redundant architecture eliminating single points of failure, while managing and training a technician team.
- Wrote production software for roughly seven years: a production scheduling platform, voice-recognition evaluation software, and multilingual dictionary infrastructure.

**Key technologies:** C++, Java, SQL, Windows Server, Linux, Active Directory, VMware vSphere, Cisco routing, firewall/VPN

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005

