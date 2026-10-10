# Data and State Model

Canonical schemas below are logical. Concrete Android serialization format is an implementation decision; schema versioning is mandatory.

| State object | Owner | Persistence | Lifecycle / migration | Corruption/reset / backup |
|---|---|---|---|---|
| `DeviceProfile` | CMP-002 | persistent local | keyed by device+firmware fingerprint; schema-versioned | corrupt → rescan; never infer missing capability |
| `ObservationSample` | CMP-003 | ring-buffer / optional incident persist | short-lived; monotonic timestamp | corrupt sample dropped + gap marker |
| `IncidentWindow` | CMP-003/008 | persistent local until retention expiry/user delete | immutable evidence bundle version | corruption quarantined; cannot backfill invented data |
| `StateEstimate` | CMP-004/008 | persistent with incident | derived + estimator version | recompute if source valid; otherwise UNKNOWN |
| `CandidateAction` | CMP-005 | audit only | immutable decision proposal | invalid → discard/no-op |
| `ActuatorQualification` | CMP-006/008 | persistent local | bound to actuator+device+firmware+test version | corruption/staleness → NOT_QUALIFIED; no recovery by guessing |
| `SafetySnapshot` | CMP-006 | ephemeral + transaction journal | per privileged transaction | missing snapshot blocks write; rollback journal retained until verified |
| `ExperimentRecord` | CMP-008 | persistent local | append/history preserving | corrupt record quarantined; do not promote conclusion |
| `SettingsAssessment` | CMP-007/008 | persistent optional | invalidated by OS/version/user change | recompute; no hidden setting mutation |
| `UserPolicy` | CMP-001/008 | persistent local | migrated explicitly | reset to conservative defaults |
| `AuditEvent` | CMP-008 | append-oriented local | retention configurable | truncated/corrupt history marks provenance incomplete |

## Core logical schemas
```text
DeviceProfile {
  schemaVersion, deviceFingerprint, firmwareFingerprint,
  manufacturer, model, androidApi, vendorBuild,
  capabilities: [{id, status: SUPPORTED|UNSUPPORTED|UNOBSERVABLE|UNKNOWN,
                  access: APP|SHELL_READ|ROOT_READ|PRIVILEGED_WRITE,
                  evidenceRef}],
  createdAt
}

StateEstimate {
  estimatorVersion, incidentId,
  state: NORMAL|MEMORY_PRESSURE|IO_BOUND|CPU_CONTENDED|THERMAL_LIMITED|VENDOR_POLICY_LIMITED|UNKNOWN_OR_MIXED,
  confidence: LOW|MEDIUM|HIGH,
  evidenceFor[], evidenceAgainst[], missingEvidence[]
}

ActuatorQualification {
  actuatorId, actuatorVersion, deviceFingerprint, firmwareFingerprint,
  status: NOT_QUALIFIED|SHADOW_OK|CANARY_OK|SUSPENDED|REJECTED,
  observedControlSemantics, allowedParameterBounds,
  preconditions[], abortConditions[], rollbackProcedure,
  experimentEvidenceRefs[], expiresOrInvalidatesOn[]
}
```

## Migration rules
- Every persisted object carries a schema version.
- Unknown future fields are ignored only when compatibility is declared; missing required fields fail closed.
- Destructive migration requires backup/transaction and rollback path.
- Firmware fingerprint change invalidates actuator qualification and any capability assertion whose semantics may have changed.
- Reset must never preserve a write qualification without its evidence.

## Privacy boundary
Raw cross-app/process evidence can be sensitive. Local data is private by default, not committed to this public repository, and export must minimize/redact identifiers unless the user explicitly requests otherwise.
