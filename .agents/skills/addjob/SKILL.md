---
name: addjob
description: Manually add a single job posting by URL — fetch it, score it against profile.md, draft a cover letter and tailored resume, and append one row to applications.md. Use when the user gives a job posting URL to add, or asks any check-* skill to file a posting it found.
---

# Add Job

Take a single job posting URL (or pasted posting text when a URL can't be fetched), score it against Marc's profile, produce a cover letter and tailored resume, and record it in `applications.md` with `Status: New`. This is the shared filing step every `check-*` skill calls once the user picks a posting to pursue — it never submits an application and never sets a row's status to `Applied`, `Skipped`, or `Rejected`.

## 1. Duplicate check

Before fetching, search `applications.md` for this exact `Source` URL or an obvious `Company`+`Role` match. If found, tell the user what's already on record (its `Status`) and ask whether to proceed before continuing — don't silently create a duplicate row.

## 2. Fetch the posting

Fetch the URL. If it fails (timeout, 404, login wall) or the content doesn't look like an actual job posting, stop and report the failure — ask the user to paste the posting text instead rather than guessing at details.

## 3. Read the source of truth

Read `profile.md` and `resume/marc-berthelette-resume-en.md` completely before scoring or drafting anything.

## 4. Extract fields

- Role title, company
- Engagement type — Contract / Fractional / Full-time / Unclear (infer from language)
- Rate/salary as stated verbatim, or "Not stated"
- Location/remote policy as stated, and days in office per week when hybrid/on-site
- Board the posting came from, if identifiable from the URL's domain (Indeed, LinkedIn, BuiltIn, Dice, Job Bank, RemoteOK, Eluta, S.i. Systems, Randstad, We Work Remotely, Braintrust, Procom, Robert Half, Glassdoor), or `Manual` if the user supplied it directly

## 5. Score (0–10) — skill/fit-based

Score primarily on skill and domain fit against `profile.md`'s scoring notes: Azure depth, platform engineering/CI-CD/IaC scope, financial or energy sector relevance, autonomy vs. ticket-taking. Apply the profile's honesty rules for AWS, GCP, Kubernetes administration, programming languages, and people management.

Do not let logistics drag the score down. On-site/hybrid requirements and below-target pay do not by themselves lower the score — a strong skill match stays high-scored even if it's on-site or under-rate. Surface those issues in the row's `Notes` field instead (e.g. "9/10 fit, but on-site").

Write a short rationale referencing concrete posting details, for the chat response — `applications.md` itself only needs the number.

## 6. Draft the cover letter and tailored resume

- **Cover letter**: a short (3–4 paragraph) draft tailored to this role and company, grounded in `profile.md` and `resume/marc-berthelette-resume-en.md` — never invent experience that isn't documented there. Write it to `resume/cover-letters/cover-letter-<company-slug>-<role-slug>.md`.
- **Tailored resume**: a resume delta — which existing experience/skills to lead with for this posting — applied against the base resume. Write it to `resume/tailored/<YYYY-MM-DD>-<company-slug>-<role-slug>-en.md`.

Slugs are lowercase, hyphenated, alphanumeric only. Follow the naming convention already used by existing files in those two folders.

## 7. Append the row to applications.md

Add one row to the table in `applications.md`:

| Date Found | Status | Status Date | Score | Company | Role | Board | Source | Notes |
|---|---|---|---:|---|---|---|---|---|

- `Date Found` and `Status Date`: today.
- `Status`: `New`.
- `Notes`: any logistics flags surfaced in step 5 (on-site, below-target rate, unstated details), or blank.

Never set `Status` to `Applied`, `Skipped`, or `Rejected` from this skill — those transitions belong to the `review` skill only, once the user confirms a decision.

## 8. Low-score handling

If the score is 0–4, still write the row and drafts (keeps a record of the reasoning) but clearly flag in the chat response that it's a low-fit posting.

## 9. Report back

Reply with the score, a one-line fit summary, any flags, and the two file paths written (cover letter, tailored resume). Nothing gets submitted or marked `Applied` — this skill only files a draft for review.
