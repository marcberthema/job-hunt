# Marc Berthelette

**Senior Site Reliability Engineer — Production Operations, Incident Response and Observability**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer with nearly 18 years across infrastructure, development, and operations, focused on production reliability: 24/7 on-call support, incident response and root cause analysis, fleet-wide patching automation, monitoring and alerting, and Linux and Windows server operations. Built Python/FastAPI validation services reporting to Dynatrace, and used Kubernetes and ArgoCD as an application and platform user rather than a cluster owner. Experience spans energy at Énergir, financial services at Desjardins, a 600+ server fleet at Tink, and live-captioning infrastructure with strict availability and latency requirements.

## Technical Skills

**Reliability:** Incident response, root cause analysis, on-call support, automated remediation, Linux\
**Observability:** Dynatrace, Splunk, ELK, PRTG; Python, FastAPI, Bash\
**Cloud & Infrastructure:** Azure, AWS (EC2, S3, Route 53, VPC; hand-built migration environment), Terraform/Ansible workflows (user of another team's modules), Puppet, Spacewalk, Linux and Windows Server, Active Directory, HAProxy\
**Delivery:** Jenkins, GitHub Actions, Azure DevOps, Artifactory, Kubernetes application deployments, ArgoCD

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Implemented four-hourly Jenkins smoke tests with Teams alerts to detect external dependency failures, including firewall changes; clarified pipeline-versus-application failure ownership.
- Achieved approximately 80–90% JaCoCo coverage of shared pipeline code with per-commit tests; built sample applications for manual integration testing across supported technology stacks.
- Eliminated recurring Oracle encoding incidents with SQL encoding checks and separate SQL/Forms locale settings; converted existing SQL files and documented procedures for developers.
- Built nightly Salesforce validation; escalated persistent failures to the project director, prompting fixes across 4–5 teams within 48 hours and enabling the project to deploy on schedule.
- Initiated and defined requirements for an availability dashboard covering Jenkins, Vault, Logstash and Nexus in development and production; a colleague implemented it.

**Key technologies:** Jenkins, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Node.js, MuleSoft

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent with the Énergir engagement.

- Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across approximately 250 repositories.
- Deployed the suite through ArgoCD/GitOps for scheduled execution, publishing configuration-version and artifact-level results to Dynatrace to expose configuration and upstream connectivity failures.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.

**Key technologies:** Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Automated PRTG-triggered response to Elasticsearch CPU saturation: attempted a process restart after two minutes and alerted on-call at five minutes if saturation persisted; supported a 24/7 rotation.
- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots.
- Controlled package versions through client-specific repositories and reported update/reboot progress and failures to Rocket.Chat; existing PRTG monitoring provided service-health checks.
- Built inventory across Unix and Windows servers for vulnerability impact analysis, end-of-life planning and TLS scoring; linked release versions and Jira references for Ops, product owners and QA.
- Built centralized ELK logging and managed fleet configuration with Puppet. Built an AWS migration target through console provisioning; the client cancelled before production cutover.

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
