# Feature: Agent Triforce Plugin — Promotion and Monetization Plan
**Status**: Approved
**Priority**: P1-High
**Date**: 2026-02-23

---

## Problem Statement

Agent Triforce is a fully packaged, installable Claude Code plugin implementing a 3-agent development system (Prometeo PM, Forja Dev, Centinela QA) with a rigorous checklist methodology derived from *The Checklist Manifesto* (Atul Gawande) and Boeing's checklist engineering (Daniel Boorman). It applies WHO Surgical Safety Checklist pause points (SIGN IN / TIME OUT / SIGN OUT) to software development workflows.

The plugin was published on 2026-02-22 at `ArtemioPadilla/agent-triforce-template`. It is currently:
- Publicly accessible on GitHub
- Installable via `/plugin marketplace add ArtemioPadilla/agent-triforce-template`
- Unknown to the broader developer community

**The problem**: a high-quality, differentiated product exists with zero active distribution. Organic discovery in the Claude Code plugin ecosystem is low-probability without deliberate promotion. Meanwhile, the methodological angle (Gawande + Boeing applied to AI agents) is a genuinely unique positioning that is not being communicated.

**For whom**: Individual developers, engineering teams, and AI tooling enthusiasts who use Claude Code and want structured, reliable multi-agent workflows.

**Evidence of demand**:
- `wshobson/agents` has 73 plugins with meaningful GitHub traction
- `michael-harris/claude-code-multi-agent-dev-system` has 126 agents — indicating the market exists and is active
- Neither competitor uses a checklist-based safety methodology — the differentiation gap is real

---

## Success Metrics

### Phase 1 — Weeks 1-4
| KPI | Baseline | Target | Measurement |
|-----|----------|--------|-------------|
| GitHub stars | 0 | 100 | GitHub repo star count |
| GitHub forks | 0 | 15 | GitHub repo fork count |
| Directory listings | 0 | 4 | Manual tracking (awesome lists, buildwithclaude.com, Anthropic directory, claudemarketplaces.com) |
| Show HN points | N/A | 50+ | Hacker News submission score |

### Phase 2 — Months 1-3
| KPI | Baseline | Target | Measurement |
|-----|----------|--------|-------------|
| GitHub stars | 100 | 500 | GitHub |
| Plugin installs (estimated) | 0 | 200 | Proxy: forks + clone traffic via GitHub Insights |
| GitHub Sponsors revenue | $0 | $100/month | GitHub Sponsors dashboard |
| Consulting inquiries | 0 | 3 | Inbound contact (email/GitHub Discussions) |
| Newsletter subscribers | 0 | 200 | Substack subscriber count |

### Phase 3 — Months 3-6
| KPI | Baseline | Target | Measurement |
|-----|----------|--------|-------------|
| GitHub stars | 500 | 1,500 | GitHub |
| Monthly recurring sponsor revenue | $100 | $500 | GitHub Sponsors |
| Consulting revenue closed | $0 | $10K | CRM / invoice tracking |
| Product Hunt upvotes | N/A | 300+ | Product Hunt launch score |
| Conference / meetup talks | 0 | 1 | Calendar / CFP tracking |

### Phase 4 — Months 6-12
| KPI | Baseline | Target | Measurement |
|-----|----------|--------|-------------|
| GitHub stars | 1,500 | 3,000 | GitHub |
| Enterprise licensing deals | 0 | 2 | Contract tracking |
| Total annual revenue | $0 | $30K | Aggregate: sponsors + consulting + enterprise |
| Team training workshops delivered | 0 | 2 | Workshop booking records |

---

## User Stories

### Persona 1: Individual Developer
As an individual developer using Claude Code, I want to discover and install a reliable multi-agent workflow system, so that I can ship features with structured PM → Dev → QA discipline without manually managing agent coordination.

### Persona 2: Engineering Team Lead
As an engineering team lead evaluating AI tooling, I want a methodology-backed multi-agent system I can introduce to my team, so that we get consistent, auditable AI-assisted development practices rather than ad-hoc prompt engineering.

### Persona 3: AI Tooling Enthusiast
As someone active in the Claude Code community, I want to stay current with the best plugins and frameworks available, so that I can evaluate and recommend Agent Triforce to peers.

### Persona 4: Enterprise Engineering Manager
As an engineering manager at a company considering AI-augmented workflows, I want a supported, customizable multi-agent system with proven methodology, so that I can justify adoption with a credible foundation rather than experimental tooling.

---

## Acceptance Criteria

### Phase 1: Distribution Foundation

GIVEN the repository is public on GitHub,
WHEN the promotion phase 1 actions are complete,
THEN the repository has all 5 GitHub topics applied (`claude-code`, `multi-agent`, `developer-tools`, `prompt-engineering`, `checklist`), at least 3 curated list submissions are confirmed, and GitHub Sponsors is enabled with at least 3 defined tiers.

GIVEN a developer searches for "claude code multi-agent" on GitHub or Google,
WHEN phase 1 is complete,
THEN Agent Triforce appears in the first page of results for at least one relevant search query (measurable via manual spot check).

### Phase 2: Community Reach

GIVEN the Show HN post is submitted,
WHEN the submission receives engagement,
THEN it reaches 50+ points OR generates a minimum of 10 substantive comments about the methodology.

GIVEN a Substack newsletter is launched,
WHEN the first 3 issues are published,
THEN at least 200 subscribers have joined organically (no paid promotion).

### Phase 3: Revenue Initiation

GIVEN GitHub Sponsors is live with defined tiers,
WHEN monthly active GitHub star count exceeds 500,
THEN at least 3 sponsors are active at any tier.

GIVEN a consulting landing page is live,
WHEN a prospect reaches out via the page,
THEN they receive a response within 48 hours with a scoping questionnaire or initial call offer.

### Phase 4: Enterprise Readiness

GIVEN an enterprise licensing offering is defined,
WHEN an enterprise prospect requests a proposal,
THEN a documented proposal template exists covering: scope of work, custom agent configuration options, onboarding timeline, SLA terms, and pricing tiers.

---

## Scope

### In Scope
- GitHub repository optimization (topics, README, FUNDING.yml)
- Submission to curated lists and directories (awesome lists, buildwithclaude.com, Anthropic directory)
- Content marketing (Show HN, Reddit posts, Twitter/X thread)
- GitHub Sponsors setup with tier definitions
- Consulting offer definition (scope, pricing, delivery format)
- Product Hunt launch planning
- Newsletter strategy (Substack) — topic calendar and first 3 issue outlines
- Enterprise licensing offer definition
- Competitive positioning documentation
- Partnership outreach strategy (MCP server creators, AI newsletters)

### Out of Scope
- Paid advertising (Google Ads, Twitter Ads) — not appropriate at this stage; revisit at Phase 3
- Building a separate SaaS product or hosted version — the plugin model is the distribution strategy
- Redesigning the core Agent Triforce system — this plan is for the current v0.1.0 release
- Hiring / team expansion — solo maintainer operation throughout all phases
- Building a custom e-commerce or billing system — use GitHub Sponsors and Stripe-based consulting invoices

---

## Promotion Strategy

### Phase 1: Discovery Infrastructure (Week 1)
**Goal**: Make the repository findable before any active promotion.

**Actions (READ-DO in execution)**:
1. Apply GitHub topics: `claude-code`, `multi-agent`, `developer-tools`, `prompt-engineering`, `checklist`
2. Verify README has clear one-line description, install command, and methodology section above the fold
3. Add `FUNDING.yml` to repository root to enable GitHub Sponsors button
4. Enable GitHub Sponsors account with 3 tiers (see Monetization section)
5. Submit to `awesome-claude-code` list (GitHub PR)
6. Submit to `awesome-claude-code-plugins` list (GitHub PR)
7. Submit to `awesome-claude-plugins` list (GitHub PR)
8. Submit to `buildwithclaude.com` via their submission form
9. Submit to Anthropic official directory via `clau.de/plugin-directory-submission`
10. Verify `claudemarketplaces.com` has picked up the repository (auto-crawled, monitor within 72h)

**Success gate for Phase 2**: All 10 actions complete. At least 3 of 5 directory submissions confirmed accepted.

### Phase 2: Content Marketing (Weeks 2-4)
**Goal**: Reach developers who are not actively searching for this plugin but will recognize its value when they see it.

**Sequencing**: Show HN first (highest authority, sets narrative), then Reddit (broader reach), then Twitter/X (amplification).

**Action 1: Show HN Post**
- Timing: Tuesday or Wednesday, 9-11am US Eastern (peak HN traffic)
- Title: "Show HN: I applied Gawande's Checklist Manifesto and Boeing's checklist engineering to AI agents"
- Angle: Lead with the methodology problem (ineptitude failures in AI-assisted dev), not the product. The product is the proof of concept.
- Format: Short narrative explaining why PM/Dev/QA agents without checklists repeat the same failures, then show the SIGN IN / TIME OUT / SIGN OUT workflow on a concrete feature. Link to repo.
- Avoid: "I built a plugin" framing — this commoditizes it. The intellectual argument comes first.

**Action 2: r/ClaudeCode Post**
- Timing: 48 hours after Show HN (let HN results compound first)
- Title: "I implemented a full SIGN IN / TIME OUT / SIGN OUT workflow for Claude Code agents — here's what it looks like on a real feature"
- Format: Screen-capture or text walkthrough of Prometeo writing a spec, Forja implementing it, Centinela auditing — all with checkpoints. Show the MEMORY.md context carrying across sessions.
- Link to HN post for methodology credibility signal.

**Action 3: r/ClaudeAI crosspost**
- Crosspost the r/ClaudeCode post with a brief additional context paragraph for non-developer users.

**Action 4: Twitter/X Thread**
- Format: 8-10 tweet thread. Tweet 1 = hook (the ineptitude vs ignorance distinction from Gawande). Tweets 2-5 = the methodology. Tweets 6-8 = the three agents and their checklists. Tweet 9 = install command + link. Tweet 10 = open question to community ("What other checklist methodologies should we apply?")
- Target accounts to engage: AI coding newsletter writers, developer productivity accounts, Anthropic official account.

**Success gate for Phase 3**: Show HN 50+ points OR r/ClaudeCode post 100+ upvotes. Twitter thread 200+ impressions.

### Phase 3: Community Building (Months 2-3)
**Goal**: Build an audience that follows the methodology evolution, not just the tool.

**Action 1: Product Hunt Launch**
- Timing: Month 2, after GitHub star count exceeds 300 (social proof for PH algorithm)
- Hunter: Self-launch unless a known PH power user can be recruited
- Tagline: "The only Claude Code multi-agent system built on WHO surgical checklist methodology"
- Gallery: 3-5 screenshots of the dashboard, a short Loom demo, the workflow diagram
- Prep: Line up 20+ pre-committed upvoters from HN/Reddit communities before launch day

**Action 2: Substack Newsletter**
- Name: "Agent Triforce Dispatch" or "Checklist-Driven AI Development"
- Frequency: Bi-weekly
- First 3 issues planned:
  1. "Why AI agents fail (it's not the model)" — the ineptitude argument applied to Claude
  2. "The WHO Surgical Checklist was designed for people who already knew what they were doing" — deep dive on methodology
  3. "Anatomy of a real feature: PM → Dev → QA with full checkpoint trace"
- Monetization hook: Free tier for methodology content; paid tier ($8/month) for industry-specific checklist packs and advanced configuration guides

**Action 3: YouTube/Loom Demo Video**
- Single 8-12 minute video showing the complete PM → Dev → QA workflow on a real feature (e.g., implementing a simple REST endpoint)
- Structure: 2min methodology context, 6-8min live workflow, 2min install and getting started
- Post to YouTube with SEO-optimized description, embed in README and Substack

**Action 4: Cross-promotion with other plugin creators**
- Identify 5-10 complementary Claude Code plugins (task management, code review, documentation)
- Reach out with a "I'll mention yours if you mention mine" structure
- Specifically target MCP server plugins for Linear, GitHub, Stripe — their users are the Agent Triforce target persona

**Success gate for Phase 4**: Product Hunt 300+ upvotes. Substack 500+ subscribers. Newsletter open rate >40%. One confirmed cross-promotion partnership.

### Phase 4: Partnerships and Speaking (Months 3-6)
**Goal**: Establish authority as the definitive methodology for multi-agent AI development.

**Action 1: AI Coding Newsletter Outreach**
- Target publications with >5K developer subscribers
- Offer: an exclusive deep-dive article on the Gawande/Boeing angle in exchange for feature placement
- Suggested targets: TLDR AI, The Pragmatic Engineer, Pointer.io, AI Engineer newsletter

**Action 2: MCP Server Integration Partnerships**
- Reach out to Linear MCP, Stripe MCP, Notion MCP maintainers
- Proposal: Agent Triforce + their MCP = a complete end-to-end AI development stack. Co-market.
- Value to them: Agent Triforce users become MCP users; methodology adds credibility to their tool

**Action 3: Conference / Meetup Talks**
- CFP targets: AI Engineer Summit, local developer meetups with AI tracks, Claude/Anthropic developer events
- Talk title: "Surgical Checklists for AI Agents: What Boeing and the WHO Teach Us About Multi-Agent Systems"
- Talk structure: methodology theory, live demo, Q&A
- Slide deck to be published openly post-talk

**Action 4: GitHub Discussions Community**
- Enable GitHub Discussions on the repository
- Seed with 3-5 discussion threads: "Share your customizations", "Industry-specific checklist ideas", "Feature requests for v0.2"
- Respond to every thread within 24 hours for the first 3 months

---

## Monetization Strategy

### Phase 1: Foundation — GitHub Sponsors (Week 1)
**Goal**: Enable revenue capture immediately; even $50/month validates willingness to pay.

**Tier structure**:
| Tier | Monthly Price | Benefit | Target Persona |
|------|--------------|---------|----------------|
| Supporter | $5 | Name in README sponsors section | Individual developer, goodwill |
| Pro | $20 | Priority GitHub Issues response (48h SLA), early access to new releases | Active user |
| Studio | $100 | Monthly 30-min office hours call, logo in README, influence on roadmap | Small team or power user |

**Setup actions**:
- Add `FUNDING.yml` to repo root: `github: [ArtemioPadilla]`
- Enable GitHub Sponsors for the account
- Add sponsor CTA to README (above fold, after install instructions)

**Revenue projection**: 5 Supporter + 3 Pro + 1 Studio = $185/month at steady state (optimistic 3-month target)

### Phase 2: Consulting — Implementation Engagements (Months 1-2)
**Goal**: High-value revenue from teams wanting a white-glove setup.

**Offering**: "Agent Triforce implementation for your engineering team"
- Scope: Configure all 3 agents for team's tech stack and workflow, run 2-hour methodology workshop, deliver custom checklist pack for team's domain, 30-day async support
- Pricing:
  - Solo developer: $1,500 (2-3 hours async)
  - Small team (2-10 devs): $5,000 (half-day workshop + async support)
  - Medium team (10-50 devs): $12,000 (full-day workshop + custom agents + 30-day support)
  - Large team (50+ devs): $20,000+ (custom scope, multi-session, custom agents)
- Delivery: Fully remote; deliverables via GitHub PR to client repo

**Landing page requirements** (to be built by Forja):
- One-page site (GitHub Pages or Vercel) explaining the offer
- 3 testimonial slots (initially empty, fill after first 3 engagements)
- Contact form → email notification
- Link from README and Substack

**Lead generation**: Show HN + r/ClaudeCode + newsletter CTA pointing to landing page. Each content piece ends with "If your team wants this implemented: [link]"

### Phase 3: Premium Digital Products (Months 2-4)
**Goal**: Scalable revenue that does not require time-for-money exchange.

**Product 1: Industry Checklist Packs**
- Format: Additional `.claude/agents/*.md` files and `.claude/skills/*.md` files pre-configured for a vertical
- Verticals: Fintech (compliance, audit trails, PCI DSS considerations), Healthcare (HIPAA data handling, clinical validation), E-commerce (A/B testing discipline, cart/checkout edge cases), SaaS (subscription lifecycle, SLA management)
- Price: $49 per pack (one-time, instant download via Gumroad or Lemon Squeezy)
- Delivery: GitHub repo access (private) or zip download with setup instructions

**Product 2: Advanced Agent Configurations**
- Additional specialized agents: Data Engineer agent, DevOps/SRE agent, Legal/Compliance reviewer agent
- Price: $79 per agent configuration
- Delivery: Same as checklist packs

**Product 3: Paid Substack Tier**
- Price: $8/month or $80/year
- Content: Deep methodology guides, annotated real-world workflow traces, early access to new agent designs, "ask me anything" monthly thread
- Free tier remains: general methodology articles, show notes

**Revenue projection at Phase 3 steady state**:
- Sponsors: $300/month
- Consulting: 1 engagement/month avg $7,500 = $7,500 (variable)
- Digital products: 10 sales/month avg $60 = $600/month
- Paid newsletter: 50 subscribers × $8 = $400/month
- Total: ~$1,300 recurring + $7,500 variable = ~$8,800/month (optimistic scenario)

### Phase 4: Enterprise (Months 4-6)
**Goal**: Large ticket deals that justify continued investment in the product.

**Enterprise License Offering**:
- Private repository fork with enterprise SLA
- Quarterly custom agent updates aligned to team's evolving workflows
- Named support contact (the author) with 4-hour SLA on critical issues
- Annual all-hands methodology training session (remote)
- Custom agents for client's internal tools (Jira, Confluence, internal APIs)
- Pricing: $10,000-$50,000/year depending on team size and customization depth
- Contract minimum: 1-year

**Team Training Workshops**:
- 4-hour workshop: "Checklist-Driven AI Development for Engineering Teams"
- Format: Methodology theory (1h), live workflow demo (1h), hands-on configuration (1.5h), Q&A (30min)
- Price: $3,500 remote / $7,500 on-site (plus travel)
- Capacity: 5-20 participants

**Trigger for enterprise outreach**: When a company (identifiable from GitHub Discussions or Sponsors) has more than 5 developers on the same team using Agent Triforce, proactively reach out with an enterprise offer.

---

## Business Rules

1. **Methodology-first positioning**: Every piece of content must lead with the Gawande/Boeing intellectual argument before mentioning the product. The product is evidence, not the pitch.
2. **No paid amplification before organic validation**: Do not spend money on ads until the organic Show HN + Reddit posts demonstrate genuine user interest (50+ HN points or 100+ Reddit upvotes). Paid promotion of an unvalidated product is waste.
3. **Response SLA discipline**: GitHub Issues and Discussions responses within 48 hours (free users) and within 24 hours (sponsors). If this cannot be maintained, pause active promotion until it can be.
4. **Honest competitive comparison**: Never claim competitors are bad. Claim Agent Triforce is differentiated by methodology. The distinction is: others have more agents; Agent Triforce has better discipline.
5. **Consulting scope gate**: Do not take consulting engagements that require building net-new features in Agent Triforce as part of the engagement scope. Consulting is configuration and methodology, not product development. Exceptions require explicit prioritization decision.
6. **Version discipline**: Before any major promotion wave (Product Hunt, newsletter launch), ensure the current release is stable and the README install instructions are verified to work. A broken first impression is unrecoverable.
7. **Revenue diversification**: No single revenue stream should represent more than 60% of monthly revenue at steady state. Consulting dependency is the primary risk (see Risks section).
8. **Open core model**: The base framework stays MIT licensed and free forever. Monetization is through premium add-ons, consulting, and enterprise SLA — not by paywalling the core product.

---

## Data Requirements

### Tracking Setup Required
- **GitHub Insights**: Enable repository traffic tracking (clones, unique visitors, referring sites). Review weekly.
- **GitHub Sponsors**: Dashboard provides revenue and tier breakdown. Review monthly.
- **UTM parameters**: All links in newsletter, Show HN, Reddit posts to use UTM parameters to identify top traffic sources (e.g., `?utm_source=hackernews&utm_medium=show_hn`).
- **Substack analytics**: Open rate, click rate, subscriber growth. Export monthly for trend analysis.

### Privacy Considerations
- No user data is collected by the plugin itself — it is a local configuration tool
- Consulting clients: store only name, company, email, and engagement scope — no code or IP
- Newsletter: Substack handles GDPR/CAN-SPAM compliance; do not export subscriber lists to third parties
- GitHub Sponsors: GitHub handles payment data; no PCI obligations on maintainer

### Competitive Intelligence
- Monitor star velocity of `wshobson/agents` and `michael-harris/claude-code-multi-agent-dev-system` monthly
- Set GitHub notification for new Claude Code plugin submissions in awesome-claude-code lists
- Subscribe to AI coding newsletters being targeted for partnership to understand their editorial calendar

---

## Competitive Differentiation

### Competitive Landscape

| Competitor | Agents / Plugins | Differentiation Claim | Agent Triforce Counter |
|---|---|---|---|
| wshobson/agents | 73 plugins | Breadth — many specialized agents | Depth — disciplined multi-agent coordination |
| michael-harris/claude-code-multi-agent-dev-system | 126 agents | Scale — largest known multi-agent collection | Methodology — checklist-governed reliability |
| Generic multi-agent templates | N/A | Simplicity | Structure — PM/Dev/QA workflow discipline |

### Agent Triforce's Unique Position

**The core claim**: Agent Triforce is the only multi-agent Claude Code system built on a validated human-safety checklist methodology. Every other system focuses on quantity of agents or specialization of tasks. None address the fundamental failure mode: even the right agents, given the right context, will skip critical steps under pressure or when context is lost between sessions.

**Three differentiators that cannot be easily copied**:

1. **Methodological foundation**: The Gawande/Boeing framework is not a prompt trick. It is a philosophy about ineptitude vs ignorance, and how checklists address the former. A competitor can copy the format; they cannot copy the coherent theory behind it. The intellectual depth creates a moat.

2. **WHO Surgical Safety Checklist parallel**: SIGN IN / TIME OUT / SIGN OUT is borrowed from a system with documented lives-saved outcomes. The analogy to software development — where "ineptitude failures" (knowing what to do but not doing it) also cause harm — is a sticky intellectual hook that competitors will struggle to claim credibly after Agent Triforce owns it.

3. **Cross-session memory architecture**: The MEMORY.md system ensures each agent builds on prior decisions rather than starting fresh. This is architecturally more sophisticated than systems that treat each invocation as stateless.

**What we are NOT claiming**:
- Most agents (competitors have more)
- Most features (we are a discipline framework, not a feature set)
- Easiest to set up (complexity is a feature for the target persona who wants rigor)

---

## Dependencies

### Technical Dependencies
- Claude Code plugin marketplace infrastructure: the `/plugin marketplace add` command must remain available and stable. If Anthropic changes the plugin installation mechanism, the install instruction in all promotional materials must be updated within 24 hours.
- GitHub Sponsors: requires US-based bank account and tax documentation. Verify eligibility before Phase 1 completion.
- Gumroad or Lemon Squeezy account: required for digital product sales in Phase 3. Both have free tiers; setup estimated at 2 hours.

### Business Dependencies
- Awesome list maintainer responsiveness: curated list PRs are reviewed by volunteer maintainers on unpredictable timelines (days to weeks). Phase 2 content marketing should not be gated on list acceptance.
- Anthropic directory submission outcome: unknown review process and timeline. Plan assumes acceptance but Phase 1 success gate does not require it.
- Show HN timing: Hacker News front page ranking is probabilistic. A low-performing HN post (< 20 points) requires a strategy revision — see Non-Normal handling in Risks.

### Content Dependencies
- Loom/YouTube video: requires 2-4 hours production time. Must be complete before Product Hunt launch (Phase 3).
- Landing page: requires Forja implementation (half-day effort). Must be live before active consulting promotion begins.
- Three Substack issues: must be drafted and scheduled before newsletter launch announcement.

---

## Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Show HN underperforms (< 20 points) | Medium | Medium | Retry once with different framing after 3 weeks. Pivot to direct outreach to AI newsletter writers instead of HN-first. |
| Anthropic changes plugin marketplace mechanism | Low | High | Monitor Anthropic developer announcements weekly. Maintain a fallback "manual setup" install path in README that does not depend on the plugin command. |
| Consulting demand exceeds capacity (good problem) | Low-Medium | Medium | Define explicit booking limit (max 2 engagements/month). Maintain waitlist. Raise prices rather than hire, until $20K/month revenue justifies hiring. |
| Consulting demand is zero (bad problem) | Medium | High | Pivot consulting offer to asynchronous format (recorded video walkthrough + custom checklist pack delivered in 72 hours, $500 price point). Lower barrier to first sale. |
| Competitor copies the methodology framing | Medium | Low-Medium | The moat is the coherence of the argument and the quality of execution, not IP. Accelerate content output to establish thought leadership before a well-resourced competitor replicates. |
| Repository quality issues embarrass on launch | Low | High | Run `/code-health` scan before every promotion wave. All critical findings must be resolved. Warnings must be at least acknowledged in TECH_DEBT.md. |
| Substack subscriber growth stalls | Medium | Low | Focus on quality over quantity. 100 engaged subscribers who share is better than 1,000 passive ones. Measure forward rates and referrals, not just subscriber count. |
| GitHub Sponsors revenue is negligible for 6+ months | High | Low | Expected. Sponsors are a signal of engagement, not a primary revenue driver. Consulting and digital products carry the revenue strategy. |

---

## Rollback Criteria

This plan does not involve product changes — it is a marketing and distribution strategy. However, the following conditions should trigger a pause and reassessment:

- **Pause promotion if**: Two consecutive content pieces (Show HN + Reddit) each receive fewer than 20 points/upvotes with no meaningful comments. This indicates the messaging or positioning is not working, not just bad timing. Reassess positioning before further investment.
- **Pause consulting offer if**: First consulting engagement results in a dissatisfied client (subjective; any explicit complaint). Do not take a second engagement until root cause is understood and the delivery process is improved.
- **Pause digital product sales if**: Return rate exceeds 20% of purchases in the first 30 days. This indicates a product quality or expectation-setting problem. Pause, gather feedback, improve product before resuming.
- **Full strategy pause if**: Anthropic announces a major change to the Claude Code plugin architecture that makes the current packaging approach obsolete. Wait for architecture clarity before any further promotion.

---

## Open Questions

1. **Anthropic partnership**: Is there an official Anthropic developer relations program that would accelerate directory listing or provide a verified badge? Who is the contact?
2. **Plugin install tracking**: Is there any mechanism (even approximate) to estimate actual plugin installs vs GitHub clones? GitHub Insights provides traffic but not install-specific data.
3. **Substack vs Beehiiv**: Substack has better brand recognition but Beehiiv has more monetization control. Which platform is optimal for the paid newsletter tier?
4. **Consulting delivery format**: Is async-first (GitHub PRs + Loom videos) or synchronous (Zoom workshops) more valued by the target persona (engineering team leads)? Recommend a brief 3-question survey to the first 50 GitHub stargazers.
5. **Naming — "Agent Triforce" vs "Claude Triforce"**: The current brand is provider-agnostic ("Agent Triforce") but the primary use case is Claude Code. Does the name create confusion for users searching specifically for Claude Code solutions? (See CHANGELOG for rebrand rationale.)
6. **Repository naming**: The GitHub repo is currently `ArtemioPadilla/claude-triforce-template` but the product is branded "Agent Triforce". Is a repository rename to `agent-triforce-template` planned? This affects all install command documentation and curated list submissions.
7. **Legal**: Are there trademark or naming considerations for using "Triforce" in the product name (Nintendo IP)?

---

## Implementation Notes for Forja

The following technical deliverables are required to execute this plan:

1. **Landing page** (`docs/landing/` or separate repo): Single-page consulting offer page. GitHub Pages deployment. Contact form (Formspree or Netlify Forms). Priority: required before Phase 2 consulting promotion.
2. **FUNDING.yml**: Three-line file in repo root. Priority: Week 1.
3. **README enhancements**: Add GitHub Sponsors badge, add methodology summary section above fold, verify install command accuracy. Priority: Week 1.
4. **UTM link tracker**: Simple markdown file `docs/utm-links.md` listing all active UTM-tagged links for tracking. Priority: before Phase 2.
5. **GitHub Discussions**: Enable via repo settings. Seed with 3 opening threads. Priority: Month 2.

---

*Spec authored by Prometeo (PM) — 2026-02-23*
*Next review: 2026-03-23 (30-day post-Phase 1 assessment)*
