# FH-A2 Component Contracts

Stable active IDs use `A2-xxx`. Historical `CMP-xxx` IDs remain in prior V10.3-B artifacts/Git history and must not be silently reinterpreted.

## A2-001 — Incident Session Coordinator
- **Purpose:** user-facing diagnose session, incident marker/intake, evidence/confidence/recovery UI.
- **Inputs:** DeviceProfile, IncidentAttribution, CaptureRequest/Status, PlatformPolicyAssessment, Experiment status.
- **Outputs:** explicit diagnose/capture/export/settings-navigation requests and user symptom context.
- **Invariants:** never hides UNKNOWN; UI cannot issue raw privileged commands; no automatic background privilege acquisition.
- **Failure:** degrade to existing local evidence/read-only status.
- **Privilege:** APP only.
- **Tests:** UI state matrix, cancellation/recovery, privilege-boundary test.

## A2-002 — Capability & Platform Profiler
- **Purpose:** establish what the exact build can observe/control before dependent logic assumes it.
- **Inputs:** OS/build metadata; safe APIs/files; optional explicit shell/root-read session.
- **Outputs:** versioned `DeviceProfile` with status + access + evidence provenance.
- **Mandatory capability families:** Android API/full-SDK; low-memory exit reporting; ApplicationStartInfo; MemoryLimiter; app-memory-budget API; cached freezer; PSI; cgroup v2/task profiles; MGLRU; DAMON; Perfetto trigger feasibility; thermal headroom; vendor-policy version.
- **Invariants:** distinguish `UNSUPPORTED`, `UNOBSERVABLE`, `UNKNOWN`; denied != absent; no system write during discovery.
- **Failure:** partial profile allowed; dependent cause/action becomes UNKNOWN/disabled.
- **Privilege:** APP, optional SHELL_READ/ROOT_READ.
- **Tests:** fixture/version matrix; denied access; no-write audit.

## A2-003 — Incident Evidence Engine
- **Purpose:** build a time-aligned incident record and attribute the strongest supported causal class.
- **Inputs:** direct exit/start records, DeviceProfile, bounded capture evidence, policy assessment, symptom context.
- **Outputs:** `IncidentAttribution {cause, confidence, directEvidence[], contextualEvidence[], contradictingEvidence[], gaps[]}`.
- **Evidence rule:** reliable direct version-qualified platform reason outranks generic pressure heuristics; conflicts lower confidence.
- **Invariants:** never parse unstable human description text as a universal semantic contract; no single heuristic authorizes a write; UNKNOWN valid.
- **Failure:** incomplete/ambiguous evidence → `UNKNOWN_OR_MIXED` with requested evidence gap.
- **Privilege:** none itself; consumes evidence with provenance.
- **Tests:** direct-reason fixtures, unsupported-low-memory-report fixture, conflict fixture, exit→start correlation fixture.

## A2-004 — Tiered Capture Orchestrator
- **Purpose:** obtain the minimum additional evidence needed for an incident.
- **Tiers:** T0 platform history; T1 cheap snapshot; T2 bounded triggered Perfetto; T3 explicit privileged read session.
- **Inputs:** evidence gaps, DeviceProfile, ObserverBudget, user approval for higher-cost/private capture.
- **Outputs:** bounded evidence bundle + capture-health/overhead record.
- **Invariants:** no continuous deep tracing by default; high-cost capture time-bounded; privacy and observer cost recorded.
- **Failure:** downgrade tier/mark gap; never “retry until it works” invisibly.
- **Privilege:** APP → optional SHELL_READ/ROOT_READ according to tier.
- **Tests:** minimum-tier selection, timeout/cancel, unsupported Perfetto, overhead shedding.

## A2-005 — Experiment & Shadow Evaluator
- **Purpose:** test whether guidance/policies/actions improve outcomes before promotion.
- **Inputs:** IncidentAttribution, DeviceProfile, candidate, user workflow, thermal/control conditions, historical experiments.
- **Outputs:** `NO_OP`, guidance, more-evidence request, or typed `CandidateAction` marked SHADOW/CANARY eligibility.
- **Invariants:** paired/repeated trials where feasible; user outcome over proxy; hysteresis/cooldown; one experimental actuator at a time.
- **Failure:** experiment uncertainty/regression → no promotion; preserve negative evidence.
- **Privilege:** none.
- **Tests:** no-op default, pairing/repetition, confound detection, regression gate.

## A2-006 — Typed Privilege Gateway
- **Purpose:** isolate privileged reads/writes behind allowlisted typed contracts.
- **Write preconditions:** exact observed control + ownership semantics sufficient + device/firmware qualification + bounded parameters + baseline + abort + read-back + rollback + same-device canary evidence.
- **Outputs:** operation result, verification, rollback result and audit record.
- **Invariants:** no arbitrary command endpoint; one write transaction; deadlines; fail closed.
- **Failure:** rollback; unresolved rollback disables all writes and raises critical fault.
- **Privilege:** SHELL/ROOT only when explicitly acquired.
- **Must not:** disable hardware/thermal safety, verified boot/integrity, DRM/account/banking/security protections.
- **Tests:** type-boundary injection, stale qualification, partial failure rollback.

## A2-007 — Platform Policy Adapter
- **Purpose:** explain OS/vendor policy restrictions separately from memory-pressure causes.
- **Adapters:** Android baseline (Doze/App Standby/background/job restrictions, MemoryLimiter capability metadata) + Huawei EMUI/HarmonyOS documented policy guidance; additional adapters can be added only with evidence.
- **Inputs:** DeviceProfile, policy observables, documented version map, user-confirmed setting state where APIs cannot read it.
- **Outputs:** `PlatformPolicyAssessment` with source/version/confidence and safe navigation guidance.
- **Invariants:** no invented UI path; no undocumented vendor-store edits; app-scoped vendor SDK != global control.
- **Failure:** unknown version → generic/UNKNOWN guidance.
- **Privilege:** APP; read-only shell when explicitly available.
- **Tests:** version maps, unknown fallback, no-undocumented-write audit.

## A2-008 — Evidence Store & Redacted Reporting
- **Purpose:** persist provenance-bearing profiles/incidents/experiments/qualifications and produce human/redacted machine reports.
- **Invariants:** schema migrations; local/private raw cross-app evidence; retention controls; qualification tied to device/firmware; export preview/redaction.
- **Failure:** transactional write; corrupt records quarantined; never infer qualification from partial state.
- **Privilege:** APP.
- **Tests:** migration, corruption recovery, redaction, export schema.

## A2-009 — Continuity Research Module (experimental)
- **Purpose:** estimate continuity value for user-designated workflows in shadow mode.
- **Inputs:** explicit user priority, relaunch distance/history where lawful, cold-start/relaunch cost, footprint, background semantic role.
- **Outputs:** explanation/ranking + experiment hypotheses only.
- **Invariants:** no page-hotness imitation; no “pin everything”; no direct kill/freeze action from prediction; calibrated fallback for insufficient history.
- **Failure:** insufficient generalization/confidence → no ranking/action.
- **Privilege:** none in stock-device form.
- **Tests:** calibration/fallback, explanation stability, background-role protection, out-of-distribution no-op.

## Cross-cutting Observer Budget
Every evidence source declares expected cost class, sampling/capture duration, privacy class, and failure behavior. Runtime records actual cost where measurable. Optional sources are shed before diagnostic instrumentation becomes a material source of jank, memory pressure, heat or battery drain.
