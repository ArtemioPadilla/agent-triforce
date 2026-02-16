---
name: implement-feature
description: >
  Implements a feature from its specification. Reads the spec, designs architecture,
  writes code, tests, and documentation. Use after a feature spec has been approved.
context: fork
agent: forja-dev
---

Implement the feature: $ARGUMENTS

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Run the Receiving-from-Prometeo checklist to verify the spec handoff
- If significant architecture decisions are needed, create an ADR in `docs/adr/`

**BUILD:**
1. Define interfaces/contracts first
2. Implement the feature in `src/` following project conventions
3. Write tests in `tests/` (unit + integration for critical paths)
4. Scan for and remove any dead code you introduced or found

**⏸️ TIME OUT — Run Implementation Complete Checklist (DO-CONFIRM):**
5. Run through every item in the Implementation Complete checklist from your agent file
6. Fix any failures BEFORE proceeding

**⏸️ TIME OUT — Run Pre-Delivery Checklist (DO-CONFIRM):**
7. Run through every item in the Pre-Delivery checklist from your agent file
8. Fix any failures BEFORE proceeding

**SIGN OUT:**
9. Write the Handoff-to-Centinela using the communication checklist
10. Run the SIGN OUT checklist from your agent file
