# Traceable Test Matrix

| Test ID | Requirement | Component/mechanism | Test | Expected result | Evidence state |
|---|---|---|---|---|---|
| T-M0-01 | R-032/R-059 | SRC-002 pressure parser | fixture valid PSI/meminfo | parsed values preserve missing vs zero | implemented; host test PASS |
| T-M0-02 | R-032 | SRC-002 conservative summary | fixture with only one signal | no high-confidence causal claim | implemented; host test PASS |
| T-M0-03 | R-029/R-031 | SRC-001 no-write boundary | static command audit | no system-setting/kernel/cgroup writes | validator + manual audit PASS |
| T-M0-04 | R-016/R-032 | SRC-001 manifest generation | execute probe in host fallback environment | manifest JSON valid; TSV fields split correctly; missing Android commands degrade safely | implemented; regression test PASS |
| T-CAP-01 | R-032/R-058 | CMP-002 | capability fixture supported/denied/missing | statuses distinct | M2 required |
| T-CAP-02 | R-032 | CMP-002 | permission denied | UNOBSERVABLE, no crash/action | M2 required |
| T-OBS-01 | R-002/R-058 | CMP-003 two-speed capture | start/incident/stop | bounded window, no orphan capture | M2 required |
| T-OBS-02 | R-034 | CMP-003 overhead | E-002 A/B target | observer inside device-derived budget | BLOCKED_BY_DEVICE_EVIDENCE |
| T-EST-01 | R-032 | CMP-004 | memory-pressure controlled fixture | supported classification/explanation | M2 + E-003 |
| T-EST-02 | R-032 | CMP-004 | conflicting evidence | UNKNOWN_OR_MIXED or lower confidence | M2 + E-003 |
| T-POL-01 | R-030 | CMP-005 | missing qualification | NO_OP; no write | M4 |
| T-POL-02 | R-030 | CMP-005 | rapid state alternation | no chatter | M4 |
| T-PRIV-01 | R-031/R-058 | CMP-006 | arbitrary command injection | impossible/rejected by type boundary | M5 |
| T-PRIV-02 | R-030 | CMP-006 | stale firmware qualification | reject write | M5 |
| T-PRIV-03 | R-030/R-062 | CMP-006 | injected partial/failure | rollback + qualification suspend | M5/E-005 |
| T-HUA-01 | R-002 | CMP-007 | known/unknown Huawei versions | version-qualified guide or UNKNOWN | M2/M3 |
| T-STATE-01 | R-060 | CMP-008 | state migration | no silent qualification corruption | M2 |
| T-STATE-02 | R-062 | CMP-008 | corrupted state | quarantine + conservative reset | M2 |
| T-EXP-01 | R-022/R-058 | CMP-009 | export identifiers | redacted by default | M2 |
| T-BUILD-01 | R-056 | Android project | clean test/assembleDebug | deterministic debug APK | M2, tooling needed |
| T-INSTALL-01 | R-056 | Android APK | install/launch target | starts, profile created, no write | BLOCKED_BY_DEVICE_EVIDENCE |
| T-FW-01 | R-060/R-062 | profile/qualification | firmware change | invalidate write qualification | M5 |
| T-VIS-01 | R-071..R-075 | visual twin | stable visual IDs resolve | all required IDs present | State D PASS |
| T-COLD-01 | R-027/R-070/R-077 | repository | fresh GitHub-only read | continue without chat | State D PASS |

Passing a host unit test never upgrades a target-device claim to TESTED.
