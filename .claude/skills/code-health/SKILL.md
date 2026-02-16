---
name: code-health
description: >
  Scans the codebase for dead code, tech debt, outdated dependencies, and code quality
  issues. Use periodically or before releases to maintain code hygiene.
context: fork
agent: centinela-qa
---

Run a comprehensive code health scan on the codebase.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Note any areas of concern based on past scans

**SCAN:**
1. Scan for dead code:
   - Unused imports: `ruff check --select F401 src/` or `biome lint src/`
   - Unused variables/functions: grep for definitions not referenced elsewhere
   - Commented-out code blocks: search for patterns spanning 3+ lines
   - Unreachable code after return/throw/break/continue
   - Files not imported by any other file
2. Check for outdated dependencies:
   - `pip list --outdated` or `npm outdated`
   - Known vulnerabilities: `pip audit` or `npm audit`
3. Scan for code smells:
   - Functions longer than 50 lines
   - Files longer than 500 lines
   - Deeply nested code (>4 levels)
   - Duplicated logic blocks
4. Check TODO/FIXME comments — do they have issue references?

**⏸️ TIME OUT — Scan Complete Checklist (DO-CONFIRM):**
- [ ] All source directories scanned (not just `src/` — also `tests/`, config files)
- [ ] Dead code findings verified (not false positives from dynamic imports or plugins)
- [ ] Dependency vulnerabilities checked with automated tools
- [ ] Findings prioritized: Critical > Warning > Suggestion
- [ ] Previous scan findings compared — are old issues resolved or recurring?

**SIGN OUT:**
5. Write findings to `docs/reviews/code-health-{date}.md`
6. Write the Findings Handoff-to-Forja using the communication checklist
7. Run the SIGN OUT checklist from your agent file
