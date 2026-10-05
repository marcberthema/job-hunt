# Spec: Local SMB Consulting Practice (Parked)

> **Status: idea, not active.** Do not start building anything against this spec until the
> current urgent job search (see `CLAUDE.md` "Current Situation") is resolved — Marc has landed
> a role and has breathing room again. This file exists so the idea isn't lost, not as a green
> light to implement.
>
> **Revised 2026-10-03** after a multi-day conversation (2026-10-02 → 10-03) that redefined the
> offer. The original 2026-09-19 version is summarized under "History" at the end.

## The philosophy

Marc's own statement (also in `profile.md` → Working Philosophy):

> **My one goal is to help you — by improving existing processes and automating repetitive ones —
> so you can spend more time doing what you actually want to do.**

For a café owner, that means less time on bookings, scheduling and stock counts, and more time
baking, trying new recipes and planning classes. The same thesis drives Marc's youth-sports SaaS
idea (`youth-sports-saas-discussion-context.md`), but the two are separate businesses with
different economics — this practice is consulting, not software for the client.

## What the offer is — and is not

**Is:** improving how a small business's *existing* systems work and removing manual steps
between them, inside the platforms the business already uses.

**Is not:**
- **Not a website builder.** Anyone can generate a site with an AI builder in 2026. The value is
  making the existing site and tools fit how this particular business actually runs.
- **Not a replacement platform.** No migrating clients off Squarespace, Wix, Shopify or Square.
- **Not a helpdesk or managed IT service.** No break-fix, no same-day emergencies, no on-site
  device repair. Those go to a named local IT shop.
- **Not custom software for the client.**

## Ownership rule — stay within their system

Marc changes how things work; he never changes who owns anything. Responsibility for the
platform, payments, domain and data stays with the business.

- Work only inside the client's existing platform and accounts.
- Access through the owner adding Marc as a collaborator/admin with his own login, revocable at
  any time. **Never** take the owner's password, and never touch payment credentials.
- Any automation (e.g. Zapier/Make) lives in the **client's** account, paid by the client — not
  Marc's — so it keeps working if they part ways.
- When the platform cannot do what the client needs, the answer is a written recommendation, not
  something Marc builds outside it.
- Marc is still responsible for the changes he makes. Document every change and hand it over.

## How an engagement runs

The conversation comes first; analysis is aimed at what the owner said hurts.

1. **Prepare — unpaid, ~30 min.** Check the public site: which builder (Wappalyzer/BuiltWith or
   page source), which payment option, how booking works. Bring two or three specific
   observations to open with — not a proposal.
2. **Conversation with the owner.** Opening question: *"What do you do every week that takes time
   away from the thing you actually want to be doing?"* Walk through their week. If they name no
   problem, there's no sale.
3. **Paid diagnostic — fixed small fee, credited toward the project if they proceed.** With
   collaborator access, map their real systems (site, booking, till, inventory, scheduling,
   email). This is where AI-assisted analysis and spec writing belong — aimed at the pain points
   the owner named, not a general audit.
4. **Proposal.** Two lists, each item tied to a named pain and the hours it gives back:
   (a) changes within their platform; (b) automations between their systems.
5. **Build and hand over.** Fixed price, tied to an outcome the owner agreed on and can see.
   Written documentation of everything changed.
6. **Optional retainer** — see Pricing.

Don't lead the pitch with "AI". The owner is buying hours back; AI is how Marc works, not what
they buy. If client data goes into AI tools, say so and say how it's handled.

## Pricing

- **Value-based, not hourly.** Price against the hours given back, never against the cost of the
  software (a café's site builder costs roughly $30–100/month — don't let the owner compare the
  fee to that).
- **Paid diagnostic** replaces the original "free assessment" — it filters out free-advice
  seekers and pays for the learning time.
- **Fixed-price project** per agreed outcome. Marc absorbs his own learning time on a new platform;
  expect the first project on each platform to pay worse than later ones.
- **Optional retainer** defined by responsibility and response time, never by hours: Marc owns the
  improvement backlog and systems decisions, monitors the automations, answers within two business
  days. Helpdesk explicitly excluded.
- **Revenue share (a % of what the client earns) — not the model.** It fits the SaaS, where an
  extra customer costs almost nothing and payments flow through the platform. In consulting every
  client costs hours and the money never passes through anything Marc controls. Acceptable once,
  at most, to land a first case study.

## Proof over promises

SEO-style consulting has a bad reputation because its results are unmeasurable. This practice's
protection is the opposite: a measured before-and-after for every engagement — hours per week
the owner gets back, in the owner's own words. Collect it from the first client onward.

## Target clients — honest economics

- **Cafés and micro-businesses** (e.g. Café C'est Tout in Smiths Falls — classes plus service,
  likely several disconnected systems): good first case studies, poor long-term economics.
  Rough estimate: saving a café owner ~5 hours/week is worth ~$6,500/year to them, so a
  value-based fee lands around $650–2,000 once. Retainers at this size: ~$100–300/month.
- **Businesses with 10–50 staff** (clinics, law/accounting firms, contractors, small
  manufacturers): where the practice pays. The same wasted hours are spread across salaried
  staff and the owner already feels it. Retainers of ~$500–750/month are plausible.
- **Market size:** Smiths Falls alone is too small. Plan for Perth, Carleton Place, Brockville,
  Kemptville, and remote clients further out.
- **Income target check:** $1,500/month of side income ≈ 8–10 café-size retainers or 2–3 at
  10–50-staff firms. With ~5–8 hours/week available alongside a full-time job, only the second
  route fits.

All figures above are estimates from the 2026-10-02/03 conversation, not market research.

## Platforms — what Marc needs to know

Small businesses mostly use one of four builders, which also host the site and usually handle
payments (details from general knowledge — verify current plans and features):

| Platform | Notes |
|---|---|
| Squarespace | Restyle freely; can duplicate the site to work on a copy. Booking via Acuity Scheduling. Own payments option plus Stripe/PayPal. |
| Shopify | Cleanest: the look (theme) is separate from products, orders and payments; build unpublished, then publish. Shopify Payments plus others. |
| Square Online | Built on Weebly; payments always Square. Common if the business uses a Square till. |
| Wix | A published site reportedly can't switch templates — a redesign may mean building a new Wix site and moving the domain and plan. |

- **Check the payment setup early.** An independent Stripe/Square/PayPal account belongs to the
  business; a built-in platform payment account (Wix/Shopify/Squarespace Payments) is tied to the
  platform.
- **Learn per client, not up front.** Ask which platform in the first conversation and learn that
  one. The connecting layer (Zapier/Make, webhooks, APIs) is the same across platforms and closest
  to Marc's existing skills — learn it once.
- **Optional head start, after landing a role:** free trial on Square Online and Squarespace, build
  one test café site with a class booking and a payment, a few evenings per platform.

## Prerequisites before the first paid client

- E&O / liability insurance — needed even with the ownership rule, because Marc is responsible for
  his own changes.
- One-page scope-of-work agreement: what's in, what's out (helpdesk, emergencies), how access is
  granted and revoked, how changes are documented.
- Check any FTE employment contract for moonlighting or IP-assignment clauses first.

## Validation before building anything

5–10 real conversations with local owners using the opening question above, before any website,
funnel or marketing. Start as a customer, not as a pitch — e.g. ask the café owner how class
bookings work and how many calls or messages they get about them.

## History

- **2026-09-19 (original):** part-time IT consulting for small businesses and organizations with
  no IT department (law firms, retail, school boards), free initial assessment then paid
  proposal, framed around Phoenix Project's Three Ways. Parked for timeline reasons. Public-sector
  targets (school boards, municipal) dropped from focus — RFP/procurement is a much slower,
  different sales motion.
- **2026-10-02/03 revision:** reframed around the philosophy above; discovery first; stay within
  the client's platform; paid diagnostic instead of free assessment; value pricing; managed-IT and
  revenue-share models rejected.
