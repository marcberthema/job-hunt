# Senior Developer - Delivery Engineering — Jane App

- **Source:** https://www.linkedin.com/jobs/view/4459055691/
- **Found:** 2026-08-26
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $128,000–$200,000/year CAD range; most new hires start at the "accomplished" stage, $152,000/year
- **Location/Remote:** Remote, Canada preferred — role explicitly wants Eastern time zone or further east (Atlantic/UK also fit) to extend delivery-window coverage past Pacific hours
- **Days in Office:** 0 (Remote)
- **Sourced via:** Manually added by Marc via URL — not surfaced by `/check-linkedin`'s keyword rotation (title "Senior Developer - Delivery Engineering" doesn't match any rotation phrase; third instance of this gap after Akamai and Lakeview)
- **Flags:** Typical starting salary ($152K) sits below the $160K target, though the band goes to $200K with growth; no named cloud platform (AWS/Azure/GCP) — role is CI/CD pipeline/delivery-orchestration focused rather than cloud-infrastructure-broad, so the usual Azure-depth advantage doesn't directly apply here, but the core skill match (GitHub Actions, Docker, YAML, observability) is otherwise excellent; healthcare-adjacent SaaS (EMR/practice management), not financial/energy but no penalty; genuinely strong Eastern-timezone fit for a Smiths Falls-based candidate — this posting explicitly wants what Marc already is

## Fit Score: 8

Unusually precise match: the role is squarely CI/CD pipeline ownership and delivery orchestration — Git/GitHub Actions, YAML, Bash, Docker/containerization, Datadog observability — which is close to a direct restatement of the Énergir CI/CD standardization work (nine runtimes, 12 teams, GitHub Actions) and the Desjardins Splunk/Dynatrace observability practice. The Eastern-timezone requirement is an exact geographic fit for a Smiths Falls-based candidate, unlike most "Canada remote" postings that don't care about time zone specifically. The "AI coding tools fluency, Claude first" requirement is an authentic, easy claim — Marc uses Claude Code directly in his own workflow, not a stretch. Salary's typical starting point ($152K) sits just under the $160K target, and the role lacks a named cloud-platform component to lean on Azure depth, which keeps this at 8 rather than 9-10, but the delivery-engineering scope itself is about as close a domain match as this search has produced.

## Resume Delta

- Lead with the Énergir CI/CD standardization bullet (nine runtimes, 12 application teams, 70+ applications, GitHub Actions) — this posting's core mandate (build/run the pipelines that take code to production for many teams sharing a codebase) is close to a direct restatement of that work.
- Emphasize the "cut false-positive pipeline failures and made build results self-diagnosing" bullet — directly answers the posting's "extreme ownership of delivery... unblocking teams quickly when issues arise."
- Highlight Desjardins Splunk/Dynatrace observability work against the Datadog observability requirement.
- Mention Docker/Kubernetes container experience (Desjardins Artifactory engagement) against "everything we run is containerized."
- Note genuine, current use of Claude Code and AI-assisted tooling in daily workflow — an honest, first-person answer to "fluency with AI coding tools," not an inflated claim.
- Mention Eastern-timezone location (Smiths Falls, ON) explicitly and early — this is a stated hiring preference, not just a logistics footnote.

## Draft Cover Letter

Hi Chris and the Delivery Engineering team,

I'm applying for the Senior Developer - Delivery Engineering role. The scope you've described — owning the pipelines that take code to production for many teams sharing a codebase, without owning their tests or features — is close to what I did at Énergir: I standardized CI/CD delivery across nine distinct technology runtimes for 12 application teams and 70+ applications, and I specifically built a way to separate application-code failures from platform-pipeline failures in build reporting, so teams could tell at a glance whose problem a failure actually was. That's the same "extreme ownership without owning the product" line your role draws.

I'm based in Eastern time (Smiths Falls, Ontario), which lines up with what you're looking for to extend delivery coverage past Pacific hours. On observability, I built Dynatrace dashboards and Splunk alerting at Énergir and Desjardins to catch issues (including changes made outside the CI/CD pipeline) before they became incidents — directly relevant to your Datadog-based pipeline visibility. And on the AI-tooling side, I'm not claiming enthusiasm from the sidelines: I use Claude Code directly in my own engineering and job-search workflow today, so directing agentic tools to do the heavy lifting while I focus on design and correctness is already how I work.

I'm incorporated in Canada, bilingual (French/English), and available immediately. I'd welcome a conversation.

Best,
Marc Berthelette
