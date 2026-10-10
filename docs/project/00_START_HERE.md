# 00 — Start Here: FixHUA FH-A2

## Current product thesis
FixHUA is an **Incident-Centric Evidence Escalation Supervisor** for Huawei-class Android devices. It aims to improve responsiveness, app-continuity/resume quality and predictability by reconstructing **why a specific incident happened** before considering any intervention.

Active architecture: **FH-A2**, selected after mandatory Arm B external research. FH-A1 is historical; the exact delta and evidence are in `docs/project/ARM_B_CHANGELOG.md` and `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`.

## Runtime in one line
`Incident → direct OS history → correlate → minimum evidence escalation → attribution → shadow experiment → typed qualified action only if proven → verify/rollback`.

## What is true now
- **VERIFIED platform facts:** current Android/Linux/Huawei mechanisms indexed in `docs/evidence/SOURCES.md`, including Android 17 MemoryLimiter, app-memory budgets, start/exit records, cached freezer, background quotas, Perfetto triggers, MGLRU/cgroup/DAMON mechanisms and Huawei documented policy controls. These are **not** target capability proof.
- **IMPLEMENTED + HOST-TESTED:** M0 shell probe, conservative host analyzer and repository/audit validators. Arm B expands the read-only probe/analyzer for newer capability evidence.
- **SELECTED/FULLY_SPECIFIED:** FH-A2 architecture and M1→M3 implementation path.
- **NOT IMPLEMENTED:** Android APK, incident engine, policy adapter runtime, Perfetto orchestration, persistent store/UI, shadow evaluator, privilege gateway runtime, continuity model.
- **NONE ADMITTED:** privileged write actuators.
- **UNKNOWN until M1:** exact Huawei model/build/API/kernel, MemoryLimiter/budget/freezer/MGLRU/DAMON/Perfetto access, cross-UID incident-history access, vendor-policy behavior, thermal-headroom quality, and actuator value/safety.

## First useful build
M0 is a read-only target snapshot + host analyzer. It exists to answer capability/pressure questions without changing phone state. Raw snapshots are private and must not be committed.

## Exact next milestone — M1 Incident & Capability Bootstrap
On the real target, determine:
1. model/firmware/Android API/full-SDK/vendor branch;
2. MemoryLimiter status and app-memory-budget availability;
3. low-memory exit-report support and ApplicationStartInfo/ExitInfo access through each available privilege tier;
4. freezer/cgroup v2/PSI/MGLRU/DAMON observability;
5. Perfetto trigger/config feasibility;
6. Huawei policy version/surfaces;
7. thermal-headroom/status behavior;
8. M0/M1 observer overhead;
9. one or more real incident timelines without any system write.

## Non-negotiable invariants
1. Direct trustworthy incident evidence outranks generic heuristic inference.
2. Missing/denied/unsupported are distinct; never invent target capability.
3. Use the minimum evidence tier necessary; measurement cost is part of correctness.
4. Root is capability, not proof of safety/benefit.
5. No arbitrary privileged command surface.
6. No thermal/hardware/integrity/security bypasses.
7. Every future write is typed, bounded, target-qualified, verified and rollback-capable.
8. Raw cross-app evidence stays local by default; shared output is minimized/redacted.
9. `UNKNOWN` and `NO_OP` are valid successful outcomes.
10. Internal knowledge proposes; external evidence challenges/expands; real-device evidence decides target-specific truth.

## Canonical navigation
| Need | File |
|---|---|
| Machine-readable current state | `PROJECT_STATE.json` |
| Arm B research questions/results | `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md` |
| Architecture selection comparison | `docs/architecture/ARCHITECTURE_REEVALUATION_ARM_B.md` |
| Active architecture | `docs/architecture/ARCHITECTURE.md` |
| Decisions/history | `docs/architecture/DECISIONS.md` |
| Component contracts | `docs/architecture/COMPONENT_CONTRACTS.md` |
| Runtime/data/recovery | `docs/architecture/INTERFACES_AND_RUNTIME.md`, `DATA_STATE_MODEL.md`, `FAILURE_RECOVERY_MATRIX.md` |
| Evidence/sources/experiments | `docs/evidence/` |
| Build/M1/M2 path | `docs/implementation/` |
| Change from previous completed state | `docs/project/ARM_B_CHANGELOG.md` |
| Visual twin | `docs/visual/*.mmd`, `VISUAL_TRACEABILITY.json` |
| Handoff | `HANDOFF_CHECKPOINT.md` |
