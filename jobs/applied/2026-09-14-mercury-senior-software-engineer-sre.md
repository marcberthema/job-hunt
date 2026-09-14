# Senior Software Engineer - SRE — Mercury

- **Source:** https://ca.linkedin.com/jobs/view/senior-software-engineer-sre-at-mercury-4462531669
- **Found:** 2026-09-14
- **Engagement type:** Full-time
- **Rate/Salary (stated):** CAD $189,700–$237,100 base salary for Canadian employees, plus equity and benefits
- **Location/Remote:** Canada; posting is nationally listed, but remote policy is not explicitly stated in the accessible description
- **Days in Office:** Not stated
- **Flags:** Confirm fully remote eligibility from Smiths Falls before applying; significant PostgreSQL and Temporal experience are requested; application-level Haskell/TypeScript work is part of the role

## Fit Score: 8/10

Mercury's reliability model maps closely to Marc's strongest pattern: embed with product teams, identify systemic weaknesses, improve on-call and observability practices, and replace recurring operational work with durable automation. His financial-services background, measurable on-call improvement, incident RCA, automated remediation, platform enablement across 12 teams, and history of extending narrow assignments into reusable systems are all strong evidence. The material gaps are significant PostgreSQL experience, authored-and-operated Temporal workflows, and deeper application development in Haskell/TypeScript; these must be addressed honestly rather than blurred into general infrastructure experience.

## Resume Delta

- Reframe the professional summary toward reliability enablement: reducing toil, improving incident response, and helping product teams adopt durable operational practices.
- Lead the Tink section with the reduction in on-call frequency from roughly one page every two rotations to one every four or five, plus the self-healing Elasticsearch remediation.
- Emphasize Énergir's root-cause analysis, monitoring, dashboards, automated remediation, and cross-team enablement for 12 application teams.
- Emphasize that the Desjardins health service created a continuous reliability signal for roughly 250 repositories and became the regression safety net for an Artifactory upgrade.
- Highlight the Python/FastAPI production service and Marc's seven years writing production software at SOVO to support the software-engineering side of the SRE role.
- Mention financial-services experience at Desjardins and the ability to translate reliability work for both technical and non-technical stakeholders.
- Do not claim PostgreSQL depth, Temporal experience, Haskell, TypeScript, Honeycomb, OpenTelemetry, formal game-day ownership, or mature SLO/error-budget program ownership.

## Draft Cover Letter

Dear Mercury team,

The part of this role that stands out to me is the expectation that SREs work with product teams to make reliability practices self-reinforcing, rather than becoming the team that repeatedly handles the same operational failures. That is how I have approached DevOps and reliability work throughout my career.

At Tink, I reduced operational toil across a fleet of more than 600 servers through automated patching and remediation. One recurring Elasticsearch failure had been waking engineers unnecessarily; I connected monitoring to an automated recovery script so the known condition no longer required a human page. Alongside broader preventive work, on-call frequency fell from roughly one page every two rotations to one every four or five.

At Desjardins, I was initially asked to verify the configuration of Artifactory repositories. I built the validation logic as a configurable, mostly tool-agnostic Python/FastAPI service instead. It tested roughly 250 repositories every four hours, published health signals to Dynatrace, and later became the regression safety net for the platform's own version upgrade. My approach is to recommend what is best for the client, not necessarily what is cheapest in the moment.

I would bring that same bias toward durable fixes, along with enterprise incident response, observability, Python, platform enablement, and recent financial-services experience. I also want to be direct about the gaps: I do not have the significant PostgreSQL or Temporal workflow experience requested, and I have not worked in Haskell. What I do have is an 18-year record of learning unfamiliar systems under real delivery constraints and turning them into reliable, maintainable platforms without overstating what I know.

I am based in Ontario, Canada, and available immediately. I would welcome a conversation about Mercury's Stability team and how this new embedded SRE model will work with product engineering.

Sincerely,

Marc Berthelette
