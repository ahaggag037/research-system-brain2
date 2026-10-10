# CHECKPOINT

CHECKPOINT_ID: CP-002-DESIGN-CONVERGED
MISSION_STATE: STATE_B_DISCOVERY complete → enter STATE_C_KNOWLEDGE_PACKAGING
CURRENT_ARCHITECTURE_CANDIDATE: Evidence-gated adaptive supervisor; diagnostic flight recorder is first useful build
LAST_MAJOR_DECISION: D-003 leading product model selected after candidate comparison and adversarial attack

## DESIGN_CONVERGED
DESIGN_CONVERGED

## Core problem model
FixHUA is not a static optimizer. It is a supervisory system whose job is to preserve interactive quality and app continuity across changing resource/policy states **without fighting Android/OEM control loops**. Similar symptoms are first classified into memory pressure, vendor policy, thermal, CPU, I/O, app failure, or UNKNOWN/MIXED.

## Selected architecture shape
1. Capability discovery / immutable device profile.
2. Low-overhead flight recorder + triggered deep capture.
3. State estimator with confidence and operating regions.
4. Shadow policy engine; NO-OP is first-class.
5. Typed privilege gateway with per-actuator admission, timeout, verification and rollback.
6. Huawei compatibility assistant using documented settings surfaces.
7. Experiment/evidence store and per-device qualification records.
8. Optional experimental continuity allocator; no automatic destructive load shedding in initial production.

## Serious alternatives considered
- C1 static tweak pack: rejected as core (brittle, noncausal).
- C2 aggressive root autotuner: research-only (controller fight / unsafe persistence risk).
- C3 diagnostics-only: selected as first useful build but insufficient as long-term product.
- C4 evidence-gated supervisor: selected leading end-state architecture.
- C5 continuity allocator: experimental module inside C4, not core/initial production.

## Adversarial attack results
- Single PSI/free-RAM thresholds fail; current AOSP itself guards PSI ambiguity. → multi-signal classifier + UNKNOWN state.
- Telemetry can cause the symptom. → two-speed recorder + E-002 overhead budget.
- Root writes can fight vendor/framework. → ephemeral/read-mostly root early, typed write actuators only after E-005 qualification.
- Freezing does not relieve memory pressure. → no freezer-as-memory-fix.
- Protecting every app worsens memory pressure. → continuity is value-under-pressure, not maximum residency.
- Huawei background policy can mimic LMK. → dedicated policy-limited state + documented settings assistant.
- If no safe actuator earns admission, architecture remains useful as diagnosis/shadow/no-op rather than inventing unsafe control.

## Why convergence is justified
- Core problem model is stable across recent research.
- Major alternatives were seriously considered and dispositions recorded.
- Leading design survived control-loop, observability, overhead, causality, privilege and privacy attacks with concrete safeguards/tests.
- Recent sources mostly refine rather than overturn the design.
- Critical unknowns are explicit and have experiments E-001..E-005.
- First useful build is clear: local diagnostic flight recorder + capability snapshot + symptom report + Huawei settings assistant; root optional/read-mostly.
- Risky ideas have explicit production/experimental/research-only dispositions.

## Current open questions / implementation-blocking unknowns
- Exact target OS/kernel/cgroup/LMKD/vendor capabilities: resolved by E-001 capability scan on device.
- Which cross-app events are accessible from the chosen root/shell broker without persistent service: prototype/test in first build.
- Which, if any, write actuators are beneficial and stable on target: none are production-admitted until E-005.

## Active blockers
- No real target device is connected in this session, so device-specific effectiveness and actuator qualification cannot be TESTED. This does not block architecture/package creation; it will remain an explicit handoff validation milestone.

## Next highest-value action
- Read STATE C contracts (`05`, `05A`, `05B`, `06`), extend Requirement Ledger, then build the durable GitHub knowledge package and implementation artifacts.

## Files/artifacts to read on recovery
1. `.v10/working_memory/CHECKPOINT.md`
2. `.v10/working_memory/REQUIREMENT_LEDGER.md`
3. `.v10/working_memory/DECISION_LOG.md`
4. `.v10/working_memory/SOURCE_INDEX.md`
5. `.v10/working_memory/EXPERIMENT_REGISTRY.md`
6. Actual canonical docs/code after STATE C is created
