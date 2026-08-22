# Spec: `/check-procom` — Procom Search & Bulk Quick-Score (via Claude in Chrome)

## Problem

Procom's public marketing site (`procom.ca/find-jobs/`) is a dead end — it redirects to a broken
client-portal shell ("ProcomClientconnections...Loading") that never resolves to real content,
via both `WebFetch` and a real Chrome session. **The real jobs portal is a different subdomain**:
`myprocom-portal.procomservices.com/jobs?loginType=contractor&lang=en` (supplied by Marc,
2026-08-20). This one loads cleanly via Chrome, no login required to browse. Confirmed **298 open
jobs** at test time.

## Capability

Same overall shape as `/check-sisystems`: optional search query (defaults to the shared role
rotation), searches Procom's real portal via Chrome, runs a lightweight eligibility gate (Procom
is Canadian but some US postings mix in), then quick-scores the rest.

## Usage

```
/check-procom [search terms]
```

- `/check-procom` (no arguments) — runs the default role rotation (same list as the other
  `/check-*` commands).
- `/check-procom site reliability engineer` — runs that single query only.

## Behavior

1. **Load Chrome tools, open a tab** — no login required.
2. **Determine query mode**: single custom query or full rotation.
3. **Search per keyword** — `navigate` to:
   `https://myprocom-portal.procomservices.com/jobs?keyword=<keyword, spaces as +>`

   Confirmed during testing: this parameter works and returns relevant results — "devops"
   returned 24 results including genuinely relevant titles ("DevOps Engineer," "Senior Cloud
   DevOps Engineer"), a real improvement over S.i. Systems' keyword search. Each result card shows
   a **remote/hybrid/onsite tag** directly (a strong, reliable signal, similar to RemoteOK's
   flag-emoji tags), plus job title, location, posted-date, and pay rate when disclosed
   (`$X-$Y/hr CAD` format for many postings).

   `get_page_text` on the results page appears to return only the first visible card's content
   rather than the full list — use `read_page` (filter: interactive, or a targeted `ref_id`) or
   repeated `find` calls on job titles to enumerate the full result set, then `get_page_text` or
   click through per posting as needed.

4. **Dedupe** (rotation mode only) — collapse by company + exact title.
5. **Read `profile.md` first**.
6. **Lightweight eligibility gate** — Procom is a Canadian staffing agency, but some US postings
   mix in (Colorado Springs and Raleigh NC postings turned up during testing despite no explicit
   US-only query). Use the location field shown per result:
   - **Canadian city/province, or "Remote" with no US-specific qualifier** → eligible.
   - **US city/state shown** → ineligible unless the description explicitly says open to
     Canada-based remote candidates — check the opened posting before excluding if ambiguous.
7. **Open each eligible posting** — click through to the job detail page. Extract title, company
   (shown as "Procom | <client, if named>" or similar), full description, pay rate, job type
   (remote/hybrid/onsite tag), and location.
8. **Quick-score each eligible posting** 0–10, same skill/domain-first philosophy as the other
   `/check-*` commands.
9. **Present two tables**: eligible sorted highest score first, ineligible listed separately with
   reason only (not scored).
10. **Offer to go deeper** — same `/addjob`-reuse pattern.

## Edge Cases

- **`get_page_text` truncates to one card** → confirmed during testing; use `read_page` or `find`
  to enumerate all results on a search page rather than relying on `get_page_text` alone.
- **Client name anonymized** (shown only as "Procom") → normal for a staffing agency, not a red
  flag; note it but don't penalize the score.
- **CAPTCHA or blocking page appears mid-run** → stop the run, tell the user, don't attempt to
  solve it.
- **Never click Apply or any write-side button** — read-only browsing only.

## Limits

15 postings for a single custom query, 8 per keyword in rotation mode (pre-gate).

## Out of Scope

- The broken public `procom.ca/find-jobs/` path — always use the `myprocom-portal` subdomain.
- Pagination beyond the first results page.
- Auto-filing eligible+high-scoring results without user confirmation.
