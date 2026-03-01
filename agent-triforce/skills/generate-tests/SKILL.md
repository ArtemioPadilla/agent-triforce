---
name: generate-tests
description: >
  Generates test cases for a module or function following FIRST principles and Arrange-Act-Assert
  pattern. Detects test framework from project config. Use to bootstrap test coverage for existing
  code or as the Red phase of TDD.
context: fork
agent: forja-dev
---

Generate tests for: $ARGUMENTS

If no specific module or function is provided, ask the user which file or function to generate tests for.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Note any existing test conventions in the project (fixtures, helpers, conftest)

**ANALYZE:**
1. Read the target module or function file
2. Identify all public functions, methods, and classes:
   - **Python**: functions/methods NOT prefixed with `_` (single underscore)
   - **TypeScript/JavaScript**: exported functions, classes, and methods only
   - Do NOT generate tests for private/unexported symbols
3. For each public function, extract:
   - Function signature (parameters, types, return type)
   - Docstring or JSDoc description (if present)
   - Business rules implied by the function name and signature
   - Edge cases: null/None inputs, empty collections, boundary values, error conditions

**DETECT FRAMEWORK:**
4. Determine the test framework from project configuration:
   - **Python**: Check for `pyproject.toml` (`[tool.pytest]`), `pytest.ini`, `setup.cfg` -> use **pytest**
   - **TypeScript**: Check `package.json` for `vitest` -> use **Vitest**; check for `jest` -> use **Jest**
   - **JavaScript**: Same as TypeScript
   - If no framework detected, ask the user which to use
5. Detect existing test conventions:
   - Fixture patterns (conftest.py, test helpers, factory functions)
   - Import patterns (absolute vs relative)
   - Naming patterns (test_*, describe/it, should)

**GENERATE:**
6. Determine the test file location following project conventions:
   - **Python**: `tests/` mirroring `src/` structure (e.g., `src/auth/token.py` -> `tests/auth/test_token.py`)
   - **TypeScript**: `tests/` mirroring `src/` or co-located `*.test.ts` files (match existing pattern)
   - Create intermediate directories if needed
7. For each public function, generate:
   - **One happy-path test**: Standard input producing expected output
   - **One edge-case test**: Boundary value, empty input, or error condition
   - Additional branch tests if the function has complex control flow (document branches that could not be inferred)
8. Every test MUST follow the **Arrange-Act-Assert** pattern:
   ```python
   def test_function_does_something():
       # Arrange
       input_data = create_valid_input()

       # Act
       result = function_under_test(input_data)

       # Assert
       assert result == expected_outcome
   ```
9. Every test MUST follow **FIRST** principles:
   - **Fast**: No network calls, no file system dependencies (unless explicitly testing I/O)
   - **Isolated**: No test depends on another test's state
   - **Repeatable**: Same result every run, no randomness without seeding
   - **Self-validating**: Clear pass/fail, no manual inspection needed
   - **Timely**: Tests written before or alongside implementation
10. Add a comment header at the top of the generated test file:
    ```
    # Generated tests -- require human review before merge
    # Generator: /generate-tests
    # Source: {path to source file}
    # Date: {YYYY-MM-DD}
    ```
11. Do NOT hardcode expected values by reading implementation output. Base test expectations on:
    - Function docstrings and type signatures
    - Spec acceptance criteria (if referenced)
    - Logical invariants from the function name and contract
    - Use placeholder comments like `# TODO: verify expected value` when the correct output cannot be inferred from the spec

**FRAMEWORK IDIOMS:**
12. Use framework-specific idioms:
    - **pytest**: Use fixtures, parametrize for multiple cases, `pytest.raises` for exceptions
    - **Vitest/Jest**: Use `describe`/`it` blocks, `beforeEach`/`afterEach`, `expect().toThrow()`
    - Match the project's existing test style if tests already exist

**TIME OUT -- Generated Tests Review (DO-CONFIRM):**
- [ ] Every public function has at least one happy-path and one edge-case test
- [ ] No tests generated for private/unexported functions
- [ ] All tests follow Arrange-Act-Assert pattern
- [ ] No hardcoded values derived from reading implementation output
- [ ] Test file location follows project conventions
- [ ] FIRST principles satisfied (no network, no shared state, deterministic)
- [ ] Comment header present with generation metadata

**SIGN OUT:**
13. Report what was generated:
    - Test file path
    - Number of tests generated per function
    - Functions skipped (private) with count
    - Branches that need manual test authoring (if any)
    - Command to run the generated tests (e.g., `pytest tests/auth/test_token.py -v`)
14. Run the SIGN OUT checklist from your agent file
