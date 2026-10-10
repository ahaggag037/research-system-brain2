# RISK REGISTER

## RISK-001 — Unsafe privileged actuation
RISK_ID: RISK-001
STATUS: ACTIVE
MECHANISM: Root-level writes can be unsupported, device-specific, persistent, interacting, or destabilizing even when technically writable.
IMPACT: Instability, boot/recovery issues, thermal/power harm, data loss, misleading conclusions.
LIKELIHOOD_OR_UNCERTAINTY: High uncertainty before device evidence.
TRIGGER: Any proposal to change privileged runtime/kernel/vendor controls.
DETECTION: Admission checks must require observed node/capability, baseline evidence, bounded expected effect, abort/rollback path, and canary validation.
MITIGATION: Observation-first architecture; allowlisted typed actuators; reversible bounded changes; no arbitrary root shell API.
ABORT_CONDITION: Missing rollback, unclear control semantics, safety interaction, or evidence below admission threshold.
RECOVERY: Revert to baseline/known-safe state; disable actuator; require explicit requalification.
AFFECTED_COMPONENTS: Future privileged actuation layer.
RELATED_EXPERIMENTS: E-001 and future device-specific canaries.

## RISK-002 — Benchmark/tweak superstition
RISK_ID: RISK-002
STATUS: ACTIVE
MECHANISM: Correlated signals or popular tweaks are mistaken for causal interventions.
IMPACT: No real UX improvement, regressions, false confidence.
LIKELIHOOD_OR_UNCERTAINTY: Material.
TRIGGER: Choosing controls from folklore, synthetic score, free-RAM target, or maximum clocks alone.
DETECTION: Require causal hypothesis, falsification path, user-visible metrics, and matched baseline.
MITIGATION: Experiment registry + evidence hierarchy + outcome metrics.
ABORT_CONDITION: Effect cannot be measured or attributed.
RECOVERY: Remove/deprecate intervention; return to observation.
AFFECTED_COMPONENTS: Research and policy engine.
RELATED_EXPERIMENTS: E-001.
