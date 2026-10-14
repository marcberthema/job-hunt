# Marc Berthelette

**Senior Linux & Cloud Engineer — Fleet Automation, Azure and Delivery**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer with nearly 18 years across Linux and Windows infrastructure, automation and delivery. Replaced reactive patching across a 600+ server fleet at Tink with staged, role-based schedules using Spacewalk and Puppet; built fleet inventory; supported 24/7 on-call. Main cloud for the last five years is Azure, with Terraform and Ansible used from another team's workflows. Has run virtualized infrastructure on VMware and led IT redundancy and office moves at SOVO.

## Technical Skills

**Linux & Fleet Automation:** Linux, Puppet, Spacewalk, Bash, Python, Ansible/Terraform workflows (user of another team's modules)\
**Virtualization & Networking:** VMware vSphere, HAProxy, Active Directory, Windows Server, switching and cabling\
**Cloud:** Azure (VMs, networking, Storage, Key Vault), AWS migration environment, Kubernetes application deployments, ArgoCD\
**Delivery & Observability:** Jenkins, GitHub Actions, Artifactory, Dynatrace, Splunk, ELK, PRTG

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Helped a team move team-owned Nexus, Jenkins controllers and agents, and HashiCorp Vault from manual Azure portal operations to Infrastructure as Code, using another team's Terraform (resource groups, networking, VMs) and Ansible (host and Docker configuration) workflows; later introduced Azure Storage accounts for Terraform state and Azure Key Vault in place of HashiCorp Vault.
- Initiated shared Jenkins pipelines adopted by all teams already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications; achieved approximately 80–90% JaCoCo coverage of shared pipeline code with per-commit unit tests and built sample applications for integration testing.
- Enforced shared stages and mandatory SonarQube checks in the shared pipelines so developers could not simply skip them.
- Migrated production Salesforce logs to direct Dynatrace ingestion; expanded error parsing and dashboards to help the team investigate previously hidden issues.
- Ran recurring enablement sessions (about six per year) with each application team after pipeline delivery; onboarded new DevOps engineers and developers and was the primary developer contact when the delivery ecosystem broke.

**Key technologies:** Jenkins, SonarQube, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Node.js, MuleSoft, Dynatrace

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent with the Énergir engagement.

- Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across approximately 250 repositories.
- Deployed the suite through ArgoCD/GitOps for scheduled execution, publishing configuration-version and artifact-level results to Dynatrace to expose configuration and upstream connectivity failures.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.

**Key technologies:** Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots.
- Controlled updates through client-specific package repositories; published patch/reboot progress and failures to Rocket.Chat, with existing PRTG monitoring covering service health.
- Built fleet inventory across Unix and Windows servers to identify vulnerable applications and upcoming end-of-life upgrades; added TLS scoring and environment version tracking for Ops, product owners, and QA.
- Automated PRTG-triggered response to Elasticsearch CPU saturation: attempted a process restart after two minutes and alerted on-call at five minutes if saturation persisted; supported a 24/7 rotation.
- Built centralized ELK logging and managed fleet configuration with Puppet.
- Built an AWS migration target using console provisioning (EC2, S3, Route 53, VPC, caching and database services); the client cancelled before production cutover.
- Standardized Jenkins pipelines for 10–15 developers supporting 80+ applications and 20+ clients, integrating release details and Jira references into deployment reporting.

**Key technologies:** Linux, Jenkins, Puppet, Spacewalk, PRTG, ELK, AWS, Rocket.Chat

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Led and performed most redundancy work across HAProxy, authentication, speech-recognition servers and file services with a second technician; supported live-captioning requirements of three minutes maximum downtime per broadcast and eight-second caption latency.
- Owned IT planning and execution for two office relocations involving approximately 15–20 workstations, preparing networks and cabling and coordinating phased moves to minimize disruption.
- Developed production scheduling, speech-recognition evaluation, and multilingual dictionary software; served as the final quality gate before production releases.

**Key technologies:** HAProxy, Active Directory, VMware vSphere, Linux, Windows Server, C++, Java, SQL

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal | 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal | 2005
