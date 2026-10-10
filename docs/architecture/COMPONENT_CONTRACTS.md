# Component Contracts

All IDs are stable. Performance numbers are `UNKNOWN` until E-002 establishes target budgets.

## CMP-001 — App/UI + Session Coordinator
- **Purpose:** render current state/evidence, start/stop explicit diagnostic sessions, collect user symptom context, show recovery/errors.
- **Inputs:** DeviceProfile, StateEstimate, IncidentReport, SettingsAssessment, Experiment status.
- **Outputs:** session lifecycle events, user-approved capture/export/settings-navigation requests.
- **Preconditions:** local state schema valid; no implicit privilege grant.
- **Postconditions:** every user-visible action has an audit event and visible state.
- **Invariants:** UI never issues raw privileged commands; no claim stronger than backing truth state.
- **Side effects:** local config/audit writes only.
- **Failure/recovery:** degrade to read-only status; preserve last known safe state; never retry privileged work invisibly.
- **Concurrency:** UI thread for rendering; long work async/cancellable.
- **Privilege:** ordinary app.
- **Must not:** hide UNKNOWN, auto-enable write actuators, or upload raw telemetry.
- **Tests:** T-UI-01 state rendering, T-UI-02 error/recovery state, T-PRIV-01 boundary.

## CMP-002 — Capability Scanner
- **Purpose:** discover what the current device/firmware actually exposes before other components assume it.
- **Inputs:** OS/build metadata, safe filesystem/API probes, optional explicit shell/root read capability.
- **Outputs:** versioned `DeviceProfile` with supported/unsupported/unknown capabilities and provenance.
- **Preconditions:** read-only probe list; bounded timeout.
- **Postconditions:** no system setting changed.
- **Invariants:** absent/denied != false support claim; distinguish unsupported from unobservable.
- **Failure/recovery:** partial profile accepted with UNKNOWN fields; scanner failure cannot trigger actuation.
- **Concurrency:** serial or bounded parallel read probes.
- **Privilege:** ordinary + optional explicit read session.
- **Must not:** hard-code unobserved vendor nodes as facts.
- **Tests:** T-CAP-01 parser fixtures, T-CAP-02 denied capability, T-CAP-03 no-write audit.

## CMP-003 — Flight Recorder
- **Purpose:** capture low-overhead system evidence and bounded incident windows.
- **Inputs:** DeviceProfile, sampling config, incident triggers.
- **Outputs:** ObservationSample stream, IncidentWindow, capture-health metrics.
- **Invariants:** two-speed collection; expensive traces are bounded; overhead metrics accompany evidence.
- **Failure/recovery:** drop optional probes first, mark gaps, keep UI usable; ring-buffer corruption resets only recorder state.
- **Concurrency:** single writer per data stream; timestamps monotonic where available.
- **Privilege:** ordinary; optional read session for privileged observables.
- **Must not:** continuously run high-overhead Perfetto by default.
- **Tests:** T-OBS-01 sampling, T-OBS-02 overhead budget, T-OBS-03 missing-probe degradation.

## CMP-004 — State Estimator
- **Purpose:** explain which operating region best fits current evidence.
- **Inputs:** DeviceProfile + ObservationSample/IncidentWindow + optional symptom context.
- **Outputs:** `StateEstimate {state, confidence, evidence_for, evidence_against, missing_evidence}`.
- **Invariants:** one signal cannot authorize action; contradictions lower confidence; UNKNOWN is valid.
- **Failure/recovery:** invalid/incomplete input → UNKNOWN with reason.
- **Concurrency:** pure/replayable computation where possible.
- **Privilege:** none.
- **Must not:** claim causality from correlation without experiment evidence.
- **Tests:** T-EST-01..05 fixture classes, T-EST-06 conflict→UNKNOWN.

## CMP-005 — Shadow Policy Engine
- **Purpose:** map state/evidence/user intent to candidate actions without direct privilege.
- **Inputs:** StateEstimate, DeviceProfile, ActuatorQualification records, user policy.
- **Outputs:** `NO_OP`, guidance, capture request, or typed CandidateAction.
- **Invariants:** default deny; no unqualified write action; one experimental actuator at a time; hysteresis/dwell/cooldown around stateful actions.
- **Failure/recovery:** engine error → NO_OP + report.
- **Privilege:** none.
- **Must not:** execute commands itself.
- **Tests:** T-POL-01 default no-op, T-POL-02 qualification gate, T-POL-03 cooldown.

## CMP-006 — Typed Privilege Gateway
- **Purpose:** isolate privileged observation/actuation behind allowlisted typed contracts.
- **Inputs:** typed request, DeviceProfile, qualification record, safety snapshot.
- **Outputs:** result + verification + rollback result + audit event.
- **Preconditions for writes:** observed control, approved qualification, exact device/firmware match, safe operating region, rollback captured.
- **Postconditions:** either verified requested state or verified rollback/degraded-safe result.
- **Invariants:** no raw command surface to UI/network; time-bounded; one actuator transaction at a time.
- **Failure/recovery:** partial/failure immediately invokes actuator-specific rollback; unresolved rollback marks critical fault and disables all writes.
- **Privilege:** shell/root only when explicitly acquired.
- **Must not:** disable thermal/hardware safety or bypass platform/app integrity/security.
- **Tests:** T-PRIV-01 command-surface denial, T-PRIV-02 precondition gate, T-PRIV-03 rollback injection.

## CMP-007 — Huawei Compatibility Assistant
- **Purpose:** distinguish/document common Huawei background-policy restrictions and guide safe user changes.
- **Inputs:** model/OS family, symptom context, observable settings/intents where documented.
- **Outputs:** SettingsAssessment + version-qualified guidance/deep links.
- **Invariants:** programmatic mutation only if a documented supported API exists; otherwise human-confirmed settings guidance.
- **Failure/recovery:** unknown UI/version → generic vendor guidance marked UNKNOWN, not invented paths.
- **Privilege:** ordinary.
- **Tests:** T-HUA-01 version mapping, T-HUA-02 unknown-version fallback.

## CMP-008 — Experiment & Evidence Store
- **Purpose:** persist versioned profiles, experiments, qualification and audit provenance.
- **Inputs:** records from scanner/recorder/estimator/policy/gateway.
- **Outputs:** queryable local evidence, replay inputs, qualification history.
- **Invariants:** migrations versioned; raw sensitive exports opt-in; qualification tied to device/firmware fingerprint.
- **Failure/recovery:** transactional writes; corruption → quarantine + rebuild from safe configuration, never infer qualification.
- **Privilege:** ordinary.
- **Tests:** T-STATE-01 migration, T-STATE-02 corruption recovery.

## CMP-009 — Report / Redacted Export
- **Purpose:** create human-readable diagnosis and privacy-reduced machine bundle.
- **Inputs:** DeviceProfile, IncidentWindow, StateEstimate, audit record.
- **Outputs:** local report/export.
- **Invariants:** export preview; no secrets; package/activity identifiers redacted by default for sharing.
- **Failure/recovery:** failed export leaves source store intact.
- **Privilege:** ordinary.
- **Tests:** T-EXP-01 redaction, T-EXP-02 schema.

## CMP-010 — Continuity Allocator (experimental)
- **Purpose:** estimate relative continuity value for user-designated workloads; initially shadow-only.
- **Inputs:** explicit user priority, recency/reuse observations, cold-start cost, footprint/background-role signals where lawful/observable.
- **Outputs:** explanation/ranking; no initial destructive action.
- **Invariants:** user intent dominates; no “pin everything”; no freezer-as-memory-relief assumption.
- **Failure/recovery:** insufficient evidence → no ranking/action.
- **Privilege:** none in initial form.
- **Tests:** T-CONT-01 explanation stability, T-CONT-02 background-role protection.
