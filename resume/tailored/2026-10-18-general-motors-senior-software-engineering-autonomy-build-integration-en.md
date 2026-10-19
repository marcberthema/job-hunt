# Marc Berthelette

**Senior DevOps Engineer — CI/CD, Build and Release Promotion Workflows**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Available immediately

## Professional Summary

Senior engineer with nearly 18 years across infrastructure, software development and operations. Built shared Jenkins delivery pipelines with mandatory quality gates and sample applications for integration testing in an environment of about 50 developers, 12 teams and 70+ applications at Énergir. Supported a 600+ server Linux and Windows fleet at Tink, and built a Python/FastAPI validation service at Desjardins deployed through ArgoCD. Replaces manual release steps with tested, repeatable release-promotion workflows, enforces quality gates before promotion, makes pipeline failures self-diagnosing, and drove delivery improvements across 12 teams outside any reporting line.

## Technical Skills

**CI/CD & Release:** Jenkins, GitHub Actions, Azure DevOps, JFrog Artifactory, Nexus, SonarQube, JaCoCo\
**Linux & Infrastructure:** Linux administration (Red Hat, CentOS, Rocky, Ubuntu), Puppet, Spacewalk, Azure, VMware vSphere, networking\
**Automation & Programming:** Python, FastAPI, Bash, Java, C++, SQL\
**Containers & Observability:** Docker, ArgoCD, Kubernetes application deployments, Dynatrace, Splunk, ELK, PRTG\
**Also used:** Terraform/Ansible provisioning workflows run by another team; Kubernetes clusters operated by other teams

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Initiated shared Jenkins pipelines adopted by all Jenkins teams; mandatory SonarQube checks could not be skipped, with approximately 80–90% JaCoCo coverage on the shared code, per-commit unit tests and sample applications for integration testing.
- Separated application-code failures from platform-pipeline failures in build reporting, so developers could tell at a glance whose fix it was; ran scheduled smoke tests of Jenkins services that alerted Teams to external changes such as firewall rules.
- Established “build once, deploy many”; migrated approximately five Node.js applications to runtime configuration through team-reviewed pull requests so the same tested build could serve each environment.
- Replaced a 15-step MuleSoft checklist with version-based deployments of QA-tested artifacts, moving release preparation ahead of production windows and simplifying rollback.
- Built nightly Salesforce validation; escalated two weeks of failures to the project director, prompting fixes across 4–5 teams within 48 hours. The project deployed on schedule.
- Automated routine Oracle releases without emergency-access requests; manual steps retained approvals. Eliminated recurring encoding incidents with SQL checks and separate SQL/Forms locale settings.
- Introduced AI-assisted engineering practices into the team's tooling over six to nine months, with scope gates and human-validation checkpoints before generated code reached production; flagged the absence of organizational safeguards to leadership.
- Helped migrate team-owned Nexus, Jenkins controllers and agents, and Vault environments onto Terraform provisioning and Ansible configuration workflows run by another team.
- Migrated production Salesforce logs to direct Dynatrace ingestion; expanded error parsing and dashboards to help the team investigate previously hidden issues.

**Key technologies:** Jenkins, SonarQube, JaCoCo, Azure, Python, Salesforce CLI, Oracle, Dynatrace, Nexus

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

- Standardized Jenkins pipelines for 10–15 developers supporting 80+ applications and 20+ clients, integrating release details, CVEs from artifact reports and Jira references from Git logs into deployment reporting.
- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots; controlled package versions with client-specific repositories and published progress and failures to Rocket.Chat.
- Built fleet inventory across Unix and Windows servers, using Puppet-deployed scanners, to identify vulnerable applications and upcoming end-of-life upgrades; added TLS scoring and environment version tracking for Ops, product owners and QA.
- Implemented PRTG-triggered Elasticsearch process restarts after sustained CPU saturation, escalating to on-call at five minutes, where the client declined an upgrade.
- Built an AWS migration target using console provisioning (EC2, S3, Route 53, VPC, caching and database services); the client cancelled before production cutover.
- Part of a 24/7 on-call rotation supporting all production systems.

**Key technologies:** Linux, Jenkins, Puppet, Spacewalk, PRTG, ELK, Rocket.Chat, AWS

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Developed production scheduling, speech-recognition evaluation and multilingual dictionary software in C++ and Java; served as the final quality gate before production releases.
- Led and performed most redundancy work across HAProxy, authentication, speech-recognition servers and file services with a second technician; supported live-captioning requirements of three minutes maximum downtime per broadcast and eight-second caption latency.
- Owned IT planning and execution for two office relocations involving approximately 15–20 workstations, preparing networks and cabling and coordinating phased moves to minimize disruption.

**Key technologies:** C++, Java, SQL, HAProxy, Active Directory, VMware vSphere, Linux, Windows Server

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal | 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal | 2005
