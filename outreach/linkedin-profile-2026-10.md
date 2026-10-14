# LinkedIn — copy refreshed 2026-10-14

Rebuilt from the current Platform core resume and the 2026-10-13 resume fact review in profile.md. Ready to paste; not applied live (external sites are read-only for the agent). Keep actual experience titles. Énergir ended September 2026. Rates and financial urgency stay out of public copy. The French sections below are the older 2026-10-09 copy and still need the same corrections before they are published.

## Headline — EN

Senior DevOps & Platform Engineering Consultant | CI/CD, Jenkins, Azure & Python | Release Automation & Production Reliability | FR/EN

## About — EN

I help engineering teams make releases repeatable and remove manual operational work.

I get productive quickly in unfamiliar systems: understand the workflow, find where it breaks, and turn a practical plan into tested automation, then work with the application teams so it actually gets used. That comes from nearly 18 years across infrastructure, software development, and production operations, including energy and financial services.

At Énergir (five-year consulting engagement, renewed four times), I initiated shared Jenkins pipelines used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams, and 70+ applications. Shared pipeline code was tested on every commit at roughly 80-90% coverage.

Examples of the work:
• Replaced a 15-step MuleSoft release checklist with version-based deployments of QA-tested artifacts, so release preparation moved ahead of the production window and rollback meant redeploying a previous version.
• Built nightly Salesforce validation. When two weeks of failures were stuck on disputed ownership, I escalated to the project director; fixes across 4-5 teams followed within 48 hours and the project deployed on schedule.
• Automated routine Oracle releases without emergency-access requests, and eliminated recurring encoding incidents with SQL checks and separate locale settings.
• Migrated production Salesforce logs to direct Dynatrace ingestion and built dashboards that exposed previously hidden errors.
• At Desjardins, built a Python/FastAPI workflow that provisioned Artifactory and tested artifact retrieval across about 250 repositories, deployed through ArgoCD and reporting to Dynatrace.
• At Tink, replaced reactive patching across 600+ servers with staged, dependency-aware Spacewalk schedules.

Core tools: Jenkins, Azure DevOps, GitHub Actions, Linux, Python/Bash, Artifactory, Dynatrace, Splunk, ELK. I work with Kubernetes application deployments and with existing Terraform/Ansible provisioning workflows.

Based in Ontario, bilingual French/English, incorporated in Canada, available immediately. Open to remote consulting contracts and full-time roles. If your team has fragile pipelines, manual releases, or operational tooling that needs work, let's talk.

## Experience — EN (paste each entry; dates as shown)

**Énergir — Senior DevOps Engineer (Contract)** | September 2021 - September 2026
Five-year consulting engagement, renewed four times.
• Initiated shared Jenkins pipelines adopted by all Jenkins teams; approximately 80-90% JaCoCo coverage with per-commit unit tests and sample applications for integration testing.
• Established "build once, deploy many"; migrated about five Node.js applications to runtime configuration through team-reviewed pull requests so one tested build serves every environment.
• Replaced a 15-step MuleSoft checklist with version-based deployments of QA-tested artifacts, simplifying rollback.
• Built nightly Salesforce validation; escalation of two weeks of failures prompted fixes across 4-5 teams within 48 hours and an on-schedule deployment.
• Automated routine Oracle releases; eliminated encoding incidents with SQL checks and separate SQL/Forms locale settings.
• Migrated production Salesforce logs to direct Dynatrace ingestion; expanded error parsing and dashboards.
Skills: Jenkins, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Dynatrace

**Desjardins — Senior DevOps Engineer (Contract)** | October 2025 - March 2026 (concurrent with Énergir)
• Built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a selected Git reference, and tested uncached artifact retrieval across about 250 repositories.
• Deployed the suite through ArgoCD/GitOps on a schedule, publishing configuration-version and artifact-level results to Dynatrace.
• Implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD.
Skills: Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

**Tink — DevOps Engineer** | January 2018 - August 2021
**SOVO Technologies — Lead Technician, then Software Engineer** | November 2008 - December 2017
Use the bullets in resume/platform/marc-berthelette-resume-en.md unchanged.

## Skills section

Top 3 to pin: Jenkins, Azure DevOps, Python. Then: CI/CD, GitHub Actions, Linux, Artifactory, Dynatrace, Splunk, Kubernetes, ArgoCD, Terraform, Ansible, Docker, Bash. Avoid positioning Kubernetes and Terraform as core expertise.

## Open items

- Kubernetes at Énergir (about a year, not primary owner): add a line only after Marc gives the specifics, then add to profile.md.
- Optional: a one-line "Open to work" setting for recruiters (Marc's choice; it is visible to recruiters only if he picks "recruiters only").
- Optional: switch headline toward SRE when applying to SRE roles; the profile's 2026-09-11 headline is "Senior / Staff SRE · Platform Engineering · DevOps · Reliability".

## Publication status

- [ ] English headline and About applied live
- [ ] English Énergir and Desjardins entries updated
- [ ] Skills reordered
- [ ] French sections corrected, then applied

## Titre — FR

Consultant senior DevOps et plateformes | CI/CD, Jenkins, Azure et Python | Automatisation des déploiements et fiabilité | FR/EN

## À propos — FR

J'aide les équipes de développement à fiabiliser leurs déploiements et à automatiser les tâches opérationnelles répétitives.

Ma force : devenir rapidement opérationnel dans un environnement que je ne connais pas encore. Je comprends le fonctionnement, cerne les problèmes, propose un plan concret et réalise l'automatisation. Mon parcours couvre près de 18 ans en infrastructure, développement logiciel et exploitation, notamment en énergie et en services financiers.

Chez Énergir, j'ai centralisé les pipelines de livraison utilisés par environ 50 développeurs, répartis dans 12 équipes responsables de plus de 70 applications. J'ai établi des étapes communes et des contrôles qualité obligatoires. Durant mes trois premières années, j'ai aussi créé la feuille de route de livraison et accompagné les nouveaux développeurs et spécialistes DevOps.

Quelques réalisations :
• Remplacé une procédure de déploiement MuleSoft de 15 étapes par quelques tâches Jenkins.
• Automatisé les déploiements Oracle courants pour éliminer le recours à un compte d'accès d'urgence approuvé chaque semaine; ajouté des tests détectant des problèmes récurrents d'encodage.
• Remplacé les scripts Salesforce existants par Salesforce CLI et une validation en environnement isolé, pour détecter les problèmes avant les mises en production.
• Livré le déploiement de services cartographiques ArcGIS versionnés et de leurs propriétés en développement, en test et en production, avec un compte de service plutôt que depuis les portables des développeurs.
• Développé chez Desjardins un service Python/FastAPI validant environ 250 dépôts Artifactory toutes les quatre heures et publiant les résultats dans Dynatrace.
• Automatisé les correctifs sur plus de 600 serveurs chez Tink et créé un outil de visibilité sur les versions logicielles, les vulnérabilités et les fins de vie.

Mes principaux outils : Jenkins, Azure DevOps, GitHub Actions, Linux, Python/Bash et les plateformes d'observabilité. J'utilise aussi Kubernetes pour le déploiement d'applications et des processus de provisionnement Terraform/Ansible existants.

Basé en Ontario, bilingue français/anglais et incorporé au Canada. Disponible immédiatement pour des mandats à distance : contrats à temps plein, soutien à temps partiel et projets à portée définie. Parlons de vos pipelines fragiles, de vos déploiements manuels ou de vos besoins en outillage opérationnel.

## Expérience Énergir — FR

Ingénieur DevOps senior | Septembre 2021 – Septembre 2026

• Centralisé les pipelines Jenkins pour environ 50 développeurs, 12 équipes et plus de 70 applications, avec des étapes communes et des contrôles SonarQube obligatoires.
• Créé la feuille de route de livraison comme responsable informel durant les trois premières années; accompagné les nouveaux développeurs et spécialistes DevOps et servi de point de contact principal pour les problèmes de livraison.
• Remplacé les scripts Salesforce par Salesforce CLI et une validation en environnement isolé, réduisant les fenêtres de déploiement manquées à une seule après la mise en place.
• Réduit la procédure de mise en production MuleSoft de 15 étapes à quelques tâches Jenkins, dont certaines exécutables avant la fenêtre de déploiement.
• Automatisé les déploiements Oracle courants sans compte d'urgence et ajouté des tests détectant des problèmes récurrents d'encodage.
• Pris en charge le pipeline ArcGIS : services cartographiques et propriétés versionnés, déployables en développement, en test et en production avec un compte de service. Première phase livrée en fin de mandat; adoption par l'équipe après mon départ.
• Utilisé les processus Terraform/Ansible d'une autre équipe pour contribuer à la migration des environnements Nexus, Jenkins et Vault vers Azure.

## Remaining experience and skills

Use the current Platform core resume for Desjardins, Tink, and SOVO factual content. Preserve the existing separate SOVO positions and dates; do not collapse the live role history automatically. Avoid older claims of deep Kubernetes ownership or personal authorship of the Terraform/Ansible platform.

Emphasize DevOps, CI/CD, Jenkins, deployment automation, Azure DevOps, Python, Linux, and observability in the skills section. Kubernetes and Terraform may remain as tools used, without positioning them as the core expertise.

## Publication status

- [ ] English headline and About applied live
- [ ] French headline and About applied live
- [ ] Énergir dates and experience updated in both languages
- [ ] Remaining experience checked against the current Platform resume

Historical September publication is documented in linkedin-profile.md; these October changes are not yet published.
