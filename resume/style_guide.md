# Resume Style Guide

> Prescriptive rules for generating Marc Berthelette's resume/CV in English and French.
> Read by Claude skills (`/buildresume`, `/buildsite`, and any future export step) **before** generating
> any resume artifact. Where this file says **MUST**, follow it exactly. Where it says **SHOULD**, follow
> it unless the source data makes it impossible, then note the deviation.
>
> Source of truth for *content* is always `profile.md`. This file governs *form*: structure, tone,
> formatting, and export. Read `profile.md` first, then apply these rules.

---

## 1. Philosophy & Visual Tone

The resume targets **enterprise procurement and senior hiring managers in regulated industries**
(financial services, energy) in the Canadian market. The reader is busy, skims for credibility and
fit in under 30 seconds, and feeds the document through an Applicant Tracking System (ATS) before a
human sees it.

Therefore the tone is **clean, executive, and modern — never graphic-designer flashy.**

- **MUST** be single-column, left-aligned, text-first.
- **MUST NOT** use columns, sidebars, text boxes, tables-for-layout, icons, photos, logos, progress
  bars, skill rating dots, color blocks, or background shading. These break ATS parsing and read as
  junior/template-driven to enterprise readers.
- **SHOULD** rely on whitespace, consistent hierarchy, and one restrained accent color (see §3) for
  structure — not decoration.
- Credibility signals (named enterprise clients, regulated-sector experience, bilingualism, years of
  experience) **MUST** appear above the fold on page 1.

The mental model: a partner-track consulting firm's one-pager, not a designer's portfolio.

---

## 2. Source & Output Files

```
resume/
  style_guide.md                      ← this file
  marc-berthelette-resume-en.md       ← English master (Markdown source of truth for content layout)
  marc-berthelette-resume-fr.md       ← French master (parallel structure, see §6)
  export/                             ← generated PDFs (gitignored or committed per repo convention)
    marc-berthelette-resume-en.pdf
    marc-berthelette-resume-fr.pdf
```

- The **Markdown files are the canonical resume artifacts.** PDFs are generated from them (see §11).
- Filenames **MUST** follow `marc-berthelette-resume-<lang>.md` where `<lang>` is `en` or `fr`.
- A skill regenerating the resume **MUST** preserve this naming and overwrite in place.

---

## 3. Typography

### Markdown source
- Use standard Markdown headings (`#`, `##`, `###`) for hierarchy — never bold-as-heading or ALL-CAPS
  pseudo-headings. ATS and PDF converters rely on real heading levels.
- One `#` (H1) for the candidate name only.
- `##` for top-level sections (Professional Summary, Work Experience, etc.).
- `###` for individual roles within Work Experience.
- Bold (`**`) for the employer line, dates, and inline labels (`**Key technologies:**`).
- Horizontal rules (`---`) **MAY** separate roles for readability in the Markdown; they are cosmetic.

### PDF / print rendering
- **Body font MUST be a clean, widely-available sans-serif:** primary choice **Inter**, fallback
  **Helvetica / Arial**. A serif (Georgia, Source Serif) is acceptable *only* for the name/headings if
  a two-typeface executive look is wanted, but **default to a single sans-serif family** for simplicity
  and ATS safety.
- **MUST NOT** use decorative, condensed, or display fonts.
- Sizes (print): body **10.5–11pt**, role/section sub-labels **11pt bold**, section headings (`##`)
  **13–14pt**, name (`#`) **20–24pt**.
- Line height **1.3–1.45**. Generous but not loose.
- **Accent color:** a single deep, professional tone — **navy (`#1a3c5e`) or the site accent blue
  (`#1a56db`)** — used only for the name and/or section-heading underlines. Body text **MUST** be near-black
  (`#111`). No other colors. Keep it printable in greyscale.
- Margins **0.6–0.8in** (1.5–2cm) on all sides.
- The exported PDF **MUST** contain selectable, real text (never a flattened image), or ATS cannot read it.

---

## 4. Section Order & Inclusion

Sections **MUST** appear in this order. Mandatory sections are marked **[REQUIRED]**.

1. **Name + Contact Header** — **[REQUIRED]**
2. **Professional Summary** — **[REQUIRED]**
3. **Technical Skills** — **[REQUIRED]** (placed high — see §5)
4. **Work Experience** — **[REQUIRED]**
5. **Certifications** — **OPTIONAL.** Omit entirely while Marc has no completed or actively-pursued
   certifications to list (see §9). Add back only once he resumes/finishes one.
6. **Education** — **[REQUIRED]**
7. **Languages** — **[REQUIRED]** if not already explicit in the header (bilingualism is a core
   differentiator and **MUST** be unmissable)
8. **Currently Building / Selected Projects** — **OPTIONAL.** Omit by default. Per `profile.md`, Brayd
   and Canopy are **NOT** to appear on the resume until announced. Only include if the user explicitly asks.
9. **References** — **OMIT.** Do not include a section, not even "available on request."

### Header contents (**[REQUIRED]** fields)
- Name (H1)
- Title line: **Senior DevOps Engineer | Platform Engineering Consultant** (use the job-board title per
  `profile.md` "Notes for Claude")
- Location + remote availability (e.g. `Smiths Falls, ON, Canada · Remote`)
- Email · LinkedIn URL
- Bilingual + incorporated status on its own line
- **MUST NOT** include: photo, full home address, date of birth, SIN, marital status, or any personal
  identifiers. This matches Canadian convention and privacy norms.

---

## 5. Skills Placement & Content

- The **Technical Skills section MUST sit near the top** (after the summary, before or interleaved with
  experience). 2025 skills-based hiring and ATS keyword scanning reward early, scannable skills.
- Group skills by category (Cloud & DevOps Platforms, IaC, Containers & Orchestration, Monitoring &
  Observability, Programming & Scripting, etc.) exactly as categorized in `profile.md`.
- A **plain category-list / definition layout MUST be used.** A simple two-column Markdown table
  (Category | Technologies) is acceptable because most PDF engines and modern ATS parse it, BUT if
  targeting a specific employer known to use a strict legacy ATS, fall back to a flat
  `**Category:** tech, tech, tech` line list. Default to the table for readability.
- **MUST NOT** use skill-level ratings, bars, stars, or percentages.
- Lead with **Azure first** in the cloud category, every time (per `profile.md`).

---

## 6. Bilingual Versions (EN / FR)

- Produce **two separate files**, not one mixed document. `-en.md` and `-fr.md`.
- The two versions **MUST share identical structure, section order, and role ordering.** Same skeleton,
  translated content. A reader comparing them side by side should see mirror documents.
- **French MUST use Canadian/Quebec French** conventions and terminology — not European French. This is
  non-negotiable for the Quebec market.
  - Job titles: keep widely-understood Anglicisms where they are the industry norm in Quebec tech
    (e.g. "DevOps", "Platform Engineering", "CI/CD", "cloud" are commonly used as-is), but translate
    surrounding prose into natural Québécois professional French (e.g. *Ingénieur DevOps principal*,
    *Architecture de pipelines CI/CD*, *Infrastructure infonuagique* / *infonuagique* for "cloud" when
    a French term is preferred).
  - Use accented capitals (É, À) correctly — `École`, `Énergir`.
  - Spell out the bilingual line in French: *Bilingue : français (langue maternelle) · anglais (courant)*.
- **Tool/product names stay in English** (Azure DevOps, Terraform, Kubernetes, JFrog Artifactory, etc.).
  Do not translate proper nouns or technology names.
- Dates and date format are identical across both (see §10).
- When `profile.md` content changes, **both** files **MUST** be regenerated together so they never drift.
- For a single bilingual-required application, deliver the FR version first or both, French first, per
  Quebec norms.

---

## 7. Bullet Point Style

Every experience bullet **MUST** follow the formula:

> **Action verb (past tense) + what you did (with the specific technology) + measurable outcome / business impact.**

- **Start with a strong action verb:** *Architected, Automated, Built, Delivered, Designed, Drove,
  Implemented, Led, Migrated, Optimized, Orchestrated, Standardized, Streamlined.* **MUST NOT** start a
  bullet with "Responsible for", "Worked on", "Helped with", or any passive/weak opener.
- **Name the technology** in the bullet where relevant — this doubles as ATS keyword coverage.
- **Quantify whenever the data exists:** time saved, release velocity, MTTR reduction, cost reduction,
  uptime/availability, deployments per day, repos/services covered, drift eliminated. If a real number
  is unknown, prefer a concrete qualitative outcome over an invented metric — **MUST NOT fabricate
  numbers.** Use directional language ("significantly accelerated release velocity", "reduced MTTR")
  rather than fake precision, but flag to the user that adding real metrics would strengthen the bullet.
- **3–5 bullets per role** for recent/relevant roles; **2–3** for older roles. The most recent and most
  relevant role (currently Énergir / Desjardins for financial-sector targets) gets the most detail.
- End each role with a **`**Key technologies:**`** line — a comma-separated tech list. This is a
  deliberate, high-density ATS keyword line and **MUST** be present on every role.
- Keep each bullet to **1–2 lines** in print. Tighten ruthlessly; no run-ons.

---

## 8. Length

- **Target two pages.** For a ~20-year senior engineer/consultant in the Canadian market, two pages is
  the correct, expected length — one page would undersell the depth, three+ reads as unfocused.
- **MUST NOT exceed two pages** for the standard resume. If content overflows, trim older-role bullets
  (SOVO, Tink) before cutting recent, sector-relevant detail.
- The full multi-page document is a *resume*, not an academic *CV*. Do not label it "CV" for private-sector
  Canadian roles; "Resume" / "CV" is interchangeable colloquially but keep the content resume-style
  (targeted, 2 pages) unless the user explicitly requests an academic/government long-form CV.
- Page 1 **MUST** be self-sufficient: header, summary, skills, and the two most recent roles all land on
  page 1.

---

## 9. Certifications, Including "In Progress"

- The Certifications section is **OPTIONAL** and currently **omitted**: Marc paused AZ-104/AZ-400 study
  and has nothing completed or actively in progress worth listing as of 2026-08. Do not add a
  Certifications section back until he resumes studying or earns one.
- If/when reinstated, format each as a row/line with an explicit **status**:
  - Completed: `Microsoft Azure Administrator (AZ-104) — 2026` (name, issuer/code, year earned).
  - In progress: `Microsoft Azure Administrator (AZ-104) — In Progress` (or *En cours* in FR).
- **MUST NOT** present an in-progress certification as if completed, and **MUST NOT** imply a pass date
  that has not happened. Honesty here is a procurement trust issue in regulated sectors.
- **SHOULD** optionally add an expected/target date if the user provides one
  (`AZ-400 — In Progress (expected Q4 2026)`).
- When a cert is earned, the skill updating this resume **MUST** also prompt to update `profile.md` so
  the two stay in sync, and re-add the Certifications section to both resumes.

---

## 10. Dates & Localization

- **Use `YYYY-MM` or `Month YYYY` consistently.** Canadian convention favors ISO-style `YYYY-MM-DD`;
  for human-readable ranges, `Month YYYY – Month YYYY` is acceptable and preferred for readability
  (e.g. `September 2021 – Present`). Pick one format and apply it to **every** date in the document.
- Current role end date is `Present` (EN) / `Présent` (FR).
- Spelling: **Canadian English** in the EN version — *labour, colour, behaviour, optimize* (note: -ize
  is standard Canadian for many verbs; keep consistent). **Canadian French** in the FR version.
- Locations as `City, Province` (e.g. `Montréal, QC`) — keep the accent on Montréal in both versions.

---

## 11. Markdown → PDF Export

- The canonical generation path is **Pandoc** (Markdown → PDF), with styling controlled by a CSS or
  Typst/LaTeX template — **not** ad-hoc per-run formatting.
- Recommended toolchain, in order of preference:
  1. **Pandoc + Typst** (modern, fast, fine layout control) or **Pandoc + a clean LaTeX template** for
     polished typographic output.
  2. **Pandoc → HTML + CSS → wkhtmltopdf / weasyprint** when web-style CSS control is easier (reuse the
     `site/` palette: accent `#1a56db`, near-black text `#111`, system/Inter sans-serif).
- The exported PDF **MUST**:
  - contain selectable real text (ATS requirement) — never an image/flattened render;
  - embed fonts so it renders identically on the reader's machine;
  - keep real heading structure and reading order (no multi-column flow);
  - stay within two pages (§8).
- **MUST NOT** rely on emoji, custom glyphs, or icon fonts in the export.
- Generate **both** `en` and `fr` PDFs in the same run so they never drift.
- Filenames: `marc-berthelette-resume-en.pdf` / `marc-berthelette-resume-fr.pdf` in `resume/export/`.

---

## 12. ATS & Keyword Optimization

- **Use the exact, conventional section headers** ("Professional Summary", "Work Experience",
  "Technical Skills", "Education", "Certifications"). Creative headers break ATS section detection.
  In FR use the conventional equivalents (*Sommaire professionnel / Profil*, *Expérience
  professionnelle*, *Compétences techniques*, *Formation*, *Certifications*).
- **Mirror the target job posting's keywords** when tailoring per application: pull required skills,
  tool names, and the exact job title from the posting and ensure they appear naturally in the summary,
  skills, and bullets — but **MUST NOT** keyword-stuff, fabricate, or list tools Marc hasn't used.
- Keep the master files general-purpose; per-application tailoring is a copy-then-adjust step, not a
  rewrite of the masters.
- Spell out acronyms once with the acronym in parentheses on first use where ambiguity is possible
  (e.g. `Infrastructure as Code (IaC)`, `Continuous Integration / Continuous Delivery (CI/CD)`), then
  use the acronym — this covers both spelled-out and abbreviated ATS searches.
- No headers/footers containing critical info (some ATS ignore header/footer zones) — keep name and
  contact in the document body.

---

## 13. Consulting vs Employment Targeting

`profile.md` positions Marc as a **consultant first, open to employment second.** The resume **SHOULD**
default to the consulting frame, with an employment-leaning variant available on request.

### When targeting consulting / contract / fractional (default)
- Title line leads with **Consultant** framing (e.g. *Senior DevOps & Platform Engineering Consultant*).
- Summary **MUST** signal: incorporated in Canada, available immediately, no onboarding friction,
  recommends approach rather than executes tickets, team-enablement component.
- Frame engagements as **delivered outcomes** (e.g. "Delivered a 6-month engagement...") — emphasize
  scoped, autonomous, high-leverage work.
- Highlight the **Desjardins contract** prominently for financial-sector targets and **Énergir** for
  energy-sector targets (per `profile.md` competitive advantages).

### When targeting employment (on request)
- Title line uses the job-board title (*Senior DevOps Engineer*).
- Soften contract-only framing; emphasize long-term ownership (Énergir tenure) and team leadership.
- Keep the same factual content — only the framing/emphasis shifts.

### Always (both modes)
- Lead with **Azure** as the primary cloud platform.
- Make **bilingualism (FR/EN)** unmissable — it is a core Canadian/Quebec/federal differentiator.
- Surface **regulated-industry credibility** (financial services, energy) early.

---

## 14. Canadian / Quebec Market Specifics (summary checklist)

A generated resume **MUST** satisfy all of these:

- [ ] No photo, no SIN, no DOB, no marital status, no full street address.
- [ ] Two pages max; page 1 self-sufficient.
- [ ] Bilingual differentiator visible on page 1.
- [ ] Two parallel files (EN + FR), FR in Canadian/Quebec French.
- [ ] Canadian spelling in EN; Canadian French in FR.
- [ ] Consistent date format throughout.
- [ ] Standard ATS-safe section headers (EN and FR equivalents).
- [ ] Single-column, no tables-for-layout, no graphics, selectable-text PDF.
- [ ] Certifications section present (with honest In Progress / *En cours* status).
- [ ] Azure-first, financial/energy credibility, consulting frame by default.
- [ ] References section omitted entirely.
- [ ] Brayd / Canopy excluded unless the user explicitly requests their inclusion.

---

## 15. Sources Informing This Guide

- ATS format best practices (single-column, reverse-chronological, standard headers, selectable PDF,
  skills near top): The Interview Guys, Resumly, Indeed, ResumeAdapter (2025–2026 guides).
- Canadian resume conventions (2-page norm for seniors, no photo/SIN, bilingual EN/FR for Quebec &
  federal, Canadian French not European, YYYY-MM-DD dates): Novoresume, Enhancv, Monster, Zety.
- DevOps/Platform bullet style (action verb + tech + quantified outcome, 3–4 bullets/role): TealHQ,
  Enhancv, The Interview Guys DevOps templates.
- Markdown→PDF workflow (Pandoc + Typst/LaTeX/CSS, embedded fonts, real text): Pandoc resume guides,
  Neil's blog (Pandoc + Typst), Small Sharp Software Tools.
