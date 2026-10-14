# Marc Berthelette

**Senior DevOps Engineer — Azure Automation, Infrastructure as Code and CI/CD**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French / English · Incorporated in Canada · Available immediately

## Professional Summary

Senior engineer with nearly 18 years across infrastructure, development and operations, and five years working mainly in Azure. Helped move team-owned Nexus, Jenkins and Vault environments to Infrastructure as Code using another team's Terraform and Ansible workflows, then introduced Azure Key Vault and Azure Storage-backed Terraform state. Built shared CI/CD for 12 teams and 70+ applications and technically directed delivery work without a formal lead title. Kubernetes experience is application deployment, not AKS operation.

## Technical Skills

**Cloud & Infrastructure:** Azure (resource groups, networking, VMs, Storage accounts, Key Vault), Terraform/Ansible workflows (user of another team's modules), Linux, Puppet\
**CI/CD & Platforms:** Azure DevOps, Jenkins, GitHub Actions, SonarQube, JFrog Artifactory, Nexus\
**Containers & Observability:** Docker, Kubernetes application deployments, ArgoCD, Dynatrace, Splunk, ELK\
**Programming:** Python, FastAPI, Bash, Java, C++, SQL

## Work Experience

### Énergir — Senior DevOps Engineer (Contract)

**Montréal, QC | September 2021 – September 2026**\
Five-year consulting engagement, renewed four times.

- Helped a team move team-owned Nexus, Jenkins controllers and agents, and HashiCorp Vault from manual Azure portal operations to Infrastructure as Code, using another team's Terraform (resource groups, networking, VMs) and Ansible (host and Docker configuration) workflows; later introduced Azure Storage accounts for Terraform state and Azure Key Vault in place of HashiCorp Vault.
- Initiated shared Jenkins pipelines adopted by all teams already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications; achieved approximately 80–90% JaCoCo coverage of shared pipeline code with per-commit unit tests and built sample applications for integration testing.
- Enforced shared stages and mandatory SonarQube checks in the shared pipelines so developers could not simply skip them.
- Ran recurring enablement sessions (about six per year) with each application team after pipeline delivery; onboarded new DevOps engineers and developers and was the primary developer contact when the delivery ecosystem broke.
- Separated application-code errors from platform-pipeline errors in build reporting so teams could see whose fix a failure was.
- Established “build once, deploy many”; migrated approximately five Node.js applications to runtime configuration through team-reviewed pull requests so the same tested build could serve each environment.
- Replaced a 15-step MuleSoft checklist with version-based deployments of QA-tested artifacts, moving release preparation ahead of production windows and simplifying rollback.
- Introduced AI-assisted engineering practices with hard scope gates and human-validation checkpoints before any AI-generated code reaches production.

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
