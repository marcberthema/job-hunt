# Marc Berthelette

**Senior DevOps Engineer — Salesforce Release Pipelines, CI/CD and Deployment Validation**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer and consultant with nearly 18 years across infrastructure, development and operations, incorporated in Canada and available immediately. Rebuilt Salesforce delivery at Énergir on the official Salesforce CLI with nightly full-suite validation and sandbox validation of candidate merges, and moved production Salesforce logging to direct Dynatrace ingestion. Initiated shared Jenkins pipelines for 12 teams and 70+ applications. Uses GitHub Actions and Bitbucket; has not done Salesforce administration or Apex development.

## Technical Skills

**Salesforce Delivery:** Salesforce CLI, sandbox validation of candidate merges, nightly full-suite test runs, release support\
**CI/CD & Source Control:** GitHub Actions, Bitbucket, Git, Jenkins (shared pipelines), Azure DevOps, SonarQube, JaCoCo, JFrog Artifactory\
**Observability & Notifications:** Dynatrace, Splunk, ELK, Teams alerting\
**Programming & Platforms:** Python, FastAPI, Bash, Java, SQL, Azure, Kubernetes application deployments, ArgoCD

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Replaced legacy ANT deployment scripts with the official Salesforce CLI and built validation that deployed each candidate merge into a dedicated sandbox and ran the full test suite.
- Built nightly Salesforce validation; escalated two weeks of failures to the project director, prompting fixes across 4–5 teams within 48 hours. The project deployed on schedule.
- Migrated production Salesforce logs to direct Dynatrace ingestion; expanded error parsing and dashboards to help the team investigate previously hidden issues.
- Initiated shared Jenkins pipelines adopted by all teams already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications; achieved approximately 80–90% JaCoCo coverage of shared pipeline code with per-commit unit tests and built sample applications for integration testing.
- Enforced shared stages and mandatory SonarQube checks in the shared pipelines so developers could not simply skip them.
- Implemented four-hourly Jenkins smoke tests with Teams alerts to detect external dependency failures, including firewall changes; clarified pipeline-versus-application failure ownership.
- Separated application-code errors from platform-pipeline errors in build reporting so teams could see whose fix a failure was.
- Automated routine Oracle releases without emergency-access requests; manual steps retained approvals. Eliminated encoding incidents with SQL checks and separate SQL/Forms locale settings.

**Key technologies:** Jenkins, SonarQube, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Node.js, MuleSoft, Dynatrace

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent with the Énergir engagement.

- Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across approximately 250 repositories.
- Deployed the suite through ArgoCD/GitOps for scheduled execution, publishing configuration-version and artifact-level results to Dynatrace to expose configuration and upstream connectivity failures.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.
- Worked with Kubernetes, ArgoCD and GitHub Actions in a large financial-services environment.

**Key technologies:** Python, FastAPI, GitHub Actions, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Standardized Jenkins pipelines for 10–15 developers supporting 80+ applications and 20+ clients, integrating release details and Jira references into deployment reporting.
- Replaced reactive patching across 600+ servers with staged Spacewalk schedules, environment/role groups, A/B frontend and middleware batches, and dependency-aware reboots.
- Controlled updates through client-specific package repositories; published patch/reboot progress and failures to Rocket.Chat, with existing PRTG monitoring covering service health.
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
