# Marc Berthelette

**Senior Site Reliability Engineer — Production Operations, Monitoring and Automation**

Smiths Falls, ON, Canada · Available for remote work · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingual: French (native) · English (fluent) · Available immediately

## Professional Summary

Senior DevOps engineer focused on production reliability, monitoring, and automation, with nearly 18 years across infrastructure and software development. Automated patching and kernel reboots across 600+ servers, supported a 24/7 production on-call rotation, built centralized log aggregation, and built Python health monitoring for approximately 250 Artifactory repositories with Dynatrace dashboards. Introduced AI-assisted engineering practices with scope gates and human-validation checkpoints. Experienced with Linux, Python, Azure, and incident response in energy and financial services.

## Technical Skills

**Reliability & Operations:** Production incident response, root cause analysis, on-call support, automated remediation, change and release execution, Linux\
**Monitoring & Observability:** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana, PRTG\
**Programming & Scripting:** Python, FastAPI, Bash, Java, C++, SQL\
**Cloud & Infrastructure:** Microsoft Azure, AWS (EC2, S3, Route 53, VPC), Terraform/Ansible workflows (user of another team's modules), Puppet, Spacewalk\
**Containers & Delivery:** Docker, Kubernetes application deployments, ArgoCD, Jenkins, GitHub Actions, JFrog Artifactory

## Work Experience

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Part of a 24/7 on-call rotation supporting all production systems and applications.
- Automated OS patching and kernel-update reboots across 600+ servers, reducing maintenance to a monthly verification check with near-zero downtime; managed fleet configuration with Puppet and Spacewalk.
- Automated recovery of a recurring Elasticsearch failure the client would not upgrade away: a local script restarted it after two minutes of probe-detected downtime, and monitoring paged the on-call engineer if it was still down at five minutes.
- Built centralized ELK log aggregation supporting incident investigation and proactive detection of production anomalies.
- Created, unprompted, a software inventory platform exposing fleet-wide application versions, vulnerability exposure, end-of-life software, and TLS certificate assessments to product owners.
- Standardized Jenkins Pipeline as Code for 80+ applications and 20+ clients, helping 10–15 developers keep build and release processes consistent; monitored build failures to maintain deployment cadence.
- Built a client's AWS migration target environment over about six months (EC2, S3, Route 53, VPC, memcached on EC2, serverless relational database), provisioned by hand with no prior AWS experience; the client cancelled the migration before cutover.

**Key technologies:** Linux, AWS, Bash, Elasticsearch, Logstash, Kibana, PRTG, Puppet, Spacewalk, Jenkins

### Desjardins — Senior DevOps Engineer (Contract)

**Montréal, QC (Remote) | October 2025 – March 2026** *(concurrent with the Énergir engagement)*

- Built a Python/FastAPI health-monitoring service validating approximately 250 Artifactory remote repositories every four hours, with results and technology-segmented dashboards in Dynatrace.
- Designed configurable tests across seven package ecosystems; reused the validation harness as a regression check for the enterprise Artifactory upgrade.
- Provisioned on-demand Artifactory environments with Kubernetes and ArgoCD, giving administrators isolated environments for configuration and upgrade testing.
- Built Splunk alerts detecting configuration changes outside CI/CD and implemented artifact retention policies to improve auditability and control storage growth.

**Key technologies:** Python, FastAPI, Dynatrace, Splunk, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – September 2026**

- Served as the primary developer contact for delivery failures; created the delivery roadmap as informal owner for the first three years and onboarded new engineers.
- Separated application-code errors from platform-pipeline errors in build reporting, reducing false-positive failures and making troubleshooting ownership clear.
- Drove root cause analysis on critical production incidents and added monitoring and dashboards to reduce time to restore.
- Centralized Jenkins continuous integration and delivery for approximately 50 developers across 12 teams and 70+ applications, enforcing shared stages and mandatory SonarQube checks.
- Built Salesforce CLI delivery with sandbox validation of candidate merges; reduced recurring missed deployment windows to one miss since launch.
- Automated Oracle and MuleSoft releases, reducing a 15-step manual MuleSoft checklist to a few Jenkins jobs.
- Introduced AI-assisted engineering practices with hard scope gates and human-validation checkpoints before any AI-generated code reaches production.

**Key technologies:** Azure, Jenkins, SonarQube, Python, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### SOVO Technologies — Lead Technician → Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Managed company IT infrastructure and a technician team; completed a server relocation without downtime and made core servers redundant to remove single points of failure.
- Developed production scheduling, voice-recognition evaluation, and multilingual dictionary software; served as the final quality gate before production releases.

**Key technologies:** Linux, Windows Server, VMware vSphere, Cisco networking, C++, Java, SQL, Active Directory

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
