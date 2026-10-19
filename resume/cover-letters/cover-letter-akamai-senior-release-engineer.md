Dear Akamai Edge Compute Hiring Team,

I am applying for the Senior Release Engineer role. The posting describes someone who sits between engineering and QA, enforces release gates, and keeps build and test infrastructure healthy enough that pipelines keep moving. That is a close description of the work I have done for the past five years.

At Énergir I initiated the consolidation of duplicated Jenkins pipelines into shared pipelines used by every team already deploying through Jenkins, in an environment of about 50 developers, 12 teams and 70+ applications. Mandatory SonarQube checks could not be skipped, the shared pipeline code carried roughly 80–90% JaCoCo coverage with unit tests on every commit, and sample applications let us run integration tests against the pipelines. I separated application-code failures from platform-pipeline failures in build reporting so developers could tell at a glance whose fix it was, and I ran scheduled smoke tests that alerted Teams when something outside the pipeline changed, such as a firewall rule.

Release control is where my experience is most direct. For MuleSoft I replaced a 15-step release checklist with Jenkins jobs that deploy a chosen, QA-tested version, so preparation moves ahead of the production window and rollback means redeploying a previous artifact. For Salesforce I implemented full-suite nightly testing of the develop branch; when two weeks of failures went unowned ahead of a major milestone, I escalated the deployment risk to the project director, fixes across four or five teams followed within 48 hours, and the release shipped on schedule. At SOVO earlier in my career I was the final QA gate before any software reached production.

On environment health, at Tink I supported a development team of 10–15 while monitoring a 600+ server fleet, was part of a 24/7 on-call rotation, and kept build and release failures moving. At Desjardins I wrote a Python/FastAPI service, deployed through ArgoCD, that tested artifact retrieval across about 250 repositories and published results to Dynatrace.

To be direct about fit: I have not written Ruby, and I have not run build and test labs at Akamai's scale. On the AI side, I introduced AI-assisted engineering practices into my team's tooling with scope gates and human-validation checkpoints before generated code reached production, and I use AI assistance heavily in my Python and automation work. I have not built production AI agents or eval frameworks, so that part of the role would be new to me. I learn unfamiliar build and release ecosystems by working out how they actually behave before changing them, which is how I entered Salesforce, MuleSoft, Oracle and Databricks delivery with no prior experience in any of them.

I am based in Ontario, bilingual in French and English, and available immediately. Could you tell me whether this role is remote within Ontario or expects regular Ottawa office days, and what the base range is for a candidate with my profile?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
