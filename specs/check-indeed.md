# Spec: `/check-indeed` — Indeed Search & Bulk Quick-Score

## Problem

`/addjob` handles one posting at a time and requires a URL or pasted text up front. During
this session we discovered that Indeed search-result pages and individual `viewjob`/`pagead/clk`
URLs are fetchable directly (unlike LinkedIn, which sits behind an auth wall), and that a single
search can surface 10+ postings worth a quick look. Doing that by hand — search, list, fetch each
one, paste it back — is repetitive. We want a command that runs the search, fetches every result,
and gives a compact score table, without the full resume-delta/cover-letter writeup for postings
that don't deserve it yet.

## Capability

A command that takes an optional search query (location is always `Remote`) and either runs it
directly, or — if no query is given — runs a **default rotation of role-title keywords** that
cover the ways Marc's actual work gets titled (DevOps Engineer, Platform Engineer, SRE, Cloud
Engineer, DevSecOps Engineer, Forward Deployed Engineer). Either way, it searches Indeed, fetches
each result posting, dedupes across keywords, and reports a **quick-score table** (title,
company, score, one-line why, key flags) — deliberately lighter than `/addjob`'s full writeup.
The user then picks which postings (if any) get the full `/addjob`-style treatment (resume delta
+ cover letter + file in `jobs/new/`).

## Usage

```
/check-indeed [search terms]
```

- `/check-indeed` (no arguments) — runs the full default role rotation.
- `/check-indeed devops engineer` — runs that single query only, same as before.

## Default Role Rotation

```
DevOps Engineer
Platform Engineer
Site Reliability Engineer
Cloud Engineer
DevSecOps Engineer
Forward Deployed Engineer
```

This exists so Marc doesn't have to remember and re-type every title variant his work matches —
see the discussion in this session about how "DevOps Engineer" work gets posted under many
different titles. The list lives directly in `.claude/commands/check-indeed.md` (and its
`/check-dice` twin) so it's easy to tweak without touching this spec.

## Behavior

1. **Determine query mode**: single custom query (arguments given) or full rotation (no
   arguments).
2. **Build and fetch the search URL(s)** — `https://ca.indeed.com/jobs?q=<keyword>&l=Remote` for
   each keyword being searched this run (location is always `Remote`, not a user-supplied
   argument). Extract every job-posting link (`pagead/clk`, `/viewjob?jk=`, `/rc/clk`) along with
   the title/company shown on the results page. Discard non-job links (ads for courses, employer
   resource pages, etc.). Cap per-keyword results lower in rotation mode (~8) than in single-query
   mode (~15), to keep the total batch size reasonable across 6 keywords.
3. **Dedupe** (rotation mode only) — the same posting often surfaces under multiple keywords
   (e.g. a role tagged both "DevOps Engineer" and "Platform Engineer"). Collapse by company +
   title before fetching full details, so nothing gets scored twice.
4. **Read `profile.md` first** (per repo convention), same as `/addjob`.
5. **For each deduped result**, fetch the individual posting (WebFetch) and extract: title,
   company, location, remote/hybrid/onsite status, salary/rate if stated, engagement type.
6. **Quick-score each** 0–10 against `profile.md`'s scoring notes, skill/domain-first — same
   scoring philosophy as `/addjob` (logistics don't drag the score down, they're flagged
   instead). Keep the rationale to one sentence per posting, not the 2-4 sentence version
   `/addjob` produces.
7. **Report a table** to the user: Role — Company | Score | one-line why | key flag(s). Sort
   highest score first. Do **not** write any files at this stage.
8. **Offer to go deeper** — ask the user which postings (if any) should get the full `/addjob`
   writeup (resume delta, cover letter, filed to `jobs/new/`). Reuse `/addjob`'s logic for
   whichever ones the user picks, using the posting content already fetched (no need to
   re-fetch).

## Edge Cases

- **A single keyword's search returns no job links**: skip that keyword, continue with the rest
  of the rotation — don't abort the whole run over one empty search.
- **Every keyword (or the single custom query) returns no job links**: report that no results
  were found/parseable, suggest the user try a different query or paste a direct URL to
  `/addjob` instead.
- **Individual posting fetch fails**: skip it, note it in the table as "couldn't fetch" rather
  than silently dropping it.
- **Duplicate of an existing `jobs/` entry**: don't block the quick-score table (it's read-only),
  but flag duplicates when the user picks a posting to file via the full `/addjob` treatment —
  same duplicate check `/addjob` already does.
- **Large result count**: cap per the limits in step 2; tell the user if results were truncated.

## Out of Scope

- Other job boards (Dice, We Work Remotely, etc.) — same approach could extend to them later,
  but this story is Indeed-only.
- Auto-filing every result to `jobs/new/` — quick-score is deliberately read-only; filing is an
  explicit, separate follow-up step per posting.
- Pagination beyond the first results page.
