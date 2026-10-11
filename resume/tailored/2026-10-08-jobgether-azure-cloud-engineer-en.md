# Marc Berthelette

**Senior Platform / DevOps Engineer · Azure**

Smiths Falls, ON, Canada · Available for remote work · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French (native) · English (fluent) · Available immediately

## Professional Summary

Senior DevOps engineer with nearly 18 years across infrastructure, software development, and production operations, and about five years working on Microsoft Azure. Standardized CI/CD for approximately 50 developers across 12 teams and 70+ applications at Énergir, helped move team-owned Nexus, Jenkins, and Vault environments from manual Azure operations to Terraform and Ansible, and built automated platform validation and monitoring at Desjardins. Experienced with root-cause analysis, observability, and incident response in energy and financial services. Focused on making deployments dependable and reducing manual work for engineering teams.

## Technical Skills

**Cloud & Infrastructure:** Microsoft Azure (VMs, networking, resource groups, Storage accounts, Key Vault), Terraform/Ansible workflows, AWS (EC2, S3, Route 53, VPC), Linux, Puppet\
**CI/CD & Platforms:** GitHub Actions, Azure DevOps, Jenkins, SonarQube, JFrog Artifactory, Nexus\
**Containers & Delivery:** Docker, Kubernetes application deployments, ArgoCD\
**Monitoring & Observability:** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana, PRTG\
**Programming & Scripting:** Python, FastAPI, Bash, Java, C++, SQL

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Helped a team move team-owned Nexus, Jenkins, and Vault environments in development and production from manual Azure portal operations to Infrastructure as Code, using another team's Terraform and Ansible workflows (Terraform for resource groups, networking, and VMs; Ansible for host and Docker configuration). Later introduced Azure Storage accounts for Terraform state and Azure Key Vault in place of HashiCorp Vault.
- Centralized Jenkins continuous integration and delivery (CI/CD) for approximately 50 developers across 12 teams and 70+ applications, enforcing shared stages and mandatory SonarQube checks.
- Separated application-code errors from platform-pipeline errors in build reporting, cutting false-positive failures and letting teams see whether a result was theirs to fix.
- Led root-cause analysis on critical production incidents; implemented proactive monitoring, observability dashboards, and automated remediation to reduce time to recover.
- Rebuilt Salesforce delivery using Salesforce CLI and sandbox validation of candidate merges; reduced recurring missed deployment windows to one miss since launch.
- Automated Oracle releases, removing the need for a weekly approved emergency-access account for routine deployments; added tests catching recurring file-encoding issues.
- Versioned ArcGIS map services and properties; delivered service-account deployments to dev, test, and production, replacing deployments from developers' laptops.
- Reduced MuleSoft production releases from a 15-step manual checklist to a few Jenkins jobs.
- Created the delivery roadmap as informal primary owner for the first three years; onboarded developers and DevOps engineers and served as their primary support contact.

**Key technologies:** Azure, Terraform, Ansible, Azure Key Vault, Jenkins, SonarQube, Nexus, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026**\
Concurrent contract alongside the Énergir engagement.

- Built a Python/FastAPI service testing approximately 250 JFrog Artifactory remote repositories every four hours, publishing results to Dynatrace across seven package ecosystems.
- Made validation logic reusable and test cases configurable; the harness also supported regression testing for the enterprise Artifactory upgrade.
- Automated on-demand Artifactory environments using Kubernetes and ArgoCD so administrators could test configuration changes and upgrades safely.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD, improving platform governance and auditability.

**Key technologies:** Python, FastAPI, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code for 10–15 developers supporting 80+ applications and 20+ clients, standardizing delivery steps and adding release visibility through Jira.
- Automated OS patching and kernel reboots across 600+ servers, reducing maintenance to a monthly verification check; managed configuration with Puppet and Spacewalk.
- Built a fleet software inventory platform exposing application versions, vulnerability exposure, end-of-life software, and TLS certificate assessments to product owners.
- Supported a 24/7 production on-call rotation; built ELK log aggregation and automated restart of an unresponsive Elasticsearch cluster to reduce manual intervention.
- Built a client's AWS migration target environment over about six months (EC2, S3, Route 53, VPC, memcached on EC2, serverless relational database), provisioned by hand with no prior AWS experience; the client cancelled the migration before cutover.

**Key technologies:** Jenkins, Linux, Puppet, Spacewalk, AWS, Bash, Elasticsearch, Logstash, Kibana, PRTG, Jira

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Managed company IT infrastructure and a technician team; delivered a server relocation without downtime and added redundancy to core servers.
- Developed production scheduling, voice-recognition evaluation, and multilingual dictionary software; served as the final quality gate before production releases.

**Key technologies:** C++, Java, SQL, Linux, Windows Server, Active Directory, VMware vSphere, Cisco networking

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
