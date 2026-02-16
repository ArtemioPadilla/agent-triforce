---
name: review-findings
description: >
  Addresses and fixes findings from a QA code review. Reads the review report,
  fixes critical and warning issues, and prepares for re-verification.
context: fork
agent: forja-dev
---

Fix the findings from the QA review: $ARGUMENTS

If no specific review is mentioned, look for the most recent review in `docs/reviews/`.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Surface any concerns about the findings — complexity, risk, dependencies

**⏸️ TIME OUT — Pre-Fix Preparation (READ-DO):**
1. Read the review report in `docs/reviews/`
2. Understand each finding's root cause BEFORE writing any fix
3. Plan the fix order: Critical first, then Warnings
4. Identify if any fixes could conflict with each other

**FIX:**
5. For each finding: understand root cause, implement fix, add/update tests, document
6. Scan for dead code after all fixes

**⏸️ TIME OUT — Run Implementation Complete + Pre-Delivery Checklists (DO-CONFIRM):**
7. Run the Implementation Complete checklist from your agent file
8. Run the Pre-Delivery checklist from your agent file
Additionally verify:
- [ ] Every Critical finding addressed
- [ ] Every Warning addressed (or explicitly deferred with justification)
- [ ] No new issues introduced by the fixes

**SIGN OUT:**
9. Write a Fix Report using the Fix Report checklist from your agent file
10. Run the SIGN OUT checklist from your agent file
