Dear NVIDIA Isaac Sim Hiring Team,

I am applying for the Senior DevOps Engineer role on the Isaac Sim team. The posting is about making build, test and release infrastructure faster, more reproducible and easier for developers to trust, and that is the work I have done for the past five years.

At Énergir I initiated the consolidation of duplicated Jenkins pipelines into shared pipelines used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications. Mandatory SonarQube checks could not be skipped, the shared pipeline code carried roughly 80–90% JaCoCo coverage with unit tests on every commit, and sample applications across the supported stacks let us run integration tests against the pipelines themselves. I separated application-code failures from platform-pipeline failures in build reporting so developers could tell at a glance whose fix it was, and I ran scheduled smoke tests that alerted Teams when something outside the pipeline changed, such as a firewall rule. I also moved teams to build-once, deploy-many: the same QA-tested artifact promoted through every environment, with configuration loaded at runtime instead of baked in at build time.

One example of the traceability side: for Salesforce I implemented full-suite nightly testing of the develop branch. When two weeks of failures went unowned ahead of a major milestone, I escalated the deployment risk to the project director, fixes across four or five teams followed within 48 hours, and the release shipped on schedule.

The Linux and fleet side comes from Tink, where I supported a development team of 10–15 while monitoring a production fleet of 600+ servers. I replaced reactive patching with staged schedules, reboot sequencing and progress reporting, and built an inventory of installed software, CVE exposure and TLS scores that Ops, QA and product owners used. At Desjardins I wrote a Python/FastAPI service that tested artifact retrieval across about 250 repositories on a schedule, deployed through ArgoCD, with results published to Dynatrace.

To be direct about fit: I have not run GPU infrastructure, debugged NVIDIA driver or CUDA issues, or worked on simulation or robotics software. I have not owned C++ build systems such as CMake at scale, and my pipeline platforms have been Jenkins and GitHub Actions rather than GitLab CI. My Kubernetes and Terraform work has been as a user of clusters and provisioning workflows run by other teams. What I do bring is a record of learning unfamiliar build and release ecosystems by working out how they actually behave before changing them, which is how I entered Salesforce, MuleSoft, Oracle and Databricks delivery with no prior experience in any of them.

I am based in Ontario, bilingual in French and English, and available immediately. Could you confirm that the remote option applies to candidates in Ontario, and how much of the role is GPU runner operations compared with pipeline and test engineering?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
