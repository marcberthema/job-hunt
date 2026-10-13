Dear Parallel Domain Hiring Team,

I am applying for the Senior Site Reliability Engineer role. Running the infrastructure that lets simulation at scale stay up, with incident response, observability, and deployment tooling that other engineers depend on, is the part of this posting that matches my work.

At Tink I was part of a 24/7 on-call rotation for all production systems and replaced reactive patching across more than 600 servers with staged schedules, dependency-aware reboots, and chat status reporting. I also automated recovery for a recurring Elasticsearch failure the client would not upgrade away: monitoring restarted the affected process after two minutes of sustained CPU saturation and paged the on-call engineer if it was still saturated at five minutes. Nobody asked me to build it, but I also built a fleet inventory that showed product owners which applications were vulnerable, end-of-life, or running weak TLS.

At Desjardins I was asked to verify the configuration of Artifactory repositories. I built a Python/FastAPI workflow that provisioned the environment, applied configuration from a chosen Git reference, tested uncached retrieval across about 250 repositories, ran through ArgoCD, and published results to Dynatrace. I chose the larger solution because it was best for the client, not the cheapest.

To be direct about fit: I have not operated EKS clusters in production, and I use Kubernetes and ArgoCD as an application and platform user, not as a cluster owner. My Terraform work was with another team's workflows, so I have not written modules or managed multi-region state. My AWS experience is a roughly six-month build of a client's migration environment at Tink (EC2, S3, Route 53, VPC), provisioned by hand and cancelled before cutover, and I have no GPU scheduling or Windows-on-Kubernetes experience. What I can show is that I have entered unfamiliar platforms under delivery pressure, Salesforce, MuleSoft, ArcGIS, and that AWS build, and made them dependable. I would rather you hear the boundaries from me than find them in an interview.

I am bilingual in French and English, based in Smiths Falls, Ontario, and available immediately. Before going further, could you confirm that you can hire a candidate based in Ontario and tell me how you weigh Kubernetes and Terraform depth against operational and incident experience for this role?

Sincerely,
Marc Berthelette
marc.berthelette@gmail.com
