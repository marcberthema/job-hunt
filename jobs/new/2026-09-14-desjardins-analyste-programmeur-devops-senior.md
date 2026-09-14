# Analyste-programmeur(euse) DevOps Senior — Desjardins

- **Source:** Recruiter outreach (name not provided in posting text), no URL — client confirmed as Desjardins
- **Found:** 2026-09-14
- **Engagement type:** Contract (agency/recruiter-sourced), hourly rate — confirm W2/T4 vs. corp-to-corp with the recruiter
- **Rate/Salary (stated):** $105/hr CAD
- **Location/Remote:** Montréal, QC — hybrid, 2 days/week on-site
- **Flags:**
  - Rate is below Marc's $110–130/hr target but above the $100/hr hard floor — minor red flag, worth pushing the recruiter on since it's agency-sourced for a named client (Desjardins) and there's likely margin between the bill rate and this offer.
  - Montréal is the outer edge of Marc's reachable radius from Smiths Falls, ON (~2.5–3hr drive each way) — 2 days/week is a real weekly commute/overnight-stay burden, not a "borderline" checkbox. Confirm whether Marc still has a Montréal foothold from the Énergir days before treating this as routine.
  - Title ("Analyste-programmeur") and language ("selon les orientations et objectifs de l'organisation") suggest execution-within-a-roadmap scope rather than architecture-owning autonomy — don't oversell seniority/autonomy in interview prep.

## Fit Score: 6/10

Skill fit is strong and low-risk: GitHub Actions, Ansible, Terraform, Docker/Kubernetes, Python/Shell, and multi-cloud (Azure/AWS/GCP/OCI, none required at depth) all map directly onto Marc's existing stack — no cloud-platform hard gate here. He also already has direct, recent credibility with this exact client from the Oct 2025–Mar 2026 JFrog Artifactory engagement. What holds this to a 6 rather than higher: the rate sits below his target band (though above the floor), the 2-days/week Montréal commute is a real logistics cost even though Montréal is technically in range, and the posting reads as IC/ticket-execution scope rather than the autonomy-first positioning he's targeting. Under the current urgent-search bar (5+ = apply), this clears — but negotiate the rate and confirm commute logistics before going further.

## Resume Delta

Use `resume/marc-berthelette-resume-fr-desjardins.md` as the base — it's already tailored to this exact client and leads with the JFrog Artifactory engagement, which is the strongest possible credibility anchor for a second Desjardins mandate.

- Lead with the Desjardins JFrog Artifactory contract (Oct 2025–Mar 2026) — same client, same environment, directly relevant GitHub Actions/Kubernetes/ArgoCD/Splunk work already on record.
- Surface Ansible and Terraform (Énergir) against "Configuration as Code" / "Infrastructure as Code" requirements — call out idempotence/reusability explicitly since the posting names those principles directly.
- Highlight the Splunk-based alerting on out-of-pipeline manual changes (Desjardins) against the posting's "gouvernance" and "processus d'approbation" requirements.
- Note Python/Shell scripting depth (Desjardins FastAPI service, Énergir automation) against "Python, TypeScript, Shell et autres langages pertinents" — TypeScript is not on his resume, don't claim it.
- Lead with native French fluency — this is a French-language posting for a Quebec-based financial institution.
- Do not lead with "Staff/Senior SRE" framing here — the posting's own title is "Analyste-programmeur," so match that register rather than over-positioning.

## Draft Cover Letter (français)

Bonjour,

Je suis ingénieur DevOps senior avec 18 ans d'expérience, dont un mandat récent de 6 mois chez Desjardins (octobre 2025 – mars 2026) où j'ai conçu un service Python/FastAPI testant automatiquement la configuration d'environ 250 dépôts JFrog Artifactory toutes les 4 heures, publiant les résultats dans Dynatrace, et bâti des alertes Splunk détectant les changements de configuration effectués hors du pipeline CI/CD — exactement le type de gouvernance et de traçabilité que ce poste vise à automatiser à plus grande échelle. J'ai aussi automatisé le provisionnement d'instances Artifactory à la demande avec Kubernetes et ArgoCD, permettant aux administrateurs de tester leurs changements en toute sécurité.

Chez Énergir, j'ai standardisé le CI/CD pour 12 équipes applicatives sur neuf écosystèmes distincts et implanté des pratiques d'Infrastructure as Code avec Terraform et Ansible, en insistant sur l'idempotence et la réutilisabilité des automatisations — des principes que je retrouve directement dans les exigences de ce mandat.

Connaissant déjà l'environnement Desjardins et ses équipes de plateforme, je serais en mesure de contribuer rapidement, sans courbe d'apprentissage organisationnelle. Je suis bilingue (français natif, anglais courant), incorporé au Canada, et disponible rapidement.

Au plaisir d'en discuter davantage.

Cordialement,
Marc Berthelette
