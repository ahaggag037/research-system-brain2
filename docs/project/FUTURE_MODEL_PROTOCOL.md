# Future Model Protocol — FH-A2 continuation

1. Read `AGENTS.md` → `PROJECT_STATE.json` → `docs/project/00_START_HERE.md` → `HANDOFF_CHECKPOINT.md`.
2. Treat V10.3-B/FH-A1 completion as historical, not current architecture truth.
3. Read Arm B external research before reopening architecture: `EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`, `ARCHITECTURE_REEVALUATION_ARM_B.md`, active ADRs.
4. Preserve epistemic hierarchy: **internal knowledge proposes; external evidence challenges/expands; real-device evidence decides device-specific truth.**
5. Never infer target support from AOSP/Huawei docs. Read/measure exact build.
6. For M1 do not add system writes. Collect only read evidence into user-writable/private storage.
7. If direct platform incident evidence is unavailable, record `UNOBSERVABLE` and use the minimum next capture tier; do not create fake certainty from PSI/free RAM.
8. Before any architecture-changing edit, update ADR + PROJECT_STATE + affected machine maps/visuals in the same change.
9. Before any privileged write, satisfy A2-006 admission/rollback contract and same-device experiment evidence.
10. Re-run tests/validators/cold-start after consequential changes.
