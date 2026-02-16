---
name: feature-spec
description: >
  Creates a complete product feature specification. Use when defining new features,
  writing user stories, or planning product work. Generates structured specs in docs/specs/.
context: fork
agent: prometeo-pm
---

Create a feature specification for: $ARGUMENTS

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Surface any initial concerns about this feature request

**RESEARCH (READ-DO):**
1. Read existing specs in `docs/specs/` to understand current patterns and avoid conflicts
2. Identify dependencies on existing features or systems

**BUILD:**
3. Create a comprehensive spec at `docs/specs/{feature-name}.md` using the template from your system prompt
4. Ensure all acceptance criteria are testable and unambiguous
5. List all dependencies, risks, and open questions

**⏸️ TIME OUT — Run Spec Completion Checklist (DO-CONFIRM):**
6. Run through every item in the Spec Completion checklist from your agent file
7. Fix any gaps BEFORE proceeding

**SIGN OUT:**
8. Write the Handoff-to-Forja using the communication checklist
9. Run the SIGN OUT checklist from your agent file
