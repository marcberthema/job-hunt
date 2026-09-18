# Marc Berthelette

**Senior DevOps Engineer · Infrastructure Automation · Kubernetes & AWS**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual French and English · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior DevOps engineer with 18 years of infrastructure and automation experience, including hands-on AWS build work (EC2, S3, Route 53, VPC, self-managed memcached, serverless relational database — built with no prior AWS experience, provisioned by hand, engagement cancelled before cutover) and deep, current Terraform and Kubernetes/ArgoCD practice standardizing production environments at Énergir and Desjardins. Learns unfamiliar platforms cold under a delivery deadline — demonstrated across three employers over eight years — and consistently delivers the structurally larger automation the problem actually needed, not just what was asked.

## Technical Skills

| Category | Technologies and Practices |
|---|---|
| **Infrastructure as Code** | Terraform, Ansible, Puppet, environment standardization, configuration-drift elimination |
| **Containers & Orchestration** | Kubernetes, Docker, ArgoCD — environment provisioning, automation, on-demand deployment |
| **Cloud Platforms** | Microsoft Azure (production, 5–10 service migrations led), AWS (EC2, S3, Route 53, VPC — hands-on build, non-production, see Work Experience) |
| **CI/CD** | Azure DevOps, GitHub Actions, Jenkins Pipeline as Code, Git |
| **Observability & Reliability** | Dynatrace, Splunk, ELK Stack, root-cause analysis, MTTR reduction, proactive monitoring and alerting, automated remediation |
| **Programming & Automation** | Python, FastAPI, Bash, Java, SQL, NoSQL |
| **Systems & Networking** | Red Hat Linux, CentOS, Rocky Linux, Ubuntu, NetScaler, Cisco routing, firewall/VPN administration |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Led cloud modernization migrating several mission-critical services to Microsoft Azure, implementing Terraform and Ansible IaC practices that standardized environment provisioning and eliminated configuration drift across dev, staging, and production.
- Standardized CI/CD delivery across nine distinct runtimes for 12 application teams and 70+ applications, entering most ecosystems with no prior experience and reverse-engineering each before automating it.
- Drove root-cause analysis on critical production incidents and built proactive monitoring, dashboards, and automated remediation to reduce MTTR.
- Cut false-positive pipeline failures by separating application-code errors from platform-pipeline errors in reporting.

**Key technologies:** Microsoft Azure, Terraform, Ansible, Azure DevOps, GitHub Actions, Python, Dynatrace, Splunk, IaC

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement alongside the Énergir role*

- Automated provisioning of on-demand Artifactory environments using Kubernetes and ArgoCD, giving administrators repeatable, isolated environments for safely testing configuration changes and upgrades.
- Designed and built a Python/FastAPI service that tested the configuration of ~250 enterprise Artifactory repositories every 4 hours and published results to Dynatrace.
- Extended the engagement past its original scope by building the validation logic tool-agnostic and the test set configurable.
- Built Splunk alerting to detect manual configuration changes made outside the CI/CD pipeline.

**Key technologies:** Kubernetes, ArgoCD, Python, FastAPI, GitHub Actions, Dynatrace, Splunk, Docker, Helm

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Built the compute, caching, and database layers of a client's full AWS migration target environment — EC2, S3, Route 53, self-managed memcached on EC2, and a serverless relational database — and contributed to VPC/network and Route 53 design, with no prior AWS experience. Roughly 6 months of work; resources were provisioned by hand in the AWS console, not through Terraform or CloudFormation; the client cancelled the migration before cutover.
- Managed fleet configuration as code via Puppet and Spacewalk across 600+ servers, including automated kernel-update reboots reduced to a monthly verification check with near-zero downtime.
- Centralized Jenkins Pipeline as Code across a team of 10–15 developers maintaining 80+ applications for 20+ clients.
- Built a self-healing response for a recurring, unstable Elasticsearch cluster — monitoring triggered an automated Bash remediation script instead of paging a human.
- Conceived and built, unprompted, a software inventory platform cataloguing every application and version across the 600+ server fleet, surfacing CVE exposure, end-of-life software, and SSL/TLS certificate scoring.

**Key technologies:** AWS (EC2, S3, Route 53, VPC), Puppet, Spacewalk, Jenkins, ELK Stack, Bash

### SOVO Technologies — Lead Technician to Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned company IT infrastructure, delivered a zero-downtime server relocation, and introduced redundancy that eliminated single points of failure.
- Wrote production software for approximately seven years before the title formalized it.

**Key technologies:** C++, Java, SQL, Windows Server, VMware vSphere, Active Directory

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure, Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
