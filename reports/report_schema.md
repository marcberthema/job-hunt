# Report data schema

Every `check-*` skill writes its run's results to `reports/data/<board>.json` instead of
hand-authoring `reports/<board>-job-search.html` directly. `reports/build_report.py` renders the
HTML deterministically from that JSON — no AI-authored HTML, no per-board bespoke CSS.

`<board>` is the lowercase slug used everywhere else in this repo (`builtin`, `dice`, `indeed`,
`linkedin`, `jobbank`, `eluta`, `randstad`, `remoteok`, `sisystems`, `braintrust`, `wwr`,
`glassdoor`, `procom`, `roberthalf`).

**`rows` uses the exact field names below for every board, no exceptions.** The renderer is one
shared template — a board whose rows use different field names (e.g. `why`/`flags` instead of
`gap`/`location`/`salary`/`status`) will render those columns as `undefined` in the browser,
silently, since nothing errors at build time. If you're hand-editing or migrating a board's data
file, verify against this schema, not against an older version of that board's own file.

## Fields

```json
{
  "board": "BuiltIn",
  "run_date": "2026-09-18",
  "eyebrow": "Candidate intelligence · Built In",
  "title": "SRE, Platform & DevOps opportunities",
  "lede": "One sentence describing this board's scope and what the score does/doesn't measure.",
  "latest_update": "Latest update: September 18, 2026 — one-line summary of this run.",
  "stats": [
    {"value": 45, "label": "search passes"},
    {"value": 25, "label": "current validated postings"}
  ],
  "rows": [
    {
      "score": 9,
      "family": "SRE",
      "title": "Job title",
      "company": "Company",
      "location": "Remote Canada",
      "salary": "CAD $128,300–$203,000/year",
      "gap": "Biggest gap, one sentence",
      "url": "https://...",
      "status": "New"
    }
  ],
  "ineligible": [
    {"title": "...", "company": "...", "reason": "...", "url": "..."}
  ],
  "could_not_validate": ["One sentence per posting that couldn't be validated."],
  "notes_sections": [
    {"heading": "Validation notes", "items": ["One <li>-ready string per item; inline <b>/<a> markup is fine, it's inserted as HTML."]}
  ],
  "method": "Closing paragraph — search boundary, run totals, methodology notes."
}
```

### Required

- `board`, `run_date`, `rows` (array; empty `[]` is valid — matches a run with nothing eligible).

### Optional — omit the key entirely when a board has nothing to say there

- `eyebrow`, `title`, `lede`, `latest_update` — default to generic text if omitted, but every skill
  should set these for a readable report.
- `stats` — the stat-card row. Use whatever counts the skill's own "Output and report" section
  already tracks (searches completed, eligible/ineligible/inaccessible, pipeline matches, etc.).
- `ineligible` — only for boards that run an eligibility gate (Dice, RemoteOK, WWR, Braintrust,
  Procom). Rendered as a separate not-scored table.
- `could_not_validate` — postings whose full description couldn't be confirmed; list of plain
  sentences.
- `notes_sections` — freeform prose the skill wants to surface (exclusions, caveats, refresh
  deltas). `items` strings may contain `<b>`/`<a>` inline HTML; everything else must already be
  escaped by the writer (the renderer does not escape these).
- `method` — a closing methodology paragraph. May contain inline HTML same as `notes_sections`.

### Row fields

- `score` (0–10, required), `family` (`SRE` | `Platform` | `DevOps`, required), `title`,
  `company`, `url` (required).
- `location`, `salary`, `gap` — optional, default to blank/"Not stated" in the rendered table.
- `status` — this posting's pipeline label, starting with one of `New`, `Applied`, `Skipped`,
  `Rejected`, or `Expired` (free text may follow, e.g. `Applied — Sep 18`), or omitted/blank when
  it isn't decided yet. `Skipped` means Marc decided not to pursue it (skill gap, duplicate, bad
  rate, etc.); `Rejected` means he applied and the employer passed on him — only reachable from
  `Applied`, never set directly on a fresh discovery row. `Applied`, `Skipped`, and `Rejected`
  should mirror the matching `applications.md` row when one exists — a `check-*` skill's own
  discovery pass typically only ever produces `New` rows, since it never files anything on its
  own (see `CLAUDE.md`'s Conventions). `Expired` is report-only (an expired posting never gets an
  `applications.md` row of its own — see the `review` skill for how a posting's expiry gets
  recorded there instead, as a `Skipped` row with a reason). The status pill under the job title
  always shows this text, and the "hide applied, rejected, skipped & expired" toggle hides any
  row whose status starts with one of those four words — so when the user confirms a decision on
  a posting, set `status` accordingly, not just a note.

## Regenerating the HTML

```
python3 reports/build_report.py <board>     # one board
python3 reports/build_report.py --all       # every board with a data file, plus reports/index.html's nav
```

Run this as the last step of every `check-*` skill invocation, and any time `reports/data/<board>.json`
is hand-edited (e.g. flagging one posting `Expired` or removing a stale entry) — no need to
re-run the search itself for a data-only fix.
