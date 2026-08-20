# Senior SRE / Infrastructure Engineer — Oscilar

- **Source:** pasted text (no URL provided)
- **Found:** 2026-07-07
- **Engagement type:** Full-time (401k, equity, comprehensive benefits, unlimited PTO all stated — no contract language)
- **Rate/Salary (stated):** "Competitive salary and equity" — not stated numerically
- **Location/Remote:** Remote-first ("work from anywhere"; health benefits noted as US-specific)
- **Flags:** Full-time role with heavy benefits emphasis (401k, 100% employer-covered health/dental/vision, unlimited PTO) — classic FTE signal per profile red flags; salary not numerically stated; no Azure or Microsoft cloud component anywhere — stack is AWS-exclusive; primary language is Go ("We use Go"), which isn't in Marc's skill set; core distributed-systems stack (Kafka, ClickHouse, Pulumi) has no overlap with the resume

## Fit Score: 2/10 (skill/domain fit — logistics noted separately above)

This is a strong domain mismatch despite the fintech/risk-management sector having some resonance with Marc's financial-services credibility (Desjardins). The infrastructure stack is AWS-only with no Azure component at all, which the profile's scoring notes flag directly as a reason to score lower. More significantly, the role requires "expert-level" AWS and Pulumi IaC (not Terraform, though Terraform is mentioned secondarily), strong Go programming ("we use Go" — Marc's language background is Python/Bash/C++/Java, no Go), and deep Kafka/ClickHouse distributed-systems experience, none of which appears anywhere in the resume. This reads as a SRE role for a Go/AWS-native high-scale startup, a meaningfully different profile from Marc's Azure-centric platform engineering background.

## Resume Delta

Not recommended — the core requirements (expert AWS, Pulumi, Go, Kafka, ClickHouse) have no basis in Marc's resume, and stretching to fit would mean overstating skills that aren't there. If pursued despite the mismatch, the only genuinely transferable points are:

- Kubernetes container orchestration experience (Desjardins, Énergir) against the "mastery of container orchestration" requirement
- CI/CD pipeline design and observability/alerting discipline (Dynatrace, Splunk) as evidence of the SRE mindset, even without the specific tools named
- Production incident RCA and MTTR-reduction work (Énergir) against "run chaos experiments and failure simulations" and reliability ownership

## Draft Cover Letter

Not drafted — the language (Go vs. Python), IaC tool (Pulumi vs. Terraform), and cloud platform (AWS vs. Azure) mismatches are all core requirements rather than nice-to-haves, so a tailored letter would need to overstate fit. Recommend rejecting unless Marc has undisclosed Go/AWS/Pulumi experience not reflected in profile.md/resume.
