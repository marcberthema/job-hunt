# Spec: Local SMB Consulting Practice (Parked)

> **Status: idea, not active.** Do not start building anything against this spec until the
> current urgent job search (see `CLAUDE.md` "Current Situation") is resolved — Marc has landed
> a role and has breathing room again. This file exists so the idea isn't lost, not as a green
> light to implement.

## Origin

Marc's own framing (2026-09-19): build a part-time IT consulting practice on the side, applying
DevOps principles (Phoenix Project's Three Ways) to small businesses and organizations with no
in-house IT department — law firms, retail shops, school boards, etc. Free initial
assessment/conversation to find their pain points, paid proposal + implementation after.

## Why it's parked, not pursued now

1. **Timeline mismatch.** Local SMB trust-based sales cycles run months; Marc's contract ends in
   ~5 weeks and he's the sole financial provider. This can't be the primary plan during the
   urgent window — see `CLAUDE.md`.
2. **Unscoped free work risks bleeding time** he can't afford right now — small business owners
   will happily consume unlimited free diagnostic hours.
3. **No liability coverage or engagement paperwork yet** — touching a client's production systems
   without E&O/CGL insurance and a written scope agreement is a real exposure, not a formality.
4. **Public-sector targets (school boards, municipal) are a different, much slower sales motion**
   (RFP/procurement/bonding) — don't conflate with cold-calling a law firm.

## What a real spec would need to cover, once revisited

- **Offer definition**: cap the free portion explicitly (e.g. a 30-minute diagnostic call, not
  open-ended "X hrs of assessment"); define what's in the paid proposal/implementation.
- **Target list**: small businesses with no IT department, reachable in person or via Teams —
  law firms, retail, and (lower priority, slower sales cycle) school boards/public-facing orgs.
- **Legal/insurance prerequisites**: E&O/CGL insurance and a one-page scope-of-work agreement
  before any hands-on assessment work, even unpaid.
- **Validation step before building anything**: 5-10 real conversations with local business
  owners about actual pain points, before a website or funnel is built.
- **Website/intake funnel**: a tailored site with a work-request form — explicitly *after*
  validation, not before. Would live alongside or reuse patterns from `site/` if pursued.
- **Relationship to `profile.md` / consulting goals**: this is the local-SMB piece of the
  longer-term retainer-client strategy (Million Dollar Consulting end-goal — value-based
  consulting, retainer clients) — see project memory `million_dollar_consulting_endgoal`.

## Next step when revisited

Talk it through in a Claude Code session again, confirm scope/target list/offer cap, then write
a proper implementation-ready spec (this file gets replaced or promoted, not built from
directly).
