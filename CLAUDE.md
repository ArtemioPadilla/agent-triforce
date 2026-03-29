# 🔱 Agent Triforce — Multi-Agent Development System

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
- `/business-review [feature-name]` → Runs with Prometeo

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

#### Standard Feature Flow

```dot
digraph standard_feature_flow {
    rankdir=TB;
    node [shape=box];

    subgraph cluster_pm {
        label="Prometeo (PM)";
        style=dashed;
        pm_signin [label="SIGN IN" shape=doublecircle];
        pm_spec [label="Write spec"];
        pm_timeout [label="TIME OUT:\nSpec Completion" shape=doublecircle];
        pm_signout [label="SIGN OUT" shape=doublecircle];
        pm_signin -> pm_spec -> pm_timeout -> pm_signout;
    }

    subgraph cluster_dev1 {
        label="Forja (Dev)";
        style=dashed;
        dev_signin [label="SIGN IN" shape=doublecircle];
        dev_impl [label="Implement"];
        dev_timeout1 [label="TIME OUT:\nImpl Complete" shape=doublecircle];
        dev_timeout2 [label="TIME OUT:\nPre-Delivery" shape=doublecircle];
        dev_signout [label="SIGN OUT" shape=doublecircle];
        dev_signin -> dev_impl -> dev_timeout1 -> dev_timeout2 -> dev_signout;
    }

    subgraph cluster_qa1 {
        label="Centinela (QA)";
        style=dashed;
        qa_signin [label="SIGN IN" shape=doublecircle];
        qa_audit [label="Audit"];
        qa_timeout [label="TIME OUT:\nSecurity + Quality" shape=doublecircle];
        qa_signout [label="SIGN OUT" shape=doublecircle];
        qa_signin -> qa_audit -> qa_timeout -> qa_signout;
    }

    subgraph cluster_dev2 {
        label="Forja (Fix Cycle)";
        style=dashed;
        dev2_signin [label="SIGN IN" shape=doublecircle];
        dev2_fix [label="Fix findings"];
        dev2_timeout [label="TIME OUT:\nImpl + Pre-Delivery" shape=doublecircle];
        dev2_signout [label="SIGN OUT" shape=doublecircle];
        dev2_signin -> dev2_fix -> dev2_timeout -> dev2_signout;
    }

    subgraph cluster_qa2 {
        label="Centinela (Re-verify)";
        style=dashed;
        qa2_signin [label="SIGN IN" shape=doublecircle];
        qa2_verify [label="Re-verify"];
        qa2_signout [label="SIGN OUT" shape=doublecircle];
        qa2_signin -> qa2_verify -> qa2_signout;
    }

    pm_signout -> dev_signin [label="handoff"];
    dev_signout -> qa_signin [label="handoff"];
    qa_signout -> dev2_signin [label="findings"];
    dev2_signout -> qa2_signin [label="fixes"];
}
```

#### Code Health Flow

```dot
digraph code_health_flow {
    rankdir=TB;
    node [shape=box];

    subgraph cluster_qa {
        label="Centinela (QA)";
        style=dashed;
        qa_signin [label="SIGN IN" shape=doublecircle];
        qa_scan [label="Scan"];
        qa_timeout [label="TIME OUT:\nScan Complete" shape=doublecircle];
        qa_signout [label="SIGN OUT" shape=doublecircle];
        qa_signin -> qa_scan -> qa_timeout -> qa_signout;
    }

    subgraph cluster_dev {
        label="Forja (Dev)";
        style=dashed;
        dev_signin [label="SIGN IN" shape=doublecircle];
        dev_cleanup [label="Cleanup"];
        dev_timeout [label="TIME OUT:\nPre-Delivery" shape=doublecircle];
        dev_signout [label="SIGN OUT" shape=doublecircle];
        dev_signin -> dev_cleanup -> dev_timeout -> dev_signout;
    }

    subgraph cluster_qa2 {
        label="Centinela (Verify)";
        style=dashed;
        qa2_signin [label="SIGN IN" shape=doublecircle];
        qa2_verify [label="Verify"];
        qa2_signout [label="SIGN OUT" shape=doublecircle];
        qa2_signin -> qa2_verify -> qa2_signout;
    }

    qa_signout -> dev_signin [label="findings"];
    dev_signout -> qa2_signin [label="fixes"];
}
```

### Communication Schedule

| From | To | When | What |
|---|---|---|---|
| Prometeo | Forja | Spec complete | Spec path, priority, constraints, open questions needing Dev input |
| Forja | Prometeo | Spec ambiguity during implementation | Specific ambiguities, proposed assumptions, blocking vs non-blocking |
| Forja | Centinela | Implementation complete | Files changed, test manifest (coverage, AC mapping), security concerns, known limitations |
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

## Software Engineering Principles

These principles guide all agents. They are a shared design compass — not rigid rules.

### Specifications (IEEE 830 + INVEST)
- Specs use tiered templates: **S** (bug fix, 5 sections), **M** (standard feature, 14 sections), **L** (epic, 19 sections)
- Every user story passes **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable
- Acceptance criteria use **GIVEN/WHEN/THEN** format
- Quality attributes: complete, consistent, unambiguous, verifiable, traceable

### Architecture (Clean Architecture — Robert C. Martin)
- **Dependency Rule**: dependencies point inward (entities → use cases → adapters → frameworks)
- **Screaming Architecture**: folder structure reveals intent, not framework
- **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion

### Development (TDD — Kent Beck + Clean Code — Robert C. Martin)
- **Red-Green-Refactor**: failing test → minimal code to pass → refactor for clarity
- **Small functions**: one thing, one level of abstraction, <30 lines
- **Meaningful names**: intention-revealing, no noise words, no abbreviations
- **DRY, YAGNI, KISS**: don't repeat, don't build unneeded things, keep it simple
- **Error handling**: prefer exceptions over null returns, fail fast

### Testing (FIRST Principles + IEEE 829 Test Design)
- **Fast, Isolated, Repeatable, Self-validating, Timely**
- **Arrange-Act-Assert** pattern for every test
- Unit tests for business logic (>80% coverage), integration tests for critical paths, e2e for user flows
- No test logic: no if/else or loops in test code
- **Test design techniques** (select based on code characteristics):
  - **Boundary Value Analysis (BVA)**: for numeric inputs, ranges, limits — test at min, max, min-1, max+1
  - **Equivalence Partitioning (EP)**: for categorical inputs (roles, statuses, types) — one test per valid class, one per invalid
  - **Decision Tables**: for complex branching, permission matrices, multi-condition logic — one test per condition combination
  - **State Transition**: for lifecycle objects (order states, workflow steps) — test each valid transition + key invalid ones
- **Test case IDs**: every test docstring includes `TC-{feature}-{NNN}` and `Verifies: {feature}-AC-{NNN}` for traceability
- **Integrity levels** (proportional to spec tier):
  - Tier S: happy-path + one edge case per change. BVA/EP only if boundary-related
  - Tier M: full technique-driven test suite. Every AC explicitly linked. Coverage >80%
  - Tier L: all of Tier M + state transition for workflows + decision tables for permission matrices + integration test plan

### Refactoring (Martin Fowler)
- Extract Method, Rename, Move, Inline — the everyday toolkit
- Code smells: long method, feature envy, data clump, primitive obsession, god class
- **Boy Scout Rule**: leave code better than you found it

### Other
- **12-Factor App**: config in environment, backing services, disposability, dev/prod parity
- **Design Patterns (GoF)**: favor composition over inheritance, program to interfaces

## Project Conventions

### File Locations
- Feature specs: `docs/specs/{feature-name}.md`
- Architecture Decision Records: `docs/adr/ADR-{NNN}-{title}.md`
- QA reviews: `docs/reviews/{feature-name}-review.md`
- Business reviews: `docs/reviews/business-review-{feature}-{date}.md`
- Source code: `src/`
- Tests: `tests/`
- Test strategy template: `templates/test-strategy.md`

### Git Conventions
- Branches: `{type}/{ticket-short-description}` (feat/, fix/, refactor/, docs/, test/)
- Commits: Conventional Commits (feat:, fix:, docs:, refactor:, test:, chore:)

### Code Standards
- Python: type hints everywhere, docstrings on public functions, no bare except
- TypeScript: strict mode, no `any` without documented justification, JSDoc on exports
- Functions <30 lines, one level of abstraction, meaningful names
- No hardcoded secrets, URLs, or config values
- No commented-out code (it's in git history)
- No TODO/FIXME without a linked issue or ticket reference
- Prefer exceptions over null returns for error handling
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
