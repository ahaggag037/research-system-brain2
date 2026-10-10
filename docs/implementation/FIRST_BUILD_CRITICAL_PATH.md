# First-Build Critical Path

## A. First useful build — current repository utility
1. Checkout repository.
2. Run `python -m unittest discover -s tests -v`.
3. Copy/run `tools/device_probe.sh` on the device as documented in `BUILD_RUNBOOK.md`.
4. Pull the snapshot directory.
5. Run `python tools/analyze_snapshot.py <snapshot_dir> --out report.json`.
6. Review `observability`, pressure summaries and unknowns. Do not tune the phone from this report alone.

**Exit:** schema-valid report is produced and no device state is changed by the probe.

## B. First installable/testable Android build — M2
Minimum components: CMP-001, CMP-002, CMP-003, conservative CMP-004, CMP-008, CMP-009, plus CMP-007 shell/UI guidance if cheap. CMP-005/006/010 may be stubbed **only as disabled interfaces**; no fake actuation.

### Exact order
1. **M1 target evidence** — cannot be stubbed; selects actual observable set.
2. Lock Android project toolchain/JDK/SDK/Gradle based on a clean generated project; commit wrapper/checksums.
3. Implement `core-model` schemas + serialization/migration and fixture tests.
4. Implement capability adapters only for M1-proven sources.
5. Implement recorder with overhead instrumentation and bounded incident capture.
6. Implement state estimator with UNKNOWN/conflict semantics; port reference fixtures.
7. Implement local evidence store + retention + corruption recovery.
8. Implement UI session/status/report/error states.
9. Implement redacted export and Huawei documented-settings assistant.
10. Build debug APK in CI and locally; install smoke on target.
11. Run E-002 observer-overhead A/B and failure matrix subset.

### Parallel after step 2
- UI skeleton ↔ state store ↔ parser fixture work ↔ settings guidance ↔ CI.
- Integration waits on stable schemas/interfaces.

### May be stubbed temporarily
- CMP-005 as `NO_OP` only;
- CMP-006 as `DisabledPrivilegeGateway` that rejects writes;
- CMP-010 absent/disabled.

### Must not be stubbed
- capability truth/UNKNOWN handling;
- local schema/migration;
- recorder stop/cancellation;
- privacy/redaction boundary;
- no-write guarantee for M2;
- build/install smoke on actual target.

### Mandatory tests before first APK exit
schema unit tests, denied-capability tests, estimator conflict→UNKNOWN, recorder lifecycle, state corruption fallback, export redaction, debug build, APK install/launch, no-write audit, E-002 preliminary overhead.

### Blocking unknowns
Exact Android API/EMUI/HarmonyOS branch, available diagnostics/permissions and chosen explicit shell/root-read broker are M1 outcomes. Until then `BUILD_READY` is false.

## C. First daily-usable build — M3
Requires a stable M2 across representative daily workload, overhead budget established, retention/privacy behavior verified, firmware-change invalidation working, and no open high-severity crash/data-loss issue. Privileged writes are not required for DAILY_USE_READY.
