# Marc Berthelette

**Senior Site Reliability Engineer — Platform Automation, Observability and Developer Enablement**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer with nearly 18 years across infrastructure, development and operations. Builds Python automation that reduces toil: shared Jenkins pipelines for 12 teams and 70+ applications, a Python/FastAPI validation service at Desjardins reporting to Dynatrace, and production Salesforce logging moved to direct Dynatrace ingestion. Supported a 24/7 on-call rotation and a 600+ server fleet at Tink. Azure is the main cloud; AWS experience is a hand-built migration environment and Terraform use is of another team's workflows.

## Technical Skills

**Reliability:** Incident response, root cause analysis, on-call support, automated remediation, Linux\
**Observability:** Dynatrace, Splunk, ELK, PRTG; Python, FastAPI, Bash\
**Cloud & Infrastructure:** Azure, Terraform/Ansible workflows (user of another team's modules), AWS migration environment, Puppet, Spacewalk\
**Delivery:** Jenkins, GitHub Actions, Azure DevOps, Artifactory, Kubernetes application deployments, ArgoCD

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Migrated production Salesforce logging from Logstash to direct Dynatrace ingestion, reproducing existing processing; extracted DML error types, messages and originating classes and built dashboards that exposed previously hidden issues, then transferred ownership to a long-standing Salesforce team member.
- Implemented four-hourly Jenkins smoke tests with Teams alerts to detect external dependency failures, including firewall changes; clarified pipeline-versus-application failure ownership.
- Initiated shared Jenkins pipelines adopted by all teams already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications; achieved approximately 80–90% JaCoCo coverage of shared pipeline code with per-commit unit tests and built sample applications for integration testing.
- Separated application-code errors from platform-pipeline errors in build reporting so teams could see whose fix a failure was.
- Built nightly Salesforce validation; escalated two weeks of failures to the project director, prompting fixes across 4–5 teams within 48 hours. The project deployed on schedule.
- Ran recurring enablement sessions (about six per year) with each application team after pipeline delivery; onboarded new DevOps engineers and developers and was the primary developer contact when the delivery ecosystem broke.
- Automated routine Oracle releases without emergency-access requests; manual steps retained approvals. Eliminated encoding incidents with SQL checks and separate SQL/Forms locale settings.

**Key technologies:** Jenkins, Azure, Python, Dynatrace, Logstash, JaCoCo, Salesforce CLI, Oracle

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent with the Énergir engagement.

- Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across approximately 250 repositories.
- Deployed the suite through ArgoCD/GitOps for scheduled execution, publishing configuration-version and artifact-level results to Dynatrace to expose configuration and upstream connectivity failures.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.
- Made most validation logic tool-agnostic and the artifact test set configurable so platform administrators could add their own cases.

**Key technologies:** Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Automated PRTG-triggered response to Elasticsearch CPU saturation: attempted a process restart after two minutes and alerted on-call at five minutes if saturation persisted; supported a 24/7 rotation.
- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots.
- Controlled updates through client-specific package repositories; published patch/reboot progress and failures to Rocket.Chat, with existing PRTG monitoring covering service health.
- Built fleet inventory across Unix and Windows servers to identify vulnerable applications and upcoming end-of-life upgrades; added TLS scoring and environment version tracking for Ops, product owners, and QA.
- Built centralized ELK logging and managed fleet configuration with Puppet.
- Built an AWS migration target using console provisioning (EC2, S3, Route 53, VPC, caching and database services); the client cancelled before production cutover.

**Key technologies:** Linux, Jenkins, Puppet, Spacewalk, PRTG, ELK, AWS, Rocket.Chat

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Led and performed most redundancy work across HAProxy, Active Directory, speech-recognition servers and file services, supported by a second technician, for live-captioning production.
- Supported client requirements allowing at most three minutes of downtime per broadcast and eight seconds from speech to caption; distributed booth PCs across separate switches and provided dual internet links.
- Planned and executed two phased office relocations involving approximately 15–20 workstations. Developed production scheduling and speech-recognition evaluation software.

**Key technologies:** HAProxy, Active Directory, VMware vSphere, Linux, Windows Server, C++, Java, SQL

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal | 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal | 2005
