# Build / Run / Install Runbook

## Current implementation reality
The repository currently contains a **host-side reference diagnostic utility**, not an Android APK. Android M2 is specified but not created, so Android SDK/Gradle versions are intentionally `UNKNOWN` rather than invented.

## Current toolchain (M0)
- POSIX-ish Android shell for `tools/device_probe.sh` (`sh`, `cat`, `getprop`, optional `dumpsys`).
- Host Python 3.10+ standard library for analyzer/tests (expected to work on newer Python 3.x; tested in the mission environment in State D).
- ADB is optional but convenient for moving the script/snapshot.

## Repository layout
- `tools/` — M0 probe/analyzer and validators.
- `tests/` — host reference tests.
- `schemas/` — machine-readable snapshot/report schema.
- `docs/` — canonical architecture/evidence/implementation/visual system.
- `.v10/working_memory/` — operational scratch, noncanonical after distillation.
- root JSON files — project state/navigation/traceability.

## Host test
```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py .
```

## Run the read-only device probe
The script only reads system metadata/`/proc`/safe `dumpsys` output and writes into the supplied **user-writable snapshot directory**. It does not write system settings, sysfs, procfs or cgroups.

Example with ADB:
```bash
adb push tools/device_probe.sh /data/local/tmp/fixhua_device_probe.sh
adb shell chmod 700 /data/local/tmp/fixhua_device_probe.sh
adb shell 'rm -rf /data/local/tmp/fixhua-snapshot && sh /data/local/tmp/fixhua_device_probe.sh /data/local/tmp/fixhua-snapshot'
adb pull /data/local/tmp/fixhua-snapshot ./private-device-snapshots/fixhua-snapshot
python tools/analyze_snapshot.py ./private-device-snapshots/fixhua-snapshot --out ./private-device-snapshots/report.json
```
Do not commit `private-device-snapshots/` to this public repository.

## Android M2 environment bootstrap — not yet executed
Smallest verification step:
1. On the implementation machine, inspect installed JDK/Android SDK or create a current empty Android app with Android Studio/Gradle.
2. Select a supported `compileSdk`, `minSdk` based on the **actual target API**, JDK and Android Gradle Plugin combination from current Android documentation/tool output.
3. Commit the Gradle wrapper and exact versions/checksums in the same change that creates M2 modules.
4. Update this runbook + `PROJECT_STATE.json` from UNKNOWN to VERIFIED/IMPLEMENTED.

Until that step, do **not** claim `BUILD_READY` for Android.

## Planned Android variants
- `debug`: local/device diagnostics; verbose diagnostic UI; no release signing.
- `release`: future daily build; release signing outside repository.
- Experimental privileged actuator support must be a separately gated feature/config and cannot silently ship enabled.

## CI path (planned M2)
Checkout → validate machine-readable docs → run unit/contract tests → Gradle clean assembleDebug → archive unsigned/debug APK + test reports. A device/emulator lane runs install/launch smoke; target Huawei lane remains required for DEVICE_TEST_READY.

## Signing boundary
Never commit private keys, keystores, passwords, API secrets or root-broker credentials. Release signing must use local secure storage or CI secret store. Repository may contain only public certificate fingerprints/verification instructions after a release process exists.

## Clean rebuild / artifact-source proof
For M0: delete Python cache/output, rerun tests/validator.  
For M2 later: `./gradlew clean test assembleDebug` from a clean checkout; record Git commit SHA and APK SHA-256 in build evidence. Artifact provenance must point to exact commit + CI run or local reproducible command.

## Common failures
- `adb` absent → install platform-tools externally; M0 host tests still run.
- permission denied reading a probe → expected; command status records denial and capability remains UNOBSERVABLE.
- parser input missing → analyzer returns unknown/missing field, not a fabricated zero.
- Android tool version mismatch later → follow Gradle/AGP error, lock compatible versions, update runbook/state in same change rather than guessing.
