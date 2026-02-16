# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
<!-- PM adds planned features here -->

### Added
<!-- Dev adds new features here -->

### Changed
- **CLAUDE.md**: Replaced Activation Phenomenon with Three Pause Points framework (SIGN IN / TIME OUT / SIGN OUT — WHO surgical checklist naming). Added Communication Schedule table (6 handoff paths), Error Recovery section with per-agent FLY THE AIRPLANE. Updated Every Agent MUST to reference SIGN IN/SIGN OUT
- **prometeo-pm.md**: Restructured with dedicated `## Checklists` section. 6 checklists: SIGN IN, Spec Completion, NON-NORMAL: Requirement Ambiguity (new), Handoff-to-Forja, Handoff-to-Centinela (new), SIGN OUT (new). Removed inline activation protocol and communication section
- **forja-dev.md**: Restructured with dedicated `## Checklists` section. 9 checklists: SIGN IN, Implementation Complete (split from Pre-Handoff), Pre-Delivery (split from Pre-Handoff), NON-NORMAL: Build Failure Recovery (new), NON-NORMAL: Test Failure Recovery (new), Receiving-from-Prometeo (new), Handoff-to-Centinela, Fix Report, SIGN OUT (new)
- **centinela-qa.md**: Restructured with dedicated `## Checklists` section. 9 checklists: SIGN IN, Security Verification (split from Pre-Verdict), Quality Verification (split from Pre-Verdict), Release Readiness (new), NON-NORMAL: Critical Vulnerability Response, Findings Handoff-to-Forja, Findings Summary-to-Prometeo (new), Receiving-from-Forja (new), SIGN OUT (new)
- **All 6 skills**: Renamed ACTIVATE → SIGN IN, PAUSE → TIME OUT, HANDOFF → SIGN OUT. All checklist references now point to canonical names in agent files

### Fixed
<!-- Dev adds bug fixes here -->

### Security
<!-- QA adds security fixes here -->

### Removed
<!-- Dev adds removed features here -->
