# 00 — Start Here

## What FixHUA is
FixHUA is an **evidence-gated adaptive supervisor** for Huawei-class Android devices. Its target outcome is not a benchmark score or maximum free RAM. It aims to improve **interactive responsiveness, smoothness, app-continuity/resume quality, sustained stability, and predictability** by distinguishing the mechanism behind a symptom before choosing any intervention.

## Selected architecture
Architecture ID: **FH-A1 / Evidence-Gated Adaptive Supervisor**.

Runtime concept:
`Observe → classify operating state → explain evidence → shadow candidate policy → (only if qualified) apply typed bounded action → verify → rollback/learn`.

`NO_OP` is a first-class successful outcome when evidence is weak or the platform already behaves well.

## What is true now
- **VERIFIED_FACT:** Android/Huawei resource management includes interacting memory reclaim/LMKD, process lifecycle, cgroup/task-profile, freezer, thermal/power, and vendor background-policy mechanisms. Public evidence is indexed in `docs/evidence/SOURCES.md`.
- **IMPLEMENTED + TESTED (host environment only):** `tools/analyze_snapshot.py` and its unit tests; it summarizes read-only snapshot data conservatively and never performs device control.
- **IMPLEMENTED, NOT TARGET-TESTED:** `tools/device_probe.sh`; it is designed to collect system-level, read-only evidence from Android shell/ADB without changing settings.
- **PROPOSED/FULLY_SPECIFIED:** Android app architecture, capability scanner, flight recorder, state estimator, shadow policy, privilege gateway, Huawei assistant, evidence store and UI flows.
- **EXPERIMENTAL:** continuity allocator and every future write actuator.
- **UNKNOWN:** exact target Huawei model/OS/kernel/cgroup/LMKD features, root broker, observable permissions, and whether any write actuator is beneficial on the target.

## What is not implemented
No Android APK, no persistent daemon, no boot-time service, no privileged write actuator, no automatic app freezer/killer, and no firmware-specific path/value catalog exist in this repository today.

## First useful build
The repository’s current read-only probe + host analyzer can create a device capability/pressure snapshot without changing the phone. See `docs/implementation/BUILD_RUNBOOK.md`.

## Next milestone
**M1 — DEVICE_EVIDENCE_BOOTSTRAP:** run the read-only probe on the actual Huawei device, store the report outside the public repo by default, evaluate telemetry feasibility/overhead, then implement the minimal Android diagnostic APK around the proven observable set.

## Non-negotiable invariants
1. Diagnose before actuation; single metrics do not authorize writes.
2. Never invent device-specific nodes, settings, values or support.
3. Root is capability, not proof of safety or benefit.
4. Thermal/hardware safety and platform integrity are not bypass targets.
5. No unrestricted arbitrary-root command interface.
6. Every actuator must be typed, bounded, verified, reversible and device-qualified.
7. The observer must have an explicit overhead budget; measurement must not become the problem.
8. Keep sensitive cross-app telemetry local by default and redact before export.
9. `NO_OP` and `UNKNOWN` are valid states.
10. Same-change documentation/state updates are mandatory.

## Where to read
| Need | Canonical file |
|---|---|
| Product problem/outcomes/non-goals | `docs/project/01_PROBLEM_AND_SUCCESS.md` |
| Architecture | `docs/architecture/ARCHITECTURE.md` |
| Decisions/alternatives | `docs/architecture/DECISIONS.md` |
| Component contracts | `docs/architecture/COMPONENT_CONTRACTS.md` |
| Runtime/interfaces/lifecycle | `docs/architecture/INTERFACES_AND_RUNTIME.md` |
| State/data | `docs/architecture/DATA_STATE_MODEL.md` |
| Privilege/safety | `docs/architecture/PRIVILEGE_AND_SAFETY.md` |
| Failure/recovery | `docs/architecture/FAILURE_RECOVERY_MATRIX.md` |
| Evidence/experiments | `docs/evidence/EVIDENCE_AND_EXPERIMENTS.md` |
| Sources | `docs/evidence/SOURCES.md` |
| Build | `docs/implementation/BUILD_RUNBOOK.md` |
| First-build critical path | `docs/implementation/FIRST_BUILD_CRITICAL_PATH.md` |
| Tests | `docs/implementation/TEST_MATRIX.md` |
| Visuals | `docs/visual/*.mmd` |

## Source-of-truth ownership / contradiction handling
For **current execution truth**, prefer: target-device evidence → checked-out code → tests/CI → build artifacts → `PROJECT_STATE.json`/docs. For **architecture intent**, prefer: active decisions → architecture → component contracts → implementation blueprint. If higher-ranked evidence contradicts a lower-ranked artifact, record it in `.v10/working_memory/CONTRADICTION_REGISTER.md`, reopen dependent decisions/requirements, fix affected artifacts, and preserve history rather than silently rewriting it.
