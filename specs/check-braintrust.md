# Spec: `/check-braintrust` — Braintrust Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

`job_sources.md` previously logged Braintrust as JS-rendered and invisible to `WebFetch`. Tested
via Claude in Chrome (2026-08-20): the site loads fully and **no login is required to browse** —
the earlier "needs a logged-in session" assumption was wrong; the real blocker was always
client-side rendering, which a real browser resolves the same way it does for the other
Chrome-driven sources. Braintrust is a freelance/contract marketplace ("Access the world's best
jobs. Keep 100% of what you earn.") — a strong fit for the contract/consulting engagement
preference in `profile.md`.

## Capability

Same shape as the other Chrome-driven `/check-*` commands: optional search query (defaults to the
shared role rotation), searches Braintrust, gates on location eligibility, and reports scored
eligible postings plus ineligible ones with reason. Unlike LinkedIn/WWR/RemoteOK, Braintrust's
filtering is built on clean, discoverable URL query parameters rather than a free-text search box
— confirmed during testing.

## Usage

```
/check-braintrust [search terms]
```

- `/check-braintrust` (no arguments) — runs the default role rotation (bare titles/skills, same
  list as `/check-indeed`/`/check-dice`/`/check-wwr`/`/check-remoteok`: DevOps Engineer, Platform
  Engineer, Site Reliability Engineer, Cloud Engineer, DevSecOps Engineer, Forward Deployed
  Engineer).
- `/check-braintrust devops` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required (confirmed 2026-08-20).
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — Braintrust filters via URL query params rather than free text:
   `https://app.usebraintrust.com/jobs/?role=5%2C16&skills=<skill-id>`
   - `role=5,16` (URL-encoded `5%2C16`) restricts to the Engineering and IT & System Admin role
     categories — confirmed the right pair to use for this rotation via the site's own Role
     filter UI.
   - `skills=<id>` filters by a specific skill chip; confirmed `1338` = DevOps during testing.
     Other rotation keywords need their own skill IDs looked up once via the Skills filter UI
     (click Skills → search the term → note the `skills=` value the URL updates to) since IDs
     aren't predictable from the name alone. Cache discovered IDs in this spec once confirmed
     rather than re-discovering them every run (see Skill ID Table below — populate as
     confirmed).
   - `get_page_text` on the results page returns clean, complete listing data directly: title,
     company, engagement type (Freelance/Employee), rate/salary, hours/week, and — critically —
     the **Location column directly on each card** (e.g. "United States only," "Work from
     anywhere," "North America + 1 more," "United States | Canada"). This is a reliable,
     structured signal — confirmed consistent between listing card and job detail page during
     testing (unlike WWR's decorative tag; more like RemoteOK's, but so far no contradicting
     body text found in initial testing — still worth a body skim per the RemoteOK lesson).
   - Cap at 15 for a single custom query, 8 per keyword in rotation mode.
4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **Location-eligibility gate BEFORE opening each posting**, using the Location column already
   visible in the results:
   - **"Work from anywhere," an explicit "Canada" mention, or "North America"** → eligible.
   - **"United States only," or a region list that excludes Canada** → ineligible — skip, no need
     to open the full posting.
   - **A specific US city/state with no "only" qualifier** → treat as likely US-restricted
     (Braintrust's convention appears to be explicit city/state = on-site in that location) —
     ineligible unless the full posting says otherwise.
7. **Open each eligible posting** — `navigate` to `https://app.usebraintrust.com/jobs/<id>`
   (from the results list's "View job" link). Confirmed during testing: `get_page_text` returns
   the full, correct job description directly — no `find`+`read_page` workaround needed. Extract
   title, company, full description, rate, skills, and re-confirm location ("Preferred location"
   field in the body, confirmed present and consistent with the card in initial testing — still
   skim for a contradicting statement per the RemoteOK lesson).
8. **Quick-score each eligible posting** 0–10, same skill/domain-first philosophy as the other
   `/check-*` commands. Freelance/contract postings here are a strong engagement-type match, not
   a flag.
9. **Present two tables**: eligible sorted highest score first; ineligible listed separately with
   reason (not scored).
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Skill ID Table (populate as confirmed)

| Rotation keyword | Braintrust skill ID |
|---|---|
| DevOps Engineer | `1338` (DevOps) — only keyword that reliably returns results (3, as of 2026-08-20) |
| Platform Engineer | **no matching skill chip exists** — searching "Platform Engineer" returns "Skill not found"; the closest chips (Cloud Platform Development, Cloud Platforms, Azure Platform) aren't real matches. Fall back to unfiltered `role=5,16` browsing + title-skim for this keyword. |
| Site Reliability Engineer | `8473` (Site Reliability Engineering) — confirmed the chip exists, but returned **0 open postings** as of 2026-08-20 |
| Cloud Engineer | `10001` (Cloud Engineering) — confirmed the chip exists, but returned **0 open postings** as of 2026-08-20 |
| DevSecOps Engineer | `6831` (DevSecOps) — confirmed the chip exists, but returned **0 open postings** as of 2026-08-20 |
| Forward Deployed Engineer | not confirmed — UI lookup was interrupted by a stuck dropdown state during testing; "Forward Deployed Engineer" also appears as a literal **role title** already (e.g. Turing's posting under the DevOps skill search), so it may not need its own skill chip — worth re-testing next run |

**Important: combining multiple `skills=` IDs in one query ANDs them, not ORs** — confirmed
during testing that `skills=8473,6831` (SRE + DevSecOps together) returned 0 results even though
each individually also returned 0. Never combine skill IDs across different rotation keywords in
one URL; run them as fully separate navigations, one per keyword.

## Edge Cases

- **A keyword's skill ID can't be found via the Skills filter UI** → fall back to browsing the
  unfiltered role-category results (`role=5,16` alone) and title-skim for the keyword, same
  triage approach used for Indeed's noisy rotation.
- **A single keyword's search returns no results** → skip it, continue the rotation.
- **Every keyword (or the single custom query) returns nothing** → report it, stop.
- **Individual posting fetch fails** → mark "couldn't fetch," continue with the rest, skip the
  gate for it.
- **Never click Apply** — read-only browsing only, same rule as every other Chrome-driven source.

## Out of Scope

- Pagination beyond the first results page.
- Signing up for a Braintrust profile (not required for browsing, and out of scope regardless).
- Auto-filing eligible+high-scoring results without user confirmation.
