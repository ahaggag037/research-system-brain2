# Documentation-Level Integration Proof

## Flow A — User investigates app reload/slow resume
CMP-001 Diagnose → CMP-002 profile → CMP-003 baseline/incident capture → CMP-004 evidence-backed state or UNKNOWN → initial CMP-005 no-op / CMP-007 documented guidance → CMP-008 local persistence → CMP-001 visible explanation; CMP-009 optional redacted export. Denied probes become UNOBSERVABLE rather than zero. No system write occurs in M2.

## Flow B — Huawei policy-limited background app
User selects continuity symptom → no critical pressure plus relevant documented settings evidence → estimator may emit `VENDOR_POLICY_LIMITED` only when supported → CMP-007 presents version-qualified official guidance/deep link → user changes setting manually → repeat observation verifies outcome. Unknown firmware/UI stays UNKNOWN; no hidden vendor database mutation.

## Flow C — Future qualified privileged actuator
StateEstimate + policy → typed candidate → CMP-006 exact-profile/qualification/safety precheck → SafetySnapshot/journal → bounded apply → read-back → canary observation → evidence on success; any failure/controller fight/regression → rollback + verify + suspend qualification. There is no path from UI text to an arbitrary root command.

## Flow D — Firmware update
Startup fingerprint change → old profile stale → all write qualifications invalid → observer-only mode → rescan → new qualification required. Failure leaves conservative read-only mode.

## Flow E — Corrupt local state
Startup validation fails → CMP-008 quarantines corrupt state → qualifications default NOT_QUALIFIED → UI recovery/degraded mode → profile rebuild. No hidden control jump or invented evidence remains.
