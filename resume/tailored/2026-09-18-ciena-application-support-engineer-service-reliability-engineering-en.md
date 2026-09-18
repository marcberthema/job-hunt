# Marc Berthelette

**Application Support Engineer · Service Reliability Engineering · Enterprise Platform Automation**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual French and English · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior reliability and infrastructure engineer with 18 years of experience designing reliable systems, leading incident response, and automating operational toil. Direct, current experience with Salesforce (CLI-based delivery rebuild), MuleSoft, and ServiceNow — the enterprise application platforms this role names as a strength. Drives root-cause analysis and MTTR reduction across 70+ applications at Énergir; built Dynatrace-published health monitoring and Splunk configuration-drift alerting at Desjardins. Built self-healing automation at Tink that eliminated a recurring on-call page. The differentiator is judgment: fixes root causes instead of patching over them.

## Technical Skills

| Category | Technologies and Practices |
|---|---|
| **Reliability Engineering** | Root-cause analysis, MTTR reduction, incident management, proactive monitoring, automated remediation, self-healing automation |
| **Enterprise Application Platforms** | Salesforce (CLI delivery, validation pipelines), MuleSoft, ServiceNow (change management), JFrog Artifactory |
| **Observability & Monitoring** | Dynatrace, Splunk, ELK Stack, health-check telemetry, dashboards, alerting |
| **Automation & Scripting** | Python, FastAPI, Bash — scripted validation, remediation, and configuration-drift detection |
| **Infrastructure as Code** | Terraform, Ansible, Puppet |
| **Cloud & CI/CD** | Microsoft Azure (production, 5–10 service migrations led), AWS (hands-on build, see Work Experience), Azure DevOps, GitHub Actions, Jenkins |
| **Systems** | Red Hat Linux, CentOS, Rocky Linux, Ubuntu, SQL, NoSQL |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Rebuilt Salesforce delivery with no prior Salesforce experience — replaced legacy ANT deployment scripts with the official Salesforce CLI tooling and built a validation pipeline testing every candidate merge in a sandbox, cutting missed deployment windows from a recurring problem to a single miss since launch.
- Standardized CI/CD delivery across nine distinct runtimes including MuleSoft, for 12 application teams and 70+ applications, entering most ecosystems with no prior experience.
- Drove root-cause analysis on critical production incidents and built proactive monitoring, dashboards, alerts, and automated remediation that reduced MTTR.
- Ran production change and release governance through ServiceNow across all 12 teams.

**Key technologies:** Salesforce, MuleSoft, ServiceNow, Microsoft Azure, Terraform, Ansible, Python, Dynatrace, Splunk

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement alongside the Énergir role*

- Designed and built a Python/FastAPI service that tested the health and configuration of ~250 enterprise JFrog Artifactory repositories every 4 hours, publishing operational telemetry to Dynatrace.
- Built Splunk alerting to detect manual configuration changes made outside the CI/CD pipeline, improving auditability and reducing incident risk.
- Extended the engagement past its original scope by building the validation logic tool-agnostic and the test set configurable.
- Automated provisioning of on-demand Artifactory environments with Kubernetes and ArgoCD.

**Key technologies:** Python, FastAPI, JFrog Artifactory, Dynatrace, Splunk, Kubernetes, ArgoCD

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Built a self-healing response for a recurring, unstable Elasticsearch cluster — monitoring detected when the service became unresponsive and automatically triggered a Bash remediation script, eliminating a recurring human page.
- Drove down 24/7 on-call frequency via root-cause analysis and prevention — from roughly one page every 2 rotations to one every 4–5 by the end.
- Built the compute, caching, and database layers of a client's full AWS migration target environment — EC2, S3, Route 53, self-managed memcached, serverless relational database — with no prior AWS experience; the client cancelled the migration before cutover.
- Centralized Jenkins Pipeline as Code across 10–15 developers maintaining 80+ applications for 20+ clients.

**Key technologies:** ELK Stack, Bash, AWS (EC2, S3, Route 53, VPC), Jenkins, Puppet, Spacewalk

### SOVO Technologies — Lead Technician to Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned company IT infrastructure, delivered a zero-downtime server relocation, and served as the final QA gate before production releases.
- Wrote production software for approximately seven years before the title formalized it.

**Key technologies:** C++, Java, SQL, Windows Server, VMware vSphere

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure, Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
