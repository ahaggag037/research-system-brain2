# FH-A2 Evidence and Experiment Program

## Evidence semantics
- Platform documentation/source proves **platform possibility/reference behavior**, not target presence.
- Target read-only observation proves **capability/observability on that device/build**.
- A correlated incident proves what was observed around that incident; it does not automatically prove general causality.
- A paired/repeated intervention experiment can support a causal claim only when confounders and rollback are controlled.

## E-001 — M1 Capability & Incident Bootstrap
**Goal:** establish exact target truth without writes.  
**Collect:** device/build/API/full-SDK; `isLowMemoryKillReportSupported`; self/cross-UID start/exit history access by privilege tier; `am memory-limiter status` if supported; app-memory-budget API presence; cached freezer/cgroup v2/PSI/MGLRU/DAMON observability; Perfetto version/trigger feasibility; thermal headroom/status; Huawei policy/version surface; observer overhead.  
**Incident proof:** capture at least one reproducible reload/exit/background-continuity incident and build a direct/indirect evidence timeline.  
**Exit:** versioned DeviceProfile + gaps; zero system writes.

## E-002 — Observer Budget A/B
Compare representative workflow with observer disabled vs each proposed capture tier. Record repetitions, thermal state/headroom, FixHUA anonymous RSS+swap where available, CPU/active duration, workflow latency/jank and capture success.  
**Reject/trim:** any source whose cost distorts the outcome or exceeds a target-derived budget without unique information gain.

## E-003 — Incident Attribution Falsification
Fixture + target incidents across at least: LMK/global pressure, limiter (if available), freezer/frozen IPC (if reproducible), crash/ANR, platform policy and conflicting/unknown evidence.  
**Pass:** direct reasons map only when version/capability supports them; conflicting evidence lowers confidence; unsupported low-memory reporting never turns SIGKILL into automatic LMK fact.

## E-004 — Platform Policy Diagnosis
For exact Huawei build, compare documented App launch/battery/background/recents/network settings and Android standby restrictions against controlled continuity workflow. Change settings only through normal user-visible supported UI/API and record before/after.  
**Goal:** separate policy-limited continuity from resource pressure.

## E-005 — Startup/Continuity Outcome Baseline
Use repeated physical-device switch/relaunch workflows. Classify cold/warm/hot where observable and record relaunch latency/TTID/TTFD when an appropriate harness exists. Keep thermal/control conditions stable enough for comparison.  
**Goal:** create user-outcome baseline before policy optimization.

## E-006 — Continuity Research Shadow Test
Evaluate A2-009 ranking using user priority + relaunch distance/cost + footprint/background role. Use holdout periods and explicit fallback.  
**No action:** prediction cannot directly kill/freeze/protect processes.  
**Promotion condition:** stable predictive/outcome value with OOD/fallback behavior.

## E-007 — Typed Actuator Qualification (future)
For exactly one candidate write after M1–M3, document control owner, expected mechanism, scope, exclusions, baseline, abort, read-back, rollback, failure injection and repeated outcome trial. One actuator at a time.  
**Reject:** any controller fight, non-repeatable benefit, material regression or rollback uncertainty.

## Experiment outcome priority
1. user-visible continuity/relaunch/responsiveness;
2. correctness/stability/thermal/battery safeguards;
3. mechanism evidence;
4. proxy metrics (PSI/free RAM/clocks) only as explanatory context.
