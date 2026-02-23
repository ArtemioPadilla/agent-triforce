# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
<!-- PM adds planned features here -->

### Added
- **Plugin Marketplace**: Packaged Agent Triforce as an installable Claude Code plugin marketplace. Users can install with `/plugin marketplace add ArtemioPadilla/claude-triforce-template` then `/plugin install agent-triforce@agent-triforce`. Includes 3 agents, 6 skills (namespaced as `/agent-triforce:*`), and 2 new commands (`setup` for project scaffolding, `methodology` for checklist reference). Zero-duplication architecture using symlinks from plugin to canonical `.claude/` files. Includes `dashboard` command and SubagentStop hook that auto-regenerates the HTML dashboard after every agent session

### Changed
- **Agent files**: Embedded condensed `## Methodology` section into all 3 agent files (prometeo-pm, forja-dev, centinela-qa). Includes pause point definitions, communication paths, workflow diagrams, and FLY THE AIRPLANE principle. Fixes subagent context loss — agents now carry methodology when invoked via skills with `context: fork`

### Fixed
<!-- Dev adds fixes here -->

### Security
<!-- QA adds security fixes here -->

### Removed
<!-- Dev adds removed features here -->

## [0.1.0] - 2026-02-22

### Added
- **Multi-agent system**: 3 specialized agents (Prometeo PM, Forja Dev, Centinela QA) with dedicated configuration files, permission modes, and model assignments
- **6 skills**: `/feature-spec`, `/implement-feature`, `/review-findings`, `/security-audit`, `/code-health`, `/release-check` — each mapped to the appropriate agent
- **24 checklists** (117 items) using WHO Surgical Safety Checklist methodology: SIGN IN / TIME OUT / SIGN OUT pause points, DO-CONFIRM and READ-DO types, Boorman's 5-9 killer items rule
- **Communication Schedule**: 6 defined handoff paths between agents with structured handoff protocol (what was done, what to watch for, what's needed, open questions)
- **Error Recovery**: NON-NORMAL READ-DO checklists for each agent with FLY THE AIRPLANE step-1 reminders
- **tools/dashboard.py**: Comprehensive multi-agent system dashboard with two output modes: Rich terminal UI and self-contained dark-themed HTML. 10 sections: What's Next (state-based action suggestions), System Overview (agent cards), Feature Pipeline (Kanban board, always-visible columns), Quality Gate (review verdicts with unique finding counts), Tech Debt Register (age tracking), Workflow Status (visual flow diagrams with active stage highlighting), Communication Schedule (6 handoff paths from CLAUDE.md), Architecture Decisions (ADR tracking), Recent Activity (git log, changelog, agent memory), Checklist Inventory (summary + per-agent breakdown). Features: sticky nav bar, stats summary bar, Quick Actions command reference, responsive CSS (900px/600px breakpoints), rich empty states with guidance. Python 3.9+ compatible, zero-dependency HTML mode, defensive parsing for all data sources
- **docs/portability/**: Portability guide for porting the framework to downstream projects
- **Project conventions**: Conventional Commits, branch naming, file location standards, code quality rules, Keep a Changelog format, TECH_DEBT.md tracking
