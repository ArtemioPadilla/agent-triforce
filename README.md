# Agent Triforce

A 3-agent development system (PM / Dev / QA) with checklist methodology for production-grade software development. Powered by [Claude Code](https://code.claude.com).

## Install

### As a Plugin (add to any existing project)

```bash
/plugin marketplace add ArtemioPadilla/agent-triforce-template
/plugin install agent-triforce@agent-triforce
/agent-triforce:setup    # scaffold project directories
```

### As a Template (start a new project)

```bash
gh repo create my-project --template ArtemioPadilla/agent-triforce-template
cd my-project
claude
```

## Agents

| Agent | Name | Role | Model | Mode |
|-------|------|------|-------|------|
| PM | **Prometeo** | Product specs, business logic, prioritization | Sonnet | Plan (read-only) |
| Dev | **Forja** | Architecture, implementation, testing, docs | Inherit | Accept Edits |
| QA | **Centinela** | Security, code review, compliance, dead code | Sonnet | Default |

## Skills

| Skill | Agent | What it does |
|-------|-------|-------------|
| `/feature-spec` | Prometeo | Create a feature specification |
| `/implement-feature` | Forja | Implement a feature from its spec |
| `/review-findings` | Forja | Fix findings from a QA review |
| `/security-audit` | Centinela | Deep OWASP security audit |
| `/code-health` | Centinela | Dead code, tech debt, dependency scan |
| `/release-check` | Centinela | Pre-release verification gate |

When installed as a plugin, skills are namespaced: `/agent-triforce:feature-spec`, etc.

## Workflow

```
/feature-spec → /implement-feature → /security-audit → /review-findings → repeat
```

```
PM  SIGN IN → spec → TIME OUT → SIGN OUT
  → Dev SIGN IN → implement → TIME OUT → TIME OUT → SIGN OUT
    → QA  SIGN IN → audit → TIME OUT → SIGN OUT
      → Dev SIGN IN → fix → SIGN OUT
        → QA  SIGN IN → verify → SIGN OUT
```

## Methodology

This system applies principles from *The Checklist Manifesto* (Atul Gawande) and Boeing's checklist engineering (Daniel Boorman), structured around the WHO Surgical Safety Checklist.

**Core ideas:**
- **Checklists supplement expertise** — reminders of the most critical steps, not how-to guides
- **FLY THE AIRPLANE** — step 1 of any emergency is to remember your primary mission
- **Three pause points** per agent invocation: **SIGN IN** (before work), **TIME OUT** (mid-workflow verification), **SIGN OUT** (before handoff)
- **Two types**: DO-CONFIRM (verify after work) and READ-DO (step-by-step for handoffs and error recovery)
- **24 checklists, 117 items** across 3 agents. No checklist exceeds 9 items.

## Project Structure

```
.
├── CLAUDE.md                          # System rules & conventions
├── CHANGELOG.md                       # Keep a Changelog format
├── TECH_DEBT.md                       # Technical debt register
├── .claude/
│   ├── agents/
│   │   ├── prometeo-pm.md             # PM agent
│   │   ├── forja-dev.md               # Dev agent
│   │   └── centinela-qa.md            # QA agent
│   └── skills/                        # 6 skill definitions
├── plugins/
│   └── agent-triforce/               # Plugin marketplace package
│       ├── .claude-plugin/plugin.json
│       ├── agents/                    # symlinks → .claude/agents/
│       ├── skills/                    # symlinks → .claude/skills/
│       ├── commands/                  # setup, methodology, dashboard
│       └── hooks/hooks.json           # auto-regenerate dashboard
├── tools/
│   └── dashboard.py                   # HTML/terminal system dashboard
├── docs/
│   ├── specs/                         # Feature specifications (PM)
│   ├── adr/                           # Architecture Decision Records (Dev)
│   └── reviews/                       # Code reviews & audits (QA)
├── src/                               # Source code
└── tests/                             # Tests
```

## Key Features

- **Persistent Memory**: Each agent remembers decisions across sessions
- **Auto-formatting**: Dev agent auto-runs ruff/biome after every file edit
- **Permission Enforcement**: PM can't edit code (plan mode), QA is read-only by default
- **System Dashboard**: HTML dashboard auto-generated after every agent session
- **Dead Code Detection**: QA scans for dead code on every review
- **Structured Handoffs**: Communication schedule with 6 defined handoff paths between agents

## Customization

| What | Where |
|------|-------|
| Tech stack preferences | `CLAUDE.md` → Tech Stack Preferences |
| Agent behavior | `.claude/agents/{agent-name}.md` |
| Add new skills | `.claude/skills/{skill-name}/SKILL.md` |
| Project-specific rules | `CLAUDE.md` or `.claude/rules/` |

## Requirements

- [Claude Code](https://code.claude.com) v2.1.32+
- Claude Max or Pro subscription (or API key)

> **Note**: Agent Triforce is a provider-agnostic methodology. The checklist framework, agent roles, and workflows are portable to other AI coding tools as they mature to support multi-agent orchestration.

## License

[MIT](LICENSE)
