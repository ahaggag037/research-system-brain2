# Problem, Outcomes, Success Model

## Problem definition
Huawei-class Android phones can exhibit app reloads/exits, slow resume, jank, stalls and unstable sustained performance for **different underlying reasons that look similar to a user**. Plausible mechanisms include global memory pressure/reclaim/LMKD, OEM background/battery policy, thermal throttling, CPU or I/O contention, app crash/ANR, storage pressure, or an update/user action. Applying a generic "optimization" to the wrong mechanism can do nothing or make the phone worse.

## User-visible goals
FixHUA optimizes the following outcome vector rather than one scalar:
- foreground interaction latency and jank;
- useful app continuity and warm resume quality;
- fewer avoidable process reloads/exits;
- stable sustained behavior under realistic thermal/battery constraints;
- predictable explanations and reversible changes;
- low observer/controller overhead.

## Success model
A policy earns adoption only if it improves a relevant user-visible metric under representative workloads **without unacceptable regression** in stability, battery/thermal behavior, privacy, background correctness or another protected workload. A no-op that correctly avoids an unjustified tweak is success.

## Non-goals
- maximizing free RAM;
- pinning every app in memory;
- forcing maximum clocks;
- disabling thermal or battery safety;
- chasing synthetic benchmarks as the primary objective;
- providing an unrestricted root shell to the UI;
- bypassing app integrity, DRM, accounts, banking protections or platform security;
- fabricating universal kernel/sysfs/cgroup settings.

## Measurement families
1. **Responsiveness:** frame/jank statistics, interaction-to-visible-response timing where measurable.
2. **Continuity:** warm-vs-cold resume, process survival reason when observable, reload frequency for explicitly tested apps.
3. **Pressure/health:** CPU/memory/I/O PSI when available, reclaim/swap/zRAM indicators, thermal state, load and I/O latency clues.
4. **Correctness:** app crash/ANR, notification/background behavior, intervention rollback correctness.
5. **Overhead:** FixHUA CPU, wakeups, memory, storage writes, battery/thermal effect.

No universal numeric acceptance threshold is claimed yet. Baselines and budgets are target-device evidence to be established in E-001/E-002 before controller admission.
