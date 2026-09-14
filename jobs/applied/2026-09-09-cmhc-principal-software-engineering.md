# Principal, Software Engineering — CMHC (Canada Mortgage and Housing Corporation)

- **Source:** https://careers.cmhc-schl.gc.ca/job/Ottawa-Advisor%2C-Software-Engineering/604788517/
- **Found:** 2026-09-09
- **Engagement type:** Full-time
- **Rate/Salary (stated):** $129,175.28 to $161,469.09 CAD
- **Location/Remote:** Montreal, QC or Ottawa, ON (Hybrid)
- **Days in Office:** Not stated
- **Flags:** Reliability Status security clearance required (process/timeline item, not a disqualifier — most citizens/PRs clear it, but it adds weeks to onboarding); days/week in office not specified — verify before accepting; URL slug reads "Advisor, Software Engineering" but the fetched posting content is titled "Principal, Software Engineering" — likely a requisition retitle, but verify the actual title before applying

## Fit Score: 8 (rescored 2026-09-11 under the three-track engagement strategy — see profile.md)

Strong cloud-native and platform-engineering overlap: Azure Functions, Logic Apps, and Kubernetes line up directly with Marc's Azure migration and Kubernetes/ArgoCD work at Énergir and Desjardins, and the role's core mandate — setting engineering standards, driving modern practices, and reducing technical debt across multiple agile teams — matches his "leads without authority" pattern (12-team CI/CD adoption at Énergir with no reporting line). Location is Ottawa or Montréal, both within reachable-hybrid range. Bilingual requirement (CBC level) plays to a real advantage.

**Compensation reality check:** this is now scored as a first-class FTE target (previously this posting's full-time-only status would have been treated as a soft negative under the old contract-first framing — that's no longer the case). The posted band is $129,175–$161,469 CAD. Be honest with yourself about where you'll actually land: this reads as a Crown-corporation pay band, which tend to be adhered to more rigidly than private-sector ranges — realistic outcome is somewhere in the upper-middle of that band (roughly $150–161k), landing at or just above your $160k floor, not anywhere near the $175k aspirational ceiling. Worth applying, but don't walk into negotiation expecting to blow past the posted max.

Two soft skill gaps, unrelated to compensation: the JavaScript/TypeScript/C#/Node.js stack is only partially represented on the resume (Node.js touched, not C#), and this is architecture/standards guidance rather than hands-on delivery, a step removed from Marc's build-it-himself track record — worth addressing directly in interview rather than papering over.

## Resume Delta

- Lead with the Énergir "drove CI/CD and platform-engineering adoption across 12 teams outside any reporting line" bullet — it's the closest direct match to this role's "guide engineering effectiveness across multiple agile teams" mandate.
- Emphasize the Azure cloud modernization bullet (5–10 mission-critical service migrations) to speak to the Azure Functions/Logic Apps requirement.
- Highlight Kubernetes/ArgoCD depth from the Desjardins engagement (on-demand instance provisioning) against the "cloud-native platforms (Kubernetes)" requirement.
- Surface the Salesforce CLI + validation-sandbox story as evidence of establishing standards and technical-debt reduction (legacy ANT scripts → governed pipeline), matching the "establishing standards for code quality, automation testing, and technical debt management" language in the posting.
- Note bilingual French/English fluency prominently near the top — it's an explicit CBC-level requirement, not just a nice-to-have here.
- Do not overstate C#/Node.js/OAuth2/OIDC/JWT experience — the resume shows Java/Python/Node.js touch points but no dedicated C# or identity-architecture work; if asked, be direct that this would be a ramp-up area.

## Draft Cover Letter

Dear Hiring Committee,

I'm writing to express interest in the Principal, Software Engineering role at CMHC. Over 18 years in DevOps and platform engineering, most recently at Énergir, I've built a track record of establishing engineering standards and driving practice adoption across teams I had no formal authority over — which is close to the core of what this role asks for.

At Énergir, I standardized CI/CD delivery across nine distinct runtimes for 12 application teams and 70+ applications, and ran recurring enablement sessions to turn delivered tooling into actual adoption rather than shelfware. A pattern that's shown up three times in my career: given a narrow, specific ask, I've consistently delivered something structurally larger than what was requested. When asked to port legacy Salesforce deployment scripts, I replaced them with the official Salesforce CLI tooling and built a validation-sandbox merge gate that made undeployable code structurally unable to reach production — turning a team that feared missing its deployment window into one with a dependable every-other-Tuesday release. I bring the same instinct to standards and technical debt: the goal isn't just compliance, it's making the right practice the path of least resistance.

On the technical side, I've led 5–10 mission-critical service migrations to Microsoft Azure and built hands-on Kubernetes/ArgoCD automation at my most recent engagement with Desjardins, provisioning on-demand instances for safe configuration testing — directly relevant to CMHC's cloud-native platform stack. I'm fully bilingual (French native, English fluent), which I understand is a requirement at the CBC level for this role.

I'd welcome the opportunity to discuss how this experience applies to CMHC's engineering organization. Thank you for your consideration.

Best regards,
Marc Berthelette
