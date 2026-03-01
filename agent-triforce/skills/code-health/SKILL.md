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
3. Scan for Clean Code violations:
   - Functions longer than 30 lines
   - Files longer than 300 lines
   - Deeply nested code (>3 levels of indentation)
   - Duplicated logic blocks (DRY violations)
   - Primitive obsession (raw strings/ints where a domain type belongs)
   - Feature envy (methods that use another class's data more than their own)
   - God classes (classes with too many responsibilities)
4. Verify architecture compliance:
   - Dependency direction: does business logic depend on frameworks or infrastructure?
   - Layer leakage: are there imports that cross architectural boundaries incorrectly?
   - Screaming Architecture: does folder structure reveal intent?
5. Check TODO/FIXME comments — do they have issue references?

**⏸️ TIME OUT — Scan Complete Checklist (DO-CONFIRM):**
- [ ] All source directories scanned (not just `src/` — also `tests/`, config files)
- [ ] Dead code findings verified (not false positives from dynamic imports or plugins)
- [ ] Dependency vulnerabilities checked with automated tools
- [ ] Findings prioritized: Critical > Warning > Suggestion
- [ ] Previous scan findings compared — are old issues resolved or recurring?

**SIGN OUT:**
6. Write findings to `docs/reviews/code-health-{date}.md`
7. Write the Findings Handoff-to-Forja using the communication checklist
8. Run the SIGN OUT checklist from your agent file
