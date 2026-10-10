# FixHUA — AI / Engineer Entry

Read **`docs/project/00_START_HERE.md` first**. Current machine state is `PROJECT_STATE.json`.

## Canonical truth locations
- Current phase / implementation / blockers: `PROJECT_STATE.json`
- Architecture and rationale: `docs/architecture/ARCHITECTURE.md`, then `docs/architecture/DECISIONS.md`
- Component ownership/contracts: `docs/architecture/COMPONENT_CONTRACTS.md`
- Interfaces/runtime/state/recovery: `docs/architecture/INTERFACES_AND_RUNTIME.md`, `DATA_STATE_MODEL.md`, `FAILURE_RECOVERY_MATRIX.md`
- Build and next implementation work: `docs/implementation/BUILD_RUNBOOK.md`, `FIRST_BUILD_CRITICAL_PATH.md`, `IMPLEMENTATION_BLUEPRINT.md`
- Validation: `docs/implementation/TEST_MATRIX.md`, `docs/evidence/EVIDENCE_AND_EXPERIMENTS.md`
- Visual twin: `docs/visual/*.mmd` and `VISUAL_TRACEABILITY.json`
- Programmatic navigation: `KNOWLEDGE_GRAPH.json`, `IMPLEMENTATION_MAP.json`

## Truth-state rule
Use only: `VERIFIED_FACT`, `IMPLEMENTED`, `TESTED`, `PROPOSED`, `EXPERIMENTAL`, `HYPOTHESIS`, `REJECTED`, `DEFERRED`, `UNKNOWN`. Never silently promote a state. "Implemented" does not mean "tested on target."

## Conflict rule
For **what runs now**: verified target-device evidence > checked-out code > current tests/CI > current build artifacts > project-state/docs. For **why it is designed this way**: active decision records > architecture > component contracts > implementation blueprint. If artifacts disagree, record the contradiction and repair it; do not guess.

## Privileged-change rule
Root/shell access is a capability, not permission to tune. A write actuator is production-admissible only after device-specific evidence establishes: observed control semantics, bounded scope, expected effect, preconditions, abort condition, verification, timeout, rollback, and a canary test. Never add an arbitrary root-command API, disable thermal/hardware safety, or bypass account/banking/DRM/integrity protections.

## Missing device facts
Do **not** invent kernel nodes, cgroup paths, LMKD properties, Huawei settings paths, actuator values, or feature availability. Mark `UNKNOWN` and run the smallest capability/discovery test.

## Same-change documentation rule
Any code change that materially changes architecture, interface, behavior, privilege, safety, state schema, build procedure, or project phase must update the affected canonical docs **and** machine-readable state in the same change. Documentation drift is a defect.

## Recovery after interruption
Read, in order: `.v10/working_memory/CHECKPOINT.md`, `.v10/working_memory/REQUIREMENT_LEDGER.md`, `.v10/working_memory/DECISION_LOG.md`, then the canonical artifacts above. Reconcile scratch claims against actual repository code/tests before acting.
