---
description: Manually add a job posting by URL — fetch, score against profile.md, draft resume delta + cover letter, file to jobs/new/
argument-hint: <url>
---

Implements `specs/addjob.md` / `plans/addjob.md`. Follow these steps in order.

## 1. Parse input

The user's argument is a job posting URL: `$ARGUMENTS`

If no URL was given, ask for one and stop.

## 2. Duplicate check

Before fetching, search existing job files for this URL or an obvious company+role match:

```
grep -ril "<url>" jobs/new/ jobs/applied/ jobs/rejected/
```

Also skim filenames for the same company/role slug in case it's a re-post with a different URL.
If you find a match, tell the user what you found and ask whether to proceed before continuing.

## 3. Fetch the posting

Use WebFetch on the URL. If it fails (timeout, 404, login wall) or the content doesn't
look like an actual job posting (e.g. a generic homepage), stop and report the failure —
suggest the user paste the posting text directly instead. Don't guess at posting details.

## 4. Read profile.md

Read `profile.md` in full before scoring or drafting anything. This is a hard requirement,
not optional context — it's the source of truth for background, rate, preferences, red flags,
and scoring notes.

## 5. Extract fields from the posting

- Role title, company
- Engagement type — Contract / Fractional / Full-time / Unclear (infer from language: "1099
  contractor" / "day rate" → Contract; "W2 employee" / "full-time employee" → Full-time; etc.)
- Rate/salary as stated verbatim, or "not stated"
- Location/remote policy as stated (Remote / Hybrid / On-site + city)

## 6. Score (0–10) — skill/fit-based

Score primarily on **skill and domain fit** against `profile.md`'s scoring notes: Azure depth,
platform engineering / CI/CD / IaC scope, financial or energy sector relevance, autonomy vs.
ticket-taking.

**Do not let logistics drag the score down.** On-site/hybrid requirements and below-target pay
do not by themselves lower the score — a strong skill match stays high-scored even if it's
on-site or under-rate. Instead, surface those issues in the `Flags` field (see schema) so the
user sees e.g. "9/10 fit, but on-site" rather than a collapsed score that hides a great match.

Write a 2–4 sentence rationale that references concrete details from the posting — not a
generic restatement of `profile.md`.

## 7. Draft

- **Resume delta**: Read `resume/marc-berthelette-resume-en.md` and write 3–6 bullets naming
  which existing experience/skills to lead with for this specific posting. Ground every
  suggestion in what's actually in the resume — never invent experience that isn't there.
- **Cover letter**: A short (3–4 paragraph) draft tailored to this role and company. Reference
  the competitive advantages in `profile.md` (bilingual FR/EN, Desjardins, Énergir, incorporated)
  where genuinely relevant to the posting — don't force all of them in.

## 8. Write the job file

Path: `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`
- Date = today
- Slugs = lowercase, hyphenated, alphanumeric only

Schema:

```markdown
# <Role Title> — <Company>

- **Source:** <url>
- **Found:** <YYYY-MM-DD>
- **Engagement type:** Contract | Fractional | Full-time | Unclear
- **Rate/Salary (stated):** <as posted, or "not stated">
- **Location/Remote:** <as posted>
- **Flags:** <e.g. "On-site (Toronto)"; "Rate not stated"; "none">

## Fit Score: <0-10> (skill/domain fit — logistics noted separately above)

<rationale, 2-4 sentences, skill/domain-focused>

## Resume Delta

- <what to emphasize>
- ...

## Draft Cover Letter

<tailored draft>
```

Never write directly to `jobs/applied/` or `jobs/rejected/` — those moves belong to `/review`
only.

## 9. Low-score handling

If the score is 0–4, still write the file (keeps a record of the reasoning) but clearly flag
in your chat response that it's a low-fit posting.

## 10. Report back

Reply to the user with: the score, a one-line fit summary, any flags, and the file path
written. Nothing gets moved to `applied/` or submitted — this command only files a draft for
review.
