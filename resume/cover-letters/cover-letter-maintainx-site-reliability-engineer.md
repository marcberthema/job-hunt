Dear MaintainX Hiring Team,

I am applying for the Site Reliability Engineer role. The posting describes an enablement-style SRE: assess how mature a service is, help teams put observability in place, and make developers autonomous in how they deploy and support their services. That is the shape of the work I have done for the past five years, and it is the part of the posting I recognise most.

At Énergir I migrated the production Salesforce logging path from a Logstash intermediary to direct Dynatrace ingestion, then, with my manager's approval and on my own initiative, expanded the parsing to extract DML error types, messages and originating classes and built dashboards that let the Salesforce team investigate issues that had been invisible. I ran four-hourly Jenkins smoke tests with Teams alerts that caught external changes such as firewall rules, and I separated pipeline failures from application failures in build reporting so teams knew whose fix it was. When two weeks of nightly Salesforce test failures went unowned ahead of a major milestone, I escalated the risk to the project director, fixes across four or five teams followed within 48 hours, and the project deployed on schedule. I then ran recurring enablement sessions with each team so improvements were adopted rather than ignored, which is where I got used to measuring success by how little teams depended on me.

At Tink I supported a development team of 10–15 while monitoring a production fleet of 600+ servers and was part of a 24/7 on-call rotation. I automated a PRTG-triggered Elasticsearch recovery that attempted a restart after two minutes of sustained CPU saturation and paged on-call at five minutes, and I replaced reactive patching with staged, scheduled updates reported to the team chat. At Desjardins I wrote a Python/FastAPI service, deployed through ArgoCD, that tested artifact retrieval across about 250 repositories and published results to Dynatrace.

To be direct about fit: I have not implemented SLOs or error budgets. My Dynatrace dashboards laid the groundwork for them, but I did not define targets or measure compliance, so that part of your posting would be new to me. My production systems have been moderate in scale rather than a large distributed platform, my infrastructure-as-code work has been using Terraform and Ansible workflows another team owned, and I have not written TypeScript or Node.js services. I am comfortable with Python and Bash, and I use AI assistance heavily in my automation work. I learn unfamiliar systems by working out how they actually behave before changing them.

I am based in Ontario, bilingual in French and English, and available immediately. Could you confirm that the role is remote for Ontario candidates, and tell me what the base range is for a candidate with my profile and how much of the role is SLO and observability standards work?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
