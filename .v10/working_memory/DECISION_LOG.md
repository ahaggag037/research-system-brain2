# DECISION LOG — compact operational history

Canonical architecture decisions are in `docs/architecture/DECISIONS.md`; this file preserves recovery history.

| ID | Status | Decision | Evidence / reopen |
|---|---|---|---|
| D-001 | ACTIVE | Use only `ahaggag037/research-system-brain2`/`main` as canonical user-repository workspace; no predecessor user repo evidence. | Mission boundary; reopen only if contract changes. |
| D-002 | SUPERSEDED | Remain architecture-neutral during original discovery. | Superseded once evidence converged. |
| D-003 | SUPERSEDED_BY_D-007 | Original V10.3-B selected FH-A1 evidence-gated supervisor. | Historical S-001..S-016; Arm B external research weakened topology. |
| D-004 | ACTIVE | Preserve target uncertainty rather than fabricate device/APK readiness. | No Huawei target available. |
| D-005 | ACTIVE/HISTORICAL_TOOL_LIMIT | Prior cold-start used authenticated GitHub reads after local clone DNS failure. | Re-test during Arm B. |
| D-006 | ACTIVE | Reopen historical completion because independent external Internet research is now mandatory. | Arm B user contract + Q1..Q12. |
| D-007 | ACTIVE | Select FH-A2 Incident-Centric Evidence Escalation Supervisor. | S-017..S-044; ADR-009..ADR-016; `ARCHITECTURE_REEVALUATION_ARM_B.md`. Reopen if M1 falsifies direct-evidence feasibility or a simpler stronger architecture emerges. |

Key consequence: direct version-qualified incident evidence outranks generic pressure inference; continuous app polling is not a correctness dependency; writes remain typed/qualified/rollback-gated.
