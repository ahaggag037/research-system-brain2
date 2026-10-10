# Integration Proof — FH-A2 specification

This file proves **integration coverage in the specification**, not runtime Android integration.

| Transition | Producer → consumer | Contract/evidence | Current status |
|---|---|---|---|
| target facts | M0.2/M1 → A2-002 | DeviceProfile/capability statuses | M0.2 partial implemented; target not run |
| incident intake | A2-001 → A2-003 | IncidentRecord | specified |
| direct history | platform adapters → A2-003 | DirectPlatformEvent + version/access | specified |
| evidence gap | A2-003 → A2-004 | requested evidence family | specified |
| capture | A2-004 → A2-003/A2-008 | CaptureBundle + ObserverBudget | specified |
| policy | A2-007 → A2-003/A2-001 | PlatformPolicyAssessment | specified |
| attribution | A2-003 → UI/experiment/store | IncidentAttribution | specified |
| experiment | A2-005 ↔ A2-008 | protocol/trials/outcome | specified |
| privileged candidate | A2-005 → A2-006 | typed CandidateAction | future/disabled |
| rollback/audit | A2-006 → A2-008 | result/SafetySnapshot/audit | future/disabled |
| report/export | A2-008 → user/share | redacted report | specified |

No transition assumes a write actuator or cross-UID API that has not been proven on target.
