# FH-A2 First-Build Critical Path

## M0.2 — first useful build (IMPLEMENTED / host-tested)
1. Run host tests and repository validator.
2. Run `tools/device_probe.sh` on the target in an Android shell. The probe writes only to the supplied output directory.
3. Pull snapshot privately and run `tools/analyze_snapshot.py`.
4. Review observability/capability facts and pressure context; do not call the report incident causality.

Arm B additions: read-only `/proc/swaps`, cgroup-v2 controller file, MGLRU enabled file, `am memory-limiter status` when available, Perfetto version, plus existing PSI/meminfo/thermal metadata.

**M0.2 exit:** schema-valid report, no device/system writes, unsupported mechanisms remain missing/unknown.

## M1 — Incident & Capability Bootstrap (BLOCKED_BY_DEVICE_EVIDENCE)
Cannot be stubbed. On exact target:
1. fingerprint model/firmware/API/full-SDK/vendor branch;
2. run M0.2 and retain raw snapshot privately;
3. test low-memory-exit-report support and self/cross-UID ApplicationExitInfo access per privilege tier;
4. test ApplicationStartInfo availability/history access;
5. read MemoryLimiter status only if command exists; do not use `ignore`/`manual`;
6. test app-memory-budget API presence without imposing a budget;
7. record freezer/cgroup v2/PSI/MGLRU/DAMON observability only;
8. test Perfetto version and a bounded trigger smoke if safely configurable;
9. identify Huawei EMUI/HarmonyOS policy UI/version using current official docs + actual UI;
10. test Thermal API/headroom behavior/cadence;
11. reproduce at least one real incident and build an evidence timeline;
12. run E-002 observer-cost A/B.

**M1 exit:** DeviceProfile + one replayable incident + observer budget evidence; zero privileged writes.

## M2 — first installable/testable Android build
Minimum modules/components: A2-001, A2-002, A2-003, A2-004 with T0/T1 only initially, A2-007, A2-008. A2-005 is `NO_OP`/shadow-only; A2-006 is a disabled write gateway; A2-009 absent/experimental.

### Exact order
1. Finish M1 (cannot be bypassed).
2. Lock current JDK/SDK/AGP/Gradle from actual implementation tool output; commit wrapper/checksums.
3. Implement versioned core models and migration fixtures.
4. Implement only M1-proven public/read adapters; no fake cross-UID access.
5. Implement incident intake + direct start/exit correlation where supported.
6. Implement attribution fallback/context using conservative snapshot evidence.
7. Implement local store + retention + corruption recovery + redacted reporting.
8. Implement Platform Policy Adapter for exact target family/version.
9. Implement bounded T1 capture; T2 Perfetto only after target trigger feasibility passes.
10. Build debug APK; install/launch on target; run no-write audit.
11. Run E-002/E-003/E-005 subset.

### Mandatory M2 exit tests
- schema/migration;
- denied/unsupported capability distinction;
- version-aware exit/start parser fixtures;
- direct-vs-heuristic conflict → conservative attribution;
- lifecycle/cancellation and capture timeout;
- observer-budget shedding;
- local-state corruption recovery;
- redacted export;
- debug build/install/launch;
- no-write static/runtime audit;
- physical-target observer A/B.

## M3 — daily incident forensics
Requires stable M2 across representative workload, validated observer budget, privacy/retention, firmware invalidation, bounded incident capture and no high-severity crash/data-loss issue. Privileged writes are not required.

## M4 — continuity shadow research
Implement A2-009 prediction/calibration with no kill/freeze actuation. Evaluate real user workflow holdouts and fallback behavior.

## M5 — first actuator canary (optional)
Only if a specific candidate has causal target evidence, unique value over guidance/no-op, exact ownership/bounds, rollback and repeated target benefit. One actuator at a time.

## M6 — custom-system research backend (optional/separate)
Framework/kernel ideas inspired by AppFlow/Ariadne/DAMON/cgroup control belong here. M6 must not silently redefine stock-device capability.
