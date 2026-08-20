---
description: Regenerate jobs/new/review-dashboard.html from the current jobs/new/ backlog and job_sources.md status
---

Regenerates the static review dashboard at `jobs/new/review-dashboard.html`. Run this any time
the `jobs/new/` backlog changes (after `/findjobs` or any `/check-*` run) or when you just want
the status bar refreshed.

## 1. Read source status

Read `job_sources.md` and pull the `Last Checked` date for each row in the "Working — automated
via skill" table (Indeed, Dice, Job Bank, BuiltIn). These populate the `sourceStatus` array in
the dashboard.

## 2. Read the backlog

List every `*.md` file in `jobs/new/` (ignore `review-dashboard.html` itself — it's the output,
not a job). For each file, read it in full and extract:

- **title** — role title (before the em-dash in the `# ` heading)
- **company** — company name (after the em-dash in the `# ` heading)
- **file** — the filename itself (used as the relative link to the full posting)
- **score** — the number after `## Fit Score:`
- **salary** — the `**Rate/Salary (stated):**` field, verbatim
- **source** — infer from the `**Source:**` URL's domain: `builtin.com` → `BuiltIn`,
  `indeed.com` → `Indeed`, `dice.com` → `Dice`, `jobbank.gc.ca` → `Job Bank`. If the domain
  doesn't match any of these, use the domain's site name as a fallback (don't guess a source
  that isn't in the list of four).
- **skills** — 3–6 short skill/tech tags, derived by judgement from the Fit Score rationale and
  Resume Delta bullets (not a literal field in the file — synthesize concise tags, e.g.
  "Azure", "Terraform", "Kubernetes/ArgoCD"). Keep each tag under ~25 characters.
- **flags** — the `**Flags:**` field, verbatim (use "none" text as-is if that's what's there)

## 3. Regenerate the HTML

Read the existing `jobs/new/review-dashboard.html` to preserve its structure, styling, and
behavior (search, source filter chips, sort dropdown, light/dark theming, status bar). Only
replace two things inside the `<script>` block:

- the `sourceStatus` array (step 1 data)
- the `jobs` array (step 2 data)
- the `today` date literal inside `renderStatusBar()` — set it to today's date so staleness
  (`STALE_AFTER_DAYS = 3`) computes correctly

Also update the header `.sub` line's posting count and date if the backlog count or newest
`Found` date changed.

If a new source (not BuiltIn/Indeed/Dice/Job Bank) starts appearing in `jobs/new/` files, add a
filter chip and a `.src-<Name>` CSS color pair for it, following the existing pattern.

Do not change the visual design, layout, or add new sections beyond what already exists unless
the user asks — this command is a data refresh, not a redesign.

## 4. Report back

Tell the user how many postings are now on the dashboard, and flag any source whose
`Last Checked` date makes it stale (>3 days old per the dashboard's own threshold).
