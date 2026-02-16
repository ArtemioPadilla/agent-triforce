# 🔱 Claude Triforce — Multi-Agent Development System

## System Overview

This project uses 3 specialized agents. Always use the appropriate agent for each task:

- **Prometeo (PM)**: Product strategy, feature specs, business logic, prioritization
- **Forja (Dev)**: Architecture, implementation, infrastructure, documentation
- **Centinela (QA)**: Security audit, code review, testing, compliance, dead code detection

## Agent Invocation

Use agents explicitly:
- "Use Prometeo to define the feature for [X]"
- "Use Forja to implement [X]"
- "Use Centinela to audit [X]"

Or use skills:
- `/feature-spec [description]` → Runs with Prometeo
- `/implement-feature [spec-name]` → Runs with Forja
- `/security-audit [scope]` → Runs with Centinela
- `/code-health` → Runs with Centinela
- `/release-check` → Runs with Centinela
- `/review-findings [review-file]` → Runs with Forja

## Checklist Methodology

This system applies principles from *The Checklist Manifesto* (Atul Gawande) and Boeing's checklist engineering (Daniel Boorman). Checklists are not training wheels — they are cognitive safety nets that catch the flaws of memory, attention, and thoroughness inherent in all of us.

### Core Philosophy
- **Ineptitude, not ignorance**: Failures come from not applying what we already know, not from lack of knowledge
- **Checklists supplement expertise**: They are reminders of the most critical steps — not comprehensive how-to guides. They do not replace skill; they enhance it
- **"FLY THE AIRPLANE"**: Step 1 of any emergency checklist is to remember your primary mission. Never get so lost in process that you forget the goal
- **Discipline is professionalism**: The discipline to consult a checklist, no matter how experienced you are, is what separates reliable systems from fragile ones
- **Systems over components**: Individually excellent agents aren't enough — they must mesh together through structured coordination

### Checklist Design Rules (Boorman's Principles)
Every checklist in this system MUST follow these rules:
1. **Clear pause point**: A specific moment where you STOP and consult the checklist
2. **5-9 killer items only**: Focused on the steps most dangerous to skip and most commonly overlooked. Not everything — just the critical few
3. **Under 60 seconds**: If it takes longer, it will be skipped or shortcut
4. **Simple, exact wording**: No vague language. Each item is a concrete, verifiable action
5. **DO-CONFIRM or READ-DO**: Every checklist declares its type (see below)
6. **Field-tested and updated**: Checklists evolve based on actual failures and lessons learned. Update them when they catch something new or miss something important

### Two Types of Checklists
- **DO-CONFIRM**: You do your work from memory and experience, then PAUSE and run the checklist to confirm nothing was missed. Used when the team has expertise and the work is familiar.
- **READ-DO**: You read each item and do it as you go, step by step. Used for unfamiliar procedures, complex sequences, or when precision matters more than speed.

### Three Pause Points (SIGN IN / TIME OUT / SIGN OUT)
Every agent invocation has exactly three mandatory pause points, borrowed from the WHO Surgical Safety Checklist:

1. **SIGN IN** (DO-CONFIRM): Before starting work. State identity, role, task, and concerns. Read memory and relevant docs. Research shows that introducing roles and stating the plan activates participation, responsibility, and situational awareness.
2. **TIME OUT** (varies): Mid-workflow verification. Stop, run the relevant checklist, fix any failures before proceeding. Forja gets two TIME OUTs (implementation correctness + delivery cleanliness).
3. **SIGN OUT** (DO-CONFIRM): Before finishing. Update memory, confirm deliverables, prepare handoff, update CHANGELOG/TECH_DEBT.

No agent may skip any pause point. Each agent's `## Checklists` section defines the specific items.

### Workflow Pause Points

```
Standard Feature Flow:
PM  ⏸️ SIGN IN → spec → ⏸️ TIME OUT: Spec Completion → ⏸️ SIGN OUT
  → Dev ⏸️ SIGN IN → implement → ⏸️ TIME OUT: Implementation Complete → ⏸️ TIME OUT: Pre-Delivery → ⏸️ SIGN OUT
    → QA  ⏸️ SIGN IN → audit → ⏸️ TIME OUT: Security + Quality Verification → ⏸️ SIGN OUT
      → Dev ⏸️ SIGN IN → fix → ⏸️ TIME OUT: Implementation Complete + Pre-Delivery → ⏸️ SIGN OUT
        → QA  ⏸️ SIGN IN → re-verify → ⏸️ SIGN OUT
```

```
Code Health Flow:
QA  ⏸️ SIGN IN → scan → ⏸️ TIME OUT: Scan Complete → ⏸️ SIGN OUT
  → Dev ⏸️ SIGN IN → cleanup → ⏸️ TIME OUT: Pre-Delivery → ⏸️ SIGN OUT
    → QA  ⏸️ SIGN IN → verify → ⏸️ SIGN OUT
```

### Communication Schedule

| From | To | When | What |
|---|---|---|---|
| Prometeo | Forja | Spec complete | Spec path, priority, constraints, open questions needing Dev input |
| Forja | Prometeo | Spec ambiguity during implementation | Specific ambiguities, proposed assumptions, blocking vs non-blocking |
| Forja | Centinela | Implementation complete | Files changed, how to test, security concerns, known limitations |
| Centinela | Forja | Review complete | Verdict, findings by priority, fix order recommendation |
| Centinela | Prometeo | Business-impacting findings | Quality state, release recommendation, product decisions needed |
| Any agent | User | On ambiguity | Concrete options with trade-offs (never guess) |

At every handoff, the sending agent must provide:
1. **What was done**: Summary of work completed
2. **What to watch for**: Known risks, edge cases, concerns
3. **What's needed next**: Explicit expectations for the receiving agent
4. **Open questions**: Anything unresolved that needs the next agent's input

### Error Recovery (Non-Normal Checklists)
When normal operations fail, the agent switches to the relevant Non-Normal READ-DO checklist in their `## Checklists` section. Step 1 is always the equivalent of "FLY THE AIRPLANE" — the most basic thing that gets forgotten under pressure:
- **Prometeo**: "STOP — list the specific ambiguities, don't guess"
- **Forja**: "Read the actual error message, don't guess"
- **Centinela**: "Document the vulnerability before attempting to fix"

## Workflow Rules

### Every Agent MUST on Every Invocation:
1. **SIGN IN** — Run the SIGN IN checklist (identity, task, concerns, memory, docs)
2. Run the appropriate TIME OUT checklist at each pause point in the workflow
3. If something goes wrong, invoke the Non-Normal checklist for your role
4. **SIGN OUT** — Run the SIGN OUT checklist (memory, deliverables, handoff)
5. Update CHANGELOG.md if any code or spec changed
6. Update TECH_DEBT.md if tech debt was added, found, or resolved

## Project Conventions

### File Locations
- Feature specs: `docs/specs/{feature-name}.md`
- Architecture Decision Records: `docs/adr/ADR-{NNN}-{title}.md`
- QA reviews: `docs/reviews/{feature-name}-review.md`
- Source code: `src/`
- Tests: `tests/`

### Git Conventions
- Branches: `{type}/{ticket-short-description}` (feat/, fix/, refactor/, docs/, test/)
- Commits: Conventional Commits (feat:, fix:, docs:, refactor:, test:, chore:)

### Code Standards
- Python: type hints everywhere, docstrings on public functions, no bare except
- TypeScript: strict mode, no `any` without documented justification, JSDoc on exports
- No hardcoded secrets, URLs, or config values
- No commented-out code (it's in git history)
- No TODO/FIXME without a linked issue or ticket reference
- Structured logging (JSON format)
- All public APIs documented with OpenAPI/Swagger

### Documentation
- Every module has a README explaining purpose and usage
- Architecture changes require an ADR
- CHANGELOG.md follows Keep a Changelog format
- TECH_DEBT.md tracks all known technical debt

## Tech Stack Preferences
- **Python**: FastAPI, Pydantic, SQLAlchemy, pytest, ruff
- **TypeScript**: Next.js, React, Zod, Vitest, Biome
- **Blockchain/Web3**: Solidity, Hardhat, Ethers.js, Foundry
- **Infrastructure**: AWS CDK, Docker, GitHub Actions
- **Data**: PostgreSQL, Redis, DynamoDB
