# Interfaces, Runtime Flows, Startup/Shutdown

## Interface map
| Interface | Caller → Callee | Data | Mode | Timeout/retry | Failure propagation | Privilege / rollback |
|---|---|---|---|---|---|---|
| IF-001 CapabilityScan | CMP-001 → CMP-002 | ScanRequest → DeviceProfile | async/cancellable | per-probe timeout; no blind retry storm | partial UNKNOWN profile | optional read session; no writes |
| IF-002 Observe | CMP-001/CMP-004 → CMP-003 | CapturePolicy → samples/window | async stream | bounded capture; optional probe backoff | gaps annotated | read-only |
| IF-003 Estimate | CMP-003 → CMP-004 | evidence bundle → StateEstimate | sync/pure or worker | no retry needed | UNKNOWN result | none |
| IF-004 Decide | CMP-004 → CMP-005 | StateEstimate + policy → candidate | sync/pure | no retry | NO_OP | none |
| IF-005 Actuate | CMP-005 → CMP-006 | typed CandidateAction | async serialized | hard deadline, no generic repeat | fault + rollback result | privileged; actuator rollback mandatory |
| IF-006 SettingsGuide | CMP-001 → CMP-007 | model/OS/symptom | async | bounded | generic UNKNOWN guidance | no undocumented writes |
| IF-007 Persist | all → CMP-008 | versioned records | async transactional | bounded storage retry | degraded in-memory status | no privilege |
| IF-008 Export | CMP-001 → CMP-009 | report request | async | user retry | no source mutation | redact/share boundary |

Interfaces are schema-versioned. A breaking schema change requires state migration + documentation + tests in the same change.

## Normal runtime trace — symptom investigation
1. User opens CMP-001 and selects **Diagnose**.
2. CMP-002 loads or refreshes DeviceProfile if firmware fingerprint changed.
3. CMP-003 starts low-cost sampling and an incident ring buffer.
4. User reproduces slow resume/jank and marks the incident.
5. CMP-003 freezes a bounded evidence window; if allowed and useful, it can request a short Perfetto/deep capture.
6. CMP-004 returns a StateEstimate with evidence/missing evidence.
7. CMP-005 evaluates candidate responses. Initial builds normally return `NO_OP`, additional capture, or CMP-007 settings guidance.
8. CMP-008 stores the evidence and provenance locally.
9. CMP-001 displays explanation, confidence, unknowns and next safe action.
10. Optional CMP-009 export shows a redaction preview before writing a shareable bundle.

## Future qualified-actuator trace
1. CMP-005 proposes a **typed** action already qualified for the exact DeviceProfile.
2. CMP-006 rechecks firmware fingerprint, operating-region exclusions and qualification freshness.
3. Gateway captures pre-state/rollback material.
4. Gateway performs one bounded actuation.
5. Gateway reads back/verifies control state and CMP-003 observes outcome during a canary window.
6. Any failed postcondition, controller fight or safety regression triggers immediate rollback and qualification revocation/suspension.
7. CMP-008 records before/after/rollback evidence; UI shows result.

## Startup lifecycle
- App process starts in ordinary privilege.
- Validate local schema/migrations; corruption enters degraded/read-only recovery.
- Load DeviceProfile; if build/firmware fingerprint differs, mark capabilities stale and require rescan before any privileged operation.
- Start only low-cost observers explicitly enabled by user/app lifecycle.
- Privileged helper is **not** boot-persistent in the first installable build; it is acquired for explicit sessions and released afterward.
- Policy engine starts with write capability disabled unless every qualification precondition is current.

## Shutdown / crash / update
- Graceful shutdown ends captures, flushes transactional records, and releases an ephemeral privileged session.
- App crash must not leave a write transaction pending; CMP-006 transaction design owns rollback/timeout independent of UI lifecycle.
- Reboot invalidates active sessions and ephemeral rollback assumptions; next start re-scans capabilities before writes.
- App/firmware update runs schema migration; firmware change invalidates write qualifications until requalification.
- No automatic boot-time tuning is part of the first daily build.
