# Quality Integration Design: Standards, Metrics, and Compliance

**Date**: 2026-03-29
**Status**: Approved
**Goal**: Integrate formal software quality models, test metrics, defect lifecycle management, license compliance, and CI/CD strategy into Agent Triforce -- practical production hardening with academic traceability.

## Approach

Layered Integration: documentation as the knowledge base (ADRs), then agent behavior enhancements that reference and enforce it. Prefer enhancing existing skills over creating new ones.

## Priority Order

1. Quality Model & Standards ADR
2. Enhance security-audit with license compliance
3. Formalize defect lifecycle in review-findings
4. GQM-based metrics in release-check
5. CI/CD Strategy ADR
6. FURPS-inspired quality attributes in code-health
7. CLAUDE.md updates

---

## 1. Quality Model & Standards ADR

**Deliverable**: `docs/adr/ADR-001-quality-model-standards.md`

**Content**:
- **Context**: Agent Triforce implements quality assurance through 3 agents with checklists, but lacks explicit traceability to recognized quality standards.
- **Decision**: Adopt a hybrid quality model drawing from ISO/IEC 25010 (product quality), GQM (measurement), and IEEE 829 (test documentation) as the theoretical foundation.
- **Mapping table**: Each ISO 25010 quality attribute (functional suitability, reliability, security, maintainability, performance efficiency, usability, compatibility, portability) mapped to which agent owns it and which skill enforces it.
- **GQM instantiation**: 3-4 concrete Goal > Question > Metric chains:
  - Goal: "Reduce escaped defects" > Question: "What % of defects found by Centinela vs post-release?" > Metric: Phase Containment Effectiveness (PCE)
  - Goal: "Ensure release readiness" > Question: "Are all critical findings resolved?" > Metric: Defect Closure Rate
  - Goal: "Maintain codebase health" > Question: "Is defect arrival rate stable or declining?" > Metric: Open Findings Trend
  - Goal: "Ensure legal compliance" > Question: "Are all dependencies license-compatible?" > Metric: % of dependencies with permissive-compatible licenses (target: 100%)
- **Why ISO 25010 over ISO 9126**: 25010 supersedes 9126 (2011), adds security as a first-class quality attribute (aligns with Centinela's security-audit).
- **Academic references**: Full bibliography section.

**References**:
- ISO/IEC 25010:2011, Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE)
- Callejas-Cuervo, M., Alarcon-Aldana, A.C., & Alvarez-Carreno, A.M. (2017). Modelos de calidad del software, un estado del arte. *Entramado*, 13(1), 230-244.
- Basili, V.R. & Rombach, H.D. (1988). The TAME Project: Towards Improvement-Oriented Software Environments. *IEEE TSE*, 14(6), 758-773.

---

## 2. Enhance security-audit with License Compliance

**Files modified**: `.claude/skills/security-audit/SKILL.md`, `.claude/agents/centinela-qa.md`

**New section in security-audit SKILL.md** -- "License Compliance Scan":
- Check all direct dependencies have an explicit license
- Flag copyleft licenses (GPL, AGPL) as Critical -- incompatible with MIT for distribution
- Flag weak copyleft (LGPL, MPL) as Warning with explanation
- Permissive licenses (MIT, BSD, Apache 2.0, Unlicense) pass automatically
- Uses `pip-licenses` (Python) or `license-checker` (Node) when available, falls back to manual dependency manifest scan

**New checklist item** in Centinela's Security Verification TIME OUT:
- "Verify dependency license compatibility with project license (MIT)"

**Output**: License compatibility table added to security audit report (`docs/reviews/security-audit-{date}.md`) with a "License Risk" severity:
- Critical: GPL/AGPL in dependency tree
- Warning: LGPL/MPL in dependency tree
- Info: All dependencies permissive-compatible

**References**:
- Skaife, D. (2021). A Short Guide to Open Source Licenses. *Nationwide Technology / Medium*.
- EPAM SolutionsHub (2023). Open Source Licenses: Definition, Types, and Comparison.
- Leroux, S. (2025). Popular Open Source Licenses and How to Choose Them. *It's FOSS*.

---

## 3. Formalize Defect Lifecycle in review-findings

**Files modified**: `.claude/skills/review-findings/SKILL.md`, review report template

**Defect severity classification** (standardized):
- **Critical**: Security vulnerability, data loss, system crash
- **Major**: Feature broken, workaround exists but painful
- **Medium**: Incorrect behavior, easy workaround
- **Minor**: Cosmetic, style, naming

**Defect status lifecycle**:
```
Open (Centinela identifies)
  > Assigned (handoff to Forja)
    > Implemented (Forja fixes)
      > Verified (Centinela re-verifies)
        > Closed
```

Maps to existing workflow: review creates findings (Open), Forja receives handoff (Assigned), implements fixes (Implemented), Centinela re-verifies (Verified/Closed).

**Entry/exit criteria** added to skill:
- **Entry**: Implementation complete, all tests pass, Forja's Pre-Delivery checklist passed
- **Exit**: All Critical/Major findings Closed, remaining Minor findings documented in TECH_DEBT.md

**Review report template update**: Each finding gets:
- Status field (Open/Assigned/Implemented/Verified/Closed)
- `Verified-By` field populated during re-verification

**Fix order**: Critical > Major > Medium > Minor (now explicit).

**What doesn't change**: The existing 3-dimension review template (Code Quality, Architecture, Spec Compliance) stays intact.

**References**:
- O'Regan, G. (2019). *Concise Guide to Software Testing*, Ch. 7, sections 7.3-7.5.

---

## 4. GQM-Based Metrics in release-check

**Files modified**: `.claude/skills/release-check/SKILL.md`

**3 new metrics** added to existing 5-point gate:

| # | Goal | Question | Metric | Threshold |
|---|------|----------|--------|-----------|
| 6 | Catch defects before release | What % of defects found in-phase vs escaped? | **Phase Containment Effectiveness (PCE)** | >= 70% |
| 7 | Resolve defects promptly | Are findings from reviews being closed? | **Defect Closure Rate** | >= 90% Critical+Major closed |
| 8 | Maintain stable codebase | Is defect arrival rate trending down? | **Open Findings Trend** | Non-increasing |

**Data sources**:
- **PCE**: Review reports in `docs/reviews/` with status lifecycle from Section 3. In-phase = found by Centinela during review. Escaped = discovered post-merge or by users.
- **Defect Closure Rate**: Findings with status Closed/Verified divided by total findings across all reviews for the release.
- **Open Findings Trend**: Compare current open findings count to count at last release-check report.

**Changes**:
- Confidence score: 8 criteria averaged 0-100 (was 5)
- Report template gains "Quality Metrics (GQM)" section showing goal-question-metric chain
- First run: metrics 6-8 report "N/A -- baseline" instead of failing

**References**:
- Basili, V.R. & Rombach, H.D. (1988). GQM paradigm.
- O'Regan, G. (2019). *Concise Guide to Software Testing*, Ch. 9.2 (GQM), Ch. 9.3.3 (PCE, Figs. 9.9-9.13).

---

## 5. CI/CD Strategy ADR

**Deliverable**: `docs/adr/ADR-002-cicd-strategy.md`

**Content**:

**Branching model** (Git Flow-lite, formalizing existing CLAUDE.md convention):
- `main` is always releasable
- Feature branches: `{type}/{ticket-short-description}`
- Merge via PR, tags trigger releases

**Pipeline stages mapped to quality gates**:

| Stage | Trigger | What Runs | Gate |
|-------|---------|-----------|------|
| Commit | Push to any branch | Lint, unit tests, security-scanner patterns | All pass |
| PR Review | PR opened/updated | Centinela code review (`pr-review.yml`) | No Critical/High findings |
| Merge to main | PR merged | Full security-audit + license compliance (`security-audit.yml`) | No Critical findings |
| Release | Tag `v*` pushed | release-check with all 8 criteria (`release-check.yml`) | GO verdict, confidence >= 70 |

**Quality gate philosophy**: Gates are binary (pass/fail) but release-check provides continuous confidence score. CI gates should be fast and strict; release decisions benefit from nuance.

**SonarQube note**: Not integrated (project is agent-based), but ADR acknowledges SonarQube-style static analysis and maps concepts to Centinela's code-health.

**What doesn't change**: The 3 existing CI templates in `templates/ci/` stay as-is.

**References**:
- Rossel, S. (2017). *Continuous Integration, Delivery, and Deployment*, Ch. 1 (foundations, quality gates), Ch. 3 (branching models).

---

## 6. FURPS-Inspired Quality Attributes in code-health

**Files modified**: `.claude/skills/code-health/SKILL.md`

**Reorganize existing checks under FURPS categories** (mostly reframing, not new logic):
- **F (Functionality)**: Dead code detection (existing)
- **U (Usability)**: Not applicable at code-health level (Prometeo's domain)
- **R (Reliability)**: Test flakiness indicators (existing), dependency vulnerabilities (existing)
- **P (Performance)**: Files >300 lines, functions >30 lines, nesting >3 levels (existing)
- **S (Supportability)**: Architecture compliance (existing), commented-out code (existing), missing docstrings on public API functions (new)

**One new check**: Missing docstrings on public API functions -- any function/class without a leading underscore in `src/` files that lacks a docstring. Excludes test files and internal helpers.

**Cost of Quality (COPQ) tracking** -- new section in code-health report:
- **Prevention cost**: Items that prevent defects (test coverage gaps, missing type hints)
- **Appraisal cost**: Items that detect defects (flaky tests, weak assertions)
- **Internal failure cost**: Defects found internally (dead code, broken imports)
- **External failure cost**: Items that could escape to users (security vulnerabilities, missing error handling)

Not dollar figures -- categorization for prioritization. A report heavy on "external failure" items is more urgent than one with mostly "prevention" items.

**References**:
- FURPS model (Hewlett-Packard), as cited in Callejas-Cuervo et al. (2017).
- Cost of Quality (Feigenbaum, 1950s), as presented in O'Regan (2019), Ch. 9.3.5.

---

## 7. CLAUDE.md Updates

**File modified**: `CLAUDE.md`

**Additions** (~40-50 lines total):

1. **New subsection** `### Quality Models & Measurement` under Software Engineering Principles:
   - Project quality framework: ISO/IEC 25010, GQM, IEEE 829
   - Reference to Quality Model ADR
   - GQM principle: "Every metric must trace to a Goal through a Question"

2. **Enhance "Testing" subsection** -- add after existing test design techniques:
   - Defect lifecycle: Open > Assigned > Implemented > Verified > Closed
   - Entry/exit criteria (one sentence each)
   - Phase Containment Effectiveness concept

3. **Enhance "Other" subsection** -- add:
   - FURPS quality attribute categories
   - Cost of Quality: prevention/appraisal/internal failure/external failure

4. **New subsection** `### License Compliance`:
   - Project license: MIT
   - Dependency compatibility rule: no copyleft; weak copyleft requires justification
   - Enforced by security-audit skill

**What stays the same**: All existing principles untouched.

---

## Full Bibliography

### Software Testing & Quality Assurance
- O'Regan, G. (2019). *Concise Guide to Software Testing*. Undergraduate Topics in Computer Science. Springer. ISBN 978-3-030-28494-7.
  - Ch. 7: Test Execution and Management (pp. 133-144)
  - Ch. 9: Test Metrics and Problem-Solving (pp. 153-179)
- Basili, V.R. & Rombach, H.D. (1988). The TAME Project: Towards Improvement-Oriented Software Environments. *IEEE Transactions on Software Engineering*, 14(6), 758-773.
- IEEE 829-2008. IEEE Standard for Software and System Test Documentation.

### Software Quality Models
- ISO/IEC 25010:2011. Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE) -- System and software quality models.
- ISO/IEC 9126-1:2001. Software engineering -- Product quality (superseded by 25010).
- Callejas-Cuervo, M., Alarcon-Aldana, A.C., & Alvarez-Carreno, A.M. (2017). Modelos de calidad del software, un estado del arte. *Entramado*, 13(1), 230-244. doi:10.18041/entramado.2017v13n1.25125
- Feigenbaum, A.V. (1956). Total Quality Control. *Harvard Business Review*, 34(6), 93-101.
- Crosby, P.B. (1979). *Quality Is Free*. McGraw-Hill.

### Open Source Licensing
- Skaife, D. (2021, January 4). A Short Guide to Open Source Licenses. *Nationwide Technology / Medium*.
- EPAM SolutionsHub (2023, February 3). Open Source Licenses: Definition, Types, and Comparison.
- Leroux, S. (2025, January 20). Popular Open Source Licenses and How to Choose Them. *It's FOSS*.

### CI/CD
- Rossel, S. (2017). *Continuous Integration, Delivery, and Deployment: Reliable and Faster Software Releases with Automating Builds, Tests, and Deployment*. Packt Publishing. ISBN 978-1-78728-661-0.

### Checklist Methodology (existing foundation)
- Gawande, A. (2009). *The Checklist Manifesto: How to Get Things Right*. Metropolitan Books.
- Boorman, D. (2001). Today's Electronic Checklists Reduce Likelihood of Crew Errors and Help Prevent Incidents and Accidents. *ICAO Journal*, 56(1), 17-20, 36.
