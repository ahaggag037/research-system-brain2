# FH-A2 Privilege, Safety and Observer Budget

## Privilege ladder
1. `APP` — default Android APIs/UI/local storage.
2. `SHELL_READ` — explicit temporary read diagnostics when user/configuration supplies a broker/ADB context.
3. `ROOT_READ` — explicit temporary root-read diagnostics only when otherwise inaccessible evidence is decision-relevant.
4. `PRIVILEGED_WRITE` — disabled by default; each actuator separately qualified.

Direct incident evidence does not waive privilege rules. If cross-UID start/exit history requires DUMP/shell/root, A2-002 records that access boundary; the app does not pretend ordinary API access exists.

## Write admission contract
No change from the strongest FH-A1 rule: exact observed control, sufficient ownership semantics, bounded scope/parameter, measurable user outcome, state preconditions/exclusions, baseline + rollback, timeout/abort, read-back verification, failure-injection rollback test, same-device/firmware canary evidence and revocable qualification. Missing any item = `NOT_QUALIFIED`.

## New observer-safety contract
Evidence gathering itself can distort the system. Therefore:
- no correctness assumption depends on continuous polling by a cached/background app;
- deep traces are bounded and gap-driven;
- capture records its own cost class/health;
- thermal headroom/status sampling obeys platform guidance and capability checks;
- anonymous RSS + swap is preferred for tracking FixHUA's own footprint where available;
- a future self memory budget is experimental and must be sized from measured workload, not a copied constant;
- privacy-sensitive cross-app data stays local and is minimized/redacted on export.

## Forbidden design space
- thermal/hardware safety disablement;
- verified-boot/integrity/DRM/account/banking/security bypasses;
- arbitrary root-command UI/network endpoint;
- deleting/disabling undocumented Huawei system managers as a “fix”;
- permanent boot/system mutation in first installable build;
- unqualified writes to MemoryLimiter config, cgroup, DAMON, MGLRU or vendor stores;
- running a second generic OOM killer against Android controllers;
- silently keeping a privileged daemon alive merely to satisfy telemetry assumptions.
