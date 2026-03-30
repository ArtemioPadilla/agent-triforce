# Superpowers Remaining — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete superpowers adoption with multi-platform distribution, GitHub templates, plugin sync fixes, and slash commands

**Architecture:** 4 independent workstreams: (1) fix plugin sync to include all new skills, (2) add multi-platform plugin configs, (3) add GitHub issue/PR templates, (4) add user-facing slash commands. All additive — no existing behavior changes.

**Tech Stack:** Markdown, JSON, POSIX shell, GitHub template syntax

---

## File Structure

```
New files:
  .claude-plugin                              # Claude Code plugin manifest
  .cursor-plugin/plugin.json                  # Cursor plugin manifest
  .codex/INSTALL.md                           # Codex installation instructions
  .opencode/INSTALL.md                        # OpenCode installation instructions
  GEMINI.md                                   # Gemini CLI context file
  gemini-extension.json                       # Gemini extension manifest
  package.json                                # npm-style metadata (version, description)
  .github/PULL_REQUEST_TEMPLATE.md            # PR template
  .github/ISSUE_TEMPLATE/bug_report.md        # Bug report template
  .github/ISSUE_TEMPLATE/feature_request.md   # Feature request template
  .github/ISSUE_TEMPLATE/config.yml           # Issue template config
  commands/brainstorm.md                      # /brainstorm slash command
  commands/implement.md                       # /implement slash command
  commands/debug.md                           # /debug slash command

Modified files:
  scripts/sync-plugin.sh                      # Add missing skills to SKILLS array
```

---

## Task 1: Fix Plugin Sync Script

The sync script is missing 7 skills added during superpowers adoption. Without this fix, `sync-plugin.sh --check` fails and pre-commit hooks reject commits.

**Files:**
- Modify: `scripts/sync-plugin.sh:25-39` (SKILLS array)

- [ ] **Step 1: Add missing skills to the SKILLS array**

In `scripts/sync-plugin.sh`, find the `declare -a SKILLS=()` block. Add these 7 skills that are currently missing:

```bash
declare -a SKILLS=(
  "feature-spec"
  "implement-feature"
  "review-findings"
  "security-audit"
  "code-health"
  "release-check"
  "generate-tests"
  "checklist-health"
  "simulate-failure"
  "traceability"
  "reindex"
  "business-review"
  "receiving-code-review"
  "self-review"
  "git-worktrees"
  "visual-companion"
  "subagent-orchestration"
  "systematic-debugging"
  "verification-before-completion"
)
```

The 7 new entries are: `self-review`, `git-worktrees`, `visual-companion`, `subagent-orchestration`, `systematic-debugging`, `verification-before-completion` (and `receiving-code-review` was already added by a subagent).

- [ ] **Step 2: Run sync and verify**

Run:
```bash
./scripts/sync-plugin.sh
```
Expected: All skills show `OK` or `CREATED`/`SYNCED`. No `MISSING` or `DRIFT`.

- [ ] **Step 3: Run check mode**

Run:
```bash
./scripts/sync-plugin.sh --check
```
Expected: "All plugin files are in sync." with exit code 0.

- [ ] **Step 4: Commit**

```bash
git add scripts/sync-plugin.sh agent-triforce/skills/
git commit -m "fix: add missing skills to plugin sync script

Adds self-review, git-worktrees, visual-companion, subagent-orchestration,
systematic-debugging, and verification-before-completion to the SKILLS
array in sync-plugin.sh. Syncs plugin distribution copies."
```

---

## Task 2: Multi-Platform Distribution — Package Metadata

Create the root `package.json` and `.claude-plugin` manifest that identify Agent Triforce as an installable plugin.

**Files:**
- Create: `package.json`
- Create: `.claude-plugin`

- [ ] **Step 1: Create package.json**

```json
{
  "name": "agent-triforce",
  "displayName": "Agent Triforce",
  "version": "0.8.0",
  "description": "PM/Dev/QA multi-agent development system with checklist methodology based on The Checklist Manifesto and Boeing's checklist engineering",
  "author": {
    "name": "Artemio Padilla",
    "url": "https://github.com/ArtemioPadilla"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/ArtemioPadilla/claude-triforce-template"
  },
  "license": "MIT",
  "keywords": [
    "claude-code",
    "multi-agent",
    "checklist",
    "tdd",
    "code-review",
    "qa",
    "product-management"
  ]
}
```

- [ ] **Step 2: Create .claude-plugin**

This file tells Claude Code's plugin system where to find agents, skills, commands, and hooks:

```json
{
  "name": "agent-triforce",
  "displayName": "Agent Triforce",
  "description": "PM/Dev/QA multi-agent development system with checklist methodology",
  "version": "0.8.0",
  "author": {
    "name": "Artemio Padilla"
  },
  "homepage": "https://github.com/ArtemioPadilla/claude-triforce-template",
  "repository": "https://github.com/ArtemioPadilla/claude-triforce-template",
  "license": "MIT",
  "skills": "./skills/",
  "agents": "./agents/",
  "commands": "./commands/",
  "hooks": "./hooks/hooks.json"
}
```

Note: `skills`, `agents`, `commands` point to the `agent-triforce/` plugin distribution directory at install time. When used as a template (cloned directly), the `.claude/` directory is used instead.

- [ ] **Step 3: Commit**

```bash
git add package.json .claude-plugin
git commit -m "feat: add package.json and .claude-plugin manifest

Creates npm-style package metadata and Claude Code plugin manifest
for installable distribution of Agent Triforce."
```

---

## Task 3: Multi-Platform Distribution — Cursor, Codex, OpenCode, Gemini

Create platform-specific config files for Cursor, Codex, OpenCode, and Gemini CLI.

**Files:**
- Create: `.cursor-plugin/plugin.json`
- Create: `.codex/INSTALL.md`
- Create: `.opencode/INSTALL.md`
- Create: `GEMINI.md`
- Create: `gemini-extension.json`

- [ ] **Step 1: Create .cursor-plugin/plugin.json**

```json
{
  "name": "agent-triforce",
  "displayName": "Agent Triforce",
  "description": "PM/Dev/QA multi-agent development system with checklist methodology",
  "version": "0.8.0",
  "author": {
    "name": "Artemio Padilla"
  },
  "homepage": "https://github.com/ArtemioPadilla/claude-triforce-template",
  "repository": "https://github.com/ArtemioPadilla/claude-triforce-template",
  "license": "MIT",
  "keywords": [
    "multi-agent",
    "checklist",
    "tdd",
    "code-review",
    "qa"
  ],
  "skills": "./skills/",
  "agents": "./agents/",
  "commands": "./commands/",
  "hooks": "./hooks/hooks.json"
}
```

- [ ] **Step 2: Create .codex/INSTALL.md**

```markdown
# Installing Agent Triforce in Codex

## Quick Install

```bash
cd ~/.codex
git clone https://github.com/ArtemioPadilla/claude-triforce-template.git agent-triforce
```

Then symlink skills into your Codex skills directory:

```bash
mkdir -p ~/.agents/skills
ln -sf ~/.codex/agent-triforce/.claude/skills/* ~/.agents/skills/
```

## Verify Installation

Start a new Codex session and ask:

> "What agents are available?"

You should see references to Prometeo (PM), Forja (Dev), and Centinela (QA).

## Updating

```bash
cd ~/.codex/agent-triforce && git pull
```
```

- [ ] **Step 3: Create .opencode/INSTALL.md**

```markdown
# Installing Agent Triforce in OpenCode

## Quick Install

```bash
cd ~/.opencode
git clone https://github.com/ArtemioPadilla/claude-triforce-template.git agent-triforce
```

## Configuration

Add to your OpenCode config:

```json
{
  "skills": {
    "agent-triforce": "~/.opencode/agent-triforce/.claude/skills"
  }
}
```

## Verify Installation

Start a new OpenCode session. The agent skills should be available automatically.

## Updating

```bash
cd ~/.opencode/agent-triforce && git pull
```
```

- [ ] **Step 4: Create GEMINI.md**

```markdown
@./CLAUDE.md
```

This loads the main project instructions into Gemini CLI context. Gemini reads `GEMINI.md` as its equivalent of `CLAUDE.md`.

- [ ] **Step 5: Create gemini-extension.json**

```json
{
  "name": "agent-triforce",
  "description": "PM/Dev/QA multi-agent development system with checklist methodology",
  "version": "0.8.0",
  "contextFileName": "GEMINI.md"
}
```

- [ ] **Step 6: Commit**

```bash
git add .cursor-plugin/plugin.json .codex/INSTALL.md .opencode/INSTALL.md GEMINI.md gemini-extension.json
git commit -m "feat: add multi-platform distribution configs

Adds plugin configs for Cursor, Codex, OpenCode, and Gemini CLI.
Each platform gets install instructions or manifest files for
discovering Agent Triforce skills and agents."
```

---

## Task 4: GitHub Templates

Create PR template and issue templates for the repository.

**Files:**
- Create: `.github/PULL_REQUEST_TEMPLATE.md`
- Create: `.github/ISSUE_TEMPLATE/bug_report.md`
- Create: `.github/ISSUE_TEMPLATE/feature_request.md`
- Create: `.github/ISSUE_TEMPLATE/config.yml`

- [ ] **Step 1: Create .github/PULL_REQUEST_TEMPLATE.md**

```markdown
## Summary

<!-- 1-3 bullet points describing what changed and why -->

-

## Changes

<!-- What files/modules were modified? What's the scope? -->

-

## Checklist

- [ ] Code follows project conventions (see CLAUDE.md)
- [ ] Tests added/updated for changes (TDD: red-green-refactor)
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] No hardcoded secrets, config values, or dead code
- [ ] Linters pass (ruff for Python, biome for TypeScript)
- [ ] If agent/skill files changed: `./scripts/sync-plugin.sh` run and plugin copies committed

## Test Plan

<!-- How can a reviewer verify this works? -->

- [ ]

## Notes

<!-- Anything else reviewers should know? Trade-offs, open questions, follow-ups? -->
```

- [ ] **Step 2: Create .github/ISSUE_TEMPLATE/bug_report.md**

```markdown
---
name: Bug Report
about: Report a problem with Agent Triforce
title: "[Bug] "
labels: bug
---

## Environment

| Item | Value |
|---|---|
| Platform | Claude Code / Cursor / Codex / OpenCode / Gemini CLI |
| Agent Triforce version | |
| OS | |

## Description

<!-- What happened? What did you expect? -->

## Steps to Reproduce

1.
2.
3.

## Expected Behavior

<!-- What should have happened? -->

## Actual Behavior

<!-- What happened instead? Include error messages if any. -->

## Additional Context

<!-- Screenshots, logs, related issues? -->
```

- [ ] **Step 3: Create .github/ISSUE_TEMPLATE/feature_request.md**

```markdown
---
name: Feature Request
about: Suggest a new skill, agent capability, or workflow improvement
title: "[Feature] "
labels: enhancement
---

## Problem Statement

<!-- What problem does this solve? Who benefits? -->

## Proposed Solution

<!-- Describe the feature or change you'd like. -->

## Alternatives Considered

<!-- What other approaches did you think about? Why is this one better? -->

## Core Appropriateness

<!-- Is this a general-purpose capability that belongs in Agent Triforce's core, or is it project-specific? -->

- [ ] This is useful across different projects and tech stacks
- [ ] This follows the existing checklist methodology
```

- [ ] **Step 4: Create .github/ISSUE_TEMPLATE/config.yml**

```yaml
blank_issues_enabled: false
contact_links:
  - name: Questions & Discussion
    url: https://github.com/ArtemioPadilla/claude-triforce-template/discussions
    about: Ask questions or share ideas in Discussions
```

- [ ] **Step 5: Commit**

```bash
git add .github/PULL_REQUEST_TEMPLATE.md .github/ISSUE_TEMPLATE/
git commit -m "feat: add GitHub PR and issue templates

Adds pull request template with project-specific checklist,
bug report template with environment table, feature request
template with core appropriateness check, and config disabling
blank issues."
```

---

## Task 5: Slash Commands

Create user-facing slash commands that map to common workflows. These live in the `commands/` directory (for the plugin distribution) and get symlinked or copied during installation.

**Files:**
- Create: `.claude/commands/brainstorm.md`
- Create: `.claude/commands/implement.md`
- Create: `.claude/commands/debug.md`

- [ ] **Step 1: Create .claude/commands/brainstorm.md**

```markdown
---
description: Start a brainstorming session to design a feature before implementation
---

I need to brainstorm and design: $ARGUMENTS

Use the brainstorming skill to explore this idea. Start by understanding the current project context, then ask clarifying questions one at a time, propose approaches, and present a design for approval before any implementation.

If Prometeo (PM agent) is available, use it to lead the brainstorming. Otherwise, follow the brainstorming process directly.
```

- [ ] **Step 2: Create .claude/commands/implement.md**

```markdown
---
description: Implement a feature from an approved spec using the full triforce workflow
---

Implement the feature: $ARGUMENTS

Use Forja (Dev agent) with the implement-feature skill. If a spec exists in docs/specs/, read it first. If no spec exists, check if we need one before proceeding.

Follow the subagent orchestration workflow if the implementation has multiple tasks:
1. Read the spec/plan
2. Dispatch fresh subagent per task
3. Two-stage review (spec compliance, then code quality)
4. Use git worktrees for isolation
```

- [ ] **Step 3: Create .claude/commands/debug.md**

```markdown
---
description: Debug an issue using the systematic 4-phase process
---

Debug this issue: $ARGUMENTS

Use the systematic-debugging skill. Follow the 4-phase process:
1. Root cause investigation (read errors, reproduce, trace data flow)
2. Pattern analysis (find working examples, compare)
3. Hypothesis testing (one variable at a time)
4. Implementation (create failing test, fix root cause, verify)

DO NOT propose fixes before completing Phase 1.
```

- [ ] **Step 4: Commit**

```bash
git add .claude/commands/
git commit -m "feat: add slash commands for brainstorm, implement, debug

Creates /brainstorm, /implement, and /debug user-facing commands
that invoke the corresponding skills and agent workflows."
```

---

## Task 6: CHANGELOG and Final Cleanup

Update CHANGELOG with all additions from this plan.

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add entries to CHANGELOG**

Add these lines to the `### Added` section under `## [Unreleased]`:

```markdown
- **Multi-Platform Distribution**: Plugin manifests for Claude Code (`.claude-plugin`), Cursor (`.cursor-plugin/`), Codex (`.codex/`), OpenCode (`.opencode/`), and Gemini CLI (`GEMINI.md`, `gemini-extension.json`). Package metadata in `package.json`.
- **GitHub Templates**: PR template with project-specific checklist, bug report and feature request issue templates.
- **Slash Commands**: `/brainstorm`, `/implement`, `/debug` user-facing commands mapping to core workflows.
```

Add to `### Changed` section:

```markdown
- sync-plugin.sh: added 6 missing skills (self-review, git-worktrees, visual-companion, subagent-orchestration, systematic-debugging, verification-before-completion) to SKILLS array
```

- [ ] **Step 2: Commit**

```bash
git add CHANGELOG.md
git commit -m "docs: update CHANGELOG with distribution, templates, commands"
```

---

## Final Verification

After all 6 tasks:

- [ ] **Verify everything**

```bash
# Plugin sync clean
./scripts/sync-plugin.sh --check

# All distribution files exist
ls package.json .claude-plugin .cursor-plugin/plugin.json .codex/INSTALL.md .opencode/INSTALL.md GEMINI.md gemini-extension.json

# GitHub templates exist
ls .github/PULL_REQUEST_TEMPLATE.md .github/ISSUE_TEMPLATE/bug_report.md .github/ISSUE_TEMPLATE/feature_request.md .github/ISSUE_TEMPLATE/config.yml

# Commands exist
ls .claude/commands/brainstorm.md .claude/commands/implement.md .claude/commands/debug.md

# Bootstrap still works
sh hooks/session-start/bootstrap.sh
```
