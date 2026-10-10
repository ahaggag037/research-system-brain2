# Future-Model Continuation Protocol

This repository is designed to continue without the originating conversation.

## First reads
1. `AGENTS.md`
2. `PROJECT_STATE.json`
3. `docs/project/00_START_HERE.md`
4. `HANDOFF_CHECKPOINT.md`
5. `docs/implementation/FIRST_BUILD_CRITICAL_PATH.md`

## Continuation rule
Treat GitHub `main` as canonical. Reconcile claims against actual code/tests before changing state. Do not rely on predecessor repositories or hidden chat context. `.v10/working_memory/` is operational history, not higher authority than canonical docs/code/tests.

## Exact next milestone
`M1 — DEVICE_EVIDENCE_BOOTSTRAP`: on the actual Huawei target, run the read-only `tools/device_probe.sh`, keep raw output private, analyze it with `tools/analyze_snapshot.py`, and execute E-001/E-002. Use the result to choose only observables proven available for M2. Do **not** add privileged writes during M1.

## When facts are missing
Mark them `UNKNOWN`; run the smallest reversible read-only probe. Never invent kernel paths, vendor settings, root brokers, thresholds, actuator values, or target support.

## Privilege rule
No write actuator is currently qualified. A future write must pass `docs/architecture/PRIVILEGE_AND_SAFETY.md` and E-005 on the exact device/firmware. No arbitrary root command surface.

## Same-change obligation
If implementation changes architecture, interfaces, state, privilege, build procedure, readiness, or risk, update affected canonical docs and `PROJECT_STATE.json` in the same change.
