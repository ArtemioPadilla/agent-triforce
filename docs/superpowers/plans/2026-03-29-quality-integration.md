# Quality Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate formal software quality models, test metrics, defect lifecycle, license compliance, and CI/CD strategy into Agent Triforce.

**Architecture:** Documentation-first approach -- two ADRs establish the knowledge base, then four existing skills are enhanced to enforce the standards, and finally CLAUDE.md is updated with concise references. No new skills created; all changes extend existing boundaries.

**Tech Stack:** Markdown (agent/skill definitions), Python (pytest for validation), GitHub Actions (existing CI templates)

**Design Spec:** `docs/superpowers/specs/2026-03-29-quality-integration-design.md`

---

## File Map

| Action | File | Responsibility |
|--------|------|---------------|
| Create | `docs/adr/ADR-001-quality-model-standards.md` | Quality model foundation, ISO 25010 mapping, GQM chains |
| Modify | `.claude/skills/security-audit/SKILL.md` | Add license compliance scan section |
| Modify | `.claude/agents/centinela-qa.md:201-209` | Add license check to Security Verification checklist |
| Modify | `.claude/skills/review-findings/SKILL.md` | Add defect lifecycle, severity, entry/exit criteria |
| Modify | `.claude/skills/release-check/SKILL.md:26-54,75-84,92-117` | Add 3 GQM metrics, update confidence score, update report template |
| Create | `docs/adr/ADR-002-cicd-strategy.md` | CI/CD strategy, branching model, pipeline stages |
| Modify | `.claude/skills/code-health/SKILL.md:18-46` | Reorganize under FURPS, add COPQ, add docstring check |
| Modify | `CLAUDE.md:133-156` | Add quality models, defect lifecycle, license compliance sections |
| Modify | `CHANGELOG.md` | Document all changes |

---

### Task 1: Quality Model & Standards ADR

**Files:**
- Create: `docs/adr/ADR-001-quality-model-standards.md`

- [ ] **Step 1: Create the ADR file**

Write the following to `docs/adr/ADR-001-quality-model-standards.md`:

```markdown
# ADR-001: Quality Model & Standards Foundation

**Date**: 2026-03-29
**Status**: Accepted
**Context**: Agent Triforce Quality Framework

## Context

Agent Triforce implements quality assurance through three specialized agents (Prometeo, Forja, Centinela) coordinated by 24 checklists following Gawande/Boorman principles. However, the system lacks explicit traceability to recognized software quality standards. This makes it harder to:
- Objectively measure quality improvements over time
- Align agent behaviors with industry-standard quality attributes
- Provide academic and professional credibility for the quality framework

## Decision

Adopt a hybrid quality model as the theoretical foundation for Agent Triforce:

1. **ISO/IEC 25010:2011** (SQuaRE) for product quality attributes -- supersedes ISO 9126, adds security as first-class attribute
2. **GQM** (Goal-Question-Metric, Basili & Rombach 1988) for measurement -- every metric must trace to a business goal through a question
3. **IEEE 829** for test documentation -- test case IDs, traceability, and reporting formats

### ISO 25010 Quality Attribute Mapping

| Quality Attribute | Owner Agent | Enforcing Skill | How |
|---|---|---|---|
| Functional Suitability | Prometeo (spec) + Centinela (verify) | feature-spec, review-findings | AC in GIVEN/WHEN/THEN, spec compliance review |
| Reliability | Forja (implement) + Centinela (verify) | generate-tests, code-health | Test flakiness detection, dependency vulnerability scan |
| Security | Centinela (primary) | security-audit | OWASP Top 10, secrets scan, license compliance |
| Maintainability | Forja (implement) + Centinela (verify) | code-health, review-findings | Clean Code checks, architecture compliance |
| Performance Efficiency | Forja (implement) | code-health | Complexity metrics (file size, function length, nesting depth) |
| Usability | Prometeo (spec) | feature-spec | User stories with INVEST criteria |
| Compatibility | Centinela (verify) | security-audit | Dependency compatibility, license compatibility |
| Portability | Forja (implement) | implement-feature | 12-Factor App principles, config in environment |

### GQM Instantiation for Agent Triforce

**Goal 1: Reduce escaped defects**
- Question: What percentage of defects are found by Centinela during review vs discovered post-merge?
- Metric: Phase Containment Effectiveness (PCE) -- target >= 70%
- Data source: Review reports with defect status lifecycle

**Goal 2: Ensure release readiness**
- Question: Are all critical and major findings resolved before release?
- Metric: Defect Closure Rate -- target >= 90% Critical+Major closed
- Data source: Finding status fields in review reports

**Goal 3: Maintain codebase health**
- Question: Is the defect arrival rate stable or declining between releases?
- Metric: Open Findings Trend -- target: non-increasing
- Data source: Comparison of open findings count across release-check reports

**Goal 4: Ensure legal compliance**
- Question: Are all dependencies license-compatible with the project license (MIT)?
- Metric: % of dependencies with permissive-compatible licenses -- target: 100%
- Data source: License compliance scan in security-audit

## Consequences

- All quality metrics must follow GQM: Goal > Question > Metric. No measurement for measurement's sake.
- Quality attributes from ISO 25010 map to specific agent responsibilities -- no ambiguity about ownership.
- New metrics (PCE, Defect Closure Rate, Open Findings Trend) require the defect status lifecycle to be tracked in review reports.
- The release-check skill expands from 5 criteria to 8 criteria.

## References

- ISO/IEC 25010:2011. Systems and software engineering -- SQuaRE -- System and software quality models.
- ISO/IEC 9126-1:2001. Software engineering -- Product quality (superseded by 25010).
- Basili, V.R. & Rombach, H.D. (1988). The TAME Project: Towards Improvement-Oriented Software Environments. *IEEE TSE*, 14(6), 758-773.
- IEEE 829-2008. IEEE Standard for Software and System Test Documentation.
- Callejas-Cuervo, M., Alarcon-Aldana, A.C., & Alvarez-Carreno, A.M. (2017). Modelos de calidad del software, un estado del arte. *Entramado*, 13(1), 230-244.
- O'Regan, G. (2019). *Concise Guide to Software Testing*. Springer. Ch. 9: Test Metrics and Problem-Solving.
- Feigenbaum, A.V. (1956). Total Quality Control. *Harvard Business Review*, 34(6), 93-101.
- Crosby, P.B. (1979). *Quality Is Free*. McGraw-Hill.
```

- [ ] **Step 2: Verify the file renders correctly**

Run: `head -5 docs/adr/ADR-001-quality-model-standards.md`
Expected: Shows the ADR header with title and date.

- [ ] **Step 3: Commit**

```bash
git add docs/adr/ADR-001-quality-model-standards.md
git commit -m "docs: add ADR-001 quality model and standards foundation

Maps ISO/IEC 25010 quality attributes to agent responsibilities,
instantiates GQM paradigm with 4 goal-question-metric chains,
and establishes measurement principles for Agent Triforce.

References: ISO 25010, GQM (Basili & Rombach 1988), IEEE 829,
Callejas-Cuervo et al. (2017), O'Regan (2019)"
```

---

### Task 2: License Compliance in security-audit

**Files:**
- Modify: `.claude/skills/security-audit/SKILL.md`
- Modify: `.claude/agents/centinela-qa.md`

- [ ] **Step 1: Read the current security-audit skill**

Run: `cat -n .claude/skills/security-audit/SKILL.md`
Note the line where the OWASP audit steps end (around line 37) and where TIME OUT checklists are referenced (around line 42).

- [ ] **Step 2: Add license compliance section to security-audit skill**

After the existing audit steps (dependency audit section) and before the TIME OUT checklist references, add a new section. Find the text that references dependency scanning and add after it:

```markdown
### License Compliance Scan

Scan all project dependencies for license compatibility with the project license (MIT):

1. **Detect dependency manifest**: `requirements.txt`, `pyproject.toml` (Python) or `package.json` (Node)
2. **Check each dependency's license** using `pip-licenses --format=markdown` (Python) or `npx license-checker --json` (Node). If tools unavailable, inspect manifests manually
3. **Classify by compatibility**:
   - **Pass** (permissive): MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Unlicense, CC0-1.0, 0BSD
   - **Warning** (weak copyleft): LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0 -- flag with explanation of linking implications
   - **Critical** (strong copyleft): GPL-2.0, GPL-3.0, AGPL-3.0 -- incompatible with MIT distribution
   - **Critical** (no license): Dependency has no detectable license -- cannot legally redistribute
4. **Output**: License compatibility table in the security audit report with columns: Dependency, Version, License, Compatibility (Pass/Warning/Critical)

References: Skaife (2021), EPAM SolutionsHub (2023), Leroux (2025)
```

- [ ] **Step 3: Add license check to Centinela's Security Verification checklist**

Open `.claude/agents/centinela-qa.md`. Find the "Security Verification (DO-CONFIRM)" checklist (around line 201-209). It currently has 5 items. Add a 6th item after the last one (line 207, "Dependencies have no known critical CVEs"):

```markdown
- [ ] Dependency licenses are compatible with project license (no GPL/AGPL in tree)
```

Update the checklist header count from "5 items" to "6 items".

- [ ] **Step 4: Verify checklist item count is valid**

The checklist now has 6 items. Boorman's rule allows 5-9 items, so 6 is within bounds. Verify by counting items in the checklist section.

Run: `grep -c '^\- \[' .claude/agents/centinela-qa.md` (approximate -- verify the Security Verification section specifically)

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/security-audit/SKILL.md .claude/agents/centinela-qa.md
git commit -m "feat: add license compliance scanning to security-audit

Adds dependency license compatibility checking against project MIT license.
Classifies: permissive (Pass), weak copyleft (Warning), strong copyleft (Critical).
Adds checklist item to Centinela Security Verification (now 6 items).

References: Skaife (2021), EPAM (2023), Leroux (2025)"
```

---

### Task 3: Defect Lifecycle in review-findings

**Files:**
- Modify: `.claude/skills/review-findings/SKILL.md`

- [ ] **Step 1: Read current review-findings skill**

Run: `cat -n .claude/skills/review-findings/SKILL.md`
Note the structure: SIGN IN (line ~16), Pre-Fix Preparation (line ~20), FIX phase (line ~26), Implementation Complete (line ~34), SIGN OUT (line ~42).

- [ ] **Step 2: Add defect lifecycle definitions at the top of the skill**

After the SIGN IN section and before the Pre-Fix Preparation TIME OUT, add:

```markdown
### Defect Severity Classification

Every finding in the review report must have a severity:
- **Critical**: Security vulnerability, data loss, system crash
- **Major**: Feature broken, workaround exists but painful
- **Medium**: Incorrect behavior, easy workaround
- **Minor**: Cosmetic, style, naming

### Defect Status Lifecycle

Each finding tracks its status through the Centinela > Forja > Centinela loop:

```
Open (Centinela identifies in review)
  > Assigned (handoff to Forja via review-findings)
    > Implemented (Forja completes fix)
      > Verified (Centinela re-verifies)
        > Closed
```

When reading the review report, update each finding's status from `Open` to `Assigned`.
When fixing is complete, update status to `Implemented`.
Centinela re-verification updates to `Verified` then `Closed`.

### Entry/Exit Criteria

**Entry criteria** (must be true before starting fixes):
- Implementation is complete and all existing tests pass
- Forja's Pre-Delivery checklist has been passed
- Review report exists at `docs/reviews/{feature-name}-review.md`

**Exit criteria** (must be true before handoff back to Centinela):
- All Critical and Major findings have status `Implemented`
- Remaining Minor findings are documented in `TECH_DEBT.md` with justification
- Fix order was respected: Critical > Major > Medium > Minor

### Review Report Finding Format

Each finding in the review report must include:

| Field | Description |
|-------|-------------|
| ID | `F-{NNN}` sequential |
| Severity | Critical / Major / Medium / Minor |
| Status | Open / Assigned / Implemented / Verified / Closed |
| Category | Code Quality / Architecture / Spec Compliance |
| Description | What the issue is |
| Location | `file:line` reference |
| Recommendation | How to fix |
| Verified-By | Agent that verified the fix (populated during re-verification) |

Reference: O'Regan (2019), Ch. 7, sections 7.3-7.5
```

- [ ] **Step 3: Verify the skill file is well-formed**

Run: `wc -l .claude/skills/review-findings/SKILL.md`
Expected: ~100-110 lines (was 45, added ~60).

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/review-findings/SKILL.md
git commit -m "feat: formalize defect lifecycle in review-findings

Adds severity classification (Critical/Major/Medium/Minor),
status lifecycle (Open>Assigned>Implemented>Verified>Closed),
entry/exit criteria, and structured finding format with ID tracking.

Reference: O'Regan (2019) Ch. 7"
```

---

### Task 4: GQM Metrics in release-check

**Files:**
- Modify: `.claude/skills/release-check/SKILL.md`

- [ ] **Step 1: Read current release-check skill**

Run: `cat -n .claude/skills/release-check/SKILL.md`
Note: criteria definitions at lines ~26-54, confidence score at lines ~75-84, report template at lines ~92-117.

- [ ] **Step 2: Add 3 new GQM metrics after existing 5 criteria**

Find the section after criterion 5 (Tech Debt Severity) and before the TIME OUT checklists. Add:

```markdown
### Quality Metrics (GQM — Basili & Rombach 1988)

Every metric below traces to a business goal through a question. No measurement for measurement's sake.

**Criterion 6: Phase Containment Effectiveness (PCE)**
- Goal: Catch defects before release
- Question: What % of defects were found in-phase (by Centinela during review) vs escaped (post-merge)?
- Metric: PCE = (in-phase defects / total defects) * 100
- Threshold: >= 70%
- Data source: Review reports in `docs/reviews/` with finding status fields. In-phase = status reached `Verified`/`Closed`. Escaped = defects found after merge without prior review finding.
- First run: If no review data exists, report "N/A — baseline" (does not fail the gate)

**Criterion 7: Defect Closure Rate**
- Goal: Resolve defects promptly
- Question: Are findings from reviews being closed before release?
- Metric: (Critical+Major findings with status Closed or Verified) / (total Critical+Major findings) * 100
- Threshold: >= 90%
- Data source: All review reports for the current release cycle
- First run: "N/A — baseline"

**Criterion 8: Open Findings Trend**
- Goal: Maintain stable codebase
- Question: Is the defect arrival rate trending down?
- Metric: Compare current open findings count to count at previous release-check
- Threshold: Non-increasing (current <= previous)
- Data source: Previous release-check report in `docs/reviews/`
- First run: "N/A — baseline"

References: Basili & Rombach (1988), O'Regan (2019) Ch. 9.2 (GQM), Ch. 9.3.3 (PCE)
```

- [ ] **Step 3: Update confidence score calculation**

Find the confidence score section (around line 75-84). Update the description to reflect 8 criteria:

Change the formula description from "5 criteria" to "8 criteria". The averaging formula stays the same but includes the 3 new metrics. Add a note:

```markdown
**Confidence score**: Average of all evaluated criteria scores (0-100 each). Criteria reporting "N/A — baseline" are excluded from the average (they neither help nor hurt the score). When all 8 criteria have data, the full 8-point average applies.
```

- [ ] **Step 4: Update the report template**

Find the structured report template (around line 92-117). Add a "Quality Metrics (GQM)" section to the report format, after the existing criteria table:

```markdown
### Quality Metrics (GQM)

| # | Goal | Question | Metric | Value | Threshold | Status |
|---|------|----------|--------|-------|-----------|--------|
| 6 | Catch defects before release | What % found in-phase? | PCE | {value}% | >= 70% | {PASS/FAIL/N/A} |
| 7 | Resolve defects promptly | Critical+Major closure rate? | Closure Rate | {value}% | >= 90% | {PASS/FAIL/N/A} |
| 8 | Maintain stable codebase | Is arrival rate declining? | Open Trend | {current} vs {previous} | Non-increasing | {PASS/FAIL/N/A} |
```

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/release-check/SKILL.md
git commit -m "feat: add GQM-based quality metrics to release-check

Adds 3 new criteria: Phase Containment Effectiveness (PCE),
Defect Closure Rate, and Open Findings Trend. Gate expands
from 5 to 8 criteria. Baseline-safe: first run reports N/A.

References: Basili & Rombach (1988) GQM, O'Regan (2019) Ch. 9"
```

---

### Task 5: CI/CD Strategy ADR

**Files:**
- Create: `docs/adr/ADR-002-cicd-strategy.md`

- [ ] **Step 1: Create the ADR file**

Write the following to `docs/adr/ADR-002-cicd-strategy.md`:

```markdown
# ADR-002: CI/CD Strategy

**Date**: 2026-03-29
**Status**: Accepted
**Context**: Agent Triforce Pipeline Architecture

## Context

Agent Triforce has three CI workflow templates in `templates/ci/` (pr-review.yml, security-audit.yml, release-check.yml) but lacks a documented strategy explaining:
- Why these specific pipeline stages were chosen
- How quality gates map to the development workflow
- What branching model the project follows
- How the pipeline stages relate to each other

## Decision

### Branching Model: Git Flow-Lite

Formalize the branching convention already implicit in CLAUDE.md:

- **`main`**: Always releasable. Protected branch. Merges only via PR.
- **Feature branches**: `{type}/{ticket-short-description}` where type is one of: `feat/`, `fix/`, `refactor/`, `docs/`, `test/`, `chore/`
- **Release tags**: `v{major}.{minor}.{patch}` following Semantic Versioning
- **No develop branch**: `main` serves as both integration and release branch. Simplicity over ceremony.

### Pipeline Stages and Quality Gates

| Stage | Trigger | What Runs | Agent | Gate | Speed |
|-------|---------|-----------|-------|------|-------|
| **Commit** | Push to any branch | Lint, unit tests, `security-scanner.py` patterns | None (automated) | All checks pass | Fast (<2 min) |
| **PR Review** | PR opened/updated | Centinela code review | Centinela (Haiku) | No Critical/High findings | Medium (~5 min) |
| **Merge to main** | PR merged | Full security-audit + license compliance | Centinela (Haiku) | No Critical findings | Medium (~10 min) |
| **Release** | Tag `v*` pushed | release-check (all 8 criteria) | Centinela (Sonnet) | GO verdict, confidence >= 70 | Slow (~10 min) |

### Quality Gate Philosophy

- **CI gates are binary**: pass or fail. A PR with a Critical finding cannot merge. This aligns with the principle that fast feedback should be unambiguous.
- **Release decisions are nuanced**: The release-check produces a continuous confidence score (0-100) alongside the GO/NO-GO verdict. A score of 72 (GO) tells you more than a simple "pass."
- **Fail fast, verify thoroughly**: Commit-stage checks are cheap and fast (lint, unit tests). Each subsequent stage adds depth but also cost. This is a deliberate trade-off.

### Static Analysis Mapping

The project does not integrate SonarQube or similar server-based tools. Instead, Centinela's skills provide equivalent coverage:

| SonarQube Concept | Agent Triforce Equivalent | Skill |
|---|---|---|
| Code smells | Clean Code violations (>30 line functions, >3 nesting) | code-health |
| Bugs | Defect findings in code review | review-findings |
| Vulnerabilities | OWASP Top 10 scan | security-audit |
| Duplications | Dead code detection, DRY violations | code-health |
| Coverage | Test coverage threshold (80%) | release-check |
| License compliance | Dependency license scan | security-audit |

### Template Installation

The CI templates in `templates/ci/` are ready to use. To install:

1. Copy templates: `cp -r templates/ci/ .github/workflows/`
2. Set `ANTHROPIC_API_KEY` as a GitHub repository secret
3. (Optional) Adjust model and timeout settings in workflow files

See `agent-triforce/commands/ci-setup.md` for detailed instructions.

## Consequences

- All PRs go through Centinela review before merge
- Security audit runs on every merge to main, not just releases
- License compliance is checked at merge time (catches issues early)
- Release confidence score enables data-driven release decisions
- No additional infrastructure required -- GitHub Actions + Anthropic API only

## References

- Rossel, S. (2017). *Continuous Integration, Delivery, and Deployment*. Packt Publishing. Ch. 1 (CI/CD foundations, quality gates), Ch. 3 (branching models, tagging).
- Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley. (Pipeline stage design principles)
```

- [ ] **Step 2: Verify the file**

Run: `head -5 docs/adr/ADR-002-cicd-strategy.md`
Expected: Shows the ADR header.

- [ ] **Step 3: Commit**

```bash
git add docs/adr/ADR-002-cicd-strategy.md
git commit -m "docs: add ADR-002 CI/CD strategy

Documents branching model (Git Flow-lite), pipeline stages
with quality gates, static analysis mapping, and quality
gate philosophy (binary CI gates, nuanced release decisions).

Reference: Rossel (2017)"
```

---

### Task 6: FURPS and COPQ in code-health

**Files:**
- Modify: `.claude/skills/code-health/SKILL.md`

- [ ] **Step 1: Read current code-health skill**

Run: `cat -n .claude/skills/code-health/SKILL.md`
Note: SCAN phase at lines ~18-46 with 6 subsections (dead code, dependencies, clean code, architecture, TODOs, flaky tests).

- [ ] **Step 2: Reorganize scan sections under FURPS categories**

Replace the existing SCAN phase content (the 6 subsections) with FURPS-categorized sections. Keep all existing checks -- just regroup them under the FURPS framework and add the new docstring check:

```markdown
### SCAN — Quality Attribute Assessment (FURPS)

Organize findings by quality attribute category (FURPS model, Hewlett-Packard):

**F — Functionality**
- Dead code: unused imports, unreachable functions, unused variables, commented-out code blocks
- Dead exports: public functions/classes never imported by other modules

**R — Reliability**
- Test flakiness indicators: timing-dependent assertions, shared mutable state between tests, non-deterministic data, missing test isolation
- Dependency vulnerabilities: run `pip audit` (Python) or `npm audit` (Node), flag Critical/High CVEs

**P — Performance (complexity proxies)**
- Files exceeding 300 lines
- Functions exceeding 30 lines
- Nesting depth exceeding 3 levels
- These are complexity proxies that correlate with performance and maintainability issues

**S — Supportability**
- Architecture compliance: dependency direction follows Clean Architecture (inward), layer separation enforced, folder structure reveals intent (Screaming Architecture)
- TODO/FIXME without linked issue or ticket reference
- Missing docstrings on public API functions: any function or class without a leading underscore in `src/` files that lacks a docstring. Excludes test files and internal helpers (functions starting with `_`)

Note: **U (Usability)** is not assessed at code-health level — this is a product concern owned by Prometeo.

### Cost of Quality (COPQ) Classification

Categorize each finding by cost type (Feigenbaum 1956, O'Regan 2019):

- **Prevention cost**: Items that prevent defects if addressed (test coverage gaps, missing type hints, missing docstrings)
- **Appraisal cost**: Items that affect defect detection capability (flaky tests, weak assertions, inadequate test isolation)
- **Internal failure cost**: Defects already present, found internally (dead code, broken imports, architecture violations)
- **External failure cost**: Issues that could escape to users if not addressed (security vulnerabilities, missing error handling, unvalidated inputs)

In the code-health report, tag each finding with its FURPS category and COPQ type. Reports heavy on "external failure" items are more urgent than those with mostly "prevention" items.

References: FURPS (Hewlett-Packard), cited in Callejas-Cuervo et al. (2017). COPQ (Feigenbaum 1956), presented in O'Regan (2019) Ch. 9.3.5.
```

- [ ] **Step 3: Verify the file is well-formed**

Run: `wc -l .claude/skills/code-health/SKILL.md`
Expected: ~85-95 lines (was 60, scan section expanded).

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/code-health/SKILL.md
git commit -m "feat: reorganize code-health under FURPS quality attributes

Groups existing checks under Functionality, Reliability, Performance,
Supportability categories. Adds public API docstring check. Adds
Cost of Quality (COPQ) classification for finding prioritization.

References: FURPS (HP, Callejas-Cuervo 2017), COPQ (O'Regan 2019)"
```

---

### Task 7: CLAUDE.md Updates

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Read the Software Engineering Principles section**

Run: `sed -n '111,157p' CLAUDE.md`
Confirm the exact location of:
- Testing subsection (should be around line 133)
- Other subsection (should be around line 154)
- End of Software Engineering Principles section

- [ ] **Step 2: Add Quality Models & Measurement subsection**

After the "Specifications" subsection (around line 119) and before the "Architecture" subsection (around line 121), add:

```markdown
### Quality Models & Measurement (ISO 25010 + GQM)
- Quality attributes follow **ISO/IEC 25010**: functional suitability, reliability, security, maintainability, performance efficiency, usability, compatibility, portability — each mapped to an owning agent (see ADR-001)
- Measurement follows **GQM** (Basili & Rombach 1988): every metric traces to a Goal through a Question. No measurement for measurement's sake
- Test documentation follows **IEEE 829**: test case IDs, structured reporting, traceability
```

- [ ] **Step 3: Add defect lifecycle and PCE to Testing subsection**

After the existing "Integrity levels" content (around line 147), add:

```markdown
- **Defect lifecycle**: Open > Assigned > Implemented > Verified > Closed (tracked in review reports)
- **Entry criteria** (before review): implementation complete, tests pass, Pre-Delivery checklist passed
- **Exit criteria** (after fixes): all Critical/Major Closed, Minor documented in TECH_DEBT.md
- **Phase Containment Effectiveness (PCE)**: % of defects found in-phase by Centinela vs escaped post-merge — target >= 70%
```

- [ ] **Step 4: Add FURPS and COPQ to Other subsection**

After the existing "Design Patterns (GoF)" line (around line 156), add:

```markdown
- **FURPS** (Hewlett-Packard): quality attribute categories used in code-health — Functionality, Reliability, Performance, Supportability
- **Cost of Quality**: findings classified as prevention, appraisal, internal failure, or external failure cost (Feigenbaum)
```

- [ ] **Step 5: Add License Compliance subsection**

After the "Code Standards" subsection in Project Conventions (after the line "All public APIs documented with OpenAPI/Swagger"), add:

```markdown
### License Compliance
- Project license: **MIT** — permissive, allows commercial use and proprietary derivatives
- Dependency rule: no strong copyleft (GPL, AGPL) in dependency tree — incompatible with MIT distribution
- Weak copyleft (LGPL, MPL) requires documented justification in an ADR
- Enforced by security-audit skill during every audit
```

- [ ] **Step 6: Verify CLAUDE.md is well-formed**

Run: `wc -l CLAUDE.md`
Expected: ~240-250 lines (was ~196, added ~45 lines).

Verify no duplicate sections:
Run: `grep -n "### " CLAUDE.md`
Expected: Each subsection header appears exactly once.

- [ ] **Step 7: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add quality models, defect lifecycle, and license compliance to CLAUDE.md

Adds Quality Models & Measurement (ISO 25010, GQM, IEEE 829),
defect lifecycle with entry/exit criteria and PCE, FURPS/COPQ
references, and License Compliance section.

References: ISO 25010, Basili & Rombach (1988), O'Regan (2019),
Callejas-Cuervo (2017), Feigenbaum (1956)"
```

---

### Task 8: CHANGELOG and Final Verification

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add release entry to CHANGELOG**

Add a new unreleased section at the top of CHANGELOG.md (after the header, before the `[0.7.0]` entry):

```markdown
## [0.8.0] - 2026-03-29

### Added
- ADR-001: Quality Model & Standards Foundation — ISO/IEC 25010 mapping, GQM instantiation, academic bibliography
- ADR-002: CI/CD Strategy — branching model, pipeline stages, quality gate philosophy, static analysis mapping
- License compliance scanning in security-audit skill — copyleft/permissive dependency classification
- Defect lifecycle management in review-findings — severity classification, status tracking (Open>Assigned>Implemented>Verified>Closed), entry/exit criteria
- GQM-based quality metrics in release-check — Phase Containment Effectiveness (PCE), Defect Closure Rate, Open Findings Trend (criteria 6-8)
- FURPS quality attribute categorization in code-health — Functionality, Reliability, Performance, Supportability
- Cost of Quality (COPQ) classification in code-health — prevention, appraisal, internal failure, external failure
- Public API docstring check in code-health
- License Compliance section in CLAUDE.md
- Quality Models & Measurement section in CLAUDE.md

### Changed
- security-audit: added license compliance scan section and checklist item (Security Verification now 6 items)
- release-check: expanded from 5 to 8 criteria with GQM section in report template
- code-health: reorganized scan under FURPS categories with COPQ tagging
- review-findings: added defect severity, status lifecycle, entry/exit criteria, structured finding format
- CLAUDE.md: added quality models, defect lifecycle, FURPS/COPQ, and license compliance references
```

- [ ] **Step 2: Run all existing tests to verify nothing broke**

Run: `cd /Users/artemiopadilla/Documents/repos/GitHub/personal/claude-triforce-template && python -m pytest tests/ -v`
Expected: All existing tests pass. The changes are to markdown skill/agent definitions, not Python code, so no test regressions are expected.

- [ ] **Step 3: Verify all new files exist**

Run:
```bash
ls -la docs/adr/ADR-001-quality-model-standards.md docs/adr/ADR-002-cicd-strategy.md
```
Expected: Both files exist.

- [ ] **Step 4: Verify modified files are consistent**

Run:
```bash
grep -c "FURPS" .claude/skills/code-health/SKILL.md
grep -c "License Compliance" .claude/skills/security-audit/SKILL.md
grep -c "Defect Severity" .claude/skills/review-findings/SKILL.md
grep -c "PCE" .claude/skills/release-check/SKILL.md
grep -c "License Compliance" CLAUDE.md
```
Expected: Each returns >= 1 match, confirming all sections were added.

- [ ] **Step 5: Commit CHANGELOG**

```bash
git add CHANGELOG.md
git commit -m "docs: update CHANGELOG for v0.8.0 quality integration release"
```

- [ ] **Step 6: Final commit — design spec and plan**

```bash
git add docs/superpowers/specs/2026-03-29-quality-integration-design.md docs/superpowers/plans/2026-03-29-quality-integration.md
git commit -m "docs: add quality integration design spec and implementation plan"
```
