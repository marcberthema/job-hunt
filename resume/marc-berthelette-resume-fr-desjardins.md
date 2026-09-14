# Marc Berthelette

**Ingénieur SRE senior/principal · Ingénierie de plateforme · DevOps · Fiabilité**

Smiths Falls, ON, Canada · Télétravail · marc.berthelette@gmail.com\
[linkedin.com/in/marc-berthelette-3aba6917](https://linkedin.com/in/marc-berthelette-3aba6917) · Bilingue : français (langue maternelle) · anglais (courant) · Incorporé au Canada

---

## Sommaire professionnel

Ingénieur DevOps principal qui prend en charge des systèmes de production que d'autres hésitent à toucher — les apprend à froid sous échéancier serré, puis remplace les processus manuels et fragiles par de l'automatisation qui tient la route. Trois fois, chez trois employeurs, sur huit ans, s'est vu confier une portée étroite — et a chaque fois livré quelque chose structurellement plus large que ce qui était demandé : une plateforme de visibilité sécurité à l'échelle du parc chez Tink, construite sans mandat assigné ; une migration Salesforce CLI chez Énergir qui a aussi rendu un mauvais déploiement structurellement incapable d'atteindre la production ; un harnais de validation JFrog chez Desjardins qui a fini par sécuriser la mise à niveau de la plateforme elle-même. Expertise approfondie en Microsoft Azure, Terraform, Kubernetes et observabilité dans des secteurs réglementés (énergie, services financiers), bâtie en standardisant le CI/CD pour 12 équipes applicatives sur neuf écosystèmes distincts. Ce qui distingue, c'est le jugement, pas le nombre d'outils : corrige les causes profondes plutôt que d'empiler des correctifs, et recommande la bonne solution plutôt que la moins chère. Bilingue français/anglais, incorporé au Canada.

## Compétences clés

| Catégorie | Focus |
|---|---|
| **Fiabilité et ingénierie de production** | Analyse de cause profonde, réduction du MTTR, surveillance et alertes proactives, gestion des incidents, remédiation automatisée, garde 24/7 |
| **Ingénierie de plateforme et habilitation** | Standardisation du CI/CD sur des piles technologiques hétérogènes, pipeline en tant que code, outillage interne pour développeurs, habilitation inter-équipes hors de tout lien hiérarchique |
| **Infrastructure et automatisation infonuagique** | Microsoft Azure (Compute, RBAC/ABAC/Policy, Firewall, VNets, NSG, Private Link, ExpressRoute), Terraform, Ansible, Puppet, Kubernetes, AKS (CKA en cours), Docker, ArgoCD |
| **CI/CD et gestion d'artefacts** | Azure DevOps, GitHub Actions, Jenkins, JFrog Artifactory, Nexus, CloudFoundry |
| **Observabilité** | Dynatrace, Splunk, ELK Stack (Elasticsearch, Logstash, Kibana) |
| **Ingénierie assistée par IA** | Développement assisté par IA à portée contrôlée, points de contrôle de validation humaine, évaluation du risque lié à la promotion de code généré |
| **Programmation et systèmes** | Python, FastAPI, PowerShell, Bash, C++, Java, SQL, NoSQL, Red Hat Linux, Ubuntu, Apache, Nginx |

## Expérience professionnelle

### Énergir — Ingénieur DevOps principal

**Montréal, QC | Septembre 2021 – Présent**

- Pris en charge la standardisation CI/CD pour 12 équipes applicatives et plus de 70 applications sur neuf écosystèmes technologiques distincts — Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce et Databricks — en abordant la plupart d'entre eux sans expérience préalable ; fait passer l'équipe Oracle du déploiement entièrement manuel à la livraison automatisée, après l'échec d'une tentative antérieure.
- Reconstruit la livraison Salesforce sans expérience préalable de la plateforme — remplaçant les anciens scripts ANT par l'outillage officiel Salesforce CLI et développant un pipeline de validation testant chaque fusion candidate dans un bac à sable — faisant passer l'équipe d'un problème récurrent de fenêtres de déploiement ratées à une seule fenêtre manquée depuis la mise en place, avec une cadence fiable un mardi sur deux.
- Réduit les faux positifs des pipelines en distinguant les erreurs de code applicatif des erreurs de plateforme, et dirigé la modernisation infonuagique migrant de 5 à 10 services vers Microsoft Azure — configurant RBAC, Azure Firewall, VNets, NSG, Private Link — avec de l'IaC Terraform/Ansible pour éliminer la dérive de configuration.
- Mené des analyses de cause profonde sur des incidents critiques et développé la surveillance proactive, les tableaux de bord et la remédiation automatisée ayant réduit le MTTR à l'échelle du parc applicatif.
- Instauré des pratiques d'ingénierie assistée par IA au cours des 6 à 9 derniers mois — garde-fous de portée et points de contrôle de validation humaine avant que tout code généré par IA n'atteigne la production — et signalé à la direction l'absence de protections équivalentes.
- Favorisé l'adoption du CI/CD et des standards d'ingénierie de plateforme auprès de 12 équipes hors de tout lien hiérarchique, en animant des séances récurrentes d'habilitation (~6/an) avec chaque équipe applicative après la livraison de son pipeline — transformant l'outillage livré en usage réel plutôt qu'en tablettage.

**Technologies clés :** Microsoft Azure, RBAC, Azure Firewall, VNets, NSG, Private Link, Azure DevOps, GitHub Actions, Terraform, Ansible, Java, Node.js, Python, Spark, Oracle, CloudFoundry, MuleSoft, Salesforce, Databricks, Data Lake, ServiceNow, IaC

### Desjardins — Ingénieur DevOps principal *(Contrat)*

**Montréal, QC (télétravail) | Octobre 2025 – Mars 2026** — *mandat mené en parallèle du poste chez Énergir*

- Livré un mandat de 6 mois axé sur le renforcement de la plateforme JFrog Artifactory d'entreprise, concevant un service Python/FastAPI testant la configuration d'environ 250 dépôts distants couvrant sept écosystèmes de paquets toutes les 4 heures, avec publication dans Dynatrace.
- Étendu le mandat bien au-delà de sa portée initiale en rendant la logique de validation agnostique de l'outil et l'ensemble des tests configurable ; le même harnais a ensuite sécurisé la mise à niveau de la plateforme JFrog d'entreprise.
- Automatisé le provisionnement d'instances Artifactory à la demande avec Kubernetes et ArgoCD, permettant aux administrateurs de déployer des environnements entièrement configurés pour tester en toute sécurité.
- Implanté des politiques de cycle de vie des artefacts pour la rétention et les coûts de stockage ; développé des alertes Splunk pour les changements de configuration manuels hors du pipeline CI/CD.

**Technologies clés :** JFrog Artifactory, Python, FastAPI, Kubernetes, ArgoCD, GitHub Actions, Dynatrace, Splunk, Docker, Helm, Maven, NuGet, Debian

### Tink — Ingénieur DevOps

**Montréal, QC | Janvier 2018 – Août 2021**

- Centralisé les pipelines Jenkins en tant que code pour une équipe de 10 à 15 développeurs maintenant plus de 80 applications pour plus de 20 clients, standardisant les étapes de pipeline peu importe la pile technologique sous-jacente et ajoutant une visibilité sur les livraisons via Jira.
- Automatisé les correctifs système (incluant les redémarrages lors des mises à jour du noyau) sur plus de 600 serveurs, réduisant le processus à une vérification mensuelle avec un temps d'arrêt quasi nul, la configuration pilotée de façon déclarative par Puppet et Spacewalk ; ajouté une agrégation centralisée des journaux avec ELK.
- Construit les couches de calcul, de cache et de base de données de l'environnement cible AWS d'un client — EC2, S3, Route 53, VPC, memcached auto-géré, base de données sans serveur — sans expérience préalable d'AWS ; le client a annulé avant la bascule.
- Conçu et développé, de sa propre initiative et hors de tout mandat assigné, une plateforme d'inventaire logiciel répertoriant chaque application et chaque version installées sur le parc de plus de 600 serveurs — exposant les vulnérabilités CVE, les logiciels en fin de vie (EoL) et une notation SSL/TLS directement aux chargés de produit, qui n'avaient jusque-là aucune visibilité sur le risque de sécurité et d'obsolescence du parc.
- Réduit la fréquence des appels de garde 24/7 grâce à l'analyse de cause profonde et à la prévention — passant d'environ un appel aux deux rotations en début de mandat à environ un appel aux 4-5 rotations à la fin ; construit une réponse auto-réparatrice pour un cluster Elasticsearch récurremment instable, la surveillance le redémarrant automatiquement au lieu d'appeler quelqu'un pour un mode de défaillance connu.

**Technologies clés :** Jenkins, ELK Stack (Elasticsearch, Logstash, Kibana), Bash, Linux, Jira, Confluence, Puppet, PRTG, Spacewalk, CentOS, RockyOS, NetScaler, AWS (EC2, S3, Route 53, VPC), suivi CVE/vulnérabilités, notation SSL/TLS

### SOVO Technologies — Technicien principal → Ingénieur logiciel

**Montréal, QC | Novembre 2008 – Décembre 2017**

- Supervisé l'ensemble de l'infrastructure TI de l'entreprise — incluant une relocalisation de serveurs sans interruption de service et une architecture redondante éliminant les points de défaillance uniques — tout en gérant une équipe de techniciens et en agissant comme dernier point de contrôle qualité avant mise en production.
- Développé des logiciels de production en parallèle du rôle d'infrastructure pendant environ sept ans avant que le titre ne l'officialise : le logiciel d'ordonnancement couvrant l'ensemble du cycle de planification du département, puis un système d'évaluation de la reconnaissance vocale et une infrastructure de dictionnaires multilingues.

**Technologies clés :** C++, Java, SQL, Windows Server, Linux, Active Directory, VMware vSphere, routage Cisco, pare-feu/VPN, sauvegarde et reprise

## Formation

**Baccalauréat en génie de la production automatisée** — École de Technologie Supérieure (ÉTS), Montréal, QC | 2005 – 2016

**DEC en Techniques de l'informatique** — Cégep André-Laurendeau, Montréal, QC | 2002 – 2005
