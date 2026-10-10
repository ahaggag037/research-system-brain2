# EXPERIMENT REGISTRY

## E-001 — Device evidence bootstrap (planned)
EXPERIMENT_ID: E-001
STATUS: PROPOSED
HYPOTHESIS: A lightweight observation-first build can identify dominant device-specific bottlenecks before any risky privileged tuning is attempted.
WHY_IT_MATTERS: Prevents superstition and device-agnostic tweak bundles.
INPUT/CONDITIONS: Real Huawei-class device, representative foreground/background workloads, baseline/no-actuation mode.
MEASUREMENTS: To be refined during Discovery; candidate classes include frame timing/jank, process/app lifecycle, memory pressure, thermal/power state, CPU/load, I/O latency, resume/reload events.
EXPECTED_RESULT: Sufficient causal clues to select bounded interventions or reject them.
FALSIFICATION_CONDITION: Collected observables cannot distinguish competing bottleneck mechanisms well enough to guide action.
ABORT_CONDITION: Measurement requires unsafe permissions, excessive overhead, sensitive data collection, or destabilizes the device.
RISK_LEVEL: LOW in observation-only form.
RESULT: Not run.
DECISION_IMPACT: Will gate privileged-actuation choices.
ARTIFACTS: Future diagnostic output schema + validation runbook.
