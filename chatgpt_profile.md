# Marc Berthelette — Job Search / CV Project Context

## Purpose

This is the consolidated working context for Marc Berthelette's job-search, career-profile, resume, CV, and application project. It combines the information available in the current conversation and the shared-chat content pasted by the user.

The intended system is:

`profile.md` → permanent CV template → master 2-page CV → job posting analysis → tailored CV → PDF → recruiter/application messaging → feedback loop.

`profile.md` is the complete career source of truth. It should contain more information than any individual CV and should not be constrained to two pages.

---

## Career Positioning

Target senior-level roles, especially approximately $175k+ CAD:

- Senior SRE
- Staff SRE
- Senior Platform Engineer
- Staff Platform Engineer
- Principal DevOps Engineer
- Senior DevOps Engineer
- Cloud Platform Engineer
- DevOps / Cloud Infrastructure Architect

Core differentiator:

**Reliability + ownership + automation + production engineering**

Emphasize production ownership, SRE principles, automation, root-cause analysis, prevention of recurring incidents, self-healing systems, platform engineering, CI/CD standardization, Infrastructure as Code, observability, developer enablement, technical leadership, and enterprise scale.

Avoid positioning Marc as simply a generic DevOps engineer who knows many tools.

---

## Contact / Identity

- Name: Marc Berthelette
- Location: Smiths Falls, Ontario, Canada
- Work preference: Remote
- Email: marc.berthelette@gmail.com
- French: Native
- English: Fluent
- Canadian incorporated
- Available immediately

---

## Professional Summary

Senior DevOps / Platform Engineer with 18 years of experience building, operating, and improving production systems across regulated and enterprise environments. Specializes in site reliability, platform engineering, CI/CD, infrastructure automation, observability, and production ownership.

Known for taking ownership of complex systems, identifying what actually needs to be monitored, eliminating recurring failure modes, and replacing manual or fragile processes with controlled automation. Experienced across 24/7 production and on-call environments, including client-facing and mission-critical systems.

Built and standardized delivery platforms supporting 12 teams and 70+ applications, automated infrastructure and operating-system maintenance across 600+ servers, and developed internal tooling supporting approximately 250 software repositories across seven technology ecosystems.

Strong believer in engineering for prevention rather than repeatedly responding to the same incident: root-cause the problem, fix it permanently when possible, and automate reliable remediation when it is not.

---

## Scale / Career Highlights

- 18 years of experience
- 70+ applications
- 12 teams
- 9 technology/runtime ecosystems
- Approximately 250 software repositories
- 600+ servers
- 24/7 production and on-call experience
- Mission-critical and client-facing systems
- CI/CD standardization
- Infrastructure automation
- Reliability improvement
- Self-healing production systems
- Cloud modernization
- Developer enablement
- Technical leadership

---

# Professional Experience

## ÉNERGIR — Montréal, QC

**Senior DevOps Engineer**  
**September 2021 – Present**

### Context

Own and evolve DevOps and delivery infrastructure supporting enterprise applications across multiple technology stacks. Provide technical leadership, platform engineering, reliability improvements, automation, and developer enablement across 12 teams and 70+ applications.

### Achievements / Responsibilities

- Standardized CI/CD practices across 9 technology runtimes, including Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, and Databricks.
- Built reusable delivery patterns allowing multiple development teams to adopt consistent deployment practices without independently reinventing pipelines.
- Own key DevOps software and delivery infrastructure, including Jenkins, Nexus, HashiCorp Vault, and Jenkins pipeline infrastructure.
- Re-engineered Oracle deployment automation after a previous automation attempt had failed, turning a manual and unreliable process into a dependable deployment workflow.
- Rebuilt Salesforce delivery using Salesforce CLI, replacing the previous ANT-based approach.
- Introduced sandbox validation and improved the observed Salesforce deployment success rate from approximately 80% to 90–95%.
- Reduced manual deployment effort.
- Separated application-code failures from platform/pipeline failures, eliminating false-positive troubleshooting and making failures significantly easier to diagnose.
- Supported cloud modernization efforts and migration of 5–10 mission-critical services to Azure.
- Develop Terraform automation using reusable modules, extending infrastructure from bare virtual machines through system configuration and required plugins.
- Use Ansible and Infrastructure as Code practices to reduce configuration drift and make infrastructure changes repeatable.
- Design monitoring and observability around meaningful failure signals rather than simply collecting metrics.
- Use Dynatrace, Splunk, and related tooling for operational visibility.
- Perform root-cause analysis and implement automated remediation to prevent recurring incidents and unnecessary manual intervention.
- Provide technical guidance, code reviews, mentoring, and best-practice support across development and DevOps teams.
- Led technical direction and acted as an informal technical lead during earlier years in the role.
- Helped teams adopt cleaner engineering and shift-left practices.
- Conduct recurring enablement sessions to improve adoption of standardized DevOps practices.
- Use AI-assisted development as an engineering accelerator while applying strict human validation, testing, review, and controlled promotion of generated code.

### Technologies

Jenkins, Nexus, HashiCorp Vault, Terraform, Ansible, Azure, Dynatrace, Splunk, Salesforce CLI, CloudFoundry, MuleSoft, Databricks, Java, Node.js, Python, Spark, Oracle.

---

## DESJARDINS — Montréal, QC / Remote

**Senior DevOps Engineer — Contract**  
**October 2025 – March 2026**

### Important Context

This was a full-time concurrent consulting engagement delivered alongside the Énergir role. The contract was initially planned for three months and extended to six months following the departure of another engineer.

The concurrent arrangement should be made clear on resumes so overlapping dates are not interpreted as an employment-history discrepancy.

### Achievements / Responsibilities

- Focused on JFrog Artifactory reliability, automation, monitoring, and operational tooling.
- Hardened and operationalized JFrog Artifactory infrastructure and supporting processes.
- Designed and implemented a Python/FastAPI health-monitoring service covering approximately 250 remote repositories across seven technology ecosystems.
- Took an existing shell-based monitoring concept and implemented the broader solution.
- Made the architecture more flexible, configurable, and technology-agnostic.
- Built configurable validation logic so the same monitoring framework could evaluate repositories without being tightly coupled to a particular technology or implementation.
- Integrated monitoring results with Dynatrace dashboards for operational visibility.
- Reused the validation framework to reduce risk during a JFrog upgrade by providing automated verification of repository health and expected behaviour.
- Automated on-demand Artifactory provisioning using Kubernetes and ArgoCD.
- Implemented repository lifecycle policies to control retention and reduce operational overhead.
- Added Splunk alerting for manual changes made outside approved CI/CD processes.
- Improved visibility into configuration drift and unauthorized operational changes.

### Technologies

Python, FastAPI, Bash, JFrog Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk, CI/CD.

---

## TINK — Montréal, QC

**DevOps Engineer**  
**January 2018 – August 2021**

### Context

Owned client-facing production systems and DevOps infrastructure in a highly operational environment with extensive 24/7 on-call responsibility. Focused heavily on eliminating recurring incidents through root-cause analysis, automation, monitoring, and preventative engineering.

### Achievements / Responsibilities

- Centralized Jenkins Pipeline as Code across approximately 10–15 developers, 80+ applications, and 20+ clients, creating a consistent and maintainable delivery platform.
- Played a significant role in the architecture and technical design of internal tooling and centralized Jenkins infrastructure.
- Automated operating-system patching across 600+ servers, including kernel updates and reboots, with monthly verification and near-zero downtime.
- Built infrastructure automation using Puppet and Spacewalk, with operational visibility through ELK.
- Developed an internal software inventory platform covering the 600+ server fleet, using Python and Spacewalk APIs to automatically collect and expose software information.
- Connected inventory information to internal chat-based visibility, making it easier for teams to identify installed software, CVEs, end-of-life components, and SSL/TLS security concerns.
- Reduced recurring production incident volume substantially: an environment that initially generated approximately 1–3 incident calls per week reached periods where a week or more could pass without an incident.
- Applied root-cause analysis to recurring failures and either implemented permanent fixes or developed automated remediation when permanent remediation was outside the engagement scope.
- Built a self-healing response for an unstable Elasticsearch cluster: monitoring detected when Elasticsearch became unresponsive and triggered a Bash remediation script to restart the service automatically.
- Avoided unnecessary human paging for a known failure mode.
- Provided technical design and validation support for products and systems developed by other teams.
- Supported an AWS migration initiative involving EC2, S3, Route 53, VPC, managed/serverless database services, and self-managed caching infrastructure.
- The AWS initiative was ultimately cancelled due to projected operational cost of maintaining the target environment.
- Maintained extensive 24/7 production on-call responsibility, including troubleshooting incidents outside the immediate technology stack by applying broad systems knowledge and structured diagnosis.

### Technologies

Jenkins, Puppet, Spacewalk, Python, Bash, ELK, Elasticsearch, AWS, EC2, S3, Route 53, VPC, databases, caching infrastructure.

---

## SOVO TECHNOLOGIES — Montréal, QC

**Lead Technician → Software Engineer**  
**November 2008 – December 2017**

### Context

Progressed from infrastructure leadership into software engineering while maintaining ownership of the company's IT infrastructure, production systems, and internal software.

### Achievements / Responsibilities

- Owned the organization's IT infrastructure and production systems, including server infrastructure, networking, virtualization, backups, and recovery.
- Designed redundant infrastructure and executed a zero-downtime server relocation.
- Served as a final technical and QA gate for production changes and systems.
- Managed a team of technicians, including scheduling, training, delegation, and technical guidance.
- Developed production software for approximately seven years, including before the Software Engineer title was formally established.
- Built a scheduling system and software supporting voice-recognition evaluation and multilingual dictionary infrastructure.
- Developed software using C++, Java, and SQL.
- Administered Windows Server and Linux environments, Active Directory, VMware, Cisco routing/firewalls/VPN infrastructure, and backup/recovery systems.
- Combined software engineering with infrastructure ownership to deliver and support complete production solutions.

### Technologies

C++, Java, SQL, Windows Server, Linux, Active Directory, VMware, Cisco, networking, virtualization, backup/recovery.

---

# Education

## École de technologie supérieure (ÉTS) — Montréal, QC

**Bachelor of Automated Manufacturing Engineering**  
2005–2016

## Cégep André-Laurendeau — Montréal, QC

**DCS, Computer Science Technology**  
2002–2005

---

# Technical Toolkit

## Cloud & Platforms

Azure · AWS · CloudFoundry · Kubernetes · Docker · ArgoCD

## CI/CD & DevOps

Jenkins · Azure DevOps · GitHub Actions · JFrog Artifactory · Nexus · Salesforce CLI · HashiCorp Vault

## Infrastructure as Code

Terraform · Ansible · Puppet · Spacewalk

## Observability & Operations

Dynatrace · Splunk · ELK · PRTG · Monitoring · Alerting · Incident Response · RCA

## Languages & Automation

Python · FastAPI · Bash · C++ · Java · SQL · NoSQL

## Operating Systems & Infrastructure

Red Hat Linux · Ubuntu · Windows Server · VMware · Active Directory · Apache · Nginx · Cisco

## Engineering Practices

SRE · Platform Engineering · CI/CD · Infrastructure as Code · Automation · Reliability Engineering · Technical Leadership · Code Review · Developer Enablement · AI-Assisted Development & Code Governance

---

# Strongest Recruiter Hooks

1. Enterprise CI/CD standardization across 12 teams, 70+ applications, and 9 technology/runtime ecosystems.
2. Large-scale infrastructure automation across 600+ servers, including OS/kernel patching with near-zero downtime.
3. Python/FastAPI repository health platform covering approximately 250 repositories across seven technology ecosystems.
4. Salesforce CI/CD modernization using Salesforce CLI and sandbox validation, improving observed deployment success from approximately 80% to 90–95%.
5. Production incident reduction from approximately 1–3 calls/week to periods where a week or more could pass without an incident.
6. Self-healing Elasticsearch remediation that detected unresponsiveness and automatically restarted the service.
7. Azure modernization and migration of 5–10 mission-critical services.
8. Technical leadership, architecture, code review, mentoring, and developer enablement.

---

# Interview Stories

## Oracle Deployment Automation

A previous Oracle automation attempt had failed. Marc re-engineered the approach and converted a manual/unreliable process into a dependable deployment workflow.

Themes:
- Failure analysis
- Architecture
- Automation
- Reliability
- Production delivery

## Salesforce CI/CD

Rebuilt Salesforce delivery using Salesforce CLI instead of ANT, added sandbox validation, and improved observed deployment success from approximately 80% to 90–95%.

Themes:
- Modernization
- CI/CD
- Release engineering
- Quality gates
- Measurable improvement

## Artifactory Repository Monitoring

Created a Python/FastAPI monitoring service covering approximately 250 remote repositories across seven technology ecosystems.

Themes:
- Platform engineering
- Generic architecture
- API design
- Monitoring
- Automation
- Technology-agnostic engineering
- Upgrade safety

## 600+ Server Automation

Automated OS/kernel patching and reboot processes across 600+ servers with monthly verification and near-zero downtime.

Themes:
- Scale
- Infrastructure automation
- Risk management
- Reliability
- Operational maturity

## Software Inventory Platform

Built a software inventory platform using Python and Spacewalk APIs across 600+ servers, exposing information useful for CVE, end-of-life, and SSL/TLS analysis.

Themes:
- Internal tooling
- Security visibility
- Automation
- Fleet management
- Operations enablement

## Elasticsearch Self-Healing

Built monitoring that detected an unresponsive Elasticsearch service and automatically restarted it through Bash remediation.

Themes:
- SRE
- Self-healing
- Alert fatigue reduction
- Automation
- Operational reliability

## Incident Reduction

Used root-cause analysis and preventative engineering to substantially reduce recurring production incidents, from approximately 1–3 calls/week to periods where a week or more could pass without an incident.

Themes:
- Reliability
- Production ownership
- RCA
- Prevention vs reaction
- Measurable operational impact

## AWS Migration

Supported an AWS migration involving EC2, S3, Route 53, VPC, managed/serverless database services, and self-managed caching infrastructure. The initiative was ultimately cancelled due to projected operational cost.

Themes:
- Cloud architecture
- Cost awareness
- Technical evaluation
- Knowing when not to proceed

---

# CV Design Requirements

The permanent CV should use a modern, professional, senior-engineer / technical-executive appearance.

Recommended:
- 2 pages for application CVs
- White background
- Dark charcoal/black text
- One restrained accent colour
- Strong typography
- Clear hierarchy
- Plenty of whitespace
- Company names visually prominent
- Job titles and dates easy to scan
- Metrics easy to notice
- ATS-friendly
- No skill bars
- No star ratings
- No photograph
- No giant decorative sidebar
- No excessive icons
- No overly graphical Canva-style design
- Avoid complicated layouts that ATS parsers can scramble

Desired impression:

**Experienced senior/staff engineer at a serious technology company.**

English and French versions should use the same visual identity.

The template stays fixed; content emphasis changes.

---

# Planned File / Workflow Structure

```text
Marc Job Search/
│
├── profile.md
│
├── templates/
│   └── marc-modern-cv
│
├── resumes/
│   ├── senior-sre.md
│   ├── staff-platform-engineer.md
│   ├── devops.md
│   └── azure-platform.md
│
└── pdf/
    ├── Marc_Berthelette_Senior_SRE.pdf
    ├── Marc_Berthelette_Platform_Engineer.pdf
    └── Marc_Berthelette_DevOps.pdf
```

---

# Job Application Workflow

1. Provide a job posting.
2. Analyze seniority, responsibilities, technologies, leadership expectations, keywords, SRE/platform/DevOps emphasis, likely compensation, company context, and concerns.
3. Compare the role against `profile.md`.
4. Identify strongest matches, partial matches, gaps, accomplishments, technologies, and interview stories.
5. Tailor the CV without inventing experience.
6. Generate the 2-page PDF using the permanent template.
7. Generate recruiter/application messaging when useful.
8. Track results and use feedback to improve the strategy.

---

# Job Search Strategy

For a $175k+ search, earlier guidance was:

**2–4 highly targeted applications/day + networking/referrals + recruiter outreach**

rather than blindly submitting 8 generic applications per day.

Quality of targeting matters more than raw application count.

Useful activities:
- Direct company research
- Recruiter outreach
- Referrals
- LinkedIn networking
- Targeted applications
- Market compensation research
- Company research
- Role-level fit analysis

---

# Job Market Research

The workflow should support questions such as:

- What is the current Canadian market for Senior/Staff SRE roles?
- Are $175k–$200k remote positions realistic?
- Which companies hire this profile?
- Which titles produce the best results?
- Is SRE, Platform Engineering, DevOps, or Cloud Infrastructure the strongest market?
- Which technologies are most valuable for this profile?
- What compensation should be expected?
- Is a particular posting actually senior/staff level?
- Is the employer likely to support remote work from rural Ontario?

Use current web research for current information. Use deep research for comprehensive multi-source market analysis when appropriate.

---

# AI Tool Strategy

The user already pays for Claude.

Important conclusion:

**Claude can absolutely accomplish this project.**

There is no need to pay for ChatGPT simply because Claude cannot handle it.

Potential strategy:
- Maintain one canonical `profile.md`.
- Use ChatGPT and Claude as complementary systems if desired.
- Use one system to generate and another to critique.
- Do not maintain two conflicting career databases.

Possible quality-control workflow:

```text
profile.md
    ↓
CV generated by AI #1
    ↓
AI #2 critiques:
- exaggerations
- ATS issues
- weak positioning
- missing accomplishments
- unclear claims
    ↓
final CV
```

The best comparison is to give both systems the same `profile.md` and same job posting and compare the outputs.

---

# ChatGPT Plan Discussion

The user previously hit a Free-tier usage limit.

Discussion conclusions:
- Free can perform many required tasks.
- Go provides more usage than Free.
- Plus provides higher limits and access to more capable reasoning/tool configurations.
- For this workflow, Plus was described as the more comfortable option.
- However, because the user already pays for Claude, there is no need to automatically subscribe to ChatGPT Plus just for this project.
- The workflow can be built and tested here first.
- Plan details can change, so current OpenAI documentation should be checked before making a purchase decision.

---

# Important Employment-Date Concern

Énergir:
**September 2021 – Present**

Desjardins:
**October 2025 – March 2026**

Desjardins was a legitimate **concurrent consulting engagement** delivered alongside Énergir.

Resume wording should make this explicit:

> Full-time concurrent engagement focused on JFrog Artifactory reliability, automation, monitoring, and operational tooling. Contract initially planned for three months and extended to six months following the departure of another engineer.

---

# Original Resume Assessment

The original CV was assessed as having strong experience but weaker positioning.

Key conclusion:

**The experience is there for the $175k+ target. The resume is the bigger problem, not the technical background.**

The original resume read more like:

> Very experienced DevOps guy who does lots of things.

Desired positioning:

> Senior/principal-level engineer worth $175k–$200k+.

Strong accomplishments were buried in paragraphs.

Example of a strong accomplishment:

> Standardized CI/CD delivery across nine distinct runtimes.

This communicates scope and standardization and should be surfaced prominently when relevant.

---

# Overall Six-Step Game Plan

1. **Build `profile.md`** — complete career source of truth.
2. **Build one permanent CV template** — modern, professional, ATS-friendly, consistent.
3. **Create the master 2-page CV** — broad Senior/Staff SRE + Platform + DevOps positioning.
4. **Analyze each job posting and market** — fit, compensation, priorities, keywords, gaps.
5. **Generate a tailored 2-page CV and application messaging** — same visual identity, different emphasis.
6. **Track results and improve the strategy** — without constantly rewriting the underlying career history.

---

# Core Principle

The system should make Marc's job search feel like software engineering:

**One source of truth → reusable template → targeted build → validation → release.**

`profile.md` is the source code.

The CV template is the build system.

The job description is the target specification.

The tailored PDF is the release artifact.

Recruiter/interview feedback is production telemetry.

---

# Source Integrity Rules

- Treat this as a working source of truth, but verify ambiguous details against original source documents when available.
- Do not invent accomplishments.
- Do not inflate metrics.
- Do not turn approximate numbers into exact numbers without confirmation.
- Preserve distinctions such as supported, developed, owned, led, and participated.
- Preserve the concurrent nature of the Desjardins engagement.
- Do not claim certifications unless confirmed.
- Do not add technologies merely because they are adjacent to listed technologies.
- Tailoring changes emphasis, not facts.

---

# Future `profile.md` Improvements

When the original CV and/or original `profile.md` become available, merge them into this canonical file.

Potential additional sections:

- Career Positioning
- Target Roles
- Target Compensation
- Executive Summary Variants
- Career Highlights
- Responsibilities by Role
- Achievements by Role
- Technology Matrix
- Architecture Examples
- Reliability Examples
- Leadership Examples
- Automation Examples
- Cloud Examples
- Security / Compliance Examples
- Developer Enablement Examples
- Incident Stories
- Failure / Recovery Stories
- Metrics
- Interview Stories
- Resume Bullet Bank
- Recruiter Messaging
- Interview Preparation

