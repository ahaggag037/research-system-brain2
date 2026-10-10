# Codebase Map — Arm B

## Implemented M0.2
- `tools/device_probe.sh` — read-only target snapshot/capability probe; Arm B adds swaps, cgroup controllers, MGLRU enabled file, MemoryLimiter status and Perfetto version probes.
- `tools/analyze_snapshot.py` — host conservative report; Arm B adds capability observations without causal promotion.
- `tests/test_analyze_snapshot.py` — parser/conservatism/capability tests.
- `tests/test_device_probe.py` — manifest + Arm B probe-presence regression.
- `tools/validate_repo.py` — structural/JSON/no-write guard.
- `tools/final_audit_check.py` — final package consistency checks.
- `schemas/` — M0 manifest/report schemas.

## Canonical FH-A2 specs
- `docs/architecture/` — selected topology/contracts/runtime/data/safety/recovery/reevaluation.
- `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md` — mandatory question-driven external evidence.
- `docs/implementation/` — M1→M6 execution path.
- root JSON maps — machine-readable state/navigation/traceability.

## Not implemented
No Android/Gradle project exists yet. No A2 production component should be mistaken for source code merely because its contract is fully specified.
