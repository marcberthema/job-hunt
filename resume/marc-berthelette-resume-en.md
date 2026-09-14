# Marc Berthelette

**Senior / Staff SRE · Platform Engineering · DevOps · Reliability**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual: French (native) · English (fluent) · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior DevOps engineer who takes ownership of production systems other people are hesitant to touch — learns them cold under a delivery deadline, then replaces manual and fragile processes with automation that holds. Given a narrow scope three times, at three employers, over eight years — and each time delivered something structurally larger than what was asked: an unprompted fleet-wide security-visibility platform at Tink, a Salesforce CLI migration at Énergir that also made bad deployments structurally unable to reach production, and a JFrog validation harness at Desjardins that ended up de-risking the platform's own version upgrade. Deep Microsoft Azure, Terraform, Kubernetes, and observability practice in regulated sectors (energy, financial services), built while standardizing CI/CD for 12 application teams. The differentiator is judgment, not tool count: fixes root causes instead of patching over them, and recommends the right answer rather than the cheapest one.

## Core Expertise

| Category | Focus |
|---|---|
| **Reliability & Production Engineering** | Root cause analysis, MTTR reduction, proactive monitoring & alerting, incident response, automated remediation, 24/7 on-call |
| **Platform Engineering & Enablement** | CI/CD standardization across heterogeneous stacks, pipeline-as-code, internal developer tooling, cross-team enablement without reporting authority |
| **Infrastructure & Cloud Automation** | Microsoft Azure, Terraform, Ansible, Puppet, Kubernetes, Docker, ArgoCD |
| **CI/CD & Artifact Management** | Azure DevOps, GitHub Actions, Jenkins, JFrog Artifactory, Nexus, CloudFoundry |
| **Observability** | Dynatrace, Splunk, ELK Stack (Elasticsearch, Logstash, Kibana) |
| **AI-Assisted Engineering** | Scoped/gated AI-assisted development, human-validation checkpoints, risk assessment of generated-code promotion |
| **Programming & Systems** | Python, FastAPI, Bash, C++, Java, SQL, NoSQL, Red Hat Linux, Ubuntu, Apache, Nginx |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Owned CI/CD standardization for 12 application teams and 70+ applications across nine distinct runtimes — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, and Databricks — entering most of those ecosystems with no prior experience; took the Oracle team from fully manual deployment to automated delivery after an earlier attempt had failed.
- Rebuilt Salesforce delivery with no prior Salesforce experience — replacing legacy ANT scripts with the official Salesforce CLI tooling and building a validation pipeline that tests every candidate merge in a sandbox — cutting missed deployment windows from a recurring problem to a single miss since launch, with a dependable every-other-Tuesday cadence.
- Cut false-positive pipeline failures by separating application-code errors from platform-pipeline errors in reporting, and led cloud modernization migrating 5–10 mission-critical services to Microsoft Azure with Terraform/Ansible IaC to eliminate configuration drift.
- Drove root cause analysis on critical production incidents and built the proactive monitoring, dashboards, and automated remediation that reduced Mean Time to Recovery (MTTR) across the application estate.
- Introduced AI-assisted engineering practices over the past 6–9 months with researched scope gates and human-validation checkpoints before any AI-generated code ships — and flagged to leadership that the organization has no equivalent safeguards.
- Drove CI/CD and platform-engineering adoption across 12 teams outside any reporting line, running recurring enablement sessions (~6/year) with each application team after pipeline delivery — turning delivered tooling into actual usage rather than shelfware.

**Key technologies:** Microsoft Azure, Azure DevOps, GitHub Actions, Terraform, Ansible, Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks, Data Lake, ServiceNow, IaC

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement, delivered alongside the Énergir role*

- Delivered a 6-month engagement hardening the enterprise JFrog Artifactory platform, building a Python/FastAPI service that tested the configuration of ~250 remote repositories across seven package ecosystems every 4 hours, publishing to Dynatrace.
- Extended the engagement well past its original scope by building the validation logic tool-agnostic and the test set configurable, so administrators could cover their own cases; the same harness then de-risked the enterprise JFrog version upgrade.
- Automated provisioning of on-demand Artifactory instances with Kubernetes and ArgoCD, letting administrators spin up fully configured environments for safe testing.
- Implemented artifact lifecycle policies to enforce retention and reduce storage overhead; built Splunk alerting for manual configuration changes made outside the CI/CD pipeline.

**Key technologies:** JFrog Artifactory, Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk, Docker, Helm, Maven, NuGet, Debian

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code across a team of 10–15 developers maintaining 80+ applications for 20+ clients, standardizing pipeline steps across tech stacks and adding release visibility via Jira.
- Automated OS-level patching (including kernel-update reboots) across 600+ servers, reducing it to a monthly verification check with near-zero downtime, fleet configuration driven declaratively through Puppet and Spacewalk; added centralized ELK log aggregation.
- Built the compute, caching, and database layers of a client's AWS migration target environment — EC2, S3, Route 53, VPC, self-managed memcached, serverless database — with no prior AWS experience; the client cancelled before cutover.
- Conceived and built, unprompted, a software inventory platform cataloguing every application and version across the 600+ server fleet — surfacing CVE exposure, end-of-life software, and SSL/TLS certificate scoring directly to product owners, who until then had no visibility into the fleet's security or obsolescence risk.
- Drove down 24/7 on-call frequency via RCA and prevention — from roughly one page every 2 rotations to one every 4–5 by the end; built a self-healing response for an unstable Elasticsearch cluster so monitoring restarted it automatically instead of paging a human.

**Key technologies:** Jenkins, ELK Stack (Elasticsearch, Logstash, Kibana), Bash, Linux, Jira, Puppet, PRTG, Spacewalk, CentOS, RockyOS, NetScaler, AWS (EC2, S3, Route 53, VPC), CVE/vulnerability tracking, SSL/TLS scoring

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned all company IT infrastructure — including a zero-downtime server relocation and a redundant architecture that eliminated single points of failure — while managing a team of technicians and serving as the final QA gate before release.
- Wrote production software alongside infrastructure work for roughly seven years before the title formalized it: a production scheduling system, then a voice recognition evaluation system and multi-language dictionary infrastructure.

**Key technologies:** C++, Java, SQL, Windows Server, Linux, Active Directory, VMware vSphere, Cisco routing, firewall/VPN, backup & recovery

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
