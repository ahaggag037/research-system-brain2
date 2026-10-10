# Arm B Architecture Re-evaluation

Baseline: FH-A1 — Evidence-Gated Adaptive Supervisor.  
Evidence input: Q1..Q12 in `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`.

## Candidate set

### FH-A1 — Evidence-Gated Adaptive Supervisor (historical baseline)
Strength: strong safety/epistemic boundaries. Weakness exposed by research: it centers a low-cost Flight Recorder + generic global State Estimator before it exploits direct Android incident records; it under-models newer MemoryLimiter/budget/freezer/background-policy causes and assumes more continuous app-level observability than Android lifecycle guarantees.

### FH-A2 — Incident-Centric Evidence Escalation Supervisor
Start from a user-visible incident or continuity failure. Query the strongest direct, version-qualified platform evidence first (exit/start reasons, process state, policy/limiter/freezer information), build a provenance-bearing timeline, and request only the **minimum additional capture tier** needed to close the evidence gap. Experiments remain shadow/paired by default; privileged writes remain typed and target-qualified.

### FH-B — Diagnostics-only incident forensics
Excellent safety/build speed but no structured experiment/policy path. It would be a good M2 subset, not the strongest end-state architecture because it cannot graduate verified improvements.

### FH-C — Additional userspace pressure controller / killer
PSI/cgroup userspace controllers work in other Linux environments, but Android already has LMKD, MemoryLimiter, freezer, reclaim and vendor policy. A second retail-phone controller creates ownership conflict and duplicates system policy. Rejected as product core.

### FH-D — Custom-system memory scheduler
AppFlow/Ariadne/relaunch-ranking research shows a high ceiling, but strongest mechanisms require framework/kernel integration. This is a future research backend for a custom image, not a realistic stock-Huawei first product.

## Qualitative decision matrix
| Criterion | FH-A1 | FH-A2 | FH-B | FH-C | FH-D |
|---|---|---|---|---|---|
| Direct incident causality | MEDIUM | **HIGH** | HIGH | LOW | HIGH |
| Works with Android lifecycle constraints | MEDIUM | **HIGH** | HIGH | LOW | HIGH |
| Stock-device feasibility | HIGH | **HIGH** | **HIGH** | LOW | LOW |
| Controller-conflict risk | LOW | **LOW** | LOW | HIGH | MEDIUM |
| User-outcome measurement path | MEDIUM | **HIGH** | MEDIUM | MEDIUM | HIGH |
| First useful/build speed | HIGH | **HIGH** | HIGH | LOW | LOW |
| Safe path to proven actuation | HIGH | **HIGH** | NONE | LOW | MEDIUM |
| Future research ceiling | MEDIUM | **HIGH** | LOW | MEDIUM | **HIGH** |

## Reconvergence decision
**Select FH-A2.** It preserves FH-A1's best invariants but changes the diagnostic center of gravity based on external evidence. It also creates a clean bridge to FH-D research without pretending stock devices expose kernel/framework modification points.

## What survives unchanged from FH-A1
- evidence/truth-state gating;
- target capability discovery;
- `UNKNOWN` and `NO_OP` as valid successful outcomes;
- local-first sensitive evidence;
- typed privilege boundary with rollback, no arbitrary root API;
- no thermal/integrity/security bypasses;
- every write actuator independently qualified on the exact device/firmware.

## What is superseded
- always-on/continuous Flight Recorder as primary truth source;
- generic global State Estimator as the first diagnostic step;
- Huawei-specific assistant as a standalone product boundary;
- separate Report/Export component;
- page-hotness-like continuity logic in user space.

## Reconvergence condition
Public research has reached diminishing marginal value. FH-A2 is selected at architecture level, but any target-specific capability/benefit remains `UNKNOWN` until M1 device evidence.
