# Elastic — Hiring Manager Interview Prep

**Role:** Senior Site Reliability Engineer (Observability & Analytics) — Platform Infra
**Interviewer:** Lindsay Sandall, hiring manager (SRE Manager – Platform Security), US west coast
**Date:** 2026-10-01
**Posting:** https://builtin.com/job/senior-site-reliability-engineer-observability-analytics-platform-infra/11250234
**Applied with:** `resume/tailored/2026-09-18-elastic-senior-site-reliability-engineer-observability-analytics-en.md` and the matching cover letter
**Comp on posting:** $138,300–$185,900 CAD base, no variable. Remote, Canada.

Updated the night of 2026-09-30 after a long working session. Sections 0 and 9 are the ones to reread in the morning.

---

## 0. Morning-of summary

**The role in one sentence:** "This team runs the observability platform that Elastic's Cloud engineers depend on to see how production is behaving, and it produces the SLA and SLO measurements for the hosted and serverless offerings."

**Your users would be Elastic's own engineers, not customers.** Do not describe the job as keeping customers' clusters healthy.

**Three things to get across:**
1. You have done the core of this job: 24/7 on-call, production Linux at fleet scale, Python, and running the Elastic Stack in production.
2. You build internal platforms that tell engineers the truth (Desjardins health service, Tink inventory, Énergir failure split). The posting describes the team as "infrastructure that tells Elastic the truth about its own platform."
3. You state your gaps precisely and don't bluff: no Go, no formal SLOs, Kubernetes practical not deep, Elastic experience from 2018–2021.

**Why this job (true, so safe to use):** you spent five years pushing toward good practice in an immature environment, without authority, and you want to work where that practice is the default.

**Expectation:** winnable conversation; fit about 6–7 out of 10; rough odds of an offer about one in five. Keep the rest of the pipeline moving.

---

## 1. Who you are talking to

**Lindsay Sandall** (from LinkedIn search snippets only; the profile would not load, so read it yourself):

- Portland, Oregon area. Pacific time, 3 hours behind you.
- Recently joined Elastic as "SRE Manager – Platform Security."
- Before Elastic: HeartFlow (AI medical-imaging SaaS, regulated), DevOps Engineer up to Senior DevOps Manager, led DevOps/SRE through to the IPO.
- Oregon State University. No public talks, GitHub or writing found.

**How to talk to them:**

- A career DevOps/SRE person who became a manager. They have carried a pager and run Terraform, so vague operational answers will be noticed.
- New to Elastic. Expect questions about how you operate (incidents, ownership, teamwork) more than Elasticsearch internals.
- Security is in their title. Present yourself as an SRE who thinks about security, not as a security engineer.
- Their HeartFlow path (regulated, fast-growing, small team) is close to your own shape.

**The two hiring managers.** The recruiter checked your Kubernetes gap with "Clem", the other hiring manager, almost certainly **Klim Markelov** (Engineering Manager, Amsterdam; backend/Ruby and Swiftype background; knows Elasticsearch from the inside). Your understanding is that the two managers cover different regions, Europe and the Americas. If so, Lindsay is the person you would report to.

**Your time zone is an asset.** Eastern overlaps with Amsterdam in the morning and Portland in the afternoon. Say so if time zones come up.

---

## 2. What the team does

**The posting, word for word:**

> "Platform Observability & Analytics runs the infrastructure that tells Elastic the truth about its own platform. The observability clusters show Cloud engineers how production is behaving right now, and the analytics pipelines show the business how the platform and the products get used over time."
>
> "This role sits on the observability side. We run 200+ hosted deployments across every supported cloud region, ingesting logs, metrics and traces for all of Elastic Cloud, plus the SLA and SLO monitoring for ESS and Serverless."

The recruiter confirmed the same split: two halves, and you would be on Observability.

**The layers:**

1. **A customer's deployment.** The customer uses it for their own data. Not your concern.
2. **The internal observability clusters.** Cloud engineers use these to see how the platform hosting customer deployments is behaving. This is what the role owns: the 200+ deployments are these clusters, and you would provision, configure, upgrade and be on call for them.
3. **Whatever watches layer 2.** Unknown. This is the "who monitors the monitor" question.

**"Production"** here is Elastic Cloud: the hosted offering (ESS) and Serverless, in regions across AWS, Azure and Google Cloud, all running in Elastic's own cloud accounts.

**Things that follow from this (inference, not confirmed):**

- New customer deployments emit telemetry automatically, so the team's load grows with the customer base. Capacity planning is ongoing.
- Missing data is a failure in itself. Detecting a silent gap is likely part of the job. The Desjardins service did the same thing for 250 repositories.
- SLOs are often measured across the whole service; an SLA is owed per customer. So SLA monitoring probably means accurate per-customer availability numbers.
- Natural SLOs for the platform itself: **freshness** (how long until data is searchable) and **completeness** (did everything arrive).

**The infrastructure is named in the posting as "ECH, ECE, and ECK":** hosted, self-managed enterprise, and on Kubernetes. Kubernetes is part of the picture even though it was cleared as not a hard gap.

**Monitoring versus observability.** Monitoring answers questions you knew to ask in advance (is it up, page if not). Observability lets you ask new questions after something unexpected. Elastic's current product does both: alerting rules, synthetic checks (the PRTG-style part), built-in SLO tracking with burn-rate alerts, application tracing. That is well beyond the 2018–2021 stack you ran; skim the current Observability product page if there is time.

**Your Tink setup is a talking point.** PRTG paged you and ELK was for investigation, so alerting did not depend on the investigation tool. When one platform does both, its outage can take the alerting with it.

---

## 3. Fit, stated plainly

**Solid, defend with confidence**

| Requirement | Your evidence |
|---|---|
| 5+ yrs SRE/platform/infra | 18 years; Tink + Énergir + Desjardins |
| 24/7 on-call, incidents, RCA | Tink rotation across all production; Énergir RCA on critical incidents |
| Deliver complex projects with minimal oversight | Desjardins harness, Salesforce validation gate, Tink inventory platform |
| Python | Desjardins FastAPI health service, ~250 repos, every 4h, published to Dynatrace |
| Deep Linux | 600+ server fleet at Tink, patching and kernel reboots automated |
| Mentoring, code/design review | 12 teams outside any reporting line, ~6 enablement sessions/yr |
| Fleet config management (bonus) | Puppet + Spacewalk at fleet scale |
| ArgoCD/Helm (bonus) | Desjardins on-demand Artifactory environments |
| Regulated infra (bonus) | Energy + financial services |
| Secrets management (bonus) | Small but real: see Vault below |

**Gaps, and the honest line for each**

1. **Go: none.** No production Go; C++ and Java background, seven years writing production software at SOVO, and a record of picking up runtimes cold. Say it once and stop.
2. **Terraform at scale: modest.** See the Terraform section below. About twenty workspaces you own; say the number.
3. **Kubernetes: practical, not deep.** Already known to them and cleared by a hiring manager. State it once in the cover letter's terms, mention CKA in progress, and don't overcompensate.
4. **Elastic Stack: 2018–2021, self-managed.** Production, but not current. No ECH/ECE/ECK.
5. **Formal SRE practice: none.** Real on-call and incident work, but you have never run SLOs or error budgets. Say so, then show you understand the mechanics (section 6).
6. **SaaS: first time.** Your recent years were in an operationally immature environment. At Elastic you would be the one catching up on scale and rigour.
7. **Async, cross-timezone work:** no named experience. Closest is the remote Desjardins contract. Don't oversell.

**Two resume claims that will get tested**

- **The self-healing Elasticsearch story.** Frame it as a deliberate mitigation: the script protected the service from a known failure while the root cause stayed open. If the cause was never found, say so. Do not present the restart as the fix.
- **"Paging dropped from one every two rotations to one every four or five."** In the tailored resume and cover letter but not in `profile.md`. Be sure it is yours and that you can say how you know it.

**On honesty.** Your rule is no faking. Apply it to Terraform too: say about three years, not five. The posting puts no number on Terraform; it tests depth, and the number has to stay consistent across the recruiter, both managers and any reference check.

---

## 4. Stories worked out tonight

### Terraform at Énergir

**How to say it:** "I own about twenty workspaces covering our CI/CD platform: Jenkins, its workers, Nexus, vaults, across dev and prod. The wider estate is 80 to 100, built by the infrastructure team, and I supported them on it."

- **Do not say** "helped set up 80 to 100." The follow-up is "what was your part?"
- **Modules:** "We started with bare resources and migrated to centralized modules; I wrote some and consumed most."
- **Still to have ready:** where your state lives and whether applies run through a pipeline with review.

**The state story (your best Terraform material).** The infrastructure team's original pipeline never stored state and re-imported everything before each change. You explained why state matters, and they moved it into a storage account.

Reasons to have ready, in your own words:
- Import only sees what exists; it cannot tell you what the code intended, so drift and orphaned resources go unnoticed.
- No state means no locking, so two runs can collide.
- Re-importing every run is slow and fragile.

Honest ending: portal access (ClickOps) stayed, so drift still happens and is reconciled with one-off imports. If asked how you would close that: read-only production access with a break-glass path, plus a scheduled plan to detect drift. Bridge: the Desjardins Splunk alerts detected exactly this, changes made outside the pipeline.

### Vault

**The claim, kept small:** "Our team owned an inherited HashiCorp Vault; it was low-touch, and I later worked through its replacement by Azure Key Vault." Do not let it grow into Vault expertise.

- **The outage.** Applications had a hard dependency on Vault with no graceful degradation: when Vault was unavailable they threw an exception and crashed, so the blast radius was the whole application instead of the features that needed secrets. The organization replaced the tool; the migration changed the tool, not the failure mode.
  - You don't remember your role in the incident, so don't give yourself one: "I wasn't the incident lead; my part came afterwards, in the migration."
  - Tone: "the contributing factor I'd have addressed was how the apps depended on it," not "the org blamed the wrong thing."
- **The migration.** You created the Key Vault in Terraform, entered about 20–30 secrets by hand, cleaned out unused ones with the team's knowledge, and human passwords moved to 1Password under an org policy (Key Vault for machines, 1Password for people).
  - It is a small task. Use it as one or two sentences, not a headline.
  - Because values were entered by hand, no secret sits in Terraform state.
  - Rotation: none, copied as they were. Say that a migration is the natural moment to rotate and it's a gap you'd flag.
  - At larger scale you would use access logs to find unused secrets, not memory.
- **The unseal key.** After a reboot the key could not be found. Only usable with the lesson: key custody was undocumented; what should exist is a runbook, tested restarts and auto-unseal.

### Security evidence (thin; know its limits)

Real pieces: Desjardins Splunk alerting for out-of-pipeline changes, the Tink CVE/EoL/TLS inventory, the human/machine credential split, the AI scope gates at Énergir. No Teleport, no Kyverno.

### A pattern to manage

Several stories end with "I identified the right answer and the organization didn't fully act": the AI safeguards, the ClickOps access, the Vault decision. Use **one at most**, and surround it with the ones where your recommendation was adopted and worked: Oracle, the Salesforce validation gate, the Desjardins harness, the Terraform state change.

### Your work in SRE terms

| SRE idea | Your story |
|---|---|
| Toil reduction | Tink patching automation; the Elasticsearch auto-restart; the app-versus-platform failure split at Énergir |
| On-call health | Tink paging reduction |
| Change safety | Salesforce validation gate |
| Design for failure | Your analysis of the Vault outage |
| A measured health signal | Desjardins repository checks |

**SLI at Énergir, the fair version:** "We had no formal SLOs, but the platform failure rate I separated out was effectively an SLI for the delivery platform." **Too far:** "I defined SLIs at Énergir."

---

## 5. Questions you will likely get

**"Walk me through your background."** Two minutes. Software first (SOVO), then operations at fleet scale (Tink, on-call, ELK), then platform work for other engineers (Énergir, Desjardins). End on why this team.

**"What do you understand the role to be?"** The one-sentence version in section 0.

**"Why Elastic / why this team?"** You ran the stack in production; the job is an internal platform other engineers depend on, which is what the Desjardins service and Tink logging were at smaller scale; and you want to work where good practice is the baseline.

**"Why are you leaving?"** The Énergir contract was not renewed after five years. One sentence. The resume says "Present"; if it has ended, say so.

**"Tell me about an incident you owned."** One real incident: detection, first hypothesis, what was actually wrong, mitigation, lasting fix, what changed. Have the timeline ready.

**"A project you delivered with little oversight."** Desjardins: asked to verify repo config, delivered a configurable harness that became the regression net for the Artifactory upgrade.

**"Tell me about your Terraform experience."** Section 4: the twenty, the wider estate, the state story.

**"A time you disagreed / raised a risk."** Pick one: the Terraform state argument (adopted) is safer than the AI safeguards (not acted on).

**"How do you make on-call better?"** A toil story, using the word. The posting's own line: "so the on-call load gets lighter over time."

**"How would you monitor X?"** What does the user experience, which SLI captures it, what target, alert on burn rate, dashboards for diagnosis, and what happens when the monitoring path itself fails.

**"How do you think about security?"** The real pieces in section 4. If asked about Vault, the small claim.

**"Have you worked with SLOs?"** No formal ones. Then the fair Énergir sentence, and show the mechanics.

**"You worked Desjardins and Énergir at the same time?"** Don't raise it yourself. If asked, in your own words:

> "My Énergir renewal was uncertain at the time, and as the main earner for my family I took a three-month contract through my corporation as a safety net. I delivered both, Desjardins extended it to six months, and by then the renewal had come through. That was a contractor's response to an uncertain renewal. As an employee, I'd give one employer my full attention."

- Neither client knew about the other, so never say it was disclosed. If asked directly whether they knew, the answer is no, followed by the same last sentence.
- Likely follow-up: "If Énergir stabilized, why are you leaving now?" The contract was not renewed this year.

**"How do you work across time zones?"** Written decisions by default; your overlap with both Europe and the west coast.

---

## 6. SRE reference

### The measurement chain

| Term | Meaning | Example |
|---|---|---|
| **SLI** | What you measure: the share of good events, chosen to represent the user's experience | 99.95% of requests succeeded this month |
| **SLO** | The internal target for that measure over a period | At least 99.9% over 30 days |
| **SLA** | The contract with customers, looser than the SLO, with penalties | 99.5% or the customer gets a credit |
| **Error budget** | 100% minus the SLO | 0.1%, about 43 minutes in 30 days |
| **Burn rate** | How fast the budget is being spent, as a multiple of the on-pace speed | 1 = on pace; 10 = gone in 3 days; 0.2 = healthy |

- **100% down to the SLO** is the error budget. **SLO down to the SLA** is a safety margin, not the budget. Below the SLA, the contract is breached.
- A burn rate of 1.001 all month misses the SLO by a hair and leaves the SLA untouched.
- Missing the SLO is internal (shift to reliability work). Missing the SLA costs money.
- Burn rate is speed; "we've used 40% of the budget" is amount.
- A burn rate needs an SLO. A measurement with no target is just a metric (used for diagnosis, baselining, or things not worth paging on).
- Keep SLOs few, two to five per service; each one can page someone.

### Burn-rate alerts

Commonly cited thresholds for a 30-day target. Teams tune these; quote the principle, not the numbers.

| Burn rate | Sustained for | Budget used | Response |
|---|---|---|---|
| 14.4 | 1 hour | 2% | Page |
| 6 | 6 hours | 5% | Page |
| 1 | 3 days | 10% | Ticket |

- **The window** filters out short problems. **The threshold** filters out small ones.
- **Principle:** page on fast burns, ticket on slow ones. A page must need a human now.
- Why not page on anything above 1: nothing to act on, alert fatigue, and the budget exists to be spent.

### What makes a good SLI

- It measures what the user experiences, not what could affect it. CPU is a cause.
- **Test:** could this be green while the user is having a bad time, or red while the user is fine? If yes, it's a cause, not an SLI.
- **Batch job example:** the SLI is the freshness of the data the user sees, not the job's status. The job can fail and a retry succeed, or succeed while the publish step breaks.
- Running the job more often is a legitimate mitigation (more attempts inside the window) but not a fix: it doesn't help when the cause persists, it costs more, and it can hide a rising failure rate. Same shape as the Elasticsearch restart script.
- SLIs are chosen by mapping **critical user journeys**. **Value stream mapping** is a different thing: Lean/DevOps, about delivery flow. Use it for the Énergir delivery work, not for SLIs.

### The four signals

- **Latency:** time to serve a request, measured at the service (not ping). Use percentiles, not averages; track failed requests separately.
- **Traffic:** demand, such as requests or events per second. Mostly context and capacity input.
- **Errors:** 5xx counts against reliability; 4xx usually doesn't. Exceptions: a 4xx spike after a release, and 429 as a capacity signal. A 200 with wrong content is also an error.
- **Saturation:** how full the most constrained resource is, as a percentage of capacity. The one leading signal.

Saturation details:
- Capacity is the limit, found by load testing (find where latency bends, note which resource ran out first, retest after changes). Saturation is how close you currently are.
- Limits come from engineering; product supplies demand forecasts.
- Percentages let one alert rule cover clusters of different sizes.
- You alert on saturation (ticket or warning) but do not set an SLO on it.
- Elasticsearch disk watermarks by default: 85% no new shards, 90% shards move away, 95% writes blocked.

### Practices

- **Toil:** manual, repetitive, automatable operational work with no lasting value, growing with the service. Guideline: under half of an SRE's time. A one-off manual task is not toil.
- **On-call:** pages rare, actionable, backed by a runbook.
- **Incidents:** mitigate first, find the cause after.
- **Blameless postmortem:** timeline, contributing factors, action items with owners. Action items go to whoever owns the fix, not only developers.
- **Change safety:** most outages come from changes; roll out gradually, be able to roll back.
- **Design for failure:** assume dependencies fail; limit the blast radius.

### Setting up SRE from nothing

1. Pick one important service and its key user journeys.
2. Define the SLIs.
3. Measure for a few weeks.
4. Set the SLO from the data and from what users need.
5. Agree what happens when the budget runs out.
6. The SLA comes last, if at all.

- Measure first, set targets after. If a contract SLA already exists, that changes the constraint, not the first step.
- Ownership: SLIs and measurement belong to engineering; the SLO is agreed with product; the SLA belongs to the business.
- It is fine for the business to start it by saying what they want measured, as long as the number waits for the data.

### Roles in a SaaS company

| Role | What they do |
|---|---|
| Software engineers | Build features, fix bugs, and usually deploy and are on call for their own service |
| Release manager | Mostly gone; deploys are automated and teams ship their own changes |
| Platform engineers | Build the shared foundation other engineers deploy onto. This was your Énergir job. |
| SRE | Own production reliability: on call, incidents, postmortems, SLOs, capacity, automation. This was your Tink on-call work. |

- SRE comes in three shapes: advisory, owning a service's production, and running shared infrastructure. **This role is the third.**
- SRE is operations done with a software engineering approach. It assumes automated delivery, infrastructure as code and decent monitoring already exist, which is why you have not met it before.
- At Elastic, SRE sits inside the Platform Engineering department, so the titles overlap.

### A list for assessing any service's reliability

1. Is there a defined reliability target, measured from the user's side?
2. Do pages fire on user-visible symptoms, and is each one actionable?
3. How often are people paged, and do runbooks exist?
4. Are there postmortems, and do action items get done?
5. What happens when each dependency fails, and how far does the damage spread?
6. Can a bad release be caught early and rolled back?
7. How much headroom is there, and has it been tested?
8. Has a restore from backup been tried?

---

## 7. Phrases to avoid

| Don't say | Say instead |
|---|---|
| "Keeping customers' clusters healthy" | The observability platform Elastic's Cloud engineers depend on |
| "Five years of Terraform" | About three years |
| "Helped set up 80 to 100 workspaces" | "I own about twenty; the wider estate is 80 to 100 and I supported that team" |
| "I defined SLIs at Énergir" | "No formal SLOs, but the platform failure rate was effectively an SLI" |
| "SRE is just ops rebranded" | Operations done with a software engineering approach |
| "A mature company doesn't need SREs" | "I try to make each recurring task unnecessary so the team can move on to the next problem" |
| "Opex tasks" | Operational work, toil |
| "Value mapping" for choosing SLIs | Critical user journeys |
| "The org blamed the wrong thing" | "The contributing factor I'd have addressed was..." |
| "Willing to learn Go" | No production Go, plus the evidence of learning runtimes cold |
| Defining SLA, SLO, SRE unprompted | Ask how Elastic draws the lines |

---

## 8. Questions to ask

Note beside you: **team, monitor the monitor, SLOs, on-call.** If the recruiter already covered something, open with "the recruiter touched on this, but I'd like to hear it from you." If time is short, ask 2 and 4.

### The four main questions

**1. Team organization**
- **Ask:** "How are the observability and analytics sides organized, and where does platform security fit in?"
- **Why:** Lindsay's title says Platform Security and the posting says Observability. You need to know what you'd work on and who you'd report to.
- **Listen for:** team size, regions, and whether Lindsay would be your manager.

**2. Monitoring the monitor**
- **Ask:** "At Tink our paging tool was separate from our logging stack, so losing one didn't take out the other. But nothing watched the paging tool itself, beyond someone glancing at a dashboard. How do you handle that at your scale?"
- **Why:** it is the most interesting problem in this job, and you are asking about a gap you have lived with.
- **Listen for:** separate clusters watching each other, external checks, or an admission that it is a known weak spot.
- **If asked how you'd close the gap:** a heartbeat. The monitoring system sends a regular "I'm alive" signal to something independent, and an alert fires when it stops.

**3. The platform's own SLOs**
- **Ask:** "The platform has its own users, the Cloud engineers. Does it have its own SLOs, for things like freshness, availability and completeness, and how is completeness measured?"
- **Say SLOs, not SLAs.** The users are internal.
- **What they would measure:** freshness (time until data is searchable), completeness (did everything arrive), availability (can engineers search and load dashboards).
- **Listen for:** concrete targets (a team that measures itself) or "we're working on that" (work you could own).
- **If it is turned back on you,** two real methods:
  - *Expected versus observed (Desjardins):* "I read the expected list of repositories from Artifactory's own configuration and checked that I was monitoring every one."
  - *The catch-all (Énergir log ingestion):* "Anything that didn't match a known category was flagged and processed generically, so gaps in our parsing were visible instead of silent."
  - The principle: nothing should fail silently.
  - Use Desjardins and Énergir as examples, not Canopy.

**4. On-call**
- **Ask:** "How many people share the rotation, and does it follow the sun across regions? During an on-call week, how much of the time typically goes to pages and interrupts, and how much is left for project work?"
- **Avoid:** "checking the monitoring during my whole shift" (suggests watching a screen) and "are the systems pretty stable?" (sounds like hoping for a quiet job).
- **Listen for:** "a few pages a week, mostly project work" (healthy); "on-call week is mostly interrupts" (acceptable if other weeks are protected); "it's pretty busy right now" (team is stretched).

### If there is time

5. Who builds the dashboards and alerts on the platform: this team, or each Cloud engineering team?
6. How is the work split across ECH, ECE and ECK?
7. How much of the team's code is Go versus Python and Terraform?
8. You joined recently. What have you decided to prioritize first?
9. What would you want a new senior engineer to have delivered at 90 days?

### The close

"I should mention I'm expecting an offer from another company shortly. This role is my preference, so I wanted you to know my timeline. What are the next steps on your side?"

The backfill-or-growth question is largely answered: the recruiter said SRE headcount went up through the June cuts. Skip comp unless they raise it.

---

## 9. Company context

- June 23, 2026: Elastic announced a ~7% workforce reduction, framed as aligning teams with AI automation. The filing says total headcount is still expected to grow. The recruiter raised it himself and said SRE roles increased through it.
- Source Code values most likely to come up: **Progress, SIMPLE Perfection** (ship and iterate), **HUMBLE, Ambitious**, **Customer, 1st**, **01.02, /FORMAT** (distributed by design). Be ready for the question about when you shipped something imperfect on purpose.
- The usual process after a hiring-manager round is technical: live coding, system design, sometimes a pull-request review. That is the harder test for you. If tomorrow goes well, put the preparation time there.

---

## 10. Before the call

1. Read Lindsay Sandall's LinkedIn profile in full (linkedin.com/in/lindsaysandall).
2. Be able to say where your Terraform state lives and how applies run.
3. Have one incident story with a timeline.
4. Settle the honest version of the Elasticsearch restart story, and confirm the paging number is yours.
5. Reread sections 0, 6 (the two tables) and 7.

## 11. After the interview (not tonight)

- Add to `profile.md`: HashiCorp Vault (inherited, low-touch), the Azure Key Vault migration, 1Password policy, and the real Terraform scale and state story. None of it is there today.
- Reconcile the paging-frequency claim between `profile.md` and the tailored resume.
- Update the Énergir end date on the resumes if the contract has ended.
- Write down what Lindsay asked and how each answer went, while it is fresh.
