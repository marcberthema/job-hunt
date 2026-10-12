# Marc Berthelette

**Senior DevOps Engineer — Azure Platform Automation**

Smiths Falls, ON, Canada · Available for remote work · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French (native) · English (fluent) · Incorporated in Canada · Available immediately

## Professional Summary

Senior DevOps engineer with nearly 18 years across infrastructure, software development, and production operations. Azure is the primary cloud: at Énergir, helped move team-owned Nexus, Jenkins, and Vault environments from manual Azure portal operations to Infrastructure as Code (Terraform provisioning, Ansible configuration), then introduced Azure Key Vault and Azure Storage-backed Terraform state. Standardized CI/CD for approximately 50 developers across 12 teams and 70+ applications in energy, and built Python monitoring for approximately 250 Artifactory repositories at Desjardins. Works in regulated environments and documents what he builds. Incorporated in Canada and available immediately.

## Technical Skills

**Azure & Infrastructure:** Microsoft Azure (resource groups, networking, virtual machines, Storage accounts, Key Vault), Terraform and Ansible workflows (user of another team's modules), Linux, Docker, AWS (EC2, S3, Route 53, VPC)\
**CI/CD & Platforms:** Azure DevOps, Jenkins (shared pipeline standards), GitHub Actions, SonarQube quality gates, JFrog Artifactory, Nexus\
**Scripting & Programming:** Python, FastAPI, Bash, Java, C++, SQL\
**Containers & Delivery:** Docker, Kubernetes application deployments, ArgoCD\
**Monitoring & Observability:** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Helped a team move team-owned Sonatype Nexus, Jenkins controllers and agents, and HashiCorp Vault in development and production from manual Azure portal operations to Infrastructure as Code. Terraform provisioned resource groups, networking, and VMs; Ansible configured the new VMs, including Docker. Supported and taught the team on these workflows, which another team owned.
- Later introduced Azure Storage accounts for Terraform state and Azure Key Vault to replace HashiCorp Vault, which was decommissioned about a year later.
- Centralized Jenkins continuous integration and delivery for approximately 50 developers across 12 teams and 70+ applications, enforcing shared stages and mandatory SonarQube checks.
- Rebuilt Salesforce delivery with Salesforce CLI and sandbox validation of candidate merges; reduced recurring missed deployment windows to one miss since launch.
- Automated Oracle releases after an earlier attempt had failed, removing the need for a weekly approved emergency-access account for routine deployments.
- Reduced MuleSoft production releases from a 15-step manual checklist to a few Jenkins jobs.
- Versioned ArcGIS map services and delivered service-account deployments across dev, test, and production, replacing deployments from developers' laptops.
- Created the delivery roadmap as informal primary owner for the first three years; onboarded developers and DevOps engineers and served as their primary support contact.
- Partnered with Enterprise Architecture on infrastructure design aligned with zero-trust principles and ran proofs of concept for emerging cloud and infrastructure technologies.

**Key technologies:** Azure, Terraform, Ansible, Jenkins, SonarQube, Nexus, Azure Key Vault, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026** *(concurrent with the Énergir engagement)*

- Built a Python/FastAPI service testing approximately 250 JFrog Artifactory remote repositories every four hours, publishing results to Dynatrace across seven package ecosystems.
- Made validation logic reusable and test cases configurable; the harness also supported regression testing for the enterprise Artifactory upgrade.
- Automated on-demand Artifactory environments using Kubernetes and ArgoCD so administrators could test configuration changes and upgrades safely.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD, improving governance and auditability.

**Key technologies:** Python, FastAPI, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code for 10–15 developers supporting 80+ applications and 20+ clients, standardizing delivery steps and adding release visibility through Jira.
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
