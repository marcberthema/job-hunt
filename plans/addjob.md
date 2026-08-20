# Plan: `/addjob` — Manual Job Intake

Implements `specs/addjob.md`.

## Deliverable

`.claude/commands/addjob.md` — a slash command definition (prompt/instructions Claude follows
when the user runs `/addjob <url>`). No new code/scripts needed; this is a prompt-driven
workflow using existing tools (WebFetch, Read, Write, Bash for duplicate-checking via `find`/
`grep`).

## Command Steps

1. **Parse input** — expect a single URL as the command argument. If missing, ask for one.

2. **Duplicate check** — before fetching, `grep -ril` the URL across `jobs/new/`,
   `jobs/applied/`, `jobs/rejected/` (source field). If a company+role match is found even
   without an exact URL match (e.g. re-posted listing), also flag it. Ask the user whether to
   proceed if any match is found.

3. **Fetch** — WebFetch the URL. On failure (timeout, 404, login wall, content that isn't
   recognizably a job posting), stop and report the failure back to the user, suggesting they
   paste the posting text instead.

4. **Read `profile.md`** in full before scoring — this is a hard requirement per repo
   convention, not optional context.

5. **Extract fields** from the fetched posting:
   - Role title, company
   - Engagement type (contract / fractional / full-time / unclear — inferred from posting
     language, e.g. "W2 employee" vs "1099 contractor" vs "day rate")
   - Rate/salary as stated (verbatim; "not stated" if absent)
   - Location / remote policy as stated (remote / hybrid / on-site + city if given)

6. **Score (0–10), skill/fit-based primarily**:
   - Score reflects skill and domain fit against `profile.md`'s scoring notes — Azure depth,
     platform engineering scope, financial/energy sector relevance, autonomy — as the dominant
     factor.
   - Logistics (on-site/hybrid, pay below target) do **not** drag the score down by default.
     A strong skill match that happens to be on-site or under-rate should still score high.
   - Instead, logistics issues are surfaced as explicit **Flags** alongside the score (see
     schema change below), so the user sees "9/10 fit, but on-site" rather than a
     collapsed 4/10 that hides a great skill match.
   - Rationale (2–4 sentences) explains the skill-fit reasoning specifically, referencing
     concrete posting details (not generic restatement of profile.md).

7. **Draft**:
   - Resume delta: 3–6 bullets naming which existing bullets/skills from
     `resume/marc-berthelette-resume-en.md` to lead with for this posting. Read that file to
     ground the suggestions in what's actually there — don't invent experience.
   - Cover letter: short (3–4 paragraph) draft, tailored to the specific role/company,
     referencing the competitive advantages in `profile.md` (bilingual, Desjardins, Énergir,
     incorporated) where relevant.

8. **Write job file** to `jobs/new/<YYYY-MM-DD>-<company-slug>-<role-slug>.md`:
   - Date = today.
   - Slugs = lowercase, hyphenated, alphanumeric only.
   - Use the schema below (adds a `Flags` line vs. the original spec draft, to carry the
     on-site/pay caveats separately from the score).

9. **Report back** in chat: score, one-line fit summary, any flags, and the file path. Do not
   move any files into `applied/` or `rejected/` — that's `/review`'s job only.

## Job File Schema (final)

```markdown
# <Role Title> — <Company>

- **Source:** <url>
- **Found:** <YYYY-MM-DD>
- **Engagement type:** Contract | Fractional | Full-time | Unclear
- **Rate/Salary (stated):** <as posted, or "not stated">
- **Location/Remote:** <as posted>
- **Flags:** <e.g. "On-site (Toronto)"; "Rate not stated"; "none">

## Fit Score: <0-10>  (skill/domain fit — logistics noted separately above)

<rationale, 2-4 sentences, skill/domain-focused>

## Resume Delta

- <what to emphasize>
- ...

## Draft Cover Letter

<tailored draft>
```

## Edge Cases (carried from spec)

- Duplicate → warn, confirm before proceeding.
- Unfetchable → report failure, suggest pasting text.
- Low score (0–4) → still write file, flag clearly in chat response as low-fit.

## Testing

Manual: run `/addjob <a few real posting URLs>` covering:
- A strong remote-contract Azure match → expect high score, no flags.
- A strong skill match but on-site → expect high score, "on-site" flag.
- An unfetchable/paywalled URL → expect graceful failure + fallback suggestion.
- A duplicate of an existing `jobs/` entry → expect the duplicate warning.

No automated test suite for this repo; verification is manual review of generated files against
the schema and spec.

## Out of Scope

Same as spec: Gmail integration, auto-apply, editing `resume/` source files.
