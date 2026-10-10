# FH-A1 — Evidence-Gated Adaptive Supervisor

Status: **PROPOSED / FULLY_SPECIFIED at architecture level; not fully implemented or target-tested.**

## Thesis
FixHUA should be a **supervisor over evidence and bounded experiments**, not a second always-on kernel policy engine. Android and Huawei already contain interacting memory, scheduler, freezer, thermal, power and lifecycle controllers. The safest opportunity is to observe their externally visible effects, classify operating conditions, explain likely mechanisms, and use privileged control only for explicitly qualified actuators.

## Major components
| ID | Component | Production disposition |
|---|---|---|
| CMP-001 | App/UI + Session Coordinator | PROPOSED |
| CMP-002 | Capability Scanner | PROPOSED; shell prototype partially implemented |
| CMP-003 | Flight Recorder | PROPOSED |
| CMP-004 | State Estimator | PROPOSED; host reference summarizer implemented |
| CMP-005 | Shadow Policy Engine | PROPOSED |
| CMP-006 | Typed Privilege Gateway | PROPOSED; no write actuator admitted |
| CMP-007 | Huawei Compatibility Assistant | PROPOSED |
| CMP-008 | Experiment & Evidence Store | PROPOSED |
| CMP-009 | Report/Redacted Export | PROPOSED |
| CMP-010 | Continuity Allocator | EXPERIMENTAL |

## Operating-state model
The estimator can emit:
- `NORMAL`
- `MEMORY_PRESSURE`
- `IO_BOUND`
- `CPU_CONTENDED`
- `THERMAL_LIMITED`
- `VENDOR_POLICY_LIMITED`
- `UNKNOWN_OR_MIXED`

It must output a confidence/evidence explanation. It must not turn a single PSI/free-RAM/thermal number into an actuator authorization.

## Control loop
1. CMP-002 discovers observable capabilities once per relevant firmware/profile change.
2. CMP-003 runs a low-cost baseline recorder; incident triggers can request a short deeper capture.
3. CMP-004 converts observations into a state estimate + confidence + evidence gaps.
4. CMP-005 evaluates candidate responses in `SHADOW` first. `NO_OP` is always legal.
5. If a candidate requires privilege, CMP-006 checks a device-specific qualification record, captures rollback state, enforces bounded parameters/timeout, executes one typed actuator and verifies the postcondition.
6. If verification or safety guards fail, CMP-006 rolls back and blacklists/revokes qualification pending investigation.
7. CMP-008 records outcome evidence. Adaptation changes recommendations/qualification confidence, not hidden arbitrary system state.

## Why not tune the kernel directly by default?
Root makes more data/control surfaces visible, but it does not prove a node exists across firmware, that writes are durable, that the framework will not overwrite them, that the observed correlation is causal, or that a value is thermally/stability safe. Direct write logic therefore lives behind a typed adapter + qualification contract, never in generic policy/UI code.

## First useful / installable / daily-use split
- **First useful now:** read-only `tools/device_probe.sh` + `tools/analyze_snapshot.py` on a host.
- **First installable/testable:** Android diagnostic APK containing CMP-001/002/003/008/009 with no privileged writes; optional explicit shell/root read session.
- **First daily-usable:** low-overhead recorder + incident report + Huawei settings assistant + stable local evidence store. Any actuator remains optional and individually qualified.
- **Long-term:** shadow policies, actuator canaries and experimental continuity allocator.

## Complexity budget
Every major component has a unique role. CMP-004 exists because symptoms are mechanism-ambiguous; CMP-005 because decision policy must be separable/testable from sensing; CMP-006 because privilege needs a stronger safety boundary than ordinary app code; CMP-008 because claims need provenance/qualification history. If future implementation can merge a component without weakening these ownership boundaries, the decision may be reopened.
