# Marc Berthelette

**Ingénieur en fiabilité des sites (SRE) senior — Observabilité, réponse aux incidents et automatisation**

Smiths Falls (Ontario), Canada · À distance · marc.berthelette@gmail.com\
[marcberthelette.com](https://marcberthelette.com) · [LinkedIn](https://linkedin.com/in/marc-berthelette-3aba6917)\
Bilingue : français / anglais · Constitué en société au Canada · Disponible immédiatement

## Sommaire professionnel

Ingénieur comptant près de 18 ans d'expérience en infrastructure, développement logiciel et exploitation. A assuré la fiabilité de la production par la validation préventive, la surveillance, l'automatisation d'un parc de serveurs et la réponse aux incidents. Expérience dans l'énergie chez Énergir, les services financiers chez Desjardins, un parc de plus de 600 serveurs chez Tink et une infrastructure de sous-titrage en direct soumise à des exigences strictes de disponibilité et de latence. Environnements Azure documentés (Nexus, Jenkins, Vault) et outils de livraison pour des équipes applicatives.

## Compétences techniques

**Fiabilité :** réponse aux incidents, analyse des causes profondes, soutien en garde (on-call), correction automatisée, Linux\
**Observabilité :** Dynatrace, Splunk, ELK, PRTG; Python, FastAPI, Bash\
**Infonuagique et infrastructure :** Azure, flux Terraform/Ansible (utilisateur de flux gérés par une autre équipe), Puppet, Spacewalk, environnement de migration AWS\
**Livraison :** Jenkins, GitHub Actions, Azure DevOps, Artifactory, déploiements applicatifs Kubernetes, ArgoCD

## Expérience professionnelle

### Énergir — Ingénieur DevOps senior (contrat)

**Montréal (Québec) | septembre 2021 – septembre 2026**\
Mandat de consultation de cinq ans, renouvelé quatre fois.

- A migré la journalisation Salesforce de production de Logstash vers l'ingestion directe dans Dynatrace en reproduisant le traitement existant, retirant l'intermédiaire de ce chemin de journalisation.
- A extrait les types et messages d'erreurs DML ainsi que les classes d'origine et bâti des tableaux de bord révélant des problèmes auparavant invisibles pour l'équipe Salesforce; la responsabilité a ensuite été transférée à un employé de longue date.
- A mis en place des tests de fumée Jenkins aux quatre heures avec alertes Teams pour détecter les défaillances de dépendances externes, notamment les changements de pare-feu; a clarifié à qui revenait la correction entre pipeline et application.
- A atteint une couverture JaCoCo d'environ 80 à 90 % du code des pipelines partagés avec des tests à chaque validation; a bâti des applications d'exemple pour les tests d'intégration manuels sur les technologies prises en charge.
- A éliminé les incidents d'encodage récurrents d'Oracle au moyen de vérifications d'encodage SQL et de paramètres régionaux distincts pour SQL et Forms; a converti les fichiers SQL existants et documenté les procédures pour les développeurs.
- A bâti une validation nocturne pour Salesforce; a signalé les échecs persistants au directeur de projet, ce qui a mené à des correctifs dans 4 à 5 équipes en 48 heures et a permis le déploiement du projet à la date prévue.

**Technologies clés :** Jenkins, Azure, Python, JaCoCo, Salesforce CLI, Oracle, Dynatrace, Logstash

### Desjardins — Ingénieur DevOps senior (contrat)

**Montréal (Québec), télétravail | octobre 2025 – mars 2026**\
En parallèle du mandat chez Énergir.

- A bâti un flux de travail Python/FastAPI qui provisionnait Artifactory, appliquait la configuration d'une référence Git choisie et testait la récupération d'artefacts sans cache sur environ 250 dépôts.
- A déployé la suite par ArgoCD/GitOps pour une exécution planifiée, avec publication dans Dynatrace des résultats par version de configuration et par artefact afin de révéler les défaillances de configuration et de connectivité en amont.
- A mis en œuvre des politiques de rétention d'artefacts et des alertes Splunk détectant les modifications de configuration faites en dehors du CI/CD.

**Technologies clés :** Python, FastAPI, Artifactory, Kubernetes, ArgoCD, Dynatrace, Splunk

### Tink — Ingénieur DevOps

**Montréal (Québec) | janvier 2018 – août 2021**

Soutenait toute l'équipe de développement de 10 à 15 développeurs et surveillait un parc de production de plus de 600 serveurs soutenant plus de 80 applications pour plus de 20 clients.

- A automatisé la réponse déclenchée par PRTG à la saturation du processeur d'Elasticsearch : tentative de redémarrage du processus après deux minutes et alerte au personnel de garde après cinq minutes si la saturation persistait; a participé à une rotation de garde 24 h sur 24, 7 jours sur 7.
- A remplacé l'application réactive des correctifs sur plus de 600 serveurs par des calendriers Spacewalk échelonnés, des groupes par environnement et par rôle, des lots A/B pour le frontal et l'intergiciel et des redémarrages tenant compte des dépendances.
- A contrôlé les versions de paquets au moyen de dépôts propres à chaque client et publié l'avancement des mises à jour et des redémarrages, ainsi que les échecs, dans Rocket.Chat; la surveillance PRTG existante couvrait la santé des services.
- A bâti un inventaire des serveurs Unix et Windows pour l'analyse de l'impact des vulnérabilités, la planification de fin de vie et l'évaluation TLS; a relié versions de livraison et références Jira pour les opérations, les responsables de produit et l'assurance qualité.
- A bâti une journalisation ELK centralisée et géré la configuration du parc avec Puppet. A construit un environnement cible de migration AWS par provisionnement manuel dans la console; le client a annulé avant la bascule en production.

**Technologies clés :** Linux, Jenkins, Puppet, Spacewalk, PRTG, ELK, AWS, Rocket.Chat

### SOVO Technologies — Technicien principal → Ingénieur logiciel

**Montréal (Québec) | novembre 2008 – décembre 2017**

- A dirigé et réalisé, avec un deuxième technicien, la majeure partie du travail de redondance (HAProxy, Active Directory, serveurs de reconnaissance vocale et serveurs de fichiers) pour la production de sous-titrage en direct.
- A soutenu des exigences clients d'au plus trois minutes d'interruption par diffusion et de huit secondes entre la parole et le sous-titre; a réparti les postes des cabines sur des commutateurs distincts et fourni deux liens Internet.
- A planifié et exécuté deux déménagements de bureaux par phases touchant environ 15 à 20 postes. A développé des logiciels d'ordonnancement de production et d'évaluation de la reconnaissance vocale.

**Technologies clés :** HAProxy, Active Directory, VMware vSphere, Linux, Windows Server, C++, Java, SQL

## Formation

**Baccalauréat en génie de la fabrication automatisée** — École de technologie supérieure (ÉTS), Montréal | 2016

**DEC en techniques de l'informatique** — Cégep André-Laurendeau, Montréal | 2005
