# RISK REGISTER

All remain ACTIVE until target/implementation evidence closes them. Canonical mitigations: `docs/architecture/PRIVILEGE_AND_SAFETY.md` and `docs/evidence/RISK_TRANSMUTATION.md`.

| ID | Risk | Primary gate |
|---|---|---|
| RISK-001 | unsafe privileged actuation | typed gateway + E-005 + rollback |
| RISK-002 | tweak/benchmark superstition | causal experiments + user-visible outcomes |
| RISK-003 | telemetry self-interference | two-speed capture + E-002 |
| RISK-004 | controller conflict/oscillation | shadow/no-op + serialization + hysteresis + verify |
| RISK-005 | Huawei policy misclassification | vendor-policy state + E-004 + documented settings |
| RISK-006 | cross-app telemetry leakage | local-first + redacted export + `.gitignore` |
