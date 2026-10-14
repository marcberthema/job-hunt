# Marc Berthelette

**Senior DevOps & Platform Engineering Consultant**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer and consultant with nearly 18 years across infrastructure, software development, and operations. Built shared delivery tooling in an environment spanning 12 teams and 70+ applications at Énergir, and automated repository validation at Desjardins. Turns manual release processes into tested, repeatable workflows and works with application teams to put improvements into use.

## Technical Skills

**CI/CD & Platforms:** Jenkins, Azure DevOps, GitHub Actions, JFrog Artifactory, JaCoCo\
**Cloud & Infrastructure:** Azure, Terraform/Ansible workflows, Linux, Puppet, AWS migration environment\
**Containers & Observability:** Kubernetes application deployments, Docker, ArgoCD, Dynatrace, Splunk, ELK\
**Programming:** Python, FastAPI, Bash, Java, C++, SQL

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Initiated shared Jenkins pipelines adopted by all Jenkins teams; achieved approximately 80–90% JaCoCo coverage with per-commit unit tests and built sample applications for integration testing.
- Established “build once, deploy many”; migrated approximately five Node.js applications to runtime configuration through team-reviewed pull requests so the same tested build could serve each environment.
- Replaced a 15-step MuleSoft checklist with version-based deployments of QA-tested artifacts, moving release preparation ahead of production windows and simplifying rollback.
- Built nightly Salesforce validation; escalated two weeks of failures to the project director, prompting fixes across 4–5 teams within 48 hours. The project deployed on schedule.
- Automated routine Oracle releases without emergency-access requests; manual steps retained approvals. Eliminated encoding incidents with SQL checks and separate SQL/Forms locale settings.
- Migrated production Salesforce logs to direct Dynatrace ingestion; expanded error parsing and dashboards to help the team investigate previously hidden issues.

**Key technologies:** Jenkins, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Dynatrace, Logstash

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent with the Énergir engagement.

- Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across approximately 250 repositories.
- Deployed the suite through ArgoCD/GitOps for scheduled execution, publishing configuration-version and artifact-level results to Dynatrace to expose configuration and upstream connectivity failures.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.

**Key technologies:** Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

Supported the entire development team of 10–15 developers and monitored a production fleet of 600+ servers supporting 80+ applications for 20+ clients.

- Standardized Jenkins pipelines for 10–15 developers supporting 80+ applications and 20+ clients, integrating release details and Jira references into deployment reporting.
- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots.
- Controlled updates through client-specific package repositories; published patch/reboot progress and failures to Rocket.Chat, with existing PRTG monitoring covering service health.
- Built fleet inventory across Unix and Windows servers to identify vulnerable applications and upcoming end-of-life upgrades; added TLS scoring and environment version tracking for Ops, product owners, and QA.
- Built an AWS migration target using console provisioning (EC2, S3, Route 53, VPC, caching and database services); the client cancelled before production cutover.

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
