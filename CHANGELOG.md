# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **ADR-001 Quality Model & Standards**: ISO/IEC 25010 mapping, GQM instantiation (4 goal-question-metric chains), academic bibliography
- **ADR-002 CI/CD Strategy**: Branching model (Git Flow-lite), pipeline stages with quality gates, static analysis mapping, quality gate philosophy
- **License compliance scanning** in security-audit: copyleft/permissive dependency classification (Pass/Warning/Critical)
- **Defect lifecycle** in review-findings: severity classification (Critical/Major/Medium/Minor), status tracking (Open>Assigned>Implemented>Verified>Closed), entry/exit criteria, structured finding format with F-{NNN} IDs
- **GQM quality metrics** in release-check: Phase Containment Effectiveness (PCE), Defect Closure Rate, Open Findings Trend -- criteria 6-8, gate expanded from 5 to 8 criteria
- **Anti-Rationalization Tables**: DO-CONFIRM rationalization red flag tables in all 3 agent checklists, tuned to role-specific failure modes. Inspired by obra/superpowers.
- **DOT Flowcharts**: Graphviz DOT process diagrams replace ASCII workflow diagrams in all agent files and CLAUDE.md.
- **Self-Review Loops**: Inline self-review checklist items in Prometeo, Forja, and Centinela TIME OUT checklists. New standalone `self-review` skill.
- **Session-Start Hooks**: POSIX-safe `hooks/session-start/bootstrap.sh` surfaces active worktrees, pending specs, open findings, and TECH_DEBT.md staleness.
- **Git Worktrees Workflow**: New `git-worktrees` skill for isolated feature branch management with 4 finish-branch options. Forja checklist items added.
- **Visual Brainstorming Companion**: New `visual-companion` skill using chrome MCP tools for browser-based mockups during design. Prometeo checklist item added.
- **Subagent Orchestration**: Forja as orchestrator with 3 prompt templates (implementer, spec-reviewer, code-quality-reviewer). New `subagent-orchestration` skill. Model selection guidance.
- **Receiving Code Review**: New `receiving-code-review` skill for handling feedback with technical rigor. Forja Receiving-from-Centinela checklist added.
- **Systematic Debugging**: New `systematic-debugging` skill with 4-phase root cause process, defense-in-depth, and architecture questioning after 3+ failed fixes. Non-Normal checklist references added.
- **Verification Before Completion**: New `verification-before-completion` skill enforcing evidence before assertions. SIGN OUT checklists updated across all agents.
- **FURPS quality attributes** in code-health: scan reorganized under Functionality, Reliability, Performance, Supportability categories
- **Cost of Quality (COPQ)** classification in code-health: prevention, appraisal, internal failure, external failure
- **Public API docstring check** in code-health
- **License Compliance** section in CLAUDE.md
- **Quality Models & Measurement** section in CLAUDE.md (ISO 25010, GQM, IEEE 829)
- **Multi-Platform Distribution**: Plugin manifests for Claude Code (`.claude-plugin`), Cursor (`.cursor-plugin/`), Codex (`.codex/`), OpenCode (`.opencode/`), and Gemini CLI (`GEMINI.md`, `gemini-extension.json`). Package metadata in `package.json`.
- **GitHub Templates**: PR template with project-specific checklist, bug report and feature request issue templates.
- **Slash Commands**: `/brainstorm`, `/implement`, `/debug` user-facing commands mapping to core workflows.

### Changed
- sync-plugin.sh: added 6 missing skills to SKILLS array (self-review, git-worktrees, visual-companion, subagent-orchestration, systematic-debugging, verification-before-completion)
- security-audit: added license compliance scan section and checklist item (Security Verification now 6 items)
- release-check: expanded from 5 to 8 criteria with GQM section in report template; confidence score excludes N/A baselines
- code-health: reorganized scan under FURPS categories with COPQ tagging
- review-findings: added defect severity, status lifecycle, entry/exit criteria, structured finding format
- CLAUDE.md: added quality models, defect lifecycle, FURPS/COPQ, and license compliance references

## [0.7.0] - 2026-03-08

### Added
- **IEEE 829 Test Design Techniques**: Added structured test design technique selection (BVA, Equivalence Partitioning, Decision Tables, State Transition, Error Guessing) to CLAUDE.md, `/generate-tests` skill, and agent checklists. Based on IEEE 829-2008, O'Regan Ch.6, and LTS QA reference materials.
- **Test Case ID Format**: `TC-{feature}-{NNN}` with `Verifies: {feature}-AC-{NNN}` docstring convention for end-to-end traceability from spec AC to test function.
- **Integrity Level Mapping**: Spec tiers (S/M/L) now map to proportional testing rigor — S: minimal, M: full technique-driven, L: comprehensive with integration plan.

### Changed
- **Traceability Tool**: Replaced naive all-to-all file matching with per-criterion bi-directional traceability. Two-phase matching: explicit (`Verifies:`/`Implements:` annotations) then implicit (keyword extraction with stopword filtering). Added orphan detection for test references to non-existent ACs. Enhanced matrix output with Test IDs, Link Type columns, and Coverage Summary section.
- **`/generate-tests` Skill**: New TECHNIQUE SELECTION step with decision table for choosing BVA/EP/Decision Table/State Transition/Error Guessing. Technique-driven test generation replaces generic happy-path/edge-case. TC-ID format required in docstrings. Checklist updated (7 → 8 items).
- **`/traceability` Skill**: Added bi-directional verification step (orphaned tests, unlinked tests, coverage gap summary). Enhanced matrix output format with Link Type column. Checklist updated (7 → 8 items).
- **`/feature-spec` Skill**: Step 8 now recommends test design technique per high-risk AC.
- **Prometeo Spec Template**: Testing Considerations section expanded with technique recommendations per AC and integrity level field.
- **Centinela Review Template**: Test Quality section now includes technique appropriateness and test case ID checks.
- **Forja Implementation Complete Checklist**: Items 2-3 refined for technique-appropriate testing and TC-ID traceability.
- **Centinela Quality Verification Checklist**: Item 2 refined for explicit TC-ID linkage and technique assessment.

## [0.6.0] - 2026-03-07

### Added
- **Growth Tracker Tool**: Growth phase tracking and pre-launch readiness gate tool (`tools/growth-tracker.py`). Four subcommands: `status` (current growth phase and metrics), `check` (pre-launch readiness gates), `milestones` (milestone-gated action items), `log` (record weekly metrics to growth-log.md). Implements growth-plan.md Appendix A (8 readiness gates) and Appendix E (7 milestone thresholds). Phase determination: Pre-Launch (stars < 10 OR repo < 30 days), Soft Launch (10-50 stars), Content Momentum (50-200 stars), Community (200+ stars). New `/growth-check` command. Tests in `tests/test_growth_tracker.py` (35 tests).
- **Strategic Planning Documents**: Three approved PM specs defining product direction. Feature Roadmap (`docs/specs/feature-roadmap.md`) — 20 features across 4 phases (all implemented). Future Roadmap (`docs/specs/future-roadmap.md`) — 25-year Working Backwards planning with 14 time horizons, categorized goals, and pivot triggers. Growth Plan (`docs/specs/growth-plan.md`) — sequenced adoption strategy with pre-launch gates, curated list resubmission strategy, Show HN/Reddit/Twitter sequencing, and milestone-gated actions.
- **Test Suite for Session Tracker**: `tests/test_session_tracker.py` (30 tests) covering `_count_findings()` agent attribution routing (regression for H-1 fix), `_compute_handoffs()`, `_estimate_cost()`, `_build_report()`, pricing loaders, and CLI commands.
- **Test Suite for Workflow Tracker**: `tests/test_workflow_tracker.py` (27 tests) covering serialization round-trips, file I/O, and all subcommands: start, phase, checklist, blocker add/resolve, complete, status, history.
- **Test Suite for Dashboard Parsers**: `tests/test_dashboard.py` (41 tests) covering `_parse_frontmatter()`, `_parse_checklists()`, `parse_specs()`, `parse_reviews()`, `parse_tech_debt()`, `parse_changelog()`, `parse_adrs()`, `compute_health()`, and `_read_file_safe()`.
- **Quickstart Guide**: Step-by-step onboarding doc (`docs/quickstart.md`) covering plugin install, setup, and first feature spec in under 5 minutes. Linked from README.
- **Growth Log**: Baseline tracking file (`docs/growth-log.md`) for weekly adoption metrics per growth plan Appendix E.
- **`/business-review` Skill**: New PM-led post-implementation business assessment skill for Prometeo. Evaluates 5 areas: Success Metrics, Scope Compliance, AC Business Validation, Risk Review, and Product Decisions. Generates structured report with confidence score (0-100), verdict (APPROVED/CONDITIONALLY APPROVED/CHANGES REQUIRED), and Mermaid-based visual representations: Feature Timeline (Gantt chart showing spec→dev→QA→review lifecycle), Project Roadmap Status (timeline of all features by phase), Confidence Score Breakdown (pie chart), and Risk & Dependency Map (flowchart). Reports saved to `docs/reviews/business-review-{feature}-{date}.md`. New Business Verification checklist (6 items) added to Prometeo agent (7 checklists total). Closes the product loop: feature-spec → implement → QA → business-review → release.
- **F05 Security Scanner Hook**: Pre-commit security scanner (`tools/security-scanner.py`) that detects hardcoded secrets (AWS keys, GitHub tokens, OpenAI keys, Stripe keys, private keys, passwords, API keys, auth tokens), SQL injection patterns (f-string, concatenation, %-formatting), XSS vectors (innerHTML, dangerouslySetInnerHTML, document.write), and unsafe eval/exec/__import__ usage. 23 versioned patterns in `src/security/patterns.json`. Supports `.agentignore` for excluding test fixtures (gitignore syntax). Outputs JSON with findings, severity, line numbers. Critical/high findings block; medium findings are logged. Appends to `docs/reviews/security-audit-trail.md` (append-only). PreToolUse hook on Write/Edit tools in `hooks.json`. Tests in `tests/test_security_scanner.py`.
- **F02 Automated Handoff Protocol**: Handoff artifact generator (`tools/handoff-generator.py`) producing structured markdown and JSON artifacts at `docs/handoffs/`. Enforces 4 required fields from CLAUDE.md Communication Schedule: what was done, what to watch for, what's needed next, open questions. Validates all fields are non-empty (blocks if incomplete). Supports direct CLI args or `--from-json` for machine-generated handoffs. `--dry-run` mode for validation without file creation. Agent name validation (prometeo, forja, centinela). Tests in `tests/test_handoff_generator.py`.
- **F10 Plan Approval Gates**: Gate enforcement system (`tools/gate-checker.py`) with 4 subcommands: create, check, approve, override. Gate documents at `docs/gates/{feature}-{gate-type}.md`. Two gate types: plan-gate (Prometeo approves before coding) and release-gate (Centinela signs off). Parses markdown gate documents for status, criteria checkboxes, approval info. Override requires reason string (logged). Exit 0 if gate passed (APPROVED/OVERRIDDEN), exit 1 if blocked (PENDING/NOT_FOUND). New `/gate` command in plugin. Tests in `tests/test_gate_checker.py`.
- **F01 Agent Team Orchestration Mode**: Team configuration (`plugins/agent-triforce/team.json`) defining Prometeo as team lead with Forja and Centinela as teammates. Supports parallel task execution, inter-agent messaging with structured handoff protocol (4 required fields), and graceful fallback to sequential mode. New `/team` command for viewing team status and orchestration info. Added `## Team Role` section to all 3 agent files defining their role in team mode.
- **F04 LSP Integration Templates**: LSP configuration templates for TypeScript (`typescript-language-server`), Python (`pylsp`), and Rust (`rust-analyzer`) in `templates/lsp/`. New `/lsp-setup` command that detects project type, copies the appropriate template, and verifies LSP server installation. Per-project `.lsp.json` configuration.
- **F06 Static Analysis MCP Templates**: MCP configuration templates for SonarQube and CodeScene in `templates/mcp/`. New `/mcp-setup` command that lists available integrations, guides environment variable setup, and helps merge configurations into `.mcp.json`. All credentials via environment variables only.
- **F09 Smart Agent Routing**: Default routing configuration (`templates/agent-routing.json`) assigning cost-appropriate models to each skill (Haiku for routine scans, Sonnet for reasoning tasks, inherit for user-default). Includes cost estimates per model tier and average token counts per skill. New `/cost-estimate` command for previewing workflow costs. Added routing awareness comments to all 3 agent files.
- **F13 Issue Tracker MCP Templates**: MCP configuration templates for Linear, Jira, and GitHub Issues in `templates/mcp/`. New `/issues-setup` command explaining per-agent usage patterns (Prometeo reads tickets, Forja updates status, Centinela creates issues for findings). All credentials via environment variables.
- **F03 Enhanced Setup Wizard**: Transformed `/setup` command into a multi-step interactive wizard. Detects tech stack by scanning for package.json, pyproject.toml, Cargo.toml, go.mod, pom.xml. Creates docs/ directory structure, starter CHANGELOG.md and TECH_DEBT.md from templates. Generates project-specific CLAUDE.md with detected tech stack. Offers optional MCP server connections and agent routing configuration. Handles "already set up" case with reconfigure mode. See `plugins/agent-triforce/commands/setup.md`.
- **F08 /generate-tests Skill**: New skill for automated test generation following FIRST principles and Arrange-Act-Assert pattern. Detects test framework from project config (pytest, Vitest, Jest). Generates happy-path and edge-case tests for public functions. Skips private/unexported symbols. Adds generation metadata header. See `.claude/skills/generate-tests/SKILL.md`.
- **F15 /checklist-health Skill**: New skill for checklist evolution tracking. Reads checklist definitions from all 3 agent files, tracks hit rates from events.jsonl, identifies stale items and coverage gaps, generates suggested improvements following Boorman's principles. See `.claude/skills/checklist-health/SKILL.md`.
- **F19 /simulate-failure Skill**: New skill for Non-Normal procedure training. Three scenarios: ambiguous-spec, failing-tests, security-finding. Creates simulation artifacts in docs/training/, scores each checklist item as PASS/FAIL, identifies missed items. All outputs labeled SIMULATION MODE. See `.claude/skills/simulate-failure/SKILL.md`.
- **F14 Cross-Agent Memory Conflict Detection**: Memory sync tool (`tools/memory-sync.py`) with CLI for detecting conflicting observations across agent MEMORY.md files. Entity extraction (backtick-quoted, path-like, keyword-based), sentiment analysis with 7 opposing pairs (stable/fragile, simple/complex, etc.), resolution system (accept A/B/investigate). Archives resolved conflicts to `docs/memory-archive/`. New `/memory-conflicts` command. Three subcommands: check, resolve, show.
- **F17 /traceability Skill and Tool**: Traceability matrix generator (`tools/traceability.py`) linking spec acceptance criteria (GIVEN/WHEN/THEN) to implementation files, test cases, and review findings. New `/traceability` skill for Centinela. Generates matrix at `docs/traceability/{feature}-matrix.md` with Covered/Partial/Missing status. Criterion IDs in format `{feature}-AC-{NNN}`. Supports IEEE 830 compliance audits.
- **F18 Context-Efficient Agent Spawning Profiles**: Context profile configuration (`templates/context-profiles.json`) defining per-skill context loading rules. Specifies which CLAUDE.md sections, agent sections, and memory entries to load per skill. Estimated token reductions: checklist-health 45%, code-health 35%, generate-tests 30%, feature-spec 25%. New `/context-profiles` command for viewing and customizing profiles. `--full-context` flag overrides profiles.
- **F20 Codebase Knowledge Index**: Codebase indexer tool (`tools/codebase-indexer.py`) building a shared module map across all agents. Scans for Python, TypeScript, JavaScript, Rust, Go, Java, Solidity files. Extracts public function/class signatures, inter-module dependency graph, circular dependency detection, orphan module identification. Cross-references TECH_DEBT.md and review files for hotspot flagging. Supports incremental builds. New `/reindex` skill and command. Output at `docs/codebase-index.json`.
- **F07 Workflow Visualization and Progress Tracking**: Workflow state tracker (`tools/workflow-tracker.py`) with CLI for managing workflow runs: start, phase, checklist, blocker add/resolve, complete, status, history. Persists state to `docs/workflow-state.json` with full phase history, checklist item pass/fail tracking, and blocker management. New `/status` command (`plugins/agent-triforce/commands/status.md`) showing current agent, phase, checklist progress, handoff summary, session analytics, and system health. Zero external dependencies, Python 3.9+.
- **F12 GitHub Actions CI/CD Integration**: Three GitHub Actions workflow templates in `templates/ci/`: `pr-review.yml` (Centinela security review on PRs, posts findings as comment, blocks on Critical/High, Haiku model, 5-min timeout), `security-audit.yml` (full OWASP audit on push to main, saves report artifact, Haiku model, 10-min timeout), `release-check.yml` (5-criterion release readiness check on tag push, GO/NO-GO with confidence score, attaches report to release, Sonnet model, 10-min timeout). New `/ci-setup` command with installation guide, cost estimates, and customization tips.
- **F16 Live Dashboard with Session Analytics**: Session analytics tracker (`tools/session-tracker.py`) with CLI for generating per-agent metrics: estimated tokens, time spent, checklists run, findings count. Reads workflow state and estimates cost based on `.agent-routing.json` pricing config. Three subcommands: report (JSON stdout), export (saves to `docs/analytics/session-{date}.json`), summary (one-line). Default pricing for Opus/Sonnet/Haiku with 60/40 input/output split estimation. Integrated into `/status` command analytics section.
- **Plugin Marketplace**: Packaged Agent Triforce as an installable Claude Code plugin marketplace. Users can install with `/plugin marketplace add ArtemioPadilla/agent-triforce` then `/plugin install agent-triforce@agent-triforce`. Includes 3 agents, 11 skills (namespaced as `/agent-triforce:*`), and 14 commands. Zero-duplication architecture using symlinks from plugin to canonical `.claude/` files. SubagentStop hooks auto-regenerate dashboard, generate handoff artifacts, and log session analytics

### Changed
- **release-check skill (F11)**: Enhanced with structured 5-criterion release readiness report. Evaluates: test coverage (threshold 80%), security scanner status (0 Critical/High), CHANGELOG completeness, dependency freshness (0 Critical CVEs), tech debt severity (0 P0/P1). Calculates confidence score (0-100) as average of criterion scores capped at 1.0 each. Outputs GO/NO-GO recommendation with specific remediation steps. Report saved to `docs/reviews/release-check-{version}-{date}.md` with criteria summary table.
- **hooks.json**: Added PreToolUse hook for security scanner on Write/Edit, SubagentStop hooks for handoff generator and session tracker alongside dashboard regeneration
- **All agent files**: Added `## Team Role` section to prometeo-pm.md, forja-dev.md, and centinela-qa.md defining each agent's role in Agent Teams mode (lead vs teammate) and noting routing configuration awareness
- **Prometeo spec templates**: Replaced single spec template with tiered system (S/M/L). Tier S has 5 sections for quick fixes, Tier M (default) has 14 sections with Glossary, Non-Functional Requirements, and Constraints & Assumptions, Tier L adds 5 more sections (Phased Delivery, API Contract, Migration, Testing Strategy, Story Map). All tiers include explicit `**Tier**` metadata field
- **Prometeo behavioral rules**: Added INVEST validation (Independent, Negotiable, Valuable, Estimable, Small, Testable) as a mandatory check for every user story
- **Prometeo Spec Completion checklist**: Updated to be tier-aware -- first item now verifies tier declaration and tier-required sections; success metrics scoped to M/L tiers; INVEST validation added to acceptance criteria check
- **feature-spec skill**: Added tier selection step (ask user or default to M), INVEST validation breakdown, and IEEE 830 quality attribute verification for M/L tiers
- **Agent files**: Embedded condensed `## Methodology` section into all 3 agent files (prometeo-pm, forja-dev, centinela-qa). Includes pause point definitions, communication paths, workflow diagrams, and FLY THE AIRPLANE principle. Fixes subagent context loss — agents now carry methodology when invoked via skills with `context: fork`
- **Centinela QA agent**: Added Review Dimensions (Code Quality, Architecture Compliance, Spec Compliance) after review template. Added Code Quality, Architecture Compliance, and Test Quality sections to review template. Enhanced Test Quality Assessment with FIRST principles, Arrange-Act-Assert pattern, and coverage-by-type. Upgraded Quality Verification checklist with Clean Code, architecture compliance, and spec traceability items
- **security-audit skill**: Added architecture review (dependency direction, layer separation) and test strategy review (security-critical path coverage) as steps 5-6
- **code-health skill**: Replaced code smells scan with Clean Code violations (30-line functions, 300-line files, 3-level nesting, DRY, primitive obsession, feature envy, god classes). Added architecture compliance step (dependency direction, layer leakage, Screaming Architecture)
- **release-check skill**: Added spec traceability verification and test quality verification (FIRST principles, Arrange-Act-Assert) as steps 8-9 in Testing & Quality Gate
- **Forja Dev agent**: Added Engineering Principles section (Clean Architecture, TDD, Clean Code, Refactoring, 12-Factor, GoF Design Patterns). Expanded Implementation Process to 7-step TDD cycle (design, red, green, refactor, coverage, document, handoff). Updated behavioral rules with TDD-first, Boy Scout Rule, YAGNI. Upgraded Implementation Complete checklist (TDD test-first, dependency direction, explicit error handling) and Pre-Delivery checklist (refactoring pass, Screaming Architecture)
- **implement-feature skill**: Added DESIGN phase (interfaces first, Clean Architecture layers), TDD Build cycle (Red/Green/Refactor with Arrange-Act-Assert), and explicit REFACTORING PASS before Pre-Delivery
- **review-findings skill**: Enhanced FIX section with Clean Code principles (Extract Method, Rename, Move, Replace Conditional with Polymorphism), Arrange-Act-Assert test updates, Boy Scout Rule scan, and "no new code smells" verification
- **CLAUDE.md**: Added Software Engineering Principles section (IEEE 830/INVEST specs, Clean Architecture, TDD/Clean Code, FIRST testing, Refactoring, 12-Factor/GoF). Updated Code Standards with function size limit (<30 lines) and error handling preference
- **Dashboard**: Added spec tier badge (S/M/L) to Feature Pipeline kanban cards in both HTML and terminal renderers
- **Dashboard**: Added acceptance criteria count badge to pipeline kanban cards, "Next Step" summary in stats bar, renamed "What's Next" to "Recommended Next Steps"
- **Dashboard**: Added project name to HTML `<title>`, page header, and terminal banner for multi-project disambiguation
- **Dashboard**: Added trident emoji favicon to HTML dashboard
- **Session Tracker**: Updated `DEFAULT_AGENT_MODELS` to assign `centinela-qa` to `sonnet` instead of `haiku`, matching actual agent model assignment and fixing underestimated cost reports (M-7)
- **Security Scanner Tests**: Refactored 3 `try/except SystemExit` patterns to use idiomatic `pytest.raises` (L-6)

### Fixed
- **Backlog**: Removed duplicate B-007 entry from the Open section (already resolved in commit a035e89)
- **Dashboard**: Added `--no-open` flag to prevent browser tab spam from SubagentStop hooks. Hook now generates HTML silently; manual `/dashboard` invocation still opens the browser.
- **Dead code**: Removed unused `SCRIPT_DIR` constant from security-scanner.py, gate-checker.py, handoff-generator.py. Removed unused `agent_css_names` variable from dashboard.py.
- **Version**: Corrected product version from 1.x.x to 0.x.x (0.5.0) across plugin.json, marketplace.json, and README badge — project is pre-1.0 stable release

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
