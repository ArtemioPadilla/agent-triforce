# Quickstart Guide

Go from zero to your first feature spec in under 5 minutes.

## Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- Claude Max or Pro subscription (agents require model access)

## Option A: Install as Plugin

### 1. Add the plugin

```bash
/plugin marketplace add ArtemioPadilla/agent-triforce
```

### 2. Activate it

```bash
/plugin install agent-triforce@agent-triforce
```

### 3. Scaffold your project

```bash
/agent-triforce:setup
```

This detects your tech stack, creates the `docs/` directory structure, and generates starter files.

### 4. Create your first feature spec

```bash
/agent-triforce:feature-spec a user login page with email and password
```

Prometeo (PM agent) will produce a structured spec at `docs/specs/user-login-page.md` with user stories, acceptance criteria, and risk assessment.

### 5. Implement it

```bash
/agent-triforce:implement-feature user-login-page
```

Forja (Dev agent) reads the spec, designs the architecture, writes code using TDD, and hands off to QA.

## Option B: Use as Template

```bash
gh repo create my-project --template ArtemioPadilla/agent-triforce
cd my-project
claude
```

Skills are available without the namespace prefix: `/feature-spec`, `/implement-feature`, etc.

## What happens next

The full workflow loop:

```
/feature-spec  -->  /implement-feature  -->  /security-audit  -->  /review-findings  -->  repeat
    (PM)                (Dev)                    (QA)                  (Dev)
```

Each agent runs SIGN IN / TIME OUT / SIGN OUT checklists at every step. Run `/agent-triforce:status` to see where you are.

## Useful commands

| Command | What it does |
|---------|-------------|
| `/agent-triforce:status` | Current workflow state and next actions |
| `/agent-triforce:code-health` | Scan for dead code, tech debt, code smells |
| `/agent-triforce:release-check` | Pre-release GO/NO-GO verification |
| `/agent-triforce:simulate-failure` | Test agent error-handling with simulated failures |
