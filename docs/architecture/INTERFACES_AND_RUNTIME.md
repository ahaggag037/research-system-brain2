# FH-A2 Interfaces, Runtime and Lifecycle

## Interface table
| ID | From → To | Payload | Runtime semantics | Failure semantics | Privilege/safety |
|---|---|---|---|---|---|
| IF2-001 Profile | A2-002 → all | `DeviceProfile` | refresh on firmware/capability invalidation | partial UNKNOWN allowed | discovery read-only |
| IF2-002 Incident | A2-001 → A2-003 | symptom marker/context | timestamped explicit session | no evidence → request gap | APP |
| IF2-003 Direct evidence | platform/adapters → A2-003 | exit/start/policy records + provenance | query on incident/session | unsupported/denied distinct | access tagged |
| IF2-004 Evidence gap | A2-003 → A2-004 | needed evidence family + reason | minimum-tier selection | cannot satisfy → gap remains | no auto privilege |
| IF2-005 Capture bundle | A2-004 → A2-003/A2-008 | bounded evidence + observer cost | cancellable, time-bounded | partial bundle valid | tier-specific |
| IF2-006 Attribution | A2-003 → A2-001/A2-005 | cause/confidence/evidence/gaps | replayable | UNKNOWN valid | none |
| IF2-007 Policy assessment | A2-007 → A2-003/A2-001 | versioned policy facts/guidance | on demand/version refresh | unknown version | no undocumented write |
| IF2-008 Experiment | A2-005 ↔ A2-008 | protocol/trials/outcomes | paired/repeated where feasible | inconclusive preserved | none |
| IF2-009 Candidate action | A2-005 → A2-006 | typed qualified request | serialized transaction | reject/no-op | privileged boundary |
| IF2-010 Evidence/report | all ↔ A2-008 | versioned records/export | transactional | quarantine corruption | private-by-default |

## Incident runtime — primary path
1. User observes a reload/exit/jank/background-continuity failure and opens/marks an incident in A2-001.
2. A2-002 validates DeviceProfile freshness.
3. A2-003 queries the highest-value direct records that are actually accessible: process exit/start reason/type/timestamps, limiter/freezer/policy facts.
4. A2-003 creates an initial attribution. If evidence is sufficient, no continuous capture is needed.
5. If a material gap remains, A2-004 selects the lowest adequate tier: T1 cheap snapshot, T2 triggered trace, or T3 explicit privileged read session.
6. A2-003 recomputes attribution and records direct/context/contradicting evidence separately.
7. A2-007 contributes Android/vendor policy assessment when the symptom could be policy-limited.
8. A2-008 persists the incident locally; A2-001 shows cause/confidence/gaps and safe next action.
9. A2-005 may define a shadow experiment. Initial product normally returns NO_OP, guidance or a measurement task.

## Qualified-actuator path
Unchanged safety shape from FH-A1, but attribution/experiment evidence is now incident-linked:
`qualified candidate → profile/firmware recheck → safety snapshot → one typed operation → read-back → paired/canary outcome window → commit evidence OR rollback/suspend`.

## Evidence escalation semantics
- **T0:** after-the-fact OS/app history, no daemon requirement.
- **T1:** bounded M0/M1 snapshot; read-only and user-writable output only.
- **T2:** privileged preconfiguration may be needed; unprivileged app can only signal predeclared Perfetto triggers where supported. Never assume trigger support from Android version alone.
- **T3:** explicit temporary shell/root-read session; release after session.

## Lifecycle implications
- App start validates/migrates local state and loads DeviceProfile.
- No first-build boot-persistent helper or permanent FGS is required.
- If FixHUA itself becomes cached/frozen/background-restricted, no correctness claim depends on uninterrupted polling.
- Firmware/full-SDK/vendor-policy changes stale affected capabilities and all write qualifications.
- Reboot terminates ephemeral sessions and pending capture assumptions; next run re-profiles.
- A2-006 transaction journal/timeout owns rollback independently of UI lifetime for any future writes.

## Version-aware direct-record rule
A2-003 must bind parsers to documented API/feature versions. Example: current `REASON_MEMORY_LIMITER` is a version 37.2 API surface, while older Android 17 behavior may expose description/command behavior differently. Human-readable descriptions are evidence for display/debugging, not stable universal parser keys unless a version-specific adapter explicitly qualifies them.
