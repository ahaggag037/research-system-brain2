# Readiness Definitions — FH-A2

- `RESEARCH_RECONVERGED`: mandatory external research complete, architecture reevaluated, source/decision delta traceable.
- `M0_HOST_TESTED`: read-only probe/analyzer source passes host tests/validators; says nothing about target command availability.
- `DEVICE_PROFILE_READY`: M1 target capability profile completed read-only.
- `INCIDENT_EVIDENCE_READY`: at least one target incident can be reconstructed with explicit gaps/provenance.
- `BUILD_READY`: Android project/toolchain locked from real environment and clean build/test succeeds.
- `DEVICE_TEST_READY`: APK installs/launches on target and no-write/observer-budget tests pass.
- `DAILY_USE_READY`: M3 stability/privacy/retention/overhead criteria pass across representative workload.
- `ACTUATOR_CANARY_READY`: exactly one actuator satisfies qualification/rollback + target causal evidence.
- `PRODUCTION_ACTUATOR_READY`: repeated benefit and safety evidence supports bounded production use on exact device/firmware class.

Knowledge-package completion never implies Android build/device readiness.
