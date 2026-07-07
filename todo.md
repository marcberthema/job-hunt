# Setup TODO — Before Production

Everything that needs to be done before `/findjobs` runs end-to-end without manual intervention.

---

## 1. Email Setup

- [ ] Create a dedicated job email address (e.g. `marc.jobs@gmail.com` or `jobs@yourdomain.com`)
- [ ] Set up a Gmail label called `job-alerts` for all incoming job notifications
- [ ] Create a Gmail filter: any email from job platforms → apply `job-alerts` label, skip inbox

---

## 2. Sign Up — Consulting-Focused (priority)

- [ ] **Toptal** — toptal.com — apply to join the network (vetted, takes time)
- [ ] **Gun.io** — gun.io — sign up, set job alerts to job email
- [ ] **Expert360** — expert360.com — sign up, set alerts
- [ ] **Contra** — contra.com — sign up, set alerts
- [ ] **Upwork** — upwork.com — create profile, set alerts (high volume, lower signal)

## 3. Sign Up — General (secondary)

- [ ] **LinkedIn** — set job alerts filtered to "Contract" only, alert email → job email
- [ ] **We Work Remotely** — weworkremotely.com — subscribe to relevant category RSS or email digest
- [ ] **Wellfound** (AngelList) — wellfound.com — set contract job alerts

---

## 4. Gmail API Setup (one-time, enables headless `/findjobs`)

- [ ] Go to [Google Cloud Console](https://console.cloud.google.com)
- [ ] Create a new project (e.g. `job-seeking-agent`)
- [ ] Enable the **Gmail API** for the project
- [ ] Create OAuth 2.0 credentials (Desktop app type), download `credentials.json`
- [ ] Place `credentials.json` in the repo root (it is gitignored)
- [ ] Run the OAuth flow once to generate `token.json` (Claude Code will guide this step)
- [ ] Confirm Claude Code can read emails from the `job-alerts` label

---

## 5. Profile

- [ ] Fill in `profile.md` — background and years of experience
- [ ] Fill in skills & expertise section
- [ ] Set target rate and engagement preferences
- [ ] Write the "what a great match looks like" section
- [ ] Add 2–3 past engagement descriptions for cover letter reference
- [ ] Review red flags list — add any specific to your domain

---

## 6. Automation Story (spec + plan + implement)

- [ ] Write spec for Gmail integration (`specs/gmail-integration.md`)
- [ ] Write plan (`plans/gmail-integration.md`)
- [ ] Implement Gmail reader in `/findjobs`
- [ ] Test end-to-end: real email → scored job → `jobs/new/`

---

## 7. Personal Website

- [ ] Register your name domain (e.g. `marcberthelette.com`) — ~$12/year
- [ ] Fill in `profile.md` (prerequisite for `/buildsite`)
- [ ] Run `/buildsite` to generate `site/index.html`
- [ ] Create a Cloudflare Pages project, connect this repo, set `site/` as the build output folder
- [ ] Add custom domain in Cloudflare Pages settings
- [ ] Verify site is live at your domain

---

## 8. Wire GitHub Remote

- [ ] Create private repo on GitHub
- [ ] `git remote add origin <url>`
- [ ] `git push -u origin main`

---

## Done when

`/findjobs` runs without prompting you for anything, finds emails in the `job-alerts` label, scores them, drafts letters, and commits results to `jobs/new/` — all within your Claude Code subscription.

Personal site is live at your domain and reflects your current profile.
