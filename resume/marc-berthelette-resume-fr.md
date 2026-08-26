# Marc Berthelette

**Ingénieur DevOps principal | Consultant en ingénierie de plateforme**

Smiths Falls, ON, Canada · Télétravail · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingue : français (langue maternelle) · anglais (courant) · Incorporé au Canada · Disponible immédiatement

---

## Sommaire professionnel

Consultant en ingénierie DevOps et de plateforme comptant 18 ans passés à rendre livrables des systèmes qu'il ne connaissait pas au départ. Chez Énergir, a standardisé le CI/CD pour neuf écosystèmes technologiques distincts — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce et Databricks — au profit de 12 équipes applicatives et de plus de 70 applications, en abordant la plupart de ces écosystèmes sans expérience préalable et en décortiquant chacun d'eux avant de l'automatiser. Chez Desjardins, a bâti le service Python/FastAPI qui a doté 250 dépôts Artifactory d'entreprise de leur premier signal de santé en continu. Expertise approfondie en Microsoft Azure, Terraform, Kubernetes et observabilité dans des secteurs réglementés (énergie, services financiers). Prend en charge le problème dans son ensemble — y compris les parties que personne ne lui a confiées — et recommande la bonne solution plutôt que la moins chère. Bilingue français/anglais, incorporé au Canada, disponible immédiatement.

## Compétences techniques

| Catégorie | Technologies |
|---|---|
| **Plateformes infonuagiques et DevOps** | Microsoft Azure, Azure DevOps, GitHub Actions, Jenkins, JFrog Artifactory, Nexus, CloudFoundry |
| **Infrastructure en tant que code** | Terraform, Ansible, Puppet |
| **Conteneurs et orchestration** | Docker, Kubernetes, ArgoCD |
| **Surveillance et observabilité** | Dynatrace, Splunk, ELK Stack (Elasticsearch, Logstash, Kibana), alertes proactives, gestion des incidents |
| **Programmation et scripting** | Python, FastAPI, Bash, C++, Java, SQL, NoSQL |
| **Systèmes d'exploitation et web** | Red Hat Linux, Ubuntu, Apache, Nginx |
| **Gestion de projet et collaboration** | Jira, Agile / Scrum, documentation technique, habilitation des parties prenantes |

## Expérience professionnelle

### Énergir — Ingénieur DevOps principal

**Montréal, QC | Septembre 2021 – Présent**

- Standardisé la livraison CI/CD pour neuf écosystèmes technologiques distincts — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce et Databricks — au profit de 12 équipes applicatives et de plus de 70 applications, faisant passer les équipes du déploiement manuel à des pipelines automatisés avec portes de qualité, et abordant la plupart d'entre eux sans expérience préalable ; fait passer l'équipe Oracle du déploiement entièrement manuel à la livraison automatisée, après l'échec d'une tentative antérieure.
- Reconstruit la livraison Salesforce sans expérience préalable de la plateforme — remplaçant les anciens scripts ANT par l'outillage officiel Salesforce CLI, puis proposant et développant un pipeline de validation testant chaque fusion candidate dans un bac à sable dédié — faisant passer l'équipe des fenêtres de déploiement ratées à une mise en production fiable un mardi sur deux. Étendu par la suite en une intégration automatisée Salesforce – Data Lake.
- Réduit les faux positifs des pipelines et rendu les résultats de build autodiagnostiques en distinguant, dans les rapports, les erreurs de code applicatif des erreurs de pipeline de plateforme — permettant à chaque équipe de savoir d'un coup d'œil de qui relevait la défaillance.
- Dirigé des initiatives de modernisation infonuagique, migrant de 5 à 10 services essentiels vers Microsoft Azure, et implanté des pratiques d'Infrastructure en tant que code (IaC) avec Terraform et Ansible pour standardiser le provisionnement et éliminer la dérive de configuration entre les environnements de développement, de test et de production.
- Mené des analyses de cause profonde (RCA) sur des incidents critiques en production et développé la surveillance proactive, les tableaux de bord d'observabilité et la remédiation automatisée ayant réduit le temps moyen de rétablissement (MTTR) à l'échelle du parc applicatif.
- Favorisé l'adoption du CI/CD et des standards d'ingénierie de plateforme auprès de 12 équipes hors de tout lien hiérarchique, en animant des séances récurrentes d'habilitation (~6/an) avec chaque équipe applicative après la livraison de son pipeline — transformant l'outillage livré en usage réel plutôt qu'en tablettage.

**Technologies clés :** Microsoft Azure, Azure DevOps, GitHub Actions, Terraform, Ansible, Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks, Data Lake, ServiceNow, IaC

### Desjardins — Ingénieur DevOps principal *(Contrat)*

**Montréal, QC (télétravail) | Octobre 2025 – Mars 2026** — *mandat mené en parallèle du poste chez Énergir*

- Livré un mandat de 6 mois axé sur le renforcement et l'opérationnalisation de la plateforme JFrog Artifactory d'entreprise, concevant un service de surveillance en Python/FastAPI testant la configuration d'environ 250 dépôts distants couvrant sept écosystèmes de paquets toutes les 4 heures, avec publication dans Dynatrace et tableaux de bord segmentés par technologie.
- Étendu le mandat bien au-delà de sa portée initiale — vérifier la configuration des dépôts — en rendant la logique de validation agnostique de l'outil plutôt que spécifique à JFrog et l'ensemble des tests configurable, afin que les administrateurs couvrent leurs propres cas ; le même harnais a ensuite sécurisé la mise à niveau de la plateforme JFrog d'entreprise.
- Automatisé le provisionnement d'instances Artifactory à la demande à l'aide de Kubernetes et ArgoCD, permettant aux administrateurs système de déployer des environnements corporatifs entièrement configurés pour tester en toute sécurité les changements de configuration et les mises à niveau.
- Implanté des politiques de cycle de vie des artefacts pour imposer des standards de rétention et réduire les coûts de stockage ; développé des alertes Splunk pour détecter les changements de configuration manuels effectués hors du pipeline CI/CD, améliorant la traçabilité et la conformité.

**Technologies clés :** JFrog Artifactory, Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk, Docker, Helm, Maven, NuGet, Debian

### Tink — Ingénieur DevOps

**Montréal, QC | Janvier 2018 – Août 2021**

- Centralisé les pipelines Jenkins en tant que code pour une équipe de 10 à 15 développeurs maintenant plus de 80 applications pour plus de 20 clients, standardisant les étapes de pipeline peu importe la pile technologique sous-jacente et ajoutant une visibilité sur les livraisons via Jira.
- Automatisé les correctifs système sur un parc de plus de 600 serveurs incluant le redémarrage lors des mises à jour du noyau, réduisant le processus à une vérification mensuelle avec un temps d'arrêt quasi nul, la configuration du parc étant pilotée de façon déclarative par Puppet et Spacewalk; développé une agrégation centralisée des journaux avec la suite ELK.
- Construit les couches de calcul, de cache et de base de données de l'environnement cible AWS d'un client en migration — EC2, S3, Route 53, VPC, memcached auto-géré, base de données relationnelle sans serveur — sans expérience préalable d'AWS; le client a annulé la migration avant la bascule.
- Conçu et développé, de sa propre initiative et hors de tout mandat assigné, une plateforme d'inventaire logiciel répertoriant chaque application et chaque version installées sur le parc de plus de 600 serveurs — exposant les vulnérabilités CVE, les logiciels en fin de vie (EoL) et une notation SSL/TLS directement aux chargés de produit, qui n'avaient jusque-là aucune visibilité sur le risque de sécurité et d'obsolescence du parc.

**Technologies clés :** Jenkins, ELK Stack (Elasticsearch, Logstash, Kibana), Bash, Linux, Jira, Puppet, PRTG, Spacewalk, CentOS, RockyOS, NetScaler, AWS (EC2, S3, Route 53, VPC), suivi CVE/vulnérabilités, notation SSL/TLS

### SOVO Technologies — Technicien principal → Ingénieur logiciel

**Montréal, QC | Novembre 2008 – Décembre 2017**

- Supervisé l'ensemble de l'infrastructure TI de l'entreprise — incluant un projet de relocalisation de serveurs sans interruption de service et une architecture de serveurs redondante éliminant les points de défaillance uniques — tout en gérant une équipe de techniciens (planification, formation, délégation) et en agissant comme dernier point de contrôle qualité avant toute mise en production.
- Développé des logiciels de production en parallèle du rôle d'infrastructure pendant environ sept ans avant que le titre ne l'officialise : le logiciel d'ordonnancement couvrant l'ensemble du cycle de planification du département, puis un système d'évaluation de la reconnaissance vocale et une infrastructure de dictionnaires multilingues.

**Technologies clés :** C++, Java, SQL, Windows Server, Linux, Active Directory, VMware vSphere, routage Cisco, pare-feu/VPN, sauvegarde et reprise

## Formation

**Baccalauréat en génie de la production automatisée** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DEC en Techniques de l'informatique** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
