---
name: security-audit
description: >
  Deep security audit of code, dependencies, and infrastructure. Checks OWASP Top 10,
  authentication, authorization, data protection, and dependency vulnerabilities.
  Use before releases or after significant changes.
context: fork
agent: centinela-qa
---

Perform a security audit on: $ARGUMENTS

If no specific scope is provided, audit the entire `src/` directory.

Follow these steps:

**SIGN IN:**
- Run the SIGN IN checklist from your agent file
- Note areas of concern based on the scope and past findings

**AUDIT:**
1. **OWASP Top 10** systematic check:
   - A01: Broken Access Control — check auth/authz on all endpoints
   - A02: Cryptographic Failures — check encryption, key management, hashing
   - A03: Injection — SQL, NoSQL, OS command, LDAP injection vectors
   - A04: Insecure Design — business logic flaws, missing rate limits
   - A05: Security Misconfiguration — default configs, verbose errors, CORS
   - A06: Vulnerable Components — `npm audit` / `pip audit`
   - A07: Auth Failures — weak passwords, missing MFA, session management
   - A08: Data Integrity — deserialization, unsigned updates
   - A09: Logging Failures — sensitive data in logs, missing audit trail
   - A10: SSRF — server-side request forgery vectors
2. **Secrets scan**: grep for API keys, tokens, passwords, connection strings
3. **Dependency audit**: check all deps for known CVEs
4. **Smart contracts** (if Solidity): reentrancy, integer overflow, access control, front-running
5. **Architecture review**: Check dependency direction (business logic must not depend on frameworks), verify layer separation (no auth bypass through adapter shortcuts, no direct DB access from use cases)
6. **Test strategy review**: Verify security-critical paths have tests, authentication/authorization flows are integration-tested, input validation has unit tests

If any Critical finding: invoke the NON-NORMAL: Critical Vulnerability Response checklist from your agent file.

**⏸️ TIME OUT — Run Verification Checklists (DO-CONFIRM):**
7. Run through the Security Verification checklist from your agent file
8. Run through the Quality Verification checklist from your agent file
9. Issue verdict based on findings

**SIGN OUT:**
10. Write report to `docs/reviews/security-audit-{date}.md`
11. Write the Findings Handoff-to-Forja using the communication checklist
12. Run the SIGN OUT checklist from your agent file
