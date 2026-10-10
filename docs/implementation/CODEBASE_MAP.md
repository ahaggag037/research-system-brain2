# Codebase / Module Map

## Implemented M0
| ID | Source path | Responsibility | Interfaces/deps | Runtime/lifecycle | Privilege | State/logs | Failures/tests/ADRs |
|---|---|---|---|---|---|---|---|
| SRC-001 | `tools/device_probe.sh` | read-only capability/pressure snapshot | shell, `/proc`, `getprop`, optional `dumpsys` | one-shot target shell process | shell read | writes only output directory + command status | partial/denied fields tolerated; manual no-write audit; ADR-002 |
| SRC-002 | `tools/analyze_snapshot.py` | host summary/reference evidence parser | stdlib JSON/path/regex | one-shot host process | none | report JSON only | malformed/missing tolerant; `tests/test_analyze_snapshot.py`; ADR-003 |
| SRC-003 | `tools/validate_repo.py` | package consistency checks | stdlib JSON/path | CI/local one-shot | none | stdout/exit code | repository package test |
| SRC-004 | `schemas/*.json` | snapshot/report interface schemas | JSON Schema convention | static | none | schemas | validator syntax checks |

## Planned Android modules
| Component | Planned path | Public interfaces | Inbound → outbound | Owner/lifecycle | Privilege/thread | Persistent state | Tests/visual/ADR |
|---|---|---|---|---|---|---|---|
| CMP-001 | `android/app/` | UI/session intents | user → all app services | app process | APP / UI + workers | UserPolicy | UI/error tests; PRODUCT_FLOW; ADR-001 |
| CMP-002 | `android/capability/` | IF-001 | CMP-001 → platform adapters | scan session | APP + optional read worker | DeviceProfile via CMP-008 | T-CAP; ARCHITECTURE; ADR-002 |
| CMP-003 | `android/observer/` | IF-002 | coordinator → sensors → estimator/store | explicit recorder session | APP/read; worker | ring buffer/IncidentWindow | T-OBS; RUNTIME diagrams |
| CMP-004 | `android/core-model/` | IF-003 | observer → estimator | pure/worker | none | derived estimates via store | T-EST; ADR-003 |
| CMP-005 | `android/policy/` | IF-004 | estimator/store → candidate | session/replay | none | policy config/evidence refs | T-POL; ADR-001 |
| CMP-006 | `android/privilege/` | IF-005 | policy → typed adapter | explicit privileged session | shell/root; serialized | qualification/journal via store | T-PRIV; ADR-004/005 |
| CMP-007 | `android/huawei-assistant/` | IF-006 | UI → guidance | app session | APP | assessment optional | T-HUA; ADR-006 |
| CMP-008 | `android/evidence-store/` | IF-007 | all components | app lifetime | APP / serialized transactions | local DB/files | T-STATE; ADR-008 |
| CMP-009 | `android/report/` | IF-008 | UI/store → export | on demand | APP / worker | exported artifact | T-EXP; ADR-008 |
| CMP-010 | `android/continuity/` | future shadow API | store → ranking | replay/session | none | experiment output | T-CONT; ADR-007 |

Planned paths are **not evidence that modules exist**. `PROJECT_STATE.json` is authoritative for implemented/unimplemented status.
