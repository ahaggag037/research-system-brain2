# Evidence, Claims, and Experiment Strategy

## Evidence hierarchy
Prefer, in order for target behavior:
1. direct target-device observation with reproducible procedure;
2. current AOSP/Linux/Huawei primary documentation/source code;
3. controlled experiment on matching device/firmware;
4. source-code/config inspection of the target build where lawful/available;
5. strong technical literature;
6. community anecdotes only as hypothesis generators.

Public-source facts describe platform mechanisms, not guaranteed target-device capability. Capability remains `UNKNOWN` until scanned.

## E-001 — Device evidence bootstrap
**Status:** PROPOSED / next milestone.  
**Hypothesis:** a read-only snapshot plus representative incident capture can distinguish enough mechanism classes to guide the first Android observer.  
**Inputs:** actual Huawei device, normal + representative app-switch/jank scenario, no system write.  
**Measure:** device/firmware profile, accessible PSI, meminfo/swap/zRAM clues, thermal state, load/I/O clues, permitted process/exit evidence, Huawei policy assessment, observer capability/denials.  
**Falsify:** observables are too weak/ambiguous to separate candidate classes.  
**Abort:** collection creates noticeable instability, privacy exposure or requires unsafe mutation.  
**Impact:** fixes exact sensor set and unblocks M2 Android diagnostic APK.

## E-002 — Observer overhead budget
A/B observer off vs baseline recorder vs triggered deep capture over the same workload. Measure CPU time, wakeups if accessible, resident memory, storage writes, battery/thermal trend and jank. If observer materially creates/hides the symptom, reduce sampling or remove the probe. Exact budget is target-derived, not invented here.

## E-003 — State-estimator falsification
Create controlled scenarios where feasible: memory pressure, CPU contention, I/O contention, thermal loading within safe ordinary use, Huawei background restriction, and known app crash. Compare multi-signal estimator with single-metric baselines. Contradictory evidence must reduce confidence/emit UNKNOWN rather than force a label.

## E-004 — Huawei continuity diagnosis
Under non-critical memory conditions, vary documented Huawei App Launch/background/battery settings for a consenting test app and observe continuity. Goal: prove the classifier can distinguish policy-limited behavior from global memory pressure. Do not automate undocumented vendor database edits.

## E-005 — Typed actuator qualification
For each future actuator, independently: capability probe → semantic/source validation → shadow prediction → capture baseline/rollback → bounded canary → read-back verify → outcome window → forced-failure rollback test → qualification or rejection. No actuator inherits qualification from another device/firmware.

## Claim promotion rule
A hypothesis becomes target-verified only when evidence directly supports it on the target with provenance. An implementation becomes `TESTED` only for the exact environment/test actually run. Architecture docs must not use platform documentation as proof that a target control exists.
