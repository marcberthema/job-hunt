# Fractional Consulting Profile — Marc Berthelette

> Positioning source for fractional and part-time consulting. All factual claims derive from
> `profile.md`, which remains authoritative. This file packages that evidence for consulting
> buyers; it does not replace or amend the master profile.

## Headline

**Fractional Senior Platform & DevOps Engineer**

**Azure | CI/CD | Terraform | Reliability | Automation**

## Value Proposition

I help engineering teams turn fragile, manual, or inconsistent infrastructure and delivery
work into reliable systems their developers can actually use. I bring senior Platform and
DevOps capability to organizations that need better CI/CD, infrastructure automation,
observability, or operational reliability but do not need another full-time hire.

My work typically combines diagnosis, hands-on implementation, and team enablement. I do not
stop at delivering a script: I learn how the system and its users actually work, build the
repeatable platform around the problem, and leave the team with standards and tooling it can
operate.

I am most useful to CTOs, engineering leaders, and platform teams in growing or regulated
organizations where developers are carrying infrastructure work, delivery practices differ
between teams, or recurring operational problems need senior ownership.

## Problems I Solve

- Manual, fragile, or inconsistent deployment processes across applications and technology
  stacks
- CI/CD pipelines that produce noise, obscure ownership of failures, or have become difficult
  to maintain
- Cloud environments that need repeatable provisioning and consistent configuration through
  Terraform and Ansible
- Platform work that needs to become a maintained internal capability rather than a collection
  of one-off scripts
- Limited visibility into service, repository, fleet, or deployment health
- Recurring operational failures that consume human attention and should be diagnosed,
  monitored, or safely automated
- Platform changes that need a safer validation path before production rollout
- Teams that need senior technical direction, standards, and enablement without adding a
  full-time senior engineer

## Core Offers

### 1. CI/CD and Delivery Modernization

The strongest lead offer. Assess and improve delivery workflows, quality gates, pipeline
maintainability, failure reporting, and deployment automation across one or many application
stacks.

Typical outcomes include:

- A current-state assessment and prioritized modernization roadmap
- Automated paths replacing manual deployment steps
- Reusable pipeline patterns and consistent quality gates
- Validation environments or pre-merge controls for risky changes
- Clearer failure reporting so application and platform teams know who owns a fix
- Documentation and enablement that turn delivered tooling into adopted practice

### 2. Fractional Platform & DevOps Engineering

Ongoing senior ownership for a defined platform backlog: Azure infrastructure, Terraform and
Ansible, CI/CD, deployment systems, observability, reliability improvements, and technical-debt
reduction. Best suited to a team that needs an autonomous builder and advisor for a limited
number of hours each week.

### 3. Reliability and Operational Visibility

Find recurring failure modes, establish useful health signals and dashboards, improve root-cause
analysis, and automate safe responses to known problems. This can begin as a focused assessment
and continue through implementation.

### 4. Infrastructure and IaC Assessment

Review Azure infrastructure, Terraform/Ansible practices, environment consistency, deployment
controls, monitoring, and operational risks. Deliver a concrete findings report and sequenced
implementation roadmap, with follow-on implementation available.

This offer should initially be sold as a scoped assessment, not as a claim of architecture depth
across every cloud. Marc's strongest cloud evidence is Azure. His AWS experience is a bounded,
six-month greenfield target-environment build that did not reach production, and he has no GCP
experience.

## Selected Evidence

### Delivery modernization across 12 teams

At Énergir, standardized CI/CD across nine runtimes—Java, Node.js, Python, Spark, Oracle,
CloudFoundry, MuleSoft, Salesforce, and Databricks—for 12 application teams and more than 70
applications. The work moved teams from manual deployment toward automated pipelines with
built-in quality gates. Recurring enablement sessions helped teams adopt the platform practices
without Marc having reporting authority over them.

### A safer Salesforce release path

Asked to replace legacy Salesforce ANT deployment scripts, Marc learned the platform, migrated
delivery to the official Salesforce CLI, and went beyond the original scope by building a
validation pipeline. Every candidate merge was deployed to a dedicated sandbox and tested. A
team that had frequently missed deployment windows missed only one after the pipeline went live
and established a dependable every-other-Tuesday release cadence.

### Automation where an earlier attempt had failed

At Énergir, took an Oracle team from fully manual deployment to automated delivery after an
earlier implementation attempt had failed. This is representative of Marc's best use case:
unfamiliar, cross-system problems that require reverse-engineering before they can be automated.

### Continuous health signals for 250 repositories

During a six-month Desjardins contract, designed and built a Python/FastAPI service that tested
the configuration of approximately 250 remote JFrog Artifactory repositories every four hours
and published technology-specific health dashboards to Dynatrace. The validation logic was made
tool-agnostic and the test set configurable, allowing the same harness to become a regression
safety net for an enterprise Artifactory upgrade.

### Repeatable platform test environments

At Desjardins, automated on-demand Artifactory environments with Kubernetes and ArgoCD so system
administrators could safely test configuration changes and upgrades. Also implemented artifact
retention policies and Splunk alerts for manual changes made outside the delivery pipeline,
improving operational visibility and auditability.

### Fleet-scale automation and visibility

At Tink, centralized Jenkins Pipeline as Code for a team of 10–15 developers supporting more
than 80 applications for over 20 clients. Marc also automated OS patching across more than 600
servers, reducing the recurring process to a monthly verification check with near-zero downtime.

Without being assigned the work, he designed and built a software-inventory platform for that
fleet. It exposed CVE risk, end-of-life software, SSL/TLS certificate scoring, and other
operational information to product owners who previously had no fleet-wide view.

### Automated response to a known reliability problem

For a recurring unstable Elasticsearch cluster at Tink, monitoring detected an unresponsive
service and triggered a Bash remediation script. A known failure mode no longer required a human
to be paged for the same manual restart.

## Why Clients Bring Me In

- **I expand a narrow assignment into the system the client actually needs.** The Salesforce
  validation gate, Desjardins validation harness, and Tink inventory platform show the same
  pattern at three organizations.
- **I learn unfamiliar platforms under a delivery clock.** Énergir required work across nine
  runtimes; the Desjardins engagement added hands-on Kubernetes, ArgoCD, GitHub Actions, and
  JFrog Artifactory work.
- **I combine implementation with adoption.** I have driven platform practices across 12 teams
  without formal authority through reusable tooling, documentation, and recurring enablement.
- **I build internal products, not disconnected scripts.** My strongest work gives technical and
  non-technical users ongoing visibility, safer workflows, or repeatable self-service.
- **I understand regulated enterprise environments.** My recent experience spans energy and
  financial services.
- **I am ready for B2B work.** I am incorporated in Canada and work fluently in French and
  English.

## Technical Capabilities

- **Cloud and infrastructure:** Microsoft Azure; Terraform; Ansible; Linux; networking and
  infrastructure fundamentals
- **Delivery and platform engineering:** Azure DevOps; Jenkins; GitHub Actions; Git; reusable
  pipeline design; quality gates; deployment automation
- **Containers and orchestration:** Docker; hands-on Kubernetes and ArgoCD delivery-environment
  automation
- **Reliability and observability:** Dynatrace; Splunk; ELK Stack; PRTG; health checks; dashboards;
  alerting; root-cause analysis; automated remediation
- **Automation and software:** Python; FastAPI; Bash; Java; SQL; API and internal-tool development
- **Enterprise platforms:** JFrog Artifactory; Salesforce delivery tooling; CloudFoundry;
  Databricks; MuleSoft; Oracle delivery automation

## Engagement Model

**Monthly retainer (preferred):** ongoing ownership of defined platform and reliability problems,
with agreed access, response expectations, boundaries, and a regular planning/check-in cadence.
The monthly fee is for continuity, responsibility, and outcomes; it has no hours attached and is
not presented as a prepaid time bundle.

**Hourly part-time engagement (transitional):** remote, flexible work at $90+/hour CAD where a
client is not ready for a retainer. Internal capacity will usually be kept around 8–15 hours per
week, but this is a bridge to the retainer model rather than the positioning Marc leads with.

**Focused project:** a defined assessment, modernization, or automation outcome with agreed
deliverables and a handoff. Suitable starting points include a CI/CD assessment, Azure/IaC
review, deployment-risk review, or operational-visibility assessment.

**Working style:** primarily asynchronous, outcome-oriented, and hands-on. Limited scheduled
meetings; no routine 24/7 on-call. Available to Canadian and international clients where the work
can legally be delivered through a Canadian corporation.

## Best-Fit Clients

- Startups, scale-ups, and small or mid-sized engineering organizations whose infrastructure has
  outgrown developer-owned, ad hoc practices
- Platform teams with a specific modernization or reliability backlog but insufficient senior
  capacity
- Organizations operating primarily in Azure or needing cloud-agnostic delivery and platform
  improvements
- Energy, financial-services, and other regulated organizations where operational controls,
  auditability, and safe change matter
- Leaders who want a consultant to diagnose and recommend, then remain accountable for hands-on
  delivery

## Qualification Boundaries

An engagement is a poor fit when it requires fixed full-time availability, routine 24/7 on-call,
meeting-heavy staff augmentation, junior ticket execution, or deep cloud-native ownership in
AWS or GCP. Kubernetes is a supporting capability backed by recent delivery work, not yet a claim
of deep cluster-administration or large-scale Kubernetes architecture expertise.

Before accepting side consulting alongside employment, confirm that the employment agreement
permits outside work and that its confidentiality, conflict-of-interest, and IP-assignment terms
do not capture the engagement.

## Internal Positioning Decisions

### Offer ranking

1. **CI/CD and delivery modernization** — most marketable and most strongly evidenced, with
   unusually broad multi-runtime and cross-team scope.
2. **Fractional platform and DevOps engineering** — credible umbrella offer, especially for
   Azure-centric teams, but it should be anchored to a concrete backlog rather than sold as vague
   senior availability.
3. **Reliability and operational visibility** — strong evidence from Desjardins, Énergir, and
   Tink; particularly credible when paired with implementation rather than executive-level SRE
   transformation language.
4. **Infrastructure/IaC assessment** — viable Azure-focused entry offer. Keep claims narrower
   than cloud architecture consulting and do not imply AWS IaC or GCP experience.

### Messaging guardrails

- Lead with business problems and delivered systems, not a technology inventory.
- Lead cloud positioning with Azure.
- Do not use an architect-first title; operational ownership and platform delivery are stronger.
- Do not describe Tink's manually provisioned VMs as full IaC or imply its AWS environment was
  operated in production.
- Do not imply deep Kubernetes administration, AWS architecture ownership, or any GCP exposure.
- Do not publish a rate in general profile copy. The internal floor for hourly part-time work is
  $90/hr CAD. The target model is a monthly retainer for defined access, responsibility, and
  outcomes with no hours attached; never market it as a bundle of prepaid time.
- Do not mention personal products or projects in consulting marketing until `profile.md` removes
  that restriction.

### Rollout sequence

This profile is ready to serve as the source for platform-specific copy. Active fractional
sourcing should follow the sequencing in `profile.md`: secure the primary role first, review its
outside-work and IP terms, stabilize, and only then invest meaningful time in outbound fractional
client acquisition.
