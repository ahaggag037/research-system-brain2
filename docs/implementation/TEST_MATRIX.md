# FH-A2 Traceable Test Matrix

| Test ID | Requirement/mechanism | Test | Expected | Current state |
|---|---|---|---|---|
| T-M0-01 | PSI parser | some/full fixture | preserve values/missing | IMPLEMENTED host |
| T-M0-02 | meminfo parser | kB fixture | byte conversion | IMPLEMENTED host |
| T-M0-03 | conservative summary | nonzero PSI | signal, not causal diagnosis | IMPLEMENTED host |
| T-M0-04 | probe manifest | execute shell probe | valid names/status; no TSV regression | IMPLEMENTED host |
| T-M0-05 | Android props | SDK fixture | observed SDK only, no target assumption | IMPLEMENTED host |
| T-M0-06 | Arm B capabilities | limiter/cgroup/MGLRU/Perfetto fixture | capability observations only | IMPLEMENTED host |
| T-M0-07 | missing evidence | empty snapshot | UNKNOWN + gaps | IMPLEMENTED host |
| T-M0-08 | zero PSI | zero fixture | NORMAL_OR_UNDETERMINED, no causal claim | IMPLEMENTED host |
| T-CAP-01 | A2-002 | supported/denied/missing/version matrix | states distinct | M2/M1 |
| T-CAP-02 | low-memory reporting | supported vs unsupported | SIGKILL not auto-LMK when unsupported | M2/M1 |
| T-INC-01 | A2-003 | direct LOW_MEMORY record | qualified LMK attribution + provenance | M2 |
| T-INC-02 | A2-003 | MEMORY_LIMITER supported version | limiter cause only with adapter/capability | M2 |
| T-INC-03 | A2-003 | FREEZER reason / frozen IPC context | freezer class | M2 |
| T-INC-04 | A2-003 | direct record conflicts with PSI heuristic | direct evidence priority + visible conflict | M2 |
| T-INC-05 | A2-003 | no direct evidence | UNKNOWN/context + capture gap | M2 |
| T-CAPTURE-01 | A2-004 | evidence gap selection | minimum adequate tier | M2 |
| T-CAPTURE-02 | A2-004 | unsupported Perfetto/cancel/timeout | safe fallback/no orphan trace | M2 |
| T-OBS-01 | Observer Budget | E-002 A/B | optional probes shed on budget breach | target M1/M2 |
| T-POLICY-01 | A2-007 | Android/Huawei known + unknown versions | version-qualified or UNKNOWN | M2 |
| T-STATE-01 | A2-008 | schema migration | no silent evidence/qualification corruption | M2 |
| T-STATE-02 | A2-008 | corrupt store | quarantine + conservative recovery | M2 |
| T-EXP-01 | A2-008 | sensitive export | redact/hash by default | M2 |
| T-SHADOW-01 | A2-005 | inconclusive/regression trial | NO_OP/no promotion | M3/M4 |
| T-PRIV-01 | A2-006 | arbitrary command injection | impossible by typed boundary | M5 |
| T-PRIV-02 | A2-006 | stale firmware | reject actuator | M5 |
| T-PRIV-03 | A2-006 | partial failure | rollback + suspend | M5 |
| T-CONT-01 | A2-009 | poor-history/OOD | fallback/no action | M4 |
| T-BUILD-01 | Android | clean unit+assembleDebug | deterministic debug APK | M2 |
| T-INSTALL-01 | target | install/launch/no-write | pass | blocked by device |
| T-ARM-B-01 | R-092..R-106 | research/ADR/delta audit | required research traceable | State D2 |
| T-VIS-02 | FH-A2 visuals | stable active IDs and flows | validator/manual consistency | State D2 |
| T-COLD-02 | revised repo | fresh GitHub-only continuation | reconstruct FH-A2 + exact next task | State D2 |

Host suite count after Arm B M0.2 update: **8 tests**. Passing host tests never upgrades target-device claims.
