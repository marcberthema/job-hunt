# Marc Berthelette

**Senior DevOps Engineer — CI/CD Platforms and Developer Experience**

Smiths Falls, ON, Canada · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French (native) · English (fluent) · Available immediately

## Professional Summary

Senior DevOps engineer with nearly 18 years across infrastructure, software development, and production operations. Runs CI/CD platforms that engineering teams depend on: centralized Jenkins delivery for approximately 50 developers across 12 teams and 70+ applications at Énergir, with shared stages and mandatory SonarQube checks. Builds internal tooling in Python and works with Terraform/Ansible workflows, Kubernetes and ArgoCD, and GitHub Actions. Experienced in energy and financial services, with a focus on making deployments dependable and reducing manual work for developers.

## Technical Skills

**CI/CD & Platforms:** Jenkins (shared pipeline standards), GitHub Actions, Azure DevOps, SonarQube quality gates, JFrog Artifactory, Nexus, Salesforce CLI\
**Programming & Scripting:** Python, FastAPI, Bash, Java, C++, SQL\
**Cloud & Infrastructure:** Microsoft Azure, AWS (EC2, S3, Route 53, VPC), Terraform/Ansible workflows (user of another team's modules), Linux, Puppet\
**Containers & Delivery:** Docker, Kubernetes application deployments, ArgoCD\
**Monitoring & Observability:** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Centralized Jenkins continuous integration and delivery for approximately 50 developers across 12 teams and 70+ applications, enforcing shared stages and mandatory SonarQube checks that developers could not simply skip.
- Drove platform adoption across 12 teams outside any reporting line through recurring enablement sessions (about six per year) after each pipeline delivery.
- Rebuilt Salesforce delivery with Salesforce CLI and sandbox validation of every candidate merge; reduced recurring missed deployment windows to one miss since launch.
- Automated Oracle releases after an earlier attempt had failed, removing the need for a weekly approved emergency-access account for routine deployments; added tests catching recurring file-encoding issues.
- Reduced MuleSoft production releases from a 15-step manual checklist to a few Jenkins jobs.
- Separated application-code errors from platform-pipeline errors in build reporting, reducing false-positive failures and clarifying who owns each fix.
- Versioned ArcGIS map services and delivered service-account deployments to dev, test, and production, replacing deployments from developers' laptops.
- Helped a team move team-owned Nexus, Jenkins, and Vault environments from manual Azure portal operations to Infrastructure as Code using another team's Terraform and Ansible workflows; later introduced Azure Key Vault in place of HashiCorp Vault.
- Acted as informal primary owner of the delivery roadmap for the first three years; served as primary developer contact when the ecosystem broke and onboarded new DevOps engineers and developers.
- Introduced AI-assisted engineering practices with hard scope gates and human-validation checkpoints before AI-generated code reaches production.

**Key technologies:** Jenkins, SonarQube, Azure, Terraform, Ansible, Nexus, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026** *(concurrent with the Énergir role)*

- Built a Python/FastAPI service testing approximately 250 JFrog Artifactory remote repositories every four hours, publishing results to Dynatrace across seven package ecosystems.
- Made validation logic reusable and test cases configurable; the harness also supported regression testing for the enterprise Artifactory upgrade.
- Automated on-demand Artifactory environments using Kubernetes and ArgoCD so administrators could test configuration changes and upgrades safely.
- Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD, improving governance and auditability.
- Worked with GitHub Actions, Kubernetes, and ArgoCD in a large financial-services environment.

**Key technologies:** Python, FastAPI, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Centralized Jenkins Pipeline as Code for 10–15 developers supporting 80+ applications and 20+ clients, standardizing delivery steps and adding release visibility through Jira.
- Automated OS patching and kernel reboots across 600+ servers, reducing maintenance to a monthly verification check; managed configuration with Puppet and Spacewalk.
- Built a fleet software inventory platform exposing application versions, vulnerability exposure, end-of-life software, and TLS certificate assessments to product owners.
- Supported a 24/7 production on-call rotation; built ELK log aggregation and automated restart of an unresponsive Elasticsearch cluster to reduce manual intervention.
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
