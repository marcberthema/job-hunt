Dear Slice Hiring Team,

I am applying for the Software Developer, DevEx (Deploy & Run) role. The part of your posting I recognise most is the goal of reducing cognitive load for engineers by replacing toil with automation, guardrails and shared tooling. That is the work I have done for the past five years.

At Énergir I initiated the consolidation of duplicated Jenkins pipelines into shared pipelines used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications. Mandatory SonarQube checks could not be skipped, the shared pipeline code carried roughly 80–90% JaCoCo coverage with unit tests on every commit, and sample applications let us run integration tests across the supported stacks. I moved about five Node.js applications to runtime configuration through team-reviewed pull requests so one tested build could serve every environment, and replaced a 15-step MuleSoft checklist with version-based deployments of QA-tested artifacts.

At Desjardins I built a Python/FastAPI workflow that provisioned Artifactory, applied configuration from a chosen Git reference, and tested uncached artifact retrieval across about 250 repositories. It ran on a schedule through ArgoCD and published results to Dynatrace, so configuration and upstream connectivity failures became visible. That is the kind of Python internal tooling plus GitOps delivery your team describes.

To be direct about fit: my Kubernetes, ArgoCD and Terraform experience is as a user of platforms that other teams operate. I have deployed applications through ArgoCD and GitHub Actions, but I have not built a Kubernetes platform from scratch or authored Terraform modules. My observability tooling has been Dynatrace, Splunk and ELK rather than Datadog, and my AWS experience is a hand-built migration environment, not a production estate. I have not used AI coding agents as a primary workflow in a team setting.

I am based in Ontario, bilingual in French and English, and available immediately. Before going further, could you tell me which hiring arrangement applies to Canadian candidates (employee or contractor, and through which entity), and what the base compensation range is for this role?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
