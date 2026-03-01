---
name: release-check
description: >
  Pre-release verification with structured report. Validates test coverage, security status,
  CHANGELOG completeness, dependency freshness, tech debt severity. Outputs GO/NO-GO
  recommendation with confidence score and specific remediation steps.
context: fork
agent: centinela-qa
---

Run a pre-release verification for: $ARGUMENTS

This is the highest-stakes checklist in the system. Like a pilot's pre-flight check, every item matters.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Note any known risks or concerns about this release
- Determine the version being checked (from $ARGUMENTS, CHANGELOG.md, or package manifest)

**RELEASE CRITERIA EVALUATION:**

Evaluate each of the following 5 criteria. For each one, record: status (PASS/FAIL), actual value, threshold, and remediation steps if failing.

**Criterion 1 -- Test Coverage (threshold: 80%)**
1. Check for coverage reports: look for `coverage/`, `htmlcov/`, `.coverage`, `coverage.xml`, or `lcov.info`
2. If a coverage report exists, extract the overall coverage percentage
3. If no coverage report exists, check if a test runner is configured (`pytest`, `vitest`, `jest`) and note that coverage was not measured
4. Record: actual coverage % (or "not measured"), PASS if >= 80%, FAIL otherwise

**Criterion 2 -- Security Scanner Status (threshold: 0 open Critical/High)**
5. Read `docs/reviews/security-audit-trail.md` if it exists
6. Count open (unresolved) findings with Critical or High severity
7. Also check the most recent security audit in `docs/reviews/security-audit-*.md`
8. Record: count of open Critical/High findings, PASS if 0, FAIL otherwise
9. For each open finding, note its ID and a one-line summary as remediation

**Criterion 3 -- CHANGELOG Completeness (threshold: entry exists for current version)**
10. Read CHANGELOG.md
11. Check that an entry exists under `## [Unreleased]` or `## [{version}]` with at least one item
12. Record: PASS if entry exists with content, FAIL if empty or missing

**Criterion 4 -- Dependency Freshness (threshold: 0 known Critical CVEs)**
13. Check for dependency manifests: `requirements.txt`, `package.json`, `Cargo.toml`, `go.mod`
14. If `npm audit`, `pip-audit`, or equivalent is available, run it and check for Critical CVEs
15. If no audit tool is available, note as "not auditable" and record as PASS with caveat
16. Record: count of Critical CVEs found, PASS if 0, FAIL otherwise

**Criterion 5 -- Tech Debt Severity (threshold: 0 P0/P1 items)**
17. Read TECH_DEBT.md
18. Count active debt items with severity "Critical" (P0) or "High" (P1)
19. Record: count of P0/P1 items, PASS if 0, FAIL otherwise
20. For each P0/P1 item, note its ID and title as remediation

**TIME OUT 1 -- Documentation & Debt Check (READ-DO):**
21. Read CHANGELOG.md -- is it up to date with all changes?
22. Read TECH_DEBT.md -- are there any critical items blocking release?
23. Verify all specs in `docs/specs/` with status "In Development" have acceptance criteria met
24. Verify documentation is current (README, API docs, ADRs)

**TIME OUT 2 -- Testing & Quality Gate (DO-CONFIRM):**
25. Run all tests and verify they pass
26. Run `/code-health` scan
27. Check that all CHANGES REQUIRED findings have been resolved
28. Verify spec traceability: every spec with status "In Development" or "Done" has ALL acceptance criteria verified
29. Verify test quality: tests follow FIRST principles (Fast, Isolated, Repeatable, Self-validating, Timely), Arrange-Act-Assert pattern, no test logic
30. Run the Quality Verification checklist from your agent file

**TIME OUT 3 -- Security & Release Gate (DO-CONFIRM):**
31. Run `/security-audit` on changed files
32. Run the Security Verification checklist from your agent file
33. Run the Release Readiness checklist from your agent file

**CONFIDENCE SCORE CALCULATION:**

Calculate the release confidence score:
- For each PASSING criterion, compute: min(actual_value / threshold_value, 1.0)
  - Test coverage: coverage_pct / 80 (capped at 1.0)
  - Security: 1.0 if 0 findings, 0.0 otherwise
  - CHANGELOG: 1.0 if exists, 0.0 otherwise
  - Dependencies: 1.0 if 0 CVEs, 0.0 otherwise
  - Tech debt: 1.0 if 0 P0/P1, 0.0 otherwise
- Confidence score = average of all 5 scores * 100 (integer, 0-100)

**RECOMMENDATION:**
- If ALL criteria pass: **GO** with confidence score
- If ANY criterion fails: **NO-GO** with list of failing criteria and specific remediation steps

**SIGN OUT:**

Write the structured release report to `docs/reviews/release-check-{version}-{date}.md` using this format:

```markdown
# Release Check: {version}
**Date**: {YYYY-MM-DD}
**Confidence Score**: {score}/100
**Recommendation**: GO | NO-GO

## Criteria Summary

| Criterion | Status | Actual | Threshold | Notes |
|-----------|--------|--------|-----------|-------|
| Test Coverage | PASS/FAIL | {pct}% | 80% | {notes} |
| Security Scanner | PASS/FAIL | {count} open | 0 Critical/High | {notes} |
| CHANGELOG | PASS/FAIL | {exists/missing} | Entry exists | {notes} |
| Dependencies | PASS/FAIL | {count} CVEs | 0 Critical | {notes} |
| Tech Debt | PASS/FAIL | {count} P0/P1 | 0 items | {notes} |

## Remediation Steps

{For each failing criterion, list specific actionable steps}

## Detailed Assessment

{Full narrative of the release readiness evaluation}
```

Provide final verdict: **READY FOR RELEASE** (GO) | **BLOCKED** (NO-GO with specific reasons)

Run the SIGN OUT checklist from your agent file.

A release blocked here prevents issues reaching users. This is the last line of defense.
