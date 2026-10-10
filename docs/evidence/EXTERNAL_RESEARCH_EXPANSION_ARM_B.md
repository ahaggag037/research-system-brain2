# Mandatory External Research Expansion — Arm B

Status: **RESEARCH COMPLETE / ARCHITECTURE RE-EVALUATION PENDING**  
Cycle: V10.3-B Arm B, 2026-10-10  
Historical baseline: FH-A1 at commit `0b114e4f224ebac957cf8245acd1002fa43081fa`.  
Isolation: only this canonical repository plus independent public Internet sources were used. No prior FixHUA repository/research, `research-system-brain`, `_human/`, Kimi, or parallel-model output was inspected.

## Research method
This cycle treats external evidence as an adversary to the current architecture. Each path follows **QUESTION → SOURCE → WHAT WAS LEARNED → CONFIDENCE → ARCHITECTURE/DECISION IMPACT**. Source count is not a completion criterion. Research stops when the remaining high-impact unknowns require target-device observation rather than more public reading.

## Q1 — What current Android mechanisms can throttle or terminate an app besides classic LMKD/global pressure?
**Sources:** S-017, S-018, S-019, S-021.  
**What was learned:** Android 17 adds a vendor-configured `MemoryLimiter` built on cgroup v2 `memory.high` and `memory.swap.max`, with state-dependent visible/non-visible limits. Current `ApplicationExitInfo` includes `REASON_MEMORY_LIMITER`. Android 17 QPR2 separately adds per-app memory budgets and `MemoryBudgetManager`; budgets can reclaim/evict/swap app memory without requiring a global low-memory event.  
**Confidence:** HIGH for platform behavior; UNKNOWN for exact target availability/configuration.  
**Impact:** FH-A1's coarse `MEMORY_PRESSURE` state is insufficient. A direct incident cause `MEMORY_LIMITER` must be modeled separately from LMKD/global pressure. Capability discovery must include limiter/budget support and version-aware reason parsing. FixHUA should consider a self-budget only after measured safe sizing, never a hardcoded universal budget.

## Q2 — Can relaunch/reload causality be reconstructed more directly than by inferring a global operating state?
**Sources:** S-019, S-020, S-043.  
**What was learned:** `ApplicationExitInfo` exposes system-recorded process-death reasons and importance; `ApplicationStartInfo` (API 35+) exposes why/how a process starts, including start type and timing. Android distinguishes cold/warm/hot startup outcomes. However, cross-UID history is privilege-sensitive; an ordinary app must not assume system-wide access. Low-memory reason reporting itself is capability-dependent.  
**Confidence:** HIGH for APIs/limitations; target access UNKNOWN.  
**Impact:** This materially changes the architecture. Start from the **incident** and the strongest direct platform record available, correlate exit → next start → user-visible restart cost, then fall back to multi-signal inference only when direct evidence is unavailable. Replace generic state-estimation-first with incident attribution.

## Q3 — Is a continuously running app-level Flight Recorder a reliable low-overhead architectural core?
**Sources:** S-022, S-023, S-024, S-025.  
**What was learned:** Android freezes cached apps, and in Android 14+ normally freezes cached processes shortly after they enter cached state. Binder interactions with frozen processes have special failure/buffering semantics. Android App Standby/background restrictions and Android 16 job quotas can limit background execution even when foreground-service/battery settings would previously have implied more runtime.  
**Confidence:** HIGH for platform behavior; vendor-specific exact enforcement UNKNOWN.  
**Impact:** FH-A1 assumption weakened. Persistent in-app polling cannot be the primary truth source. Replace CMP-003's always-on baseline role with **tiered, incident-driven evidence escalation**. A persistent foreground service is not a default architecture requirement.

## Q4 — What is the strongest practical deep-capture model without turning observability into the problem?
**Sources:** S-026.  
**What was learned:** Perfetto supports trigger-driven START/STOP/CLONE_SNAPSHOT workflows; on Android the privileged tracing consumer can predeclare allowed triggers while unprivileged code can signal them. Triggered ring-buffer capture is designed for causes occurring just before an incident.  
**Confidence:** HIGH for Perfetto; exact target permissions/version support UNKNOWN.  
**Impact:** Use capture tiers: Tier 0 platform history; Tier 1 cheap snapshot; Tier 2 bounded preconfigured/triggered Perfetto; Tier 3 explicit shell/root-read diagnostics. Deep tracing is escalation, not continuous default telemetry.

## Q5 — Does FixHUA need its own page-hotness/reclaim controller to preserve app continuity?
**Sources:** S-027, S-039.  
**What was learned:** Linux Multi-Gen LRU already performs adaptive aging/eviction using refault feedback and a PID-like control loop. Ariadne demonstrates that hotness-aware compressed swap/proactive decompression can materially reduce relaunch latency, but it requires deep kernel/system integration.  
**Confidence:** HIGH that the mechanisms exist; MEDIUM for research generalization; target MGLRU support UNKNOWN.  
**Impact:** Narrow the Continuity module. Do not duplicate kernel page-hotness policy from user space. Its defensible role is user-value/relaunch-cost/relaunch-distance research and experiment selection, not page-level reclaim imitation.

## Q6 — Are cgroup protection/reclaim or DAMON proactive reclaim high-impact opportunities missed by FH-A1?
**Sources:** S-028, S-029, S-030.  
**What was learned:** cgroup v2 exposes strong memory controls (`memory.low`, `memory.high`, `memory.max`, `memory.reclaim`), and DAMON_RECLAIM can proactively reclaim cold memory. Android's cgroup/task-profile layer permits API/vendor overrides, so raw paths and ownership are not stable contracts. These mechanisms can also create reclaim pressure/OOM behavior if misapplied.  
**Confidence:** HIGH for Linux/AOSP mechanisms; LOW/UNKNOWN for safe stock-Huawei applicability.  
**Impact:** Add them to a **research actuator catalog**, not the initial product. Privileged production admission remains device-qualified and typed. No raw cgroup/DAMON writes in M1/M2.

## Q7 — Is Huawei background policy a single special case, and can public documentation settle it?
**Sources:** S-031, S-032, S-033, S-034.  
**What was learned:** Huawei documents separate App launch/Auto-launch/Secondary launch/Run in background, battery optimization, recent-task lock, power-saving, and network controls, with UI differences across EMUI/HarmonyOS. PerfGenius is an app-integrated vendor SDK for system/performance signals and app-specific performance hints; it is not a generic system-wide optimizer API.  
**Confidence:** HIGH for documented surfaces; target-version behavior UNKNOWN.  
**Impact:** Replace a Huawei-only assistant component with a **versioned Platform Policy Adapter**: Android baseline policy + Huawei EMUI/HarmonyOS adapter. Keep guidance version-qualified; do not mutate undocumented vendor databases. PerfGenius may be capability-gated for FixHUA's own app behavior, not a global control shortcut.

## Q8 — Can Android/SoC thermal/performance APIs justify stronger system tuning?
**Sources:** S-035, S-036.  
**What was learned:** ADPF exposes app-scoped thermal/performance feedback and acknowledges diverse CPU core topologies/thermal dynamics. Thermal headroom/status support varies by device, and aggressive polling can itself fail (`NaN`); the API is intended to adapt the calling workload rather than globally tune other apps.  
**Confidence:** HIGH for API scope; target support UNKNOWN.  
**Impact:** Treat thermal state/headroom as an experimental confounder and observer self-management signal, not a global actuator. Avoid “max clocks” or SoC-specific magic settings.

## Q9 — Does systems research support a more ambitious continuity optimization direction?
**Sources:** S-038, S-039, S-040, S-041.  
**What was learned:** AppFlow coordinates preloading/reclaim/killing at framework+kernel level; Ariadne changes compressed swap; relaunch-distance work and RankProp show user/app reuse prediction can improve eviction decisions, but direct policies can regress unless calibrated/fallback-aware. These are system-integration research results, not stock-device proof.  
**Confidence:** MEDIUM/HIGH that reported systems/results exist; LOW for direct transfer to the Huawei target.  
**Impact:** Preserve an experimental Continuity Research Module, but make it shadow-only on stock devices. Inputs may include explicit user priority, observed relaunch distance, cold-start cost and footprint. Kernel/framework modifications belong to a future custom-system-image research backend, not the first product.

## Q10 — How should FixHUA test whether an intervention improves user experience rather than a proxy metric?
**Sources:** S-037, S-036, S-043.  
**What was learned:** Android benchmark guidance distinguishes cold/warm/hot startup and recommends repeated controlled physical-device measurements; thermal state materially changes performance. TTID/TTFD and relaunch type are user-relevant outcomes.  
**Confidence:** HIGH.  
**Impact:** Promotion of any policy/actuator requires paired/repeated trials with stable environmental conditions, thermal annotation, and outcome metrics such as avoidable cold-start conversion, TTID/TTFD where observable, relaunch latency distribution and continuity success—not merely free RAM or clocks.

## Q11 — How should observer self-interference be controlled on newer Android?
**Sources:** S-021, S-036, S-044.  
**What was learned:** Android 17 QPR2 lets an app declare/query a memory budget and receive over-budget feedback; current Android memory guidance recommends anonymous RSS + swap for true app-controlled footprint and warns that heavier memory metrics can be expensive. Thermal APIs also impose sensible sampling constraints.  
**Confidence:** HIGH for APIs/metrics; target API support UNKNOWN.  
**Impact:** Add an explicit **Observer Budget** contract. Prefer event/session-driven capture; measure FixHUA's anonymous RSS+swap/CPU/wakeups; on supported Android 17 QPR2 consider a tested self-budget as a safety rail, not a universal constant.

## Q12 — Does userspace OOM research suggest FixHUA should become another killer/controller?
**Sources:** S-042, S-003, S-027.  
**What was learned:** userspace OOM controllers such as oomd use PSI+cgroup v2 and duration/policy windows effectively in server environments. Android already has LMKD, newer MemoryLimiter, freezer, MGLRU/reclaim and vendor controls. A second independent killer on a retail phone risks controller conflict.  
**Confidence:** HIGH that temporal/hysteretic pressure control is valuable; HIGH that direct server-policy transfer is architecturally risky.  
**Impact:** Retain temporal windows/hysteresis as design lessons, reject “run another OOM killer” as a product core.

## Externally verified important claims before reconvergence
1. Android 17 introduces a distinct MemoryLimiter that can throttle/reclaim/kill app processes with cgroup v2 controls; this is not equivalent to LMKD. [S-017, S-018, S-019]
2. Android 17 QPR2 adds app memory budgets/`MemoryBudgetManager`. [S-021]
3. Android exposes historical process exit records and, on API 35+, start records; both are version/permission bounded. [S-019, S-020]
4. Cached-app freezer/Binder freezer behavior can itself explain failure classes. [S-022, S-023]
5. Android background-policy quotas can stop/delay work independently of process-memory pressure. [S-024, S-025]
6. Perfetto supports bounded trigger-based capture with an Android privilege model suitable for evidence escalation. [S-026]
7. MGLRU already implements adaptive page-reclaim feedback; cgroup/DAMON controls exist but do not prove target-safe actuation. [S-027..S-030]
8. Huawei background continuity depends on multiple documented policy surfaces and version families. [S-031..S-033]
9. Thermal/SoC dynamics are legitimate confounders, but ADPF/PerfGenius are app-scoped integrations, not universal system optimizer APIs. [S-034..S-036]
10. Relaunch latency/continuity is a legitimate systems objective, but strongest published approaches usually require OS/kernel integration. [S-038..S-041]

## Research-caused architecture changes
- Promote **incident reconstruction/attribution** above generic global-state classification.
- Replace default continuous Flight Recorder with **tiered evidence escalation** and triggered deep capture.
- Add Android 17 **MemoryLimiter / app-memory-budget** awareness.
- Add explicit **exit→start→cold/warm/hot** correlation and outcome metrics.
- Generalize Huawei Assistant into **Platform Policy Adapter** (Android baseline + vendor/version adapters).
- Merge Evidence Store + Report/Export into one provenance/reporting boundary; separate component was not earning enough complexity.
- Add Observer Budget/self-interference contract.
- Constrain Continuity module to relaunch/user-value research; no user-space page-hotness duplication.
- Strengthen experiment promotion around paired/repeated physical-device trials and thermal controls.

## Rejected or weakened FH-A1 assumptions
- **Rejected:** an ordinary app can rely on a continuously running low-cost recorder as the primary system-wide truth source.
- **Rejected:** `MEMORY_PRESSURE` is a sufficiently specific root-cause class for modern Android.
- **Rejected:** Huawei policy can be modeled as a one-off settings assistant rather than one adapter in a broader platform-policy system.
- **Weakened:** generic multi-signal state estimation should be the first diagnostic step; direct platform incident evidence should dominate when available and trustworthy.
- **Weakened:** Continuity Allocator should reason about low-level hotness; kernel reclaim already owns that domain on capable systems.
- **Retained:** evidence gating, UNKNOWN/NO_OP, typed privilege, rollback, local-first evidence, and target qualification.

## Newly discovered mechanisms/opportunities
- Android 17 MemoryLimiter (`memory.high`, `memory.swap.max`, state-based limits).
- Android 17 QPR2 app memory budgets and `MemoryBudgetManager`.
- `ApplicationStartInfo` historical start type/reason/timestamps.
- `REASON_MEMORY_LIMITER` and explicit freezer exit attribution.
- Binder/freezer incident semantics.
- Triggered Perfetto escalation / clone snapshots.
- Observer self-budgeting and anonymous RSS+swap budget accounting.
- DAMON_RECLAIM and cgroup memory protection/reclaim as research-only actuators.
- Relaunch-distance/ranking and coordinated preloading/reclaim research as future custom-system-image paths.

## Claims still based only on model prior knowledge
No model-prior-only claim is promoted to VERIFIED_FACT or used to admit a write actuator. The following remain hypotheses pending target or implementation evidence:
- that exit/start correlation will be sufficiently complete for cross-app diagnosis on the target;
- that a shell/root broker can expose cross-UID history with acceptable UX/security;
- that triggered Perfetto can be deployed reliably on the target firmware;
- that user-priority/relaunch-distance ranking will improve the user's actual workload;
- that a self memory budget is beneficial for FixHUA rather than merely available.

## Device-specific questions Internet research cannot settle
- Exact Huawei model, Android API/EMUI/HarmonyOS branch, kernel and vendor build.
- Whether MemoryLimiter exists, is enabled, and its vendor configuration.
- Whether MemoryBudgetManager/API 37.2 exists.
- Whether low-memory exit reporting is supported and whether shell/DUMP/root access exposes cross-UID start/exit histories.
- Cached-app-freezer state and vendor changes.
- cgroup v2/task profiles, PSI, MGLRU, DAMON and Perfetto trigger availability/permissions.
- Huawei policy UI/behavior on the exact build.
- Thermal-headroom quality and telemetry overhead.
- Any privileged actuator's causal benefit, controller ownership, safe bounds and rollback.

## Reconvergence recommendation
External evidence does **not** falsify evidence-gating or typed privilege. It **does** falsify FH-A1 as the strongest current architecture because FH-A1 over-centers generic continuous observation/state estimation and under-models direct incident evidence and newer Android control planes.

Leading candidate: **FH-A2 — Incident-Centric Evidence Escalation Supervisor**.

Research stopping rule: further public search is unlikely to change the architectural choice materially; remaining consequential uncertainty is target-specific and moves to M1 device evidence.
