# Independent Public Source Index

Accessed during the V10.3-B clean-room discovery run on 2026-10-10. No predecessor/user FixHUA source was used.

| ID | Primary source | Key support | Limitation |
|---|---|---|---|
| S-001 | AOSP LMKD source — https://android.googlesource.com/platform/system/memory/lmkd/+/refs/heads/master/ | Android userspace LMKD monitors memory state and uses PSI/thrashing/swap signals to reclaim by killing less-essential processes. | OEM behavior/properties vary. |
| S-002 | AOSP LMKD 2026 change — https://android.googlesource.com/platform/system/memory/lmkd/+/da500621995ff2578e4d5e2a0d1648709ab8e42c%5E%21/ | Full memory PSI alone can be misleading in some memcg-limit cases; AOSP added a guard. | Exact patch may not exist on target. |
| S-003 | Linux PSI — https://docs.kernel.org/accounting/psi.html | CPU/memory/I/O stall information and threshold monitoring support state-aware load control. | Target kernel/access must be probed. |
| S-004 | AOSP cached-app freezer — https://source.android.com/docs/core/perf/cached-apps-freezer | Platform may freeze cached apps to reduce CPU while keeping them resident. | Freezing does not imply memory is freed; OEM enablement varies. |
| S-005 | Android Activity lifecycle — https://developer.android.com/reference/android/app/Activity | Process importance affects retention/killing under memory pressure. | OEM policies add behavior. |
| S-006 | Android ApplicationExitInfo / ActivityManager — https://developer.android.com/reference/android/app/ApplicationExitInfo | Process exit reasons can distinguish low-memory, ANR, crash, freezer, etc.; cross-UID history is privilege-sensitive. | Low-memory reason/support varies. |
| S-007 | Android memory management — https://developer.android.com/topic/performance/memory-management | Reclaim/zRAM are normal Android memory-management mechanisms; free RAM alone is not the objective. | Device zRAM/reclaim configuration varies. |
| S-008 | AOSP cgroup abstraction — https://source.android.com/docs/core/perf/cgroups | Android task profiles abstract cgroups and allow vendor/version overrides. | Direct hard-coded paths are unreliable. |
| S-009 | AOSP task profiles — https://android.googlesource.com/platform/system/core/+/master/libprocessgroup/profiles/task_profiles.json | Reference concepts include cpusets, memory controls, uclamp and freezer. | Reference is not target capability proof. |
| S-010 | AOSP thermal mitigation — https://source.android.com/docs/core/power/thermal-mitigation | Thermal framework throttles workload and should not be disabled. | Sensor/HAL details vary. |
| S-011 | Perfetto Android tracing — https://perfetto.dev/docs/learning-more/android | Bounded traces can expose scheduling, frequency, graphics, binder, memory, etc. | Continuous tracing can add overhead/privacy cost. |
| S-012 | Android dumpsys — https://developer.android.com/tools/dumpsys | Shell diagnostics expose meminfo/procstats/gfxinfo and other services. | Output/permissions vary. |
| S-013 | Huawei background apps — https://consumer.huawei.com/en/support/content/en-us00428704/ | Huawei documents App launch/background permission/battery optimization/power saver/running memory as distinct causes. | UI paths vary by product/version. |
| S-014 | Huawei background protection — https://consumer.huawei.com/en/support/content/en-us15850065/ and https://consumer.huawei.com/en/support/content/en-us15850069/ | Documented user controls can change app continuity. | Not a stable programmatic API contract. |
| S-015 | Huawei Accelerate Kit PerfGenius — https://developer.huawei.com/consumer/en/codelab/HMSAccKit-PerfGenius/ | Vendor performance interfaces are scenario/state-aware rather than universal max-performance toggles. | Scope/eligibility differs from global system tuning. |
| S-016 | Linux Multi-Gen LRU — https://docs.kernel.org/mm/multigen_lru.html | Reclaim uses recency/refault-informed adaptive mechanisms. | Availability/config on target unknown. |

The canonical conclusion drawn from these sources is intentionally narrow: **multiple interacting controllers and failure mechanisms exist, so target capability and causality must be measured before control.**
