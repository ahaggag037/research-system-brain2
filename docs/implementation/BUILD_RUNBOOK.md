# Build / Run / Install Runbook — FH-A2

## Current implementation reality
The repository contains **M0.2 read-only shell probe + host analyzer/tests/validators**, not an Android APK. FH-A2 Android M2 is specified but not implemented; Android toolchain versions remain `UNKNOWN` until M1/M2 bootstrap rather than being guessed.

## M0.2 host verification
```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py .
python tools/final_audit_check.py .   # final-state checks; may intentionally fail during active edits
sh -n tools/device_probe.sh
python -m py_compile tools/*.py tests/*.py
```

## Run the read-only target probe
```bash
adb push tools/device_probe.sh /data/local/tmp/fixhua_device_probe.sh
adb shell chmod 700 /data/local/tmp/fixhua_device_probe.sh
adb shell 'rm -rf /data/local/tmp/fixhua-snapshot && sh /data/local/tmp/fixhua_device_probe.sh /data/local/tmp/fixhua-snapshot'
adb pull /data/local/tmp/fixhua-snapshot ./private-device-snapshots/fixhua-snapshot
python tools/analyze_snapshot.py ./private-device-snapshots/fixhua-snapshot --out ./private-device-snapshots/report.json
```
`private-device-snapshots/` is gitignored and must stay private by default.

The probe only reads optional system facts. `am memory-limiter status` is read-only; **do not** substitute `am memory-limiter ignore` or `manual` in M0/M1. Missing/denied commands are recorded rather than treated as false capability.

## M1 manual evidence checklist
After the probe, use only read/API checks needed by `FIRST_BUILD_CRITICAL_PATH.md`. Record command/API, version, privilege and result. Do not hard-code a node/path because AOSP lists it. Do not copy consumer-support UI paths without checking exact target version.

## Android M2 bootstrap — not yet executed
1. Read actual target API/full-SDK and available build environment.
2. Select a current supported JDK/AGP/Gradle/compileSdk/minSdk combination from official Android docs/tool output.
3. Commit Gradle wrapper and exact versions in same change as Android project bootstrap.
4. Update this runbook + `PROJECT_STATE.json` from UNKNOWN to actual values.
5. CI: validate docs/JSON → host tests → Android unit/contract tests → clean debug build → archive artifact/test reports.
6. Device lane: install/launch target smoke + no-write audit + observer-budget subset.

## Planned variants
- `debug`: diagnostics and evidence visibility; no release signing.
- `release`: future daily build; signing secrets outside repository.
- experimental privileged write support: separate feature/config, default disabled and gated by qualification record.

## Artifact proof
Every APK/build artifact must map to exact Git commit + reproducible command/CI run + SHA-256. Host M0.2 proof is test output from the exact tree.

## Common failures
- `adb` absent: host tests still run; target M1 blocked.
- optional probe denied/missing: expected capability result; do not retry with writes.
- MemoryLimiter unavailable: do not infer Android 17 behavior applies to target.
- Perfetto trigger unavailable: fall back to T1 snapshot; do not force continuous tracing.
- thermal headroom NaN/unsupported: record capability gap and use available thermal status/context.
- Android tool mismatch: use tool/official compatibility evidence and update runbook/state; do not invent versions.
