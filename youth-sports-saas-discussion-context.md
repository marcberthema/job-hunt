# Youth Sports SaaS — Discussion Context & Decision Record

**Date:** 2026-10-02  
**Purpose:** Preserve the product reasoning, competitor takeaways, business philosophy, monetization model, and current strategic decisions from this discussion.

---

## 1. Why this product idea exists

The idea started from direct frustration with youth-sports software, especially TeamSnap.

The emotional origin is simple:

> A parent should be able to answer “Where and when is my kid's next basketball game?” without fighting through ads, unnecessary friction, fragmented screens, or an app that seems designed partly around extracting more money.

The original idea was loosely “build a better TeamSnap.”

Competitive research showed that this framing is too weak. The market already has many capable products, and recreating schedules, rosters, chat, RSVP, registration, payments, and basic family calendars would mostly reproduce commodity functionality.

The idea evolved into:

> **A family-centered youth-sports operating system that preserves each athlete's sporting journey and actively removes low-value administrative and coordination work from families, coaches, and volunteer organizations.**

The system should not simply digitize repetitive work.

It should ask:

> **Why is a human doing this step at all?**

If the platform has enough context and permission to safely perform a repetitive task, it should attempt to do it.

---

## 2. Core operating philosophy

High-value human work includes:

- coaching;
- athlete development;
- mentoring;
- judgment;
- team-building decisions;
- conversations with families;
- resolving ambiguous situations;
- creating community.

Low-value work includes:

- chasing RSVPs;
- finding snack volunteers;
- arranging rides;
- sending repetitive reminders;
- manually identifying who should receive an invitation;
- redistributing cancelled gym time;
- rebuilding season information;
- moving the same information between spreadsheets, registration tools, email, and team apps.

The desired pattern is:

```text
Detect
  ↓
Attempt Resolution
  ↓
Confirm
  ↓
Escalate only when necessary
```

A key design rule is:

> **Do not create a dashboard telling users about work the platform could perform itself.**

---

## 3. Four product pillars

### Pillar 1 — Family as an operational center

The family is not merely a login containing several children.

It should be meaningful operational context.

Conceptually:

```text
Family
├── Guardian A
├── Guardian B
├── Athlete A
├── Athlete B
├── Athlete C
└── Athlete D
```

The system should eventually understand:

- siblings share guardians;
- a guardian may coach another team;
- siblings may have overlapping events;
- one guardian may be available to drive;
- a family may already have volunteered several times;
- optional opportunities should go to the appropriate guardian;
- schedule decisions can create impossible household logistics.

Important design decision:

> **Person is the durable human identity. Family/Household is the operational relationship and the center of the family experience.**

A person may simultaneously be:

- guardian;
- coach;
- volunteer;
- administrator;
- official.

A child may belong to more than one household where needed.

**Research correction:** competitors do support real household/family models. The opportunity is not “we have families.” It is:

> **Use the household graph operationally.**

Sibling/family-aware operational scheduling was not strongly verified in the research.

---

### Pillar 2 — Proactive coordination / low-value-work automation

Examples:

- RSVP chasing;
- snack duty;
- volunteer assignment;
- ride coordination;
- spare-player invitations;
- optional practices;
- tournament invitations;
- coach vacancies;
- payment follow-up;
- cancelled facility time.

These should be reusable workflows rather than unrelated one-off features.

```text
Need detected
→ eligible people/resources identified
→ request/offer sent
→ response received
→ state updated
→ retry if needed
→ escalate only if unresolved
```

**Research correction:** automation is not unique. BenchApp and Spond already automate meaningful coordination.

The differentiation is:

> **Automation as a platform-wide operating philosophy rather than a few isolated features.**

---

### Pillar 3 — Persistent athlete history and development

An athlete should not be modeled merely as `PlayerOnTeam`.

The athlete persists.

Team memberships are temporary relationships.

History can include:

- sports;
- organizations;
- seasons;
- teams;
- coaches;
- games;
- official results;
- statistics;
- evaluations;
- development goals;
- tournaments;
- camps;
- optional practices;
- achievements;
- media.

Long term, identity should survive:

- team changes;
- season changes;
- organization changes;
- sport changes.

**Research correction:** athlete history already exists in meaningful forms. GameChanger is strong in career stats/video, while PlayMetrics and Sprocket Sports have club-owned history and evaluations.

The sharper opportunity is:

> **A family/athlete-controlled sporting identity that can eventually span teams, seasons, organizations, and sports.**

---

### Pillar 4 — Organization intelligence and planning

The organization should not merely record decisions. It should help make them.

Potential areas:

- team formation;
- coach recruitment;
- facility allocation;
- schedule generation;
- conflict detection;
- roster imbalance;
- play-up candidates;
- volunteer load;
- released capacity;
- exception handling.

Example:

```text
U12 registered: 15
Target roster: 12

U13 registered: 9
Target roster: 12

System surfaces:
- 4 U12 athletes age-eligible for U13
- 2 previously played up
- 3 have coach evaluations suggesting readiness
```

The human makes the final decision.

**Research correction:** scheduling/team building are much more mature than initially assumed.

The remaining opportunity is stronger in cross-domain reasoning:

- family-aware scheduling;
- guardian/coach conflicts;
- proactive coach staffing;
- released-gym redistribution;
- exception-based operations;
- using development history as one planning input.

---

## 4. Important reusable concepts

### Person

Durable human identity.

### Family / Household

Persistent family relationship and operational context.

### Athlete

Persistent sporting identity independent of team and season.

### Membership

Temporary relationship such as:

```text
Athlete → Team → Season
```

### Opportunity

Reusable abstraction for:

- optional practice;
- tournament;
- guest-player invite;
- clinic;
- open gym;
- pickup session.

Pattern:

```text
Opportunity created
→ eligible audience
→ invitation
→ response
→ participation
→ calendar
→ history
```

### Participation Blocker

Attendance should not be only Yes/No.

Example:

```text
Attendance: YES
Transportation: NEEDS RIDE
Overall: PENDING RESOLUTION
```

Once resolved:

```text
Attendance: YES
Transportation: ARRANGED
Overall: CONFIRMED
```

---

## 5. Example automation workflows

### Snack duty

```text
Duty unfilled
→ identify eligible willing families
→ ask one
→ if declined, try another
→ confirm assignment
→ escalate only if unresolved
```

Future fairness inputs may include:

- previous volunteer load;
- availability;
- preferences;
- family conflicts;
- recent declines.

### Transportation

Guardian answers:

```text
Yes
Yes, but needs a ride
No
```

The system may:

- identify attending families;
- find families willing/allowed to drive;
- send a request;
- record acceptance;
- update participation;
- notify relevant guardians.

The coach should not act as dispatcher.

### Optional practice

Coach selects eligible athletes.

The platform sends structured invitations and aggregates responses.

### Tournament invitation

Coach selects athletes.

The platform manages invitations, responses, capacity, and calendar.

### Released gym time

A cancelled practice should create organization knowledge:

```text
Gym 2
Thursday 18:00–19:30
AVAILABLE
```

The system may then:

- expose the slot;
- notify eligible teams;
- apply organization priorities;
- check team practice count;
- check coach availability;
- check conflicts;
- recommend a recipient;
- require approval if needed.

---

## 6. Competitive research

A structured matrix was built with **57 capabilities** across:

- Family & Identity
- Athlete Identity & Continuity
- Coach & Team Operations
- Organization Administration
- Scheduling, Facilities & Resource Use
- Communication, Opportunities & Workflow Automation
- Development, Statistics & Sporting History
- Platform, Privacy & Commercial Model

Competitors researched:

1. TeamSnap
2. PlayMetrics
3. SportsEngine
4. LeagueApps
5. TeamLinkt
6. GameChanger
7. Spond
8. Sports Connect
9. Heja
10. BenchApp
11. Sprocket Sports
12. RAMP Interactive
13. Upper Hand
14. Jersey Watch
15. Demosphere / OTTO SPORT

---

## 7. Top competitors by pillar

| Product pillar | Closest overlap | Second | Third |
|---|---|---|---|
| Family as operational center | OTTO SPORT / Demosphere | LeagueApps | TeamLinkt |
| Automating low-value coordination | BenchApp | Spond | PlayMetrics |
| Persistent athlete history & development | GameChanger | PlayMetrics | Sprocket Sports |
| Organization intelligence & planning | PlayMetrics | TeamLinkt | OTTO SPORT / Demosphere |

These are pillar-specific overlaps, not overall product rankings.

---

## 8. Competitor lessons

### PlayMetrics

Probably the most important overall competitor to study.

Strong in:

- organization management;
- player profile;
- evaluations;
- tryouts;
- team formation;
- facilities;
- scheduling;
- family calendar;
- communication.

Less established relative to the thesis:

- family relationships used as operational constraints;
- generalized proactive resolution;
- cross-organization history;
- cross-sport identity;
- ride coordination.

If only one competitor is studied deeply first, PlayMetrics is the strongest candidate.

### TeamLinkt

Important because it combines:

- explicit Family entity;
- registration;
- league operations;
- AI rostering;
- schedule generation;
- official gamesheets;
- low organization pricing;
- free core product.

Its free family experience can include ads, with a paid plan removing them.

That pricing pattern is explicitly rejected for this product.

### OTTO SPORT / Demosphere

Strong in:

- persistent household/person identity;
- multiple guardians;
- durable person UUID;
- history;
- facility/schedule constraints;
- coach conflict handling.

It has a narrow version of:

```text
Detect conflict
→ try to resolve
→ mark unresolved if no valid solution
```

This is very close to the desired automation philosophy.

### LeagueApps

Strong in:

- Family Accounts;
- multiple guardians;
- multiple children;
- family calendar;
- team building;
- Player Reports;
- facilities;
- organization operations.

### GameChanger

Most serious athlete-history competitor.

Strong in:

- official game records;
- sport-specific stats;
- video/highlights;
- Career Profiles;
- cross-team career history.

Limitation: career history is still largely sport-specific.

### BenchApp

One of the biggest research surprises.

Already supports:

- ride-needed RSVP notes;
- carpool offers/requests;
- automatic spare-player invitations;
- automatic vacancy/waitlist filling;
- overdue fee reminders.

It strongly validates the proactive-coordination concept.

### Spond

Strong in:

- automatic RSVP reminders;
- event capacity;
- automatic waitlist replacement;
- claimable driving/food tasks;
- event coordination.

It also validates a transaction-funded business model.

### Sprocket Sports

Strong in:

- club-owned player history;
- Player Progress;
- evaluations;
- facility schedules;
- registration/payments;
- team operations.

Its history appears more club-owned than family-portable.

---

## 9. What is commodity

These are required but not strong differentiators by themselves:

- rosters;
- chat;
- announcements;
- schedules;
- RSVP;
- multiple children under one account;
- basic family calendar;
- registration;
- payments;
- league scheduling;
- basic team formation;
- volunteer signup;
- archived seasons;
- coach evaluations;
- basic stats.

---

## 10. Where differentiation may still exist

### Operational household graph

Not merely:

> This parent has three children.

But:

> These athletes share guardians, this guardian coaches another team, and this schedule creates an actual household conflict.

### Generalized resolution engine

Reusable:

```text
Detect
→ identify eligible people/resources
→ ask/offer
→ receive response
→ update state
→ retry
→ escalate
```

Possible uses:

- volunteer need;
- ride;
- spare player;
- optional practice;
- tournament;
- coach vacancy;
- open gym;
- payment exception;
- missing RSVP.

### Durable athlete sporting graph

```text
Athlete
├── Basketball
│   ├── Organization A
│   └── Organization B
└── Soccer
    └── ...
```

### Exception-based organization operations

Desired experience:

```text
42 routine items handled automatically.

4 need your attention.
```

Not:

```text
Here are 46 tasks for the admin.
```

---

## 11. Do not simply rebuild TeamSnap

The research suggests that rebuilding a generic youth-sports platform would be a poor use of time.

Before broad implementation:

1. Become an expert user of the strongest competitors.
2. Try real workflows.
3. Record repeated unresolved problems.
4. Build only where the strongest products still leave meaningful manual work.

Suggested file:

```text
unresolved-problems.md
```

Each entry should capture:

- workflow;
- actor;
- frequency;
- time cost;
- failure of existing tools;
- competitor comparison;
- potential reusable primitive.

---

# BUSINESS / COMPANY PHILOSOPHY

## 12. Company objective

The goal is **not** to maximize extraction from every user.

The initial goal is:

- build useful software;
- make it sustainable;
- generate side income;
- potentially grow enough one day to replace consulting income.

It is not initially intended to:

- maximize ARR at all costs;
- create artificial plans;
- hide useful capabilities behind tiers;
- use advertising as a monetization engine.

Working philosophy:

> **Make good software. Charge fairly. Do not make the product worse on purpose so people will pay to make it tolerable.**

---

## 13. No ads — absolute principle

Firm decision:

> **No ads. None. Ever.**

The product should not monetize family attention.

Checking a child's schedule is family infrastructure, not an advertising surface.

Unacceptable examples:

- ads in schedules;
- sponsored posts between team messages;
- interstitials while checking game location;
- targeted ads based on family/team behavior;
- creating an intentionally annoying free experience to sell ad removal.

If revenue is required, charge transparently somewhere else.

This should be a product/company invariant.

---

## 14. No artificial feature gating

Another firm philosophical direction:

> **Do not intentionally remove useful capabilities solely to manufacture upgrade pressure.**

The company is not anti-profit.

It is against manufactured scarcity.

Examples that would violate the philosophy:

```text
Sibling conflict detection → Enterprise only
Advanced calendar → Pro only
Multiple children → Family Premium
Volunteer automation → Business Plus
```

If a capability makes the core product better and does not create meaningful incremental operating cost, the preference is to include it.

The question should not be:

> How much can we charge for this feature?

It should be:

> Does this feature create real ongoing cost for the company?

---

## 15. Preferred business model

The preferred model has three revenue sources.

### 15.1 Transaction-funded core platform

Organizations use the complete core platform.

Revenue primarily comes from a small transparent percentage of money processed through the system.

Conceptually:

```text
Registration / program payments
        ↓
Small transaction fee
        ↓
Funds hosting, maintenance, development, support
```

This is similar in spirit to Spond.

Benefits:

- small organizations pay little;
- large organizations pay more;
- revenue grows with customer activity;
- no arbitrary SaaS plan selection;
- less friction than a large annual software invoice.

A figure around **3%** has been discussed conceptually, but is not final.

### 15.2 Optional supporter / cosmetic purchases

Families should never need these.

Examples:

- athlete themes;
- profile skins;
- cards;
- badges;
- icons;
- family themes;
- visual customization.

The positioning is:

> **Support the product and get something fun in return.**

Not:

> Pay or the app becomes unpleasant.

### 15.3 Usage-based charges for real marginal cost

If a capability materially increases operating cost, charging for it is reasonable.

Examples:

- video storage;
- video transcoding;
- large media libraries;
- AI film analysis;
- AI play-by-play analysis;
- compute-heavy optimization;
- high-volume SMS;
- expensive external APIs;
- unusually large storage/retention.

Working rule:

> **You are not paying because the feature is valuable. You are paying because using it costs the company meaningful money.**

---

## 16. Business-model summary

```text
Transactions fund the network.

Organizations receive the complete core operating system.

Families participate for free and see zero ads.

Optional cosmetic purchases let users support the company voluntarily.

Expensive storage/compute/AI is usage-funded.
```

---

## 17. Pricing philosophy

Avoid “Contact Sales” for normal customers.

Pricing should ideally be understandable without:

- sales calls;
- negotiation;
- artificial bundles;
- hidden modules;
- upsell-heavy demos.

A volunteer organization should be able to understand:

- what it costs;
- why it costs that;
- what happens as they grow.

---

## 18. Ads in competitor context

Advertising was explicitly tracked in the research.

Examples:

### TeamLinkt
Free family app can contain ads. A paid family plan removes them.

### Heja
Free tier is ad-supported. Paid plans can remove ads.

### GameChanger
Advertiser presence exists in the free ecosystem. Exact intrusiveness was not measured.

### TeamSnap
Legacy product explicitly uses targeted advertising and offers paid ad-free paths.

### Sprocket Sports
Supports sponsor placements, though this is not necessarily identical to generic third-party ad inventory.

For several other competitors, advertising was unverified. Unknown does not mean ad-free.

This reinforces the decision:

> **The product should be ad-free by design, not “ad-free if you pay.”**

---

## 19. Feasibility under this philosophy

This philosophy makes the project more attractive as a:

> **bootstrapped side-income SaaS**

than as a conventional venture-scale startup.

The success threshold is lower.

A meaningful outcome could be:

```text
5–10 organizations
→ software pays for itself
→ meaningful side income

20–30 organizations
→ substantial recurring income

100+ organizations
→ potentially a serious standalone company
```

The product does not need thousands of organizations on day one.

This fits the personal goal:

> Build something good first. If it eventually becomes large enough to replace consulting income, excellent.

---

## 20. Transaction economics

Illustrative gross fee at 3%:

| Annual payment volume | 3% gross fee |
|---:|---:|
| $100,000 | $3,000 |
| $250,000 | $7,500 |
| $500,000 | $15,000 |
| $1,000,000 | $30,000 |
| $3,000,000 | $90,000 |
| $5,000,000 | $150,000 |

Example:

```text
Organization payment volume: $250,000/year
Platform fee: 3%
Gross platform revenue: $7,500/year
```

Ten similar organizations:

```text
~$75,000/year gross
```

Twenty:

```text
~$150,000/year gross
```

This is before optional supporter purchases or metered features.

---

## 21. Important transaction-fee caveat

`GMV × 3%` is **not automatically profit**.

Two different models exist.

### Model A

```text
Platform fee
+
Payment processor fee
```

### Model B

```text
One blended transaction fee
```

Under Model B, the company pays processing costs out of its fee.

Real economics:

```text
Transaction revenue
- Card/ACH processing
- Refunds
- Chargebacks/disputes
- Payment infrastructure
- Hosting
- Support
= Actual margin
```

The final financial model must distinguish these.

---

## 22. Why this model may improve feasibility

### Lower adoption friction

Compare:

```text
$8,000/year software contract
```

with:

```text
Small transparent percentage when money is collected
```

The latter may be easier for volunteer organizations to accept.

### Natural alignment

Small organization:

- processes less;
- pays less.

Large organization:

- processes more;
- pays more.

Organization grows:

- platform revenue grows.

### Simpler product architecture

Traditional SaaS gating requires questions like:

```text
Does this org have Pro?
Can this user access evaluations?
What happens after downgrade?
Can they view but not edit?
```

The preferred model reduces much of this to:

```text
Does the user have permission?
```

Paid checks are mainly needed for truly metered resources:

```text
Does the account have available AI/video/storage usage?
```

---

## 23. Trust as a potential moat

The business philosophy is not the feature moat.

But it may become a **trust moat**.

Potential reputation:

> No ads.

> No stupid tiers.

> No hidden pricing.

> No sales call to discover the price.

> No intentionally crippled free experience.

> Pay a small amount when money moves.

> Pay for expensive compute/storage only when you actually consume it.

For volunteer-run sports organizations spending families' registration money, this may be meaningful.

---

## 24. Intentional tradeoff

This philosophy may reduce maximum revenue per customer.

That is acceptable.

Tradeoff:

```text
Possibly lower extraction per customer
```

in exchange for:

```text
Higher trust
Lower friction
Simpler pricing
Simpler product logic
Potentially stronger word-of-mouth
A product the founder personally respects
```

This is intentional.

---

## 25. Current feasibility conclusion

Do **not** pursue this as:

> another generic youth-sports management platform.

The market is too mature for that to be compelling.

The idea remains plausible as:

> **A family-centered youth-sports operating system built around proactive resolution, durable athlete identity, organization intelligence, transparent transaction-funded economics, and zero advertising.**

The research did not identify one competitor clearly combining all of:

- first-class family/household context;
- operational use of household relationships;
- generalized proactive workflow resolution;
- cross-sport / cross-organization athlete continuity;
- organization-wide resource intelligence;
- no-ad family participation;
- transparent low-friction economics.

Pieces exist across many products.

The combination remains the interesting part.

---

## 26. Recommended next strategic step

Before broad implementation, become an expert user of the strongest competitors.

Priority:

1. PlayMetrics
2. TeamLinkt
3. OTTO SPORT / Demosphere
4. BenchApp
5. Spond
6. GameChanger

Test real workflows:

- multi-child family setup;
- sibling conflicts;
- optional practice invitations;
- tournaments;
- carpool;
- volunteer duty;
- gym cancellation/reuse;
- coach staffing;
- season rollover;
- athlete history;
- evaluation history.

The key question is:

> **After giving the strongest competitor all the information it needs, what work am I still doing manually?**

That answer should determine the first product wedge.

---

## 27. Candidate first vertical slice

A useful first slice remains:

```text
Organization
  ↓
Family joins
  ↓
Multiple guardians + children
  ↓
Athlete joins team
  ↓
Event created
  ↓
Family calendar updates
  ↓
Guardian says:
“Yes, but needs a ride”
  ↓
Participation blocker created
  ↓
Platform attempts resolution
  ↓
Another approved guardian accepts
  ↓
Participation becomes confirmed
  ↓
Event/history persists
```

This exercises:

- person identity;
- family;
- athlete;
- team membership;
- events;
- calendar;
- RSVP;
- participation blockers;
- workflow engine;
- permissions;
- history.

It is a better architecture/product proof than starting with generic CRUD screens.

---

## 28. Company-principle draft

> **Build software people enjoy using. Charge where the economics require it, not where artificial scarcity can be manufactured. Never monetize family attention with advertising. Keep core functionality complete, make pricing transparent, let supporter purchases remain genuinely optional, and charge for storage/compute-heavy capabilities only when their use creates meaningful cost.**

Short form:

> **Useful first. Sustainable second. Extractive never.**

---

## 29. Internal origin story / north star

The product did not begin because a market category looked monetizable.

It began because:

> **A parent trying to find the time and location of a child's basketball game should not end up angry at their phone because the app is slow, fragmented, or showing yet another advertisement.**

When a business/product decision is proposed, ask:

> **Does this make the experience better for families, coaches, or volunteers—or are we intentionally making it worse because we think we can extract more money?**

If the answer is the latter, it conflicts with the company philosophy.

---

## 30. Existing project artifacts

Current/created project artifacts include:

```text
competitive-matrix-v1.1.md
competitor-research-prompt-v1.1.md
batch-competitor-research-work-prompt.md
competitive-synthesis-v1.md
product_overview.md
```

Independent competitor reports also exist for all researched products.

Future work should build on these rather than restart discovery.

---

## 31. Current decision record

| Question | Current direction |
|---|---|
| Build a TeamSnap clone? | No |
| Continue exploring the product? | Yes |
| Family-centered model? | Yes |
| Person as durable identity? | Yes |
| Persistent athlete identity? | Yes |
| Sport-agnostic foundation? | Yes |
| Basketball first proving ground? | Yes |
| Automation core to product? | Yes |
| Exception-based operations? | Yes |
| Cross-sport athlete identity long term? | Yes |
| Cross-org portability long term? | Yes, policy unresolved |
| Ads? | **Never** |
| Participation-critical family paywall? | No |
| Artificial feature gating? | Avoid |
| Transaction-funded core platform? | Preferred model to validate |
| Cosmetics/supporter purchases? | Yes, genuinely optional |
| AI/video/storage charges? | Yes when tied to real incremental cost |
| Opaque/custom pricing? | Avoid wherever possible |
| Venture-scale growth required? | No |
| Side-income / sustainable SaaS acceptable? | Yes |
| Replacing consulting someday? | Desired upside, not initial requirement |

---

## 32. Bottom line

The strongest version of the idea is no longer:

> **Build a better TeamSnap.**

It is:

> **Build youth-sports software that treats the family and athlete as durable entities, actively removes repetitive coordination work, helps organizations make better operational decisions, preserves sporting history, shows zero ads, avoids artificial feature gating, and funds itself through transparent transaction economics plus optional usage-based/supporter revenue.**

The opportunity is not that competitors are bad or featureless.

Many are strong.

The opportunity is that the market still appears fragmented across:

- family identity;
- athlete history;
- organization intelligence;
- proactive coordination;
- pricing philosophy;
- user trust.

The product thesis is the integration of those ideas into one coherent system.
