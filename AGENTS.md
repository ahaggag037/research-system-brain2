# FixHUA FH-A2 — AI / Engineer Entry

Read **`docs/project/00_START_HERE.md` first**, then `PROJECT_STATE.json`. Active architecture is FH-A2. FH-A1/V10.3-B completion is historical and must not override Arm B research.

## Epistemic hierarchy
**Internal knowledge proposes. External evidence challenges and expands. Real-device evidence decides device-specific truth.**

Platform/AOSP/Huawei/Linux documentation establishes a mechanism/reference behavior, never target capability. Every target claim must carry device/build/access evidence or remain UNKNOWN/UNOBSERVABLE.

## Canonical truth locations
- current phase/build/blockers: `PROJECT_STATE.json`
- mandatory Arm B evidence: `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`, `docs/evidence/SOURCES.md`
- architecture reevaluation/delta: `docs/architecture/ARCHITECTURE_REEVALUATION_ARM_B.md`, `docs/project/ARM_B_CHANGELOG.md`
- selected design: `docs/architecture/ARCHITECTURE.md`, `DECISIONS.md`, `COMPONENT_CONTRACTS.md`
- runtime/data/recovery/safety: `INTERFACES_AND_RUNTIME.md`, `DATA_STATE_MODEL.md`, `FAILURE_RECOVERY_MATRIX.md`, `PRIVILEGE_AND_SAFETY.md`
- implementation: `docs/implementation/`
- navigation: `KNOWLEDGE_GRAPH.json`, `IMPLEMENTATION_MAP.json`, `VISUAL_TRACEABILITY.json`

## Incident evidence rule
For an incident, prefer reliable direct, version-qualified platform evidence over generic pressure inference. If direct evidence is unavailable/denied/ambiguous, request the minimum next evidence tier. `UNKNOWN` is correct when evidence remains insufficient.

## Privilege rule
No raw root command surface. A write actuator needs exact target control semantics, bounds, expected user outcome, preconditions/exclusions, baseline, timeout/abort, read-back, failure-tested rollback and same-device/firmware canary evidence. No thermal/hardware/integrity/DRM/account/banking/security bypasses.

## Observer rule
Measurement can become the problem. Deep traces are bounded, capture cost is recorded, and no correctness assumption depends on an ordinary app polling continuously while cached/backgrounded.

## Recovery after interruption
Read `.v10/working_memory/CHECKPOINT.md` → `REQUIREMENT_LEDGER.md` → `DECISION_LOG.md` → `SOURCE_INDEX.md`, then reconcile with `PROJECT_STATE.json` and actual code/tests. Scratch state is noncanonical and cannot override verified artifacts.

## Same-change rule
Architecture/interface/privilege/state/build changes update ADR + PROJECT_STATE + affected machine maps/visuals/tests in the same logical change. Documentation drift is a defect.
