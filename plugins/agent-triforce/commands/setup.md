---
description: Initialize project structure for the Agent Triforce workflow (specs, reviews, ADRs, source, tests)
---

Set up the project directory structure expected by the Agent Triforce agents. For each item below, check if it already exists before creating it. Never overwrite existing files.

**Directories to create:**
1. `docs/specs/` — feature specifications (Prometeo output)
2. `docs/reviews/` — QA review reports (Centinela output)
3. `docs/adr/` — architecture decision records (Forja output)
4. `src/` — source code
5. `tests/` — test files

**Files to create (only if missing):**

6. `CHANGELOG.md` with this template:
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

7. `TECH_DEBT.md` with this template:
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

8. Add `.claude/agent-memory/` to `.gitignore` (append if not already present)

**After setup, report:**
- Which directories were created vs already existed
- Which files were created vs already existed
- Any issues encountered
