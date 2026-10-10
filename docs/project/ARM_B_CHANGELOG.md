# Arm B Change Log — from completed V10.3-B to research-expanded architecture

Baseline final commit: `0b114e4f224ebac957cf8245acd1002fa43081fa`  
Baseline architecture: FH-A1 Evidence-Gated Adaptive Supervisor.  
Reason for reopen: independent external Internet research was underspecified as optional/encouraged; Arm B makes it mandatory and architecture-changing.

## What changed and why
| Area | V10.3-B / FH-A1 | Arm B / FH-A2 | Why external research changed it |
|---|---|---|---|
| Diagnostic center | global state estimation from periodic evidence | incident-first direct platform evidence + correlation | Android exposes exit/start/limiter/freezer reasons; direct evidence can be more specific |
| Observability | low-cost Flight Recorder as core baseline | tiered evidence escalation; no continuous recorder correctness dependency | cached freezer/background quotas make app-level continuous runtime unreliable |
| Memory causes | broad memory pressure/LMKD framing | separate MemoryLimiter vs LMK/global pressure vs app-self footprint | Android 17 MemoryLimiter is a distinct cgroup-based control plane |
| Relaunch outcome | generic continuity/resume quality | explicit exit→next start, cold/warm/hot, TTID/TTFD where measurable | ApplicationStartInfo + current startup metrics provide stronger outcome structure |
| Vendor policy | Huawei assistant | Platform Policy Adapter (Android baseline + Huawei version adapters) | background limits exist in Android and Huawei layers; vendor UI varies |
| Evidence capture | periodic + incident ring buffer | T0 history → T1 snapshot → T2 triggered Perfetto → T3 explicit privileged read | Perfetto supports trigger model; deep capture should be bounded |
| Reporting | separate CMP-009 | merged with evidence/provenance store | same privacy/schema/recovery owner; separate component added little value |
| Continuity research | generic allocator potentially hotness-aware | shadow relaunch/user-value research only | MGLRU already adapts page reclaim; strongest academic mechanisms require OS/kernel integration |
| Experiment method | canary/evidence gate | paired/repeated outcome trials with thermal/control-condition annotation | Android benchmark/thermal guidance exposes confounding and startup modes |
| Observer safety | overhead budget present but secondary | explicit cross-cutting Observer Budget | current memory/thermal guidance and background limits make self-interference first-class |
| M1 | generic target capability/pressure bootstrap | direct incident/capability matrix including MemoryLimiter/start-exit/freezer/Perfetto/MGLRU/vendor policy | new current mechanisms materially affect architecture |

## What did not change
- no arbitrary root command surface;
- no thermal/hardware/integrity/security bypass;
- no undocumented Huawei state mutation;
- no write without same-device/firmware qualification + rollback;
- local-first sensitive telemetry;
- `UNKNOWN`/`NO_OP` are legitimate results;
- real-device evidence, not Internet claims, decides target-specific truth.
