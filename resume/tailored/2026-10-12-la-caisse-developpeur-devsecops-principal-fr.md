# Marc Berthelette

**Ingénieur DevOps principal — Plateformes CI/CD et automatisation de la qualité**

Smiths Falls (Ontario), Canada · À distance · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingue : français / anglais · Constitué en société au Canada · Disponible immédiatement

## Sommaire professionnel

Ingénieur et consultant principal comptant près de 18 ans d'expérience en infrastructure, développement logiciel et exploitation. A bâti chez Énergir des outils de livraison partagés dans un environnement de 12 équipes et plus de 70 applications, avec des contrôles SonarQube obligatoires, puis a animé des séances d'accompagnement pour favoriser leur adoption. A automatisé chez Desjardins la validation de dépôts Artifactory avec Python/FastAPI et Dynatrace. Utilise Terraform/Ansible et Kubernetes à partir de plateformes gérées par d'autres équipes.

## Compétences techniques

**CI/CD et plateformes :** Jenkins (pipelines partagés), Azure DevOps, GitHub Actions, contrôles de qualité SonarQube, JaCoCo, JFrog Artifactory, Nexus, Salesforce CLI\
**Programmation et scripts :** Python, FastAPI, Bash, Java, C++, SQL\
**Infonuagique et infrastructure :** Azure, flux Terraform/Ansible (utilisateur de modules d'une autre équipe), Linux, Puppet, environnement de migration AWS\
**Conteneurs et observabilité :** déploiements applicatifs Kubernetes, Docker, ArgoCD, Dynatrace, Splunk, ELK

## Expérience professionnelle

### Énergir — Ingénieur DevOps senior (contrat)

**Montréal (Québec) | septembre 2021 – septembre 2026**\
Mandat de consultation de cinq ans, renouvelé quatre fois.

- A initié des pipelines Jenkins partagés adoptés par toutes les équipes qui déployaient déjà avec Jenkins, dans un environnement d'environ 50 développeurs, 12 équipes et plus de 70 applications; a atteint une couverture JaCoCo d'environ 80 à 90 % avec des tests unitaires à chaque validation et bâti des applications d'exemple pour les tests d'intégration.
- A imposé des étapes communes et des contrôles SonarQube obligatoires dans les pipelines partagés, que les développeurs ne pouvaient pas simplement contourner.
- A séparé les erreurs de code applicatif des erreurs de pipeline dans les rapports de build afin que chaque équipe sache à qui revenait la correction.
- A animé des séances d'accompagnement récurrentes (environ six par année) avec chaque équipe après la livraison des pipelines; a intégré de nouveaux ingénieurs DevOps et développeurs et a été la personne-ressource principale des développeurs lors des pannes.
- A établi le principe « construire une fois, déployer partout » : a migré environ cinq applications Node.js vers une configuration à l'exécution au moyen de demandes de fusion révisées par les équipes, afin qu'un même build testé serve chaque environnement.
- A remplacé une liste de contrôle MuleSoft de 15 étapes par des déploiements par version d'artefacts validés par l'assurance qualité, déplaçant la préparation avant les fenêtres de production et simplifiant le retour arrière.
- A remplacé d'anciens scripts de déploiement ANT par Salesforce CLI et bâti une validation qui déploie chaque fusion candidate dans un bac à sable dédié et exécute la suite de tests complète.
- A automatisé les livraisons Oracle courantes sans demande d'accès d'urgence (les étapes manuelles conservaient leurs approbations); a éliminé les incidents d'encodage au moyen de vérifications SQL et de paramètres régionaux distincts pour SQL et Forms.
- A migré la journalisation Salesforce de production vers l'ingestion directe dans Dynatrace; a enrichi l'analyse des erreurs et les tableaux de bord pour aider l'équipe à examiner des problèmes auparavant invisibles.

**Technologies clés :** Jenkins, SonarQube, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Node.js, MuleSoft, Dynatrace

### Desjardins — Ingénieur DevOps senior (contrat)

**Montréal (Québec), télétravail | octobre 2025 – mars 2026**\
En parallèle du mandat chez Énergir.

- A bâti un flux de travail Python/FastAPI qui provisionnait Artifactory, appliquait la configuration d'une référence Git choisie et testait la récupération d'artefacts sans cache sur environ 250 dépôts.
- A déployé la suite par ArgoCD/GitOps pour une exécution planifiée, avec publication dans Dynatrace des résultats par version de configuration et par artefact afin de révéler les défaillances de configuration et de connectivité en amont.
- A mis en œuvre des politiques de rétention d'artefacts et des alertes Splunk détectant les modifications de configuration faites en dehors du CI/CD.
- A rendu la majeure partie de la logique de validation indépendante de l'outil et l'ensemble de tests configurable, pour que les administrateurs de la plateforme puissent ajouter leurs propres cas.
- A travaillé avec Kubernetes, ArgoCD et GitHub Actions dans un grand environnement de services financiers.

**Technologies clés :** Python, FastAPI, GitHub Actions, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — Ingénieur DevOps

**Montréal (Québec) | janvier 2018 – août 2021**

- A uniformisé les pipelines Jenkins pour 10 à 15 développeurs soutenant plus de 80 applications et plus de 20 clients, en intégrant les détails de livraison et les références Jira aux rapports de déploiement.
- A remplacé l'application réactive des correctifs sur plus de 600 serveurs par des calendriers Spacewalk échelonnés, des groupes par environnement et par rôle, des lots A/B pour le frontal et l'intergiciel et des redémarrages tenant compte des dépendances.
- A contrôlé les mises à jour au moyen de dépôts de paquets propres à chaque client; a publié l'avancement des correctifs et des redémarrages, ainsi que les échecs, dans Rocket.Chat, la surveillance PRTG existante couvrant la santé des services.
- A bâti un inventaire du parc de serveurs Unix et Windows pour repérer les applications vulnérables et les mises à niveau de fin de vie; a ajouté une évaluation TLS et le suivi des versions par environnement pour les opérations, les responsables de produit et l'assurance qualité.
- A construit un environnement cible de migration AWS par provisionnement manuel dans la console (EC2, S3, Route 53, VPC, services de cache et de base de données); le client a annulé avant la bascule en production.

**Technologies clés :** Linux, Jenkins, Puppet, Spacewalk, PRTG, ELK, AWS, Rocket.Chat

### SOVO Technologies — Technicien principal → Ingénieur logiciel

**Montréal (Québec) | novembre 2008 – décembre 2017**

- A dirigé et réalisé, avec un deuxième technicien, la majeure partie du travail de redondance (HAProxy, authentification, serveurs de reconnaissance vocale et serveurs de fichiers); soutenait des exigences de sous-titrage en direct d'au plus trois minutes d'interruption par diffusion et de huit secondes de latence.
- A assuré la planification et l'exécution informatiques de deux déménagements de bureaux touchant environ 15 à 20 postes, en préparant réseaux et câblage et en coordonnant des déplacements par phases pour limiter les perturbations.
- A développé des logiciels d'ordonnancement de production, d'évaluation de la reconnaissance vocale et de dictionnaires multilingues; a servi de dernier contrôle de qualité avant les mises en production.

**Technologies clés :** HAProxy, Active Directory, VMware vSphere, Linux, Windows Server, C++, Java, SQL

## Formation

**Baccalauréat en génie de la fabrication automatisée** — École de technologie supérieure (ÉTS), Montréal | 2016

**DEC en techniques de l'informatique** — Cégep André-Laurendeau, Montréal | 2005
