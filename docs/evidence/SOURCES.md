# SOURCE INDEX

> Independent public sources only. No predecessor/user FixHUA sources are permitted. Accessed 2026-10-10 unless noted.

## S-001 — AOSP LMKD current source/README
SOURCE_ID: S-001
TYPE: SOURCE_CODE
TITLE: Android Low Memory Killer Daemon (`platform/system/memory/lmkd`)
LOCATION: https://android.googlesource.com/platform/system/memory/lmkd/+/refs/heads/master/
DATE/RECENCY: Current branch as accessed 2026-10-10
CLAIMS_SUPPORTED: Android uses userspace `lmkd` to monitor memory state and kill less-essential processes under pressure; current LMKD exposes PSI/thrashing/swap-related configuration and behavior.
LIMITATIONS: AOSP behavior can be vendor-customized; property availability/value on a Huawei-class target must be observed, not assumed.
NOTES: Strong evidence that app reload/exits can be a memory-pressure outcome, but not the only one.

## S-002 — 2026 LMKD PSI correction
SOURCE_ID: S-002
TYPE: SOURCE_CODE
TITLE: `lmkd: avoid killing if full PSI stall but device is not low on memory`
LOCATION: https://android.googlesource.com/platform/system/memory/lmkd/+/da500621995ff2578e4d5e2a0d1648709ab8e42c%5E%21/
DATE/RECENCY: 2026-04-22 commit
CLAIMS_SUPPORTED: Full memory PSI alone can be misleading in at least some memcg-limit conditions; current AOSP added a guard to avoid treating every full stall as global critical pressure.
LIMITATIONS: Specific patch applicability depends on platform/version; do not generalize exact logic to vendor builds.
NOTES: Supports multi-signal diagnosis and rejection of single-threshold “magic PSI” control.

## S-003 — Linux PSI
SOURCE_ID: S-003
TYPE: PRIMARY_PLATFORM
TITLE: PSI — Pressure Stall Information
LOCATION: https://docs.kernel.org/accounting/psi.html
DATE/RECENCY: Current Linux kernel documentation
CLAIMS_SUPPORTED: PSI quantifies CPU/memory/I/O contention as stall time and supports threshold-triggered monitoring; intended uses include dynamic load shedding and preventing disruption under resource crunch.
LIMITATIONS: Availability/permissions and semantics on a target Android kernel must be probed.
NOTES: Strong candidate for low-overhead pressure sensing when supported.

## S-004 — Android cached-app freezer
SOURCE_ID: S-004
TYPE: PRIMARY_PLATFORM
TITLE: Cached apps freezer
LOCATION: https://source.android.com/docs/core/perf/cached-apps-freezer
DATE/RECENCY: Current AOSP documentation
CLAIMS_SUPPORTED: Android can freeze cached apps via cgroup v2 to keep them resident while reducing CPU use; Android 14+ freezes cached processes after entry; supported devices can keep more cached processes and reduce cold starts.
LIMITATIONS: OEM enablement and kernel support vary; direct third-party control is not implied.
NOTES: Demonstrates that “keep warm without letting cached apps consume CPU” is already a platform design pattern; FixHUA should observe/augment rather than blindly duplicate it.

## S-005 — Android process lifecycle/importance
SOURCE_ID: S-005
TYPE: PRIMARY_PLATFORM
TITLE: Activity process lifecycle
LOCATION: https://developer.android.com/reference/android/app/Activity
DATE/RECENCY: Current Android API documentation
CLAIMS_SUPPORTED: Android retains processes opportunistically and kills less-important processes under memory pressure according to process importance tied to user interaction.
LIMITATIONS: OEM policies can add behavior; framework internals evolve.
NOTES: User-visible reloads are partly an intentional cache-eviction tradeoff, not simply a “bug.”

## S-006 — ApplicationExitInfo
SOURCE_ID: S-006
TYPE: PRIMARY_PLATFORM
TITLE: `ApplicationExitInfo` and `ActivityManager.getHistoricalProcessExitReasons`
LOCATION: https://developer.android.com/reference/android/app/ApplicationExitInfo and https://developer.android.com/reference/android/app/ActivityManager
DATE/RECENCY: Current Android API documentation
CLAIMS_SUPPORTED: Android 11+ can report reasons for process deaths including low memory, ANR, crash, freezer, excessive resource usage, user request, and others; querying another UID requires DUMP permission.
LIMITATIONS: Low-memory reporting is not supported on every device; ordinary apps cannot query arbitrary other UIDs without privileged access.
NOTES: Root/shell capability can materially improve diagnosis, while a non-root build should not pretend to know cross-app exit causes.

## S-007 — Android memory allocation / zRAM
SOURCE_ID: S-007
TYPE: PRIMARY_PLATFORM
TITLE: Memory allocation among processes
LOCATION: https://developer.android.com/topic/performance/memory-management
DATE/RECENCY: Current Android performance documentation
CLAIMS_SUPPORTED: Android uses reclaim and zRAM under memory pressure; memory management is not reducible to “free RAM.”
LIMITATIONS: Device-specific zRAM size, writeback, reclaim policy, and kernel features must be measured.
NOTES: Supports pressure/stall and refault-aware metrics over free-RAM targets.

## S-008 — Android cgroup abstraction/task profiles
SOURCE_ID: S-008
TYPE: PRIMARY_PLATFORM
TITLE: Cgroup abstraction layer
LOCATION: https://source.android.com/docs/core/perf/cgroups
DATE/RECENCY: Current AOSP documentation
CLAIMS_SUPPORTED: Android uses cgroup/task-profile abstractions; vendor/API-level overrides can change underlying profile definitions; direct cgroup assumptions are device/version-specific.
LIMITATIONS: Root writability does not establish framework compatibility or durability of a change.
NOTES: Strong reason to prefer capability discovery + typed adapters over hard-coded paths.

## S-009 — AOSP task profile definitions
SOURCE_ID: S-009
TYPE: SOURCE_CODE
TITLE: `libprocessgroup/profiles/task_profiles.json`
LOCATION: https://android.googlesource.com/platform/system/core/+/master/libprocessgroup/profiles/task_profiles.json
DATE/RECENCY: Current AOSP branch as accessed
CLAIMS_SUPPORTED: Modern task profiles expose concepts such as cpusets, memory controls, utilization clamps, and freezer state, but exact files/controllers differ across versions.
LIMITATIONS: AOSP reference only; vendor overrides are explicitly allowed by S-008.
NOTES: Candidate control surface for research qualification, not evidence for production writes on a Huawei target.

## S-010 — Thermal mitigation
SOURCE_ID: S-010
TYPE: PRIMARY_PLATFORM
TITLE: Thermal mitigation
LOCATION: https://source.android.com/docs/core/power/thermal-mitigation
DATE/RECENCY: Current AOSP documentation
CLAIMS_SUPPORTED: Android thermal framework actively throttles work and can materially degrade UX under thermal stress; platform guidance explicitly says not to disable thermal mitigation.
LIMITATIONS: Detailed sensor access may be limited; OEM HAL/policies vary.
NOTES: Any “boost” policy must be thermal-aware and must never disable hardware/platform safety protections.

## S-011 — Perfetto system tracing
SOURCE_ID: S-011
TYPE: PRIMARY_PLATFORM
TITLE: Advanced System Tracing on Android / Perfetto CLI
LOCATION: https://perfetto.dev/docs/learning-more/android and https://perfetto.dev/docs/reference/perfetto-cli
DATE/RECENCY: Current Perfetto documentation
CLAIMS_SUPPORTED: Android 9+ supports on-device/system tracing with Perfetto; traces can cover scheduling, frequencies, ActivityManager/WindowManager, graphics, binder, memory and other sources depending on version/config.
LIMITATIONS: Always-on tracing can add overhead/storage cost; source availability and permissions vary.
NOTES: Best as bounded triggered “deep capture,” not the default continuous telemetry loop.

## S-012 — Android dumpsys diagnostics
SOURCE_ID: S-012
TYPE: PRIMARY_PLATFORM
TITLE: `dumpsys` developer documentation
LOCATION: https://developer.android.com/tools/dumpsys
DATE/RECENCY: Current Android developer documentation
CLAIMS_SUPPORTED: `dumpsys` exposes meminfo, procstats, gfxinfo/framestats, input and other service diagnostics from shell/ADB context.
LIMITATIONS: Output varies by Android version and vendor; parsing must be version tolerant.
NOTES: Useful first-build evidence surface with shell/root capability.

## S-013 — Huawei background-app troubleshooting
SOURCE_ID: S-013
TYPE: VENDOR
TITLE: Unable to run background apps on my HUAWEI phone/tablet
LOCATION: https://consumer.huawei.com/en/support/content/en-us00428704/
DATE/RECENCY: Current Huawei Support as accessed
CLAIMS_SUPPORTED: Huawei documents App launch management, background-running permission, battery optimization, power saving, recents locking, and insufficient running memory as distinct reasons background apps may stop.
LIMITATIONS: Support guidance is product/version dependent and user-facing rather than a stable developer API contract.
NOTES: Critical evidence that “app exits” can be vendor policy/settings rather than LMKD; diagnosis must classify before tuning memory.

## S-014 — Huawei background protection
SOURCE_ID: S-014
TYPE: VENDOR
TITLE: Setting background protection for HUAWEI (EMUI 9.0 or later / HarmonyOS 2.0 or later)
LOCATION: https://consumer.huawei.com/en/support/content/en-us15850065/ and https://consumer.huawei.com/en/support/content/en-us15850069/
DATE/RECENCY: Current Huawei Support as accessed
CLAIMS_SUPPORTED: Huawei exposes user controls for auto-launch/secondary launch/background running, battery optimization, and recents locking that can affect app continuity.
LIMITATIONS: Exact UI paths and semantics vary by model/version; programmatic mutation is not documented here.
NOTES: Supports a safe “settings compatibility assistant” before undocumented root edits.

## S-015 — Huawei Accelerate Kit / PerfGenius
SOURCE_ID: S-015
TYPE: VENDOR
TITLE: HUAWEI Accelerate Kit — PerfGenius
LOCATION: https://developer.huawei.com/consumer/en/codelab/HMSAccKit-PerfGenius/
DATE/RECENCY: Current Huawei developer documentation as accessed
CLAIMS_SUPPORTED: Huawei itself uses state-aware performance interfaces for frame rate/key-thread/system-state coordination in supported app scenarios, reinforcing state-aware rather than static maximum-performance strategies.
LIMITATIONS: SDK scope/eligibility does not imply system-wide control of arbitrary apps and may require Huawei developer integration.
NOTES: Conceptual/vendor evidence only, not selected as a FixHUA dependency.

## S-016 — Multi-Gen LRU
SOURCE_ID: S-016
TYPE: PRIMARY_PLATFORM
TITLE: Multi-Gen LRU
LOCATION: https://docs.kernel.org/mm/multigen_lru.html
DATE/RECENCY: Current Linux kernel documentation
CLAIMS_SUPPORTED: Modern reclaim can use recency-aware generations and self-correcting heuristics to improve reclaim under pressure.
LIMITATIONS: Target kernel may not enable MGLRU; a root app must not assume the feature.
NOTES: Supports capability discovery and the broader principle that recency/reuse matters for memory continuity.

## Arm B mandatory external-research expansion — 2026-10-10

| ID | Primary source | Key support | Limitation |
|---|---|---|---|
| S-017 | Android 17 behavior changes — https://developer.android.com/about/versions/17/behavior-changes-all | App memory limits are a new Android 17 behavior and expose `am memory-limiter` status/test commands. | Exact OEM enablement/config remains device-specific. |
| S-018 | AOSP MemoryLimiter — https://android.googlesource.com/platform/frameworks/base/+/android17-release/services/core/java/com/android/server/am/MemoryLimiter.md | MemoryLimiter uses cgroup v2 `memory.high`/`memory.swap.max`, process state and vendor XML configuration. | Android 17 reference behavior; target fork may differ. |
| S-019 | `ApplicationExitInfo` — https://developer.android.com/reference/android/app/ApplicationExitInfo | Direct exit reasons include LOW_MEMORY, FREEZER and version 37.2 MEMORY_LIMITER; low-memory reporting capability varies. | Cross-UID history and reason fidelity are permission/device dependent. |
| S-020 | `ApplicationStartInfo` — https://developer.android.com/reference/android/app/ApplicationStartInfo | API 35+ records startup reason/type/timestamps, enabling relaunch reconstruction. | Cross-package access is privilege-sensitive and older Android lacks it. |
| S-021 | Android app memory budgets — https://developer.android.com/topic/performance/memory/app-memory-budgets | Android 17 QPR2/API 37.2 memory budgets/`MemoryBudgetManager` bound app footprint and expose runtime feedback. | Future/minor-SDK feature; target support unknown. |
| S-022 | AOSP cached-app freezer — https://source.android.com/docs/core/perf/cached-apps-freezer | Cached apps can be frozen while retained in RAM; Android 14+ has robust automatic freezing behavior. | OEM enablement/changes vary. |
| S-023 | AOSP Binder freezer — https://source.android.com/docs/core/architecture/ipc/binder-freezer | IPC into frozen apps has failure/buffering semantics and can explain freezer-related exits. | Exact app interaction needs incident evidence. |
| S-024 | App Standby Buckets — https://developer.android.com/topic/performance/appstandby | Background job/alarm restrictions vary by bucket and Android version. | OEM prediction/policy can differ. |
| S-025 | Power-management resource limits — https://developer.android.com/topic/performance/power/power-details | Android 16 changed background job quota behavior; FGS/battery exemptions do not imply unlimited execution. | Does not describe Huawei-specific additions. |
| S-026 | Perfetto trigger configuration — https://perfetto.dev/docs/concepts/config | Privileged consumer can preconfigure START/STOP/CLONE_SNAPSHOT triggers while unprivileged producers signal incidents. | Deployment/version/permissions must be tested on target. |
| S-027 | Linux Multi-Gen LRU — https://docs.kernel.org/mm/multigen_lru.html | Adaptive aging/eviction uses refault feedback and PID-like control; kernel already owns page-hotness policy. | Target kernel/config support unknown. |
| S-028 | Linux cgroup v2 memory controller — https://docs.kernel.org/admin-guide/cgroup-v2.html | `memory.low/high/max/reclaim` provide strong protection/throttle/reclaim mechanisms. | Strong writes can cause pressure/OOM and may conflict with Android controllers. |
| S-029 | DAMON_RECLAIM — https://docs.kernel.org/admin-guide/mm/damon/reclaim.html | Kernel can proactively reclaim cold pages under configured watermarks. | Kernel config/module/sysfs availability on target unknown. |
| S-030 | AOSP cgroup abstraction — https://source.android.com/docs/core/perf/cgroups | Android task profiles/cgroups can be API/vendor overridden; raw paths are not portable contracts. | Does not prove a target profile or writable ownership. |
| S-031 | Huawei EMUI background protection — https://consumer.huawei.com/en/support/content/en-us15850065/ | EMUI documents Auto-launch/Secondary launch/Run in background, battery optimization and recents lock. | Version/product UI varies. |
| S-032 | Huawei HarmonyOS background protection — https://consumer.huawei.com/en/support/content/en-us15850069/ | HarmonyOS has similar but differently located continuity controls. | Exact target branch/UI remains unknown. |
| S-033 | Huawei unable-to-run-background-apps guidance — https://consumer.huawei.com/qa/support/content/en-gb00428704/ | Huawei explicitly lists App launch, battery optimization, power saver, network/sleep, recents and developer settings as separate causes. | Consumer support guidance is not a programmable API contract. |
| S-034 | Huawei Accelerate Kit / PerfGenius — https://developer.huawei.com/consumer/en/codelab/HMSAccKit-PerfGenius/ | App-integrated system/performance monitoring and frame-rate/key-thread controls exist. | App-scoped SDK; not a generic cross-app system optimizer. |
| S-035 | Android Dynamic Performance Framework — https://developer.android.com/games/optimize/adpf | Thermal/performance APIs expose dynamic SoC/thermal behavior for the calling workload. | Primarily app/game-scoped; device support varies. |
| S-036 | Android Thermal API — https://developer.android.com/games/optimize/adpf/thermal | Thermal headroom/status are useful experiment confounders; sampling/support limitations are documented. | Headroom/status quality varies by device. |
| S-037 | Android Macrobenchmark — https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview | Controlled repeated physical-device startup tests distinguish COLD/WARM/HOT. | Cross-app/system-wide use still needs a harness and target access. |
| S-038 | AppFlow (2026) — https://arxiv.org/abs/2603.17259 | Coordinated preloading/reclaim/killing can reduce cold-launch latency in a framework+kernel implementation. | Preprint/system modification; not stock-Huawei applicability proof. |
| S-039 | Ariadne (HPCA 2025) — https://arxiv.org/abs/2502.12826 | Hotness-aware compressed swap/proactive decompression reduced relaunch latency on Pixel 7 in reported evaluation. | Deep OS/kernel integration; target transfer unverified. |
| S-040 | Relaunch-distance memory management (2023) — https://doi.org/10.32604/csse.2023.038139 | Relaunch distance is a useful continuity objective beyond simple next-app prediction. | Research workload/model; production generalization unproven. |
| S-041 | RankProp (2026) — https://www.mdpi.com/2076-3417/16/15/7511 | Learned resident-app ranking can influence reclaim priority, but gains are modest/context-dependent. | Emulator/simulation components; not target proof. |
| S-042 | Meta oomd — https://github.com/facebookincubator/oomd | PSI+cgroupv2 userspace pressure control demonstrates temporal policy/hysteresis value. | Server/Linux design; duplicating Android controllers would risk conflict. |
| S-043 | Android app startup time — https://developer.android.com/topic/performance/issues/launch-time | Cold/warm/hot, TTID and TTFD are user-facing outcome metrics. | Per-app measurement accessibility varies across targets. |
| S-044 | Android memory usage guidance — https://developer.android.com/topic/performance/memory/guide/concepts | Anonymous RSS + swap is recommended for app footprint over time; PSS/USS have distinct costs/uses. | App-focused guidance, not system-wide cause attribution. |

Arm B source interpretation is question-driven in `EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`; source inclusion alone does not establish a target-device fact.
