# Marc Berthelette

**Senior DevOps Engineer — Cloud Infrastructure and Developer Platforms**

Smiths Falls, ON, Canada · Available for remote work · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French (native) · English (fluent) · Available immediately

## Professional Summary

Senior DevOps engineer with nearly 18 years across infrastructure, software development, and production operations. Standardized CI/CD for approximately 50 developers across 12 teams and 70+ applications at Énergir, and helped move team-owned Nexus, Jenkins, and Vault environments on Azure from manual operations to Infrastructure as Code. Built a Python/FastAPI monitoring service for approximately 250 Artifactory repositories at Desjardins. Experienced in Azure, deployment pipelines, observability, and incident response in energy and financial services, with Kubernetes experience at the application level rather than as a cluster owner. Focused on making deployments dependable and giving engineering teams less to run by hand.

## Technical Skills

**Cloud & Infrastructure:** Microsoft Azure (resource groups, networking, VMs, Storage accounts, Key Vault), AWS (EC2, S3, Route 53, VPC), Terraform and Ansible workflows (user of another team's modules), Linux, Puppet\
**CI/CD & Platforms:** Jenkins (shared pipeline standards), GitHub Actions, Azure DevOps, SonarQube quality gates, JFrog Artifactory, Nexus\
**Containers & Delivery:** Docker, Kubernetes application deployments, ArgoCD\
**Monitoring & Observability:** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana, incident response and runbooks\
**Programming & Scripting:** Python, FastAPI, Bash, Java, C++, SQL

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Centralized Jenkins continuous integration and delivery for approximately 50 developers across 12 teams and 70+ applications, enforcing shared stages and mandatory SonarQube checks.
- Drove platform adoption across 12 teams outside any reporting line through recurring enablement sessions (about six per year) after each pipeline delivery.
- Helped a team move team-owned Nexus, Jenkins controllers and agents, and HashiCorp Vault from manual Azure portal operations to Infrastructure as Code, using another team's Terraform (resource groups, networking, VMs) and Ansible (host and Docker configuration) workflows; later introduced Azure Storage accounts for Terraform state and Azure Key Vault in place of HashiCorp Vault.
- Separated application-code errors from platform-pipeline errors in build reporting, reducing false-positive failures and making troubleshooting ownership clear.
- Rebuilt Salesforce delivery with Salesforce CLI and sandbox validation of candidate merges; reduced recurring missed deployment windows to one miss since launch.
- Automated Oracle releases after an earlier attempt had failed, and reduced MuleSoft production releases from a 15-step manual checklist to a few Jenkins jobs.
- Versioned ArcGIS map services and delivered service-account deployments across dev, test, and production, replacing deployments from developers' laptops.
- Drove root cause analysis on critical production incidents and added monitoring and dashboards to reduce time to restore.
- Introduced AI-assisted engineering practices with hard scope gates and human-validation checkpoints before any AI-generated code reaches production.

**Key technologies:** Azure, Jenkins, SonarQube, Terraform, Ansible, Nexus, Azure Key Vault, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026** *(concurrent with the Énergir engagement)*

- Built a Python/FastAPI service testing approximately 250 JFrog Artifactory remote repositories every four hours, publishing results and technology-segmented dashboards to Dynatrace across seven package ecosystems.
- Made validation logic reusable and test cases configurable; the harness also supported regression testing for the enterprise Artifactory upgrade.
- Automated on-demand Artifactory environments using Kubernetes and ArgoCD so administrators could test configuration changes and upgrades safely.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD, improving auditability and control.

**Key technologies:** Python, FastAPI, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code for 10–15 developers supporting 80+ applications and 20+ clients, adding release visibility through Jira.
- Automated OS patching and kernel reboots across 600+ servers, reducing maintenance to a monthly verification check; managed configuration with Puppet and Spacewalk.
- Built a fleet software inventory platform exposing application versions, vulnerability exposure, end-of-life software, and TLS certificate assessments to product owners.
- Supported a 24/7 production on-call rotation; built ELK log aggregation and automated restart of an unresponsive Elasticsearch cluster.
- Built a client's AWS migration target environment over about six months (EC2, S3, Route 53, VPC, memcached on EC2, serverless relational database), provisioned by hand with no prior AWS experience; the client cancelled the migration before cutover.

**Key technologies:** Jenkins, Linux, Puppet, Spacewalk, AWS, Bash, Elasticsearch, Logstash, Kibana, Jira

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Managed company IT infrastructure and a technician team; delivered a server relocation without downtime and added redundancy to core servers.
- Developed production scheduling, voice-recognition evaluation, and multilingual dictionary software; served as the final quality gate before production releases.

**Key technologies:** C++, Java, SQL, Linux, Windows Server, Active Directory, VMware vSphere, Cisco networking

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
