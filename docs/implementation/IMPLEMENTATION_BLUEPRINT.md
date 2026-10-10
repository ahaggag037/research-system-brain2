# FH-A2 Implementation Blueprint

## Dependency direction
`core-model` is pure/versioned → platform capability adapters → incident evidence engine → capture orchestration/platform policy → local evidence store/report → UI → experiment/shadow → typed privilege gateway. Continuity research depends on evidence/experiment interfaces, never on raw privilege.

## Suggested Android modules (M2+)
- `core-model`: DeviceProfile, IncidentRecord, DirectPlatformEvent, Attribution, Capture/ObserverBudget, experiment schemas.
- `platform-android`: public API adapters for start/exit/thermal/background policy supported by target API.
- `platform-shell`: explicit broker/read adapters; no arbitrary write command API.
- `incident-engine`: correlation/evidence ranking/UNKNOWN semantics.
- `capture`: T0/T1 orchestration; optional Perfetto trigger adapter after M1 proof.
- `policy-adapters`: Android baseline + Huawei version-qualified guidance.
- `evidence-store`: migrations/retention/redaction/reporting.
- `app`: UI/session lifecycle.
- `experiment`: paired trial/shadow logic; initially NO_OP.
- `privilege-gateway`: disabled-write implementation until M5 qualification.
- `continuity-research`: optional M4 module, shadow only.

## Concurrency
- one incident session coordinator state machine;
- capture tier has one active bounded operation per session unless explicitly proven safe;
- evidence store transactional single-writer/serialized migrations;
- privileged writes globally serialized;
- expensive target evidence collection cancellable/deadline-bound.

## Version strategy
Platform adapters declare min/max or tested API/full-SDK/vendor ranges. New direct reason codes (for example MemoryLimiter) enter through adapters/fixtures, not ad-hoc string matching. Unsupported/denied are first-class.

## Privacy strategy
Target package/process identifiers are local. Incident export hashes/redacts by default. Raw Perfetto/dumpsys snapshots are never automatically committed or uploaded.
