---
description: Interactive setup wizard for Agent Triforce — detects tech stack, creates project structure, and configures agents
---

# Agent Triforce — Interactive Setup Wizard

Set up or reconfigure an Agent Triforce project. This wizard detects your tech stack, creates the required directory structure, generates starter files, and optionally configures MCP server connections.

**Goal**: Go from zero to first spec in under 5 minutes.

## Step 1 — Detect Existing Configuration

Check if the project has already been set up:

1. Look for existing `CLAUDE.md`, `docs/` directory, and `.claude/agents/` files
2. If ALL exist:
   - Inform the user: "This project already has an Agent Triforce configuration."
   - Ask: "Would you like to (A) reconfigure tech stack preferences only, or (B) run full setup (will not overwrite existing specs, reviews, or memory files)?"
   - If reconfigure: skip to Step 3 (tech stack detection), then Step 6 (CLAUDE.md update), then Step 9 (summary)
   - If full setup: continue from Step 2 but check before overwriting each file
3. If NONE exist: proceed with full setup from Step 2

## Step 2 — Create Directory Structure

For each directory below, check if it already exists before creating it. Never overwrite existing content.

**Directories:**
1. `docs/specs/` — feature specifications (Prometeo output)
2. `docs/reviews/` — QA review reports (Centinela output)
3. `docs/adr/` — architecture decision records (Forja output)
4. `src/` — source code
5. `tests/` — test files

## Step 3 — Detect Tech Stack

Scan the project root for manifest files and infer the tech stack:

| File | Stack |
|------|-------|
| `package.json` | Node.js / TypeScript / JavaScript |
| `pyproject.toml` or `requirements.txt` or `setup.py` | Python |
| `Cargo.toml` | Rust |
| `go.mod` | Go |
| `pom.xml` or `build.gradle` | Java / Kotlin |
| `Gemfile` | Ruby |
| `composer.json` | PHP |
| `*.sol` files in project | Solidity / Web3 |

Additionally detect:
- **Framework**: Check `package.json` dependencies for Next.js, React, Vue, Express, etc. Check `pyproject.toml` for FastAPI, Django, Flask, etc.
- **Test framework**: pytest, vitest, jest, mocha, cargo test, go test
- **Linter/formatter**: ruff, biome, eslint, prettier, rustfmt, gofmt

Present the detected stack to the user:
```
Detected tech stack:
  Language(s): Python, TypeScript
  Frameworks: FastAPI, Next.js
  Test runners: pytest, Vitest
  Linters: ruff, Biome
```

Ask the user to **confirm or correct** before proceeding. If nothing was detected, ask the user to describe their stack.

## Step 4 — Create Starter Files

Create each file ONLY if it does not already exist. Never overwrite.

**CHANGELOG.md:**
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

### Added

### Changed

### Fixed

### Security

### Removed
```

**TECH_DEBT.md:**
```markdown
# Technical Debt Register

Track all known technical debt. Updated by both Dev (Forja) and QA (Centinela) agents.

## Active Debt

<!-- Use this format for each debt item:

### [TD-{NNN}] {Short description}
- **Type**: Design | Code | Test | Infra | Security | Dependency
- **Severity**: Critical | High | Medium | Low
- **Found**: {YYYY-MM-DD}
- **Estimated effort**: {hours or T-shirt size}
- **Impact if not fixed**: {what happens}
- **Proposed fix**: {approach}

-->

## Resolved Debt

<!-- Move items here when fixed, add resolution date and how it was resolved -->
```

## Step 5 — Configure .gitignore

Append the following to `.gitignore` if not already present (check before appending):

```
# Agent Triforce — agent memory (session-specific, not shared)
.claude/agent-memory/
```

## Step 6 — Generate Starter CLAUDE.md

Create `CLAUDE.md` ONLY if it does not already exist. If it exists, ask before updating the tech stack section.

Use the detected (or user-confirmed) tech stack to populate the `## Tech Stack Preferences` section. The starter CLAUDE.md should include:

```markdown
# {Project Name} — Agent Triforce Configuration

## System Overview

This project uses the Agent Triforce multi-agent development system:
- **Prometeo (PM)**: Product strategy, feature specs, business logic
- **Forja (Dev)**: Architecture, implementation, testing, documentation
- **Centinela (QA)**: Security audit, code review, compliance

## Agent Invocation

- "Use Prometeo to define the feature for [X]"
- "Use Forja to implement [X]"
- "Use Centinela to audit [X]"

Or use skills:
- `/feature-spec [description]` — Create a feature specification
- `/implement-feature [spec-name]` — Implement a feature from its spec
- `/security-audit [scope]` — Run a security audit
- `/code-health` — Scan for dead code and tech debt
- `/release-check` — Pre-release verification gate
- `/review-findings [review-file]` — Fix QA review findings

## Tech Stack Preferences

{Populated from detected/confirmed stack. Example:}

- **Language**: Python 3.12, TypeScript 5.x
- **Frameworks**: FastAPI, Next.js 14
- **Testing**: pytest, Vitest
- **Linting**: ruff, Biome
- **Infrastructure**: Docker, GitHub Actions
- **Database**: PostgreSQL

## Project Conventions

### File Locations
- Feature specs: `docs/specs/{feature-name}.md`
- Architecture Decision Records: `docs/adr/ADR-{NNN}-{title}.md`
- QA reviews: `docs/reviews/{feature-name}-review.md`
- Source code: `src/`
- Tests: `tests/`

### Git Conventions
- Branches: `{type}/{short-description}` (feat/, fix/, refactor/, docs/, test/)
- Commits: Conventional Commits (feat:, fix:, docs:, refactor:, test:, chore:)

### Code Standards
- Functions <30 lines, one level of abstraction, meaningful names
- No hardcoded secrets, URLs, or config values
- No commented-out code (it belongs in git history)
- Prefer exceptions over null returns for error handling
```

## Step 7 — Optional MCP Server Connections

Ask the user if they want to configure optional MCP server integrations:

> "Would you like to configure any MCP server connections? These are optional and can be set up later."
>
> Available integrations:
> 1. **SonarQube** — static analysis metrics for Centinela reviews
> 2. **Linear** — issue tracker integration for all agents
> 3. **GitHub Issues** — issue tracking via GitHub's API
> 4. Skip for now

If the user **declines**, add this section to CLAUDE.md:
```markdown
## MCP Configuration (Not Set Up)

MCP server integrations are available but not configured. To set up later:
- **SonarQube**: Add SonarQube MCP server to `.mcp.json` for static analysis data in Centinela reviews
- **Linear**: Add Linear MCP server to `.mcp.json` for issue tracker integration
- **GitHub Issues**: Add GitHub MCP server to `.mcp.json` for issue tracking
```

If the user **accepts** any integration, guide them through providing the configuration and add the MCP server entries to `.mcp.json`. Do NOT collect or store API keys directly -- instruct users to set them as environment variables.

## Step 8 — Optional Agent Routing Configuration

Ask the user if they want to create a `.agent-routing.json` file with model preferences:

> "Would you like to configure agent model routing? This assigns different Claude models to different task types for cost efficiency."

If accepted, create `.agent-routing.json`:
```json
{
  "routing": {
    "code-health": { "model": "haiku", "note": "Routine scan, cost-efficient" },
    "security-audit": { "model": "sonnet", "note": "Thorough analysis needed" },
    "feature-spec": { "model": "sonnet", "note": "Balanced capability and cost" },
    "implement-feature": { "model": "sonnet", "note": "Standard implementation" },
    "release-check": { "model": "sonnet", "note": "Thorough verification needed" },
    "complex-architecture": { "model": "opus", "note": "High-capability for complex decisions" }
  }
}
```

If declined, skip. This can be configured later.

## Step 9 — Summary Report

After all steps complete, report:

```
Agent Triforce Setup Complete
=============================

Directories:
  [created] docs/specs/
  [created] docs/reviews/
  [created] docs/adr/
  [exists]  src/
  [created] tests/

Files:
  [created] CLAUDE.md
  [created] CHANGELOG.md
  [created] TECH_DEBT.md
  [updated] .gitignore

Tech Stack: Python (FastAPI, pytest, ruff), TypeScript (Next.js, Vitest, Biome)

MCP Integrations: None configured (run /setup to add later)
Agent Routing: Default (all agents use inherited model)

Next steps:
  1. Run `/feature-spec [your feature]` to create your first spec
  2. Run `/implement-feature [spec-name]` to implement it
  3. Run `/code-health` to scan your existing codebase
```
