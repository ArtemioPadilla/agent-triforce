---
name: traceability
description: >
  Generates a spec-to-implementation traceability matrix linking acceptance
  criteria from specs to implementation files, test cases, and review findings.
  Supports IEEE 830 compliance audits.
context: fork
agent: centinela-qa
---

Generate a traceability matrix for a feature spec.

**Input**: The user provides a spec file path (e.g., `docs/specs/auth-feature.md`) or feature name.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Read the specified spec file

**EXTRACT:**
1. Parse the spec for acceptance criteria in GIVEN/WHEN/THEN format
2. Assign stable criterion IDs in format `{feature-id}-AC-{NNN}` if not already present
3. Extract: criterion ID, criterion text, any referenced modules or components

**TRACE:**
4. For each acceptance criterion, scan `src/` for implementation files:
   - Search for function names, class names, or module names referenced in the criterion
   - Search for comments referencing the criterion ID
   - Use `tools/traceability.py` if available for automated scanning
5. For each acceptance criterion, scan `tests/` for test cases:
   - Search for test names that reference the criterion or its subject
   - Search for test docstrings mentioning the criterion
   - Search for comments with criterion IDs
6. For each acceptance criterion, scan `docs/reviews/` for findings:
   - Search review files for references to the criterion or its subject
   - Link findings by severity

**GENERATE MATRIX:**
7. Create the traceability matrix at `docs/traceability/{feature-name}-matrix.md`:
   ```markdown
   # Traceability Matrix: {Feature Name}
   **Spec**: {spec_file_path}
   **Generated**: {YYYY-MM-DD}
   **Status**: {X covered / Y partial / Z missing}

   | ID | Criterion | Implementation | Tests | Findings | Status |
   |----|-----------|---------------|-------|----------|--------|
   | {id} | {text} | {files} | {tests} | {findings} | Covered/Partial/Missing |
   ```
8. Status determination:
   - **Covered**: has implementation file(s) AND at least one test
   - **Partial**: has implementation but no test, or has test but unclear implementation link
   - **Missing**: no implementation or test found

**TIME OUT — Traceability Verification (DO-CONFIRM):**
- [ ] All acceptance criteria extracted from spec
- [ ] Criterion IDs assigned (stable, format: `{feature}-AC-{NNN}`)
- [ ] `src/` scanned for implementation links
- [ ] `tests/` scanned for test coverage links
- [ ] `docs/reviews/` scanned for finding references
- [ ] Each criterion has a status (Covered/Partial/Missing)
- [ ] Missing criteria flagged with `/generate-tests` recommendation

**SIGN OUT:**
9. Report matrix summary (covered/partial/missing counts)
10. If any criteria are Missing, suggest running `/generate-tests` on the relevant modules
11. Run the SIGN OUT checklist from your agent file
