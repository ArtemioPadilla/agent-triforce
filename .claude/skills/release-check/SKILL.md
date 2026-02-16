---
name: release-check
description: >
  Pre-release verification checklist. Validates that all features are complete,
  tests pass, docs are updated, no critical issues remain, and the release is safe.
context: fork
agent: centinela-qa
---

Run a pre-release verification for: $ARGUMENTS

This is the highest-stakes checklist in the system. Like a pilot's pre-flight check, every item matters.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Note any known risks or concerns about this release

**⏸️ TIME OUT 1 — Documentation & Debt Check (READ-DO):**
1. Read CHANGELOG.md — is it up to date with all changes?
2. Read TECH_DEBT.md — are there any critical items blocking release?
3. Verify all specs in `docs/specs/` with status "In Development" have acceptance criteria met
4. Verify documentation is current (README, API docs, ADRs)

**⏸️ TIME OUT 2 — Testing & Quality Gate (DO-CONFIRM):**
5. Run all tests and verify they pass
6. Run `/code-health` scan
7. Check that all CHANGES REQUIRED findings have been resolved
8. Run the Quality Verification checklist from your agent file

**⏸️ TIME OUT 3 — Security & Release Gate (DO-CONFIRM):**
9. Run `/security-audit` on changed files
10. Run the Security Verification checklist from your agent file
11. Run the Release Readiness checklist from your agent file

**SIGN OUT:**
12. Write release assessment to `docs/reviews/release-check-{version}.md`
13. Provide final verdict: **READY FOR RELEASE** | **BLOCKED** (with specific reasons)
14. Run the SIGN OUT checklist from your agent file

A release blocked here prevents issues reaching users. This is the last line of defense.
