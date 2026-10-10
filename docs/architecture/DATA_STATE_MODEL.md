# FH-A2 Data and State Model

| Object | Owner | Persistence | Key rule / recovery |
|---|---|---|---|
| `DeviceProfile` | A2-002 | persistent local | version/device/firmware keyed; stale on relevant build change; corrupt → rescan |
| `IncidentRecord` | A2-003/A2-008 | persistent local | immutable incident identity/times/symptom + evidence refs; no invented backfill |
| `DirectPlatformEvent` | A2-003/A2-008 | incident-scoped | source/API/access/version attached; unstable descriptions not semantic keys |
| `CaptureBundle` | A2-004/A2-008 | bounded retention | tier, duration, observer-cost and privacy metadata required |
| `IncidentAttribution` | A2-003/A2-008 | derived with incident | recomputable; contradictory/missing evidence retained |
| `PlatformPolicyAssessment` | A2-007/A2-008 | versioned optional | documentation source/version; unknown target branch invalidates specifics |
| `ObserverBudgetRecord` | A2-004/A2-008 | per capture/experiment | records cost; breach disables optional probes |
| `ExperimentRecord` | A2-005/A2-008 | append/history preserving | paired trials, conditions, outcomes, negative evidence preserved |
| `CandidateAction` | A2-005 | audit | proposal only; cannot encode free-form shell |
| `ActuatorQualification` | A2-006/A2-008 | persistent local | exact actuator+device+firmware+evidence; corruption/stale → NOT_QUALIFIED |
| `SafetySnapshot` | A2-006 | transaction journal | missing rollback state blocks write |
| `UserPolicy` | A2-001/A2-008 | persistent local | conservative default; explicit priority is input, not hidden inference |
| `AuditEvent` | A2-008 | append-oriented | provenance gaps are visible |

## Logical schemas
```text
DeviceProfile {
  schemaVersion, deviceFingerprint, firmwareFingerprint,
  androidApi, androidFullSdk?, vendorFamily, vendorBuild,
  capabilities: [{id, status: SUPPORTED|UNSUPPORTED|UNOBSERVABLE|UNKNOWN,
                  access: APP|SHELL_READ|ROOT_READ|PRIVILEGED_WRITE,
                  versionScope, evidenceRef}],
  createdAt
}

IncidentRecord {
  incidentId, sessionId, observedAt, userSymptom?, targetPackageHash?,
  directEvents[], captureRefs[], policyAssessmentRef?,
  attributionRef?, outcomeRefs[]
}

DirectPlatformEvent {
  eventType: EXIT|START|MEMORY_LIMITER|FREEZER|POLICY|USER_STATE|OTHER,
  timestamp, processState?, reasonCode?, startType?,
  sourceApi, sourceVersion, accessMethod, rawEvidenceRef
}

IncidentAttribution {
  engineVersion, incidentId,
  cause: MEMORY_LIMITER|LMK_GLOBAL_PRESSURE|FREEZER_OR_FROZEN_IPC|
         PLATFORM_BACKGROUND_POLICY|CRASH_ANR_OR_INIT_FAILURE|
         APP_SELF_RESOURCE_PRESSURE|CPU_CONTENDED|IO_BOUND|THERMAL_LIMITED|
         USER_OR_PACKAGE_STATE_CHANGE|UNKNOWN_OR_MIXED,
  confidence: LOW|MEDIUM|HIGH,
  directEvidence[], contextualEvidence[], contradictingEvidence[], gaps[]
}

ObserverBudgetRecord {
  captureTier, plannedDuration, actualDuration?,
  anonymousRssSwapBefore?, anonymousRssSwapAfter?, cpuDelta?, wakeupDelta?,
  thermalBefore?, thermalAfter?, budgetBreach: boolean|UNKNOWN
}
```

## Migration rules
- Schema-version every persistent object.
- Missing required evidence fields fail closed to UNKNOWN; never convert missing to zero/false.
- Full SDK/API/vendor build changes invalidate affected adapters/capabilities.
- Firmware change invalidates every write qualification and any device-specific semantic mapping.
- Raw cross-app evidence stays local/private by default; shared exports hash/redact package/process identifiers unless explicitly retained by user.
- Old FH-A1 persisted objects, if ever implemented, require explicit migration mapping; no current Android store exists, so this is specification only.
