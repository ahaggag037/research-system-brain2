# ACTIVE NOTES

> Noncanonical operational scratch. Canonical truth is in `PROJECT_STATE.json`, `docs/**`, `FINAL_AUDIT.md`, and `HANDOFF_CHECKPOINT.md`.

## Final-session facts
- Selected architecture: FH-A1 Evidence-Gated Adaptive Supervisor.
- M0 read-only probe + host analyzer are implemented; host suite is 6/6 PASS.
- Android APK and privileged write actuators are not implemented.
- F-001 portable TSV manifest parsing defect was found, repaired, and regression-tested.
- GitHub-only cold-start via authenticated connector PASS.
- Direct `git clone` from the execution container failed because DNS could not resolve github.com; treated as a tool limitation, not repository evidence.
- B-001 remains: no actual Huawei target device in-session. It blocks target validation/M1 evidence, not this completed knowledge mission.
- `_human/` and all predecessor user repositories remained unread.

## Exact next task
Run M1 E-001/E-002 on the actual target using read-only tools; keep raw device evidence private.
