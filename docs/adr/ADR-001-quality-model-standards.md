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
