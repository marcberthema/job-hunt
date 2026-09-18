# Marc Berthelette

**Site Reliability Engineer · Incident Automation · Kubernetes Operations**

Smiths Falls, ON, Canada · Remote · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingual French and English · Incorporated in Canada · Available immediately

---

## Professional Summary

Senior site reliability and platform engineer with 18 years of experience reducing operational toil through automation and root-cause-driven prevention. At Tink, cut on-call paging frequency roughly in half through RCA and built self-healing automation for an unstable Elasticsearch cluster. At Énergir, drives root-cause analysis and automated remediation across 70+ applications, reducing MTTR. At Desjardins, automated Kubernetes environment provisioning with ArgoCD. Deep observability practice (Dynatrace, Splunk, ELK Stack), current Terraform and Ansible IaC, and a demonstrated pattern of learning unfamiliar platforms cold under a delivery deadline — including a hands-on, no-prior-experience AWS build at Tink.

## Technical Skills

| Category | Technologies and Practices |
|---|---|
| **Site Reliability Engineering** | 24/7 on-call, incident response, root-cause analysis, post-incident reviews, MTTR reduction, automated remediation, self-healing automation |
| **Containers & Orchestration** | Kubernetes, Docker, ArgoCD — environment provisioning and automation |
| **Observability** | Dynatrace, Splunk, ELK Stack (Elasticsearch, Logstash, Kibana), PRTG, dashboards, alerting |
| **Infrastructure as Code** | Terraform, Ansible, Puppet, Spacewalk |
| **Cloud Platforms** | Microsoft Azure (production, 5–10 service migrations led), AWS (EC2, S3, Route 53, VPC — hands-on build, non-production, see Work Experience) |
| **Programming & Automation** | Python, FastAPI, Bash, Java, SQL, NoSQL |
| **Systems & Networking** | Red Hat Linux, CentOS, Rocky Linux, Ubuntu, NetScaler, Cisco routing, firewall/VPN administration |

## Work Experience

### Énergir — Senior DevOps Engineer

**Montréal, QC | September 2021 – Present**

- Drove root-cause analysis on critical production incidents and built proactive monitoring, dashboards, alerts, and automated remediation that reduced MTTR across 12 application teams and 70+ applications.
- Led cloud modernization migrating several mission-critical services to Microsoft Azure, implementing Terraform and Ansible IaC practices that standardized environment provisioning and reduced configuration drift.
- Standardized CI/CD delivery across nine distinct runtimes, entering most ecosystems with no prior experience and reverse-engineering each before automating it.

**Key technologies:** Microsoft Azure, Terraform, Ansible, Python, Dynatrace, Splunk, Azure DevOps, GitHub Actions

### Desjardins — Senior DevOps Engineer *(Contract)*

**Montréal, QC (Remote) | October 2025 – March 2026** — *concurrent engagement alongside the Énergir role*

- Automated provisioning of on-demand environments using Kubernetes and ArgoCD, giving administrators repeatable, isolated environments for safely testing configuration changes and upgrades.
- Designed and built a Python/FastAPI service that tested the configuration of ~250 enterprise Artifactory repositories every 4 hours and published results to Dynatrace.
- Built Splunk alerting to detect manual configuration changes made outside the CI/CD pipeline.

**Key technologies:** Kubernetes, ArgoCD, Python, FastAPI, Dynatrace, Splunk, Docker, Helm

### Tink — DevOps Engineer

**Montréal, QC | January 2018 – August 2021**

- Participated in 24/7 on-call for all production systems and reduced paging frequency from roughly one page every two rotations to one every four or five through root-cause analysis and preventive engineering.
- Built self-healing automation for a recurring, unstable Elasticsearch cluster — monitoring detected when the service became unresponsive and automatically triggered a Bash remediation script to restart it, so a known failure mode no longer required a human page.
- Implemented centralized ELK Stack logging and alerting across a fleet of 600+ Linux servers to accelerate incident diagnosis.
- Built the compute, caching, and database layers of a client's full AWS migration target environment — EC2, S3, Route 53, self-managed memcached, serverless relational database — with no prior AWS experience; the client cancelled the migration before cutover, and resources were provisioned by hand rather than through Terraform or CloudFormation.
- Managed fleet configuration as code via Puppet and Spacewalk, including automated kernel-update reboots reduced to a monthly verification check with near-zero downtime.

**Key technologies:** ELK Stack, Bash, AWS (EC2, S3, Route 53, VPC), Puppet, Spacewalk, Linux, networking, incident response

### SOVO Technologies — Lead Technician to Software Engineer

**Montréal, QC | November 2008 – December 2017**

- Owned company IT infrastructure, delivered a zero-downtime server relocation, and introduced redundancy that eliminated single points of failure.
- Wrote production software for approximately seven years before the title formalized it.

**Key technologies:** C++, Java, SQL, Windows Server, VMware vSphere, Active Directory

## Education

**Bachelor of Automated Manufacturing Engineering** — École de Technologie Supérieure, Montréal, QC | 2005 – 2016

**DCS in Computer Science Technology** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
