Dear Affirm Hiring Team,

I am applying for the Staff Software Engineer (Continuous Integration) role. Making build and delivery pipelines fast, reliable and trusted by the developers who depend on them is the work I have done for the past five years, and the part of your posting I recognise most is the combination of reliability, developer feedback and enablement.

At Énergir I initiated the consolidation of duplicated Jenkins pipelines into shared pipelines used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications. Mandatory SonarQube checks could not be skipped, the shared pipeline code carried roughly 80–90% JaCoCo coverage with unit tests on every commit, and sample applications let us run integration tests across the supported stacks. I separated application-code failures from platform-pipeline failures in build reporting so developers could tell at a glance whose fix it was, and I ran scheduled smoke tests that alerted Teams when something outside the pipeline changed, such as a firewall rule. I then ran recurring enablement sessions with each team, because a CI standard only counts once people use it.

At Desjardins I built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a chosen Git reference, tested uncached retrieval across about 250 repositories on a schedule through ArgoCD, and published results to Dynatrace. I made most of the validation logic tool-agnostic and the test set configurable so administrators could add their own cases.

To be direct about fit: this is a Staff role and I have never held a formal lead title. I drove delivery improvements, was the primary developer contact when the ecosystem broke and onboarded new engineers, but I have not managed or formally mentored a CI team. My pipelines have been Jenkins and GitHub Actions, not Buildkite, and I have not worked on build systems for large monorepos or at the scale of a large technology company. My AWS and Kubernetes experience is as a user: a hand-built AWS migration environment, and application deployments to clusters other teams operate. I do not contribute to open source. I learn unfamiliar build systems by working out how they actually behave before changing them.

I am based in Ontario, bilingual in French and English, and available immediately. Before going further, could you tell me how you weigh Jenkins and GitHub Actions experience against Buildkite and monorepo experience for this team, and what the scope of the Staff role looks like in the first year?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
