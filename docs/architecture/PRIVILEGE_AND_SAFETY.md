# Privilege and Safety Model

## Privilege ladder
1. **APP:** ordinary Android APIs; safest/default.
2. **SHELL_READ:** explicit ADB/Shizuku-like shell read capability where user-configured; exact broker is not selected yet.
3. **ROOT_READ:** explicit temporary root session for otherwise inaccessible diagnostics.
4. **PRIVILEGED_WRITE:** disabled by default; per-actuator qualification required.

The architecture does not depend on unrestricted root being continuously available.

## Production actuator admission contract
A privileged write can be admitted only when all are true:
- exact target control is **observed**, not assumed;
- semantics and owner/controller interactions are understood sufficiently for the bounded use;
- action scope and parameter bounds are explicit;
- expected user-visible/system effect is measurable;
- operating-state preconditions/exclusions are encoded;
- baseline and rollback state can be captured;
- timeout and abort conditions are explicit;
- post-write verification exists;
- rollback has been failure-injection tested;
- canary evidence on the same device/firmware supports benefit/no unacceptable regression;
- qualification is tied to that device/firmware and can be revoked.

If any item is missing: `NOT_QUALIFIED` → shadow/research only.

## Forbidden design space
FixHUA must not:
- disable thermal throttling/hardware safety protections;
- bypass verified boot, app integrity, DRM, account/banking/security protections;
- expose a network/UI API that accepts arbitrary root commands;
- make permanent boot/system modifications in the first installable build;
- treat writable sysfs/procfs/cgroup files as proof of safe ownership;
- repeatedly fight a value that Android/Huawei controllers restore.

## Transaction model for future writes
`precheck → capture SafetySnapshot → apply typed bounded operation → read-back verify → canary observe → commit qualification evidence OR rollback → verify recovery`.

One write actuator transaction at a time. Policy has hysteresis/dwell/cooldown so the supervisor does not oscillate with platform controllers.

## Safety on uncertainty
- missing capability → no write;
- conflicting evidence → UNKNOWN/no write;
- firmware changed → qualification invalidated;
- rollback unavailable → no write;
- thermal/stability regression → immediate abort/rollback and suspend actuator;
- control repeatedly overwritten by another controller → blacklist as conflict-prone.
