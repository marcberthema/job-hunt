# Spec: `/check-linkedin` — LinkedIn Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

LinkedIn sits behind an auth wall — `WebFetch` cannot retrieve postings (see `job_sources.md`,
"Not usable" table). It's flagged in `CLAUDE.md` as the single highest-value source right now:
most recruiter activity happens there, and it's the channel `/findjobs` can't currently touch.
Claude in Chrome drives the user's real logged-in browser session, which clears the auth wall the
same way a human browsing would.

This is the first of several `job_sources.md` "Not usable" entries planned to move to a
Chrome-driven `/check-*` command (We Work Remotely, RemoteOK, Braintrust, Eluta.ca are queued as
follow-on stories — same pattern, one at a time, after this one is validated).

## Capability

Same overall shape as `/check-indeed` / `/check-builtin`: optional search query (defaults to the
shared role rotation), searches LinkedIn Jobs, opens each result, and reports a quick-score table.
No files written until the user picks postings for the full `/addjob` treatment.

Difference from the curl-based `/check-*` commands: this one drives Chrome via
`mcp__claude-in-chrome__*` tools instead of `WebFetch`, and depends on the user already being
logged into LinkedIn in their Chrome profile.

## Usage

```
/check-linkedin [search terms]
```

- `/check-linkedin` (no arguments) — runs the default phrase rotation (see below).
- `/check-linkedin platform engineer remote` — runs that single query only.

### Query design — matched to Marc's real LinkedIn alerts (2026-08-20)

Marc has LinkedIn job alerts already configured, and comparing four of his actual alert emails
to this command's original approach exposed why the command was under-finding roles: LinkedIn's
alert/semantic search behaves very differently from a plain keyword+filter search.

Confirmed from real alert URLs:

| Keyword (as phrased in the alert) | geoId | Resolves to | Results |
|---|---|---|---|
| `DevOps Consultant Remote` | 106234700 | Ottawa, ON | 42 |
| `DevOps Consultant Remote` | 101330853 | Montréal, QC | 84 |
| `DevOps Consultant Remote` | 100025096 | Toronto, ON | 99+ |
| `Senior Site Reliability Engineer Remote` | 101174742 | **Canada** (broad, no city) | 99+ |

Two takeaways that reshape the query design:

1. **The keyword is a full natural-language phrase** (e.g. `"DevOps Consultant Remote"`), not a
   bare title. LinkedIn's semantic search matches on phrase intent, not exact title — this is
   what drives the much higher yield compared to bare-title keywords.
2. **The broad `geoId=101174742` ("Canada", no specific city) alone returns just as many results**
   as the city-anchored versions, with heavy overlap between them. Anchoring to individual cities
   isn't worth the added complexity — use the broad Canada `geoId` for every query.

### Default phrase rotation

```
DevOps Consultant Remote
Senior Site Reliability Engineer Remote
Platform Engineer Remote
Cloud Engineer Remote
DevSecOps Engineer Remote
Forward Deployed Engineer Remote
```

The first two are confirmed directly from Marc's real alerts; the rest follow the same
`"<Role> Remote"` phrasing pattern for consistency with the other `/check-*` commands' role
rotation. Revisit if Marc shares more alert emails with different confirmed phrasings.

## Behavior

1. **Load Chrome tools** — batch-load the core `mcp__claude-in-chrome__*` tool set plus
   `get_page_text` and `find` in one `ToolSearch` call before doing anything else.
2. **Open a tab, confirm login** — navigate to `linkedin.com/feed/`. If the page shows a login/
   join wall instead of a feed, stop and tell the user to log into LinkedIn in Chrome first, then
   re-run the command.
3. **Determine query mode**: single custom query or full phrase rotation.
4. **Search per keyword**:
   `https://www.linkedin.com/jobs/search/?keywords=<keyword phrase>&geoId=101174742&f_TPR=r172800&sortBy=DD`
   — `geoId=101174742` is the broad "Canada" geo used by Marc's real alerts (do not substitute
   `location=Canada` text or a city-specific geoId — confirmed equivalent-or-better yield from the
   broad geoId alone). `f_TPR=r172800` limits to postings from the **past 2 days** (confirmed
   preference, 2026-08-20). No `f_WT` (remote) filter param is used — "Remote" is already part of
   the keyword phrase itself, matching how the real alerts are built.

   **Scroll the results list before reading it** — the unscrolled view shows the same ~7-10
   "recently viewed/recommended" cards regardless of keyword; the genuinely relevant results only
   appear after scrolling the results panel down. Scroll it at least twice (roughly 20 items deep)
   before extracting job links via `read_page`.
5. **Dedupe** (rotation mode only) — collapse by company + exact title, same rule as
   `/check-builtin`.
6. **Read `profile.md` first**.
7. **Open each posting** — navigate directly to `linkedin.com/jobs/view/<job-id>/` for each
   result (extracted from the search results' job links) rather than clicking through the UI.
   Extract title, company, location, remote/hybrid/onsite, salary if shown, engagement type,
   requirements via `get_page_text`. **The description body lazy-loads and won't appear in
   `get_page_text` right after navigation** — confirmed during testing: a `wait` alone isn't
   reliable, but scrolling the page down a few ticks reliably triggers the description to render.
   Always scroll before extracting.
8. **Quick-score each** 0–10, same skill/domain-first philosophy as the other `/check-*` commands.
9. **Present a table**, sorted highest score first. No files written.
10. **Offer to go deeper** — same `/addjob`-reuse pattern as the other commands.

## Edge Cases

- **Not logged in** → stop immediately, tell the user, do not attempt to log in on their behalf.
- **Security checkpoint / CAPTCHA / "verify it's you" challenge** appears mid-run → stop, tell
  the user what happened, ask them to clear it manually in the browser before retrying. Never
  attempt to solve or click through a challenge.
- **Easy Apply / Apply buttons on job pages** → never click these. Read-only browsing only —
  this command's job is discovery and scoring, not application.
- **A single keyword's search returns no jobs** → skip it, continue the rotation.
- **Every keyword (or the single custom query) returns nothing** → report it, stop.
- **Individual job page fails to load or shows "this job is no longer accepting applications"**
  → mark "couldn't fetch / expired," don't drop it silently or abort the batch.
- **Rate/flagging risk** — LinkedIn is known to challenge automated-looking browsing. Keep the
  pace unhurried (this is inherent to driving a real browser one page at a time; don't add
  artificial batching or parallel tabs to go faster) and cap volume per the limits below.

## Limits

Result volumes are much higher with phrase-based queries (42-99+ per keyword, vs. single digits
under the old bare-title approach), so caps are raised accordingly: 20 postings for a single
custom query, 12 per keyword in rotation mode (post-scroll, post-dedupe).

## Out of Scope

- Pagination past the first results *page* (page 2+ via the numbered pager) — scrolling within
  the first page's results panel is required (see step 4), but clicking "Page 2" etc. is not.
- Logging in on the user's behalf, solving verification challenges, or handling 2FA.
- Clicking Easy Apply or any application-submission UI.
- Reading LinkedIn recruiter messages/InMail (separate capability, not part of this command).
