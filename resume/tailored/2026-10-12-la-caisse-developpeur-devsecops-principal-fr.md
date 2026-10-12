# Marc Berthelette

**Ingénieur DevOps principal — Plateformes CI/CD et automatisation de la qualité**

Smiths Falls (Ontario), Canada · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingue : français (langue maternelle) · anglais (courant) · Disponible immédiatement

## Sommaire professionnel

Ingénieur DevOps principal comptant près de 18 ans d'expérience en infrastructure, développement logiciel et exploitation de production. A centralisé la livraison Jenkins pour environ 50 développeurs, 12 équipes et plus de 70 applications chez Énergir, avec des étapes communes et des contrôles SonarQube obligatoires. A conçu chez Desjardins un service Python/FastAPI validant environ 250 dépôts Artifactory. Connaît Azure, Azure DevOps, GitHub Actions, Terraform et Ansible (flux de travail gérés par une autre équipe), Kubernetes et ArgoCD, dans les secteurs de l'énergie et des services financiers. Vise des livraisons fiables et moins de travail manuel pour les équipes de développement.

## Compétences techniques

**CI/CD et plateformes :** Jenkins (standards de pipelines partagés), Azure DevOps, GitHub Actions, contrôles de qualité SonarQube, JFrog Artifactory, Nexus, Salesforce CLI\
**Programmation et scripts :** Python, FastAPI, Bash, Java, C++, SQL\
**Infonuagique et infrastructure :** Microsoft Azure, AWS (EC2, S3, Route 53, VPC), flux Terraform/Ansible (utilisateur de modules d'une autre équipe), Linux, Puppet\
**Conteneurs et livraison :** Docker, déploiements applicatifs Kubernetes, ArgoCD\
**Surveillance et observabilité :** Dynatrace, Splunk, Elasticsearch, Logstash, Kibana

## Expérience professionnelle

### Énergir — Ingénieur DevOps senior

**Montréal (Québec) | septembre 2021 – septembre 2026**

- A centralisé l'intégration et la livraison continues Jenkins pour environ 50 développeurs, 12 équipes et plus de 70 applications, avec des étapes communes et des contrôles SonarQube obligatoires que les développeurs ne pouvaient pas simplement contourner.
- A favorisé l'adoption de la plateforme auprès de 12 équipes en dehors de toute ligne hiérarchique, au moyen de séances d'accompagnement récurrentes (environ six par année) après chaque livraison de pipeline.
- A refait la livraison Salesforce avec Salesforce CLI et la validation de chaque fusion candidate dans un bac à sable; les fenêtres de déploiement manquées de façon récurrente se sont réduites à une seule depuis la mise en service.
- A automatisé les livraisons Oracle après l'échec d'une tentative antérieure, éliminant le besoin d'un compte d'accès d'urgence approuvé chaque semaine pour les déploiements courants; a ajouté des tests détectant des problèmes récurrents d'encodage de fichiers.
- A ramené les mises en production MuleSoft d'une liste de contrôle manuelle de 15 étapes à quelques tâches Jenkins.
- A séparé les erreurs de code applicatif des erreurs de plateforme dans les rapports de build, réduisant les faux positifs et clarifiant la responsabilité de chaque correction.
- A versionné des services cartographiques ArcGIS et livré des déploiements par compte de service vers les environnements de développement, de test et de production, remplaçant les déploiements depuis les portables des développeurs.
- A aidé une équipe à faire passer ses environnements Nexus, Jenkins et Vault de l'exploitation manuelle dans le portail Azure à l'infrastructure en tant que code, avec les flux Terraform et Ansible d'une autre équipe; a ensuite introduit Azure Key Vault pour remplacer HashiCorp Vault.
- A agi comme responsable principal informel de la feuille de route de livraison pendant les trois premières années, a été la personne-ressource des développeurs lors des pannes et a intégré de nouveaux ingénieurs DevOps et développeurs.
- A introduit des pratiques d'ingénierie assistée par IA avec des limites de portée strictes et des points de validation humaine avant que du code généré par IA n'atteigne la production.

**Technologies clés :** Jenkins, SonarQube, Azure, Terraform, Ansible, Nexus, Salesforce CLI, Oracle, MuleSoft, ArcGIS

### Desjardins — Ingénieur DevOps senior (contrat)

**Montréal (Québec), télétravail | octobre 2025 – mars 2026** *(en parallèle du poste chez Énergir)*

- A bâti un service Python/FastAPI testant environ 250 dépôts distants JFrog Artifactory toutes les quatre heures, avec publication des résultats dans Dynatrace pour sept écosystèmes de paquets.
- A rendu la logique de validation réutilisable et les cas de test configurables; le même banc d'essai a servi de test de régression pour la mise à niveau d'entreprise d'Artifactory.
- A automatisé le provisionnement d'environnements Artifactory à la demande avec Kubernetes et ArgoCD, pour permettre aux administrateurs de tester en toute sécurité les changements de configuration et les mises à niveau.
- A mis en œuvre des politiques de rétention d'artefacts et des alertes Splunk détectant les modifications de configuration faites en dehors du CI/CD, améliorant la gouvernance et la traçabilité.
- A travaillé avec GitHub Actions, Kubernetes et ArgoCD dans un grand environnement de services financiers.

**Technologies clés :** Python, FastAPI, JFrog Artifactory, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk

### Tink — Ingénieur DevOps

**Montréal (Québec) | janvier 2018 – août 2021**

- A centralisé Jenkins Pipeline as Code pour 10 à 15 développeurs soutenant plus de 80 applications et plus de 20 clients, en uniformisant les étapes de livraison et en ajoutant de la visibilité des livraisons avec Jira.
- A automatisé l'application des correctifs et les redémarrages de noyau sur plus de 600 serveurs, réduisant l'entretien à une vérification mensuelle; a géré la configuration avec Puppet et Spacewalk.
- A créé une plateforme d'inventaire logiciel du parc exposant aux responsables de produit les versions d'applications, l'exposition aux vulnérabilités, les logiciels en fin de vie et l'état des certificats TLS.
- A participé à une rotation de garde 24/7 en production; a mis en place l'agrégation de journaux ELK et le redémarrage automatisé d'une grappe Elasticsearch non réactive.
- A construit pendant environ six mois l'environnement cible de migration AWS d'un client (EC2, S3, Route 53, VPC, memcached sur EC2, base de données relationnelle sans serveur), provisionné manuellement et sans expérience AWS préalable; le client a annulé la migration avant la bascule.

**Technologies clés :** Jenkins, Linux, Puppet, Spacewalk, AWS, Bash, Elasticsearch, Logstash, Kibana, Jira

### SOVO Technologies — Technicien principal → Ingénieur logiciel

**Montréal (Québec) | novembre 2008 – décembre 2017**

- A géré l'infrastructure informatique de l'entreprise et une équipe de techniciens; a réalisé un déménagement de serveurs sans interruption et a rendu redondants les serveurs essentiels.
- A développé des logiciels de planification de production, d'évaluation de reconnaissance vocale et de dictionnaire multilingue; a servi de dernière barrière de qualité avant les mises en production.

**Technologies clés :** C++, Java, SQL, Linux, Windows Server, Active Directory, VMware vSphere, réseau Cisco

## Formation

**Baccalauréat en génie de la fabrication automatisée** — École de technologie supérieure (ÉTS), Montréal (Québec) | 2005 – 2016

**DEC en techniques de l'informatique** — Cégep André-Laurendeau, Montréal (Québec) | 2002 – 2005
