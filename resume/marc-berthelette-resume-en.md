# Marc Berthelette

**Senior DevOps Engineer | Platform Engineering Consultant**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual: French (native) · English (fluent) · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior DevOps and Platform Engineering consultant with 18 years spent making unfamiliar systems deliverable. At Énergir, standardized CI/CD across nine distinct runtimes — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, and Databricks — for 12 application teams and 70+ applications, entering most of those ecosystems with no prior experience and reverse-engineering each one before automating it. At Desjardins, built the Python/FastAPI service that gave 250 enterprise Artifactory repositories their first continuous health signal. Deep Microsoft Azure, Terraform, Kubernetes, and observability practice in regulated sectors (energy, financial services). Takes ownership of the whole problem — including the parts nobody assigned — and recommends the right answer rather than the cheapest one. Bilingual French/English, incorporated in Canada, available immediately.

## Technical Skills

| Category | Technologies |
|---|---|
| **Cloud & DevOps Platforms** | Microsoft Azure, Azure DevOps, GitHub Actions, Jenkins, JFrog Artifactory, Nexus, CloudFoundry |
| **Infrastructure as Code** | Terraform, Ansible, Puppet |
| **Containers & Orchestration** | Docker, Kubernetes, ArgoCD |
| **Monitoring & Observability** | Dynatrace, Splunk, ELK Stack (Elasticsearch, Logstash, Kibana), proactive alerting, incident response |
| **Programming & Scripting** | Python, FastAPI, Bash, C++, Java, SQL, NoSQL |
| **Operating Systems & Web** | Red Hat Linux, Ubuntu, Apache, Nginx |
| **Project & Collaboration** | Jira, Agile / Scrum, technical documentation, stakeholder enablement |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Standardized CI/CD delivery across nine distinct runtimes — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, and Databricks — for 12 application teams and 70+ applications, entering most of those ecosystems with no prior experience; took the Oracle team from fully manual deployment to automated delivery after an earlier attempt had failed.
- Rebuilt Salesforce delivery with no prior Salesforce experience — replacing legacy ANT scripts with the official Salesforce CLI tooling, then proposing and building a validation pipeline that tests every candidate merge in a dedicated sandbox — taking the team from missed deployment windows to a dependable every-other-Tuesday release. Later extended into an automated Salesforce-to-Data-Lake integration.
- Cut false-positive pipeline failures and made build results self-diagnosing by separating application-code errors from platform-pipeline errors in reporting — so teams could tell at a glance whose failure it was.
- Led cloud modernization initiatives, migrating 5–10 mission-critical services to Microsoft Azure, and implemented Infrastructure as Code (IaC) practices with Terraform and Ansible to standardize provisioning and eliminate configuration drift across dev, staging, and production.
- Drove root cause analysis (RCA) on critical production incidents and built the proactive monitoring, observability dashboards, and automated remediation that reduced Mean Time to Recovery (MTTR) across the application estate.
- Drove CI/CD and platform-engineering adoption across 12 teams outside any reporting line, running recurring enablement sessions (~6/year) with each application team after pipeline delivery — turning delivered tooling into actual usage rather than shelfware.

**Key technologies:** Microsoft Azure, Azure DevOps, GitHub Actions, Terraform, Ansible, Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks, Data Lake, ServiceNow, IaC

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement, delivered alongside the Énergir role*

- Delivered a 6-month engagement hardening and operationalizing the enterprise JFrog Artifactory platform, designing and building a Python/FastAPI health-monitoring service that tested the configuration of ~250 remote repositories across seven package ecosystems every 4 hours, publishing to Dynatrace with technology-segmented dashboards.
- Extended the engagement well past its original scope — verifying repository configuration — by building the validation logic tool-agnostic rather than JFrog-specific and the test set configurable, so administrators could cover their own cases; the same harness then de-risked the enterprise JFrog version upgrade.
- Automated provisioning of on-demand Artifactory instances using Kubernetes and ArgoCD, enabling system administrators to spin up fully configured corporate environments for safe testing of configuration changes and upgrades.
- Implemented artifact lifecycle policies to enforce retention standards and reduce storage overhead; built Splunk alerting to flag manual configuration changes made outside the Continuous Integration / Continuous Delivery (CI/CD) pipeline, improving auditability and compliance.

**Key technologies:** JFrog Artifactory, Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk, Docker, Helm, Maven, NuGet, Debian

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code across a team of 10–15 developers maintaining 80+ applications for 20+ clients, standardizing pipeline steps regardless of underlying tech stack and adding release visibility through Jira integration.
- Automated OS-level patching across a fleet of 600+ servers including kernel-update reboots, reducing the process to a monthly verification check with near-zero downtime, with fleet configuration driven declaratively through Puppet and Spacewalk; built centralized ELK Stack log aggregation for proactive anomaly detection.
- Built the compute, caching, and database layers of a client's full AWS migration target environment — EC2, S3, Route 53, VPC, self-managed memcached, serverless relational database — with no prior AWS experience; the client cancelled the migration before cutover.
- Conceived and built, unprompted, a software inventory platform cataloguing every application and version across the 600+ server fleet — surfacing CVE exposure, end-of-life software, and SSL/TLS certificate scoring directly to product owners, who until then had no visibility into the fleet's security or obsolescence risk.

**Key technologies:** Jenkins, ELK Stack (Elasticsearch, Logstash, Kibana), Bash, Linux, Jira, Puppet, PRTG, Spacewalk, CentOS, RockyOS, NetScaler, AWS (EC2, S3, Route 53, VPC), CVE/vulnerability tracking, SSL/TLS scoring

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned all company IT infrastructure — including a zero-downtime server relocation and a redundant server architecture that eliminated single points of failure — while managing a team of technicians (scheduling, training, delegation) and serving as the final QA gate before any release reached production.
- Wrote production software alongside the infrastructure role for roughly seven years before the title formalized it: the production scheduling system covering the department's full planning cycle, then a voice recognition evaluation system and multi-language dictionary infrastructure.

**Key technologies:** C++, Java, SQL, Windows Server, Linux, Active Directory, VMware vSphere, Cisco routing, firewall/VPN, backup & recovery

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
