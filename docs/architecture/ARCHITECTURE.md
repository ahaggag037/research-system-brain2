# FH-A2 — Incident-Centric Evidence Escalation Supervisor

Status: **SELECTED / FULLY_SPECIFIED at architecture level; partially implemented; not target-tested.**  
Supersedes: FH-A1 as the active architecture after mandatory Arm B external research. FH-A1 remains historical and its surviving invariants are traceable in `ARCHITECTURE_REEVALUATION_ARM_B.md`.

## Thesis
FixHUA should diagnose **incidents, not abstract system health first**. Modern Android can terminate, throttle, freeze or restrict work through several independently meaningful mechanisms. When direct platform evidence exists, it is more specific than inferring a cause from a periodic pressure sample.

Runtime principle:

`Incident/outcome → direct platform history → correlate timeline → identify evidence gap → minimum capture escalation → cause attribution → shadow/paired experiment → (only if qualified) typed bounded actuation → verify/rollback → evidence`

`UNKNOWN`, `NO_OP`, and “insufficient privilege” are valid outcomes.

## Major components
| ID | Component | Role / disposition |
|---|---|---|
| A2-001 | Incident Session Coordinator | UI/session lifecycle; incident marker/intake; user-visible evidence state. PROPOSED. |
| A2-002 | Capability & Platform Profiler | Versioned Android/vendor/kernel capability truth. Shell M0 probe partially implements this boundary. |
| A2-003 | Incident Evidence Engine | Correlates exit/start/policy/pressure/thermal evidence and attributes cause with provenance/confidence. PROPOSED; host snapshot summarizer is a narrow precursor. |
| A2-004 | Tiered Capture Orchestrator | Selects the minimum extra evidence tier; triggered deep capture rather than continuous default polling. PROPOSED. |
| A2-005 | Experiment & Shadow Evaluator | Paired/repeated outcome tests; recommends NO_OP/guidance/candidate action; never executes privilege. PROPOSED. |
| A2-006 | Typed Privilege Gateway | Allowlisted read/write operations, target qualification, transaction/rollback. PROPOSED; no write actuator admitted. |
| A2-007 | Platform Policy Adapter | Android baseline restrictions plus vendor/version adapters (Huawei EMUI/HarmonyOS first). PROPOSED. |
| A2-008 | Evidence Store & Redacted Reporting | Versioned provenance, incident/experiment history, private-by-default raw data, redacted export. PROPOSED. |
| A2-009 | Continuity Research Module | Shadow-only user-value/relaunch-cost/relaunch-distance research; no page-hotness duplication. EXPERIMENTAL. |

FH-A2 uses **nine** major components. FH-A1's separate reporting component was merged into A2-008 because it did not justify a separate ownership boundary; its state estimator/correlator responsibilities were re-centered into A2-003.

## Evidence hierarchy
For a specific incident, prefer the highest available trustworthy layer:
1. **Direct platform incident record** — version-qualified exit/start reason, process state/importance, MemoryLimiter/freezer/policy evidence.
2. **Correlated platform timeline** — exit → start/relaunch type/timestamps plus relevant policy/limiter state.
3. **Bounded incident trace/snapshot** — targeted Perfetto or M0/M1 read-only capture.
4. **System-level inference** — PSI/memory/I/O/CPU/thermal windows and vendor-policy context.
5. **Symptom-only report** — useful for requesting evidence, never sufficient for actuation.

A lower layer cannot silently override contradictory higher-quality direct evidence. Missing/version-ambiguous evidence lowers confidence or yields `UNKNOWN_OR_MIXED`.

## Cause taxonomy
A2-003 may emit, with provenance and confidence:
- `MEMORY_LIMITER`
- `LMK_GLOBAL_PRESSURE`
- `FREEZER_OR_FROZEN_IPC`
- `PLATFORM_BACKGROUND_POLICY`
- `CRASH_ANR_OR_INIT_FAILURE`
- `APP_SELF_RESOURCE_PRESSURE`
- `CPU_CONTENDED`
- `IO_BOUND`
- `THERMAL_LIMITED`
- `USER_OR_PACKAGE_STATE_CHANGE`
- `UNKNOWN_OR_MIXED`

These are diagnostic labels, not permissions to write system state.

## Tiered evidence escalation
- **Tier 0 — history/query:** ApplicationExitInfo/ApplicationStartInfo or equivalent accessible OS records; zero/near-zero continuous cost.
- **Tier 1 — cheap snapshot:** M0/M1 read-only `/proc`, PSI, swap, cgroup capability, MGLRU and MemoryLimiter status where observable.
- **Tier 2 — bounded triggered trace:** preconfigured Perfetto START/STOP/CLONE_SNAPSHOT around a reproducible incident when supported.
- **Tier 3 — explicit privileged read session:** shell/root-read-only probes for facts unavailable to ordinary app APIs.

The orchestrator must justify why a higher tier is needed and obey an **Observer Budget**. It must not turn high-overhead tracing into an always-on service.

## Observer Budget
FixHUA's own footprint is part of the experiment:
- measure anonymous RSS + swap, CPU time, wakeups/active duration and capture overhead where practical;
- respect thermal API sampling constraints;
- shed optional probes when observer cost threatens validity;
- on Android 17 QPR2+, a self memory budget may be evaluated as a measured safety rail, never hardcoded or assumed beneficial;
- background execution restrictions/freezer state are capabilities/constraints, not bugs to bypass.

## Outcome model
Primary outcomes are user-visible continuity and responsiveness, not free RAM:
- avoidable cold-start/reload incidence;
- cold/warm/hot relaunch distribution where observable;
- relaunch latency / TTID / TTFD when an appropriate harness can measure them;
- incident recurrence rate;
- app-state continuity success for user-designated workflows;
- jank/responsiveness and thermal stability during controlled trials;
- observer overhead.

## Control and experiment rule
A2-005 runs shadow/paired experiments before any control promotion. Direct actuation remains optional. If no actuator produces repeatable user benefit without regressions, a successful product can remain diagnostic/guidance-first.

## Stock-device vs custom-system boundary
On stock Huawei/Android, FixHUA does not attempt to replace LMKD, MemoryLimiter, MGLRU or vendor policy. cgroup/DAMON/reclaim and research-inspired memory schedulers remain research-only unless exact target ownership and safe actuator contracts are established. Framework/kernel concepts from AppFlow/Ariadne inform future custom-system research, not current capability claims.

## First useful / installable / daily split
- **First useful now:** M0 read-only probe + host analyzer, upgraded by Arm B to expose newer capability facts.
- **M1:** target incident/capability bootstrap, including MemoryLimiter/start-exit/freezer/cgroup/MGLRU/Perfetto/Huawei-policy/thermal feasibility.
- **First installable M2:** no-write Android incident-forensics APK implementing A2-001/002/003/004/007/008 with A2-005 in NO_OP/shadow-only mode and A2-006 disabled for writes.
- **Daily-use M3:** stable low-overhead incident history, user-visible attribution/guidance, bounded capture, privacy/retention, validated target overhead.
- **M4+:** experimental continuity model and individually qualified actuators only after causal evidence.
