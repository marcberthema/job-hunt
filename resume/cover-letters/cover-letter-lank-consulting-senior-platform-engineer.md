Dear LANK Consulting Hiring Team,

I am applying for the Senior Platform Engineer role. Setting platform standards, pipeline templates and quality gates, then getting delivery teams to adopt them, is the part of this posting that matches my work.

At Énergir I initiated the consolidation of duplicated Jenkins pipelines into one shared repository used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications. Shared stages and mandatory SonarQube checks could not be skipped, shared pipeline code carried roughly 80–90% JaCoCo coverage with tests on every commit, and the same tested artifact was promoted from QA to production. I separated application-code failures from platform-pipeline failures in build reporting so teams could tell whose fix it was. I then ran recurring enablement sessions with each team, because a standard only counts once people use it. I also gave implementation direction to a junior engineer on repository-governance tooling for stale branches, branch protection and review configuration.

My best work usually starts when the request is narrower than the real problem. At Desjardins I was asked to verify the configuration of Artifactory repositories. I built a Python/FastAPI workflow that provisioned the platform, applied configuration from a chosen Git reference, tested uncached retrieval across about 250 repositories, ran through ArgoCD, and published results to Dynatrace. I also implemented artifact retention policies and Splunk alerts for configuration changes made outside CI/CD, which is the same drift and release-control concern your posting describes. I chose the larger solution because it was best for the client, not the cheapest.

To be direct about fit: the posting asks for expert Bicep and Terraform module architecture, policy-as-code, APIM and service catalogs. I have not written Bicep. My Terraform and Ansible work was with workflows owned by another team, while helping move team-owned Nexus, Jenkins and Vault environments in Azure from manual portal operations to Infrastructure as Code, and later introducing Azure Storage-backed Terraform state and Key Vault. I have not authored module libraries, run policy-as-code or built APIM. I also have no formal lead title, though I have acted as the technical owner for delivery tooling. I would rather you hear the boundaries from me than find them in an interview.

I am bilingual in French and English, based in Smiths Falls, Ontario, and available immediately. Before going further, could you confirm the client's identity once we speak, whether the role is contract or permanent, the pay currency and basis, and that a candidate based in Ontario is eligible?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
