# Rejected / Constrained Ideas — FH-A2

| Idea | Disposition | Evidence/reason |
|---|---|---|
| Static “performance tweak pack” | REJECTED as core | Multiple controllers/causes; target semantics vary. |
| Maximize free RAM | REJECTED objective | Reclaim/cache/swap are normal; continuity can worsen when useful residency is destroyed. |
| Max clocks / disable thermal protections | REJECTED | Thermal framework/ADPF show sustainable performance is dynamic; safety boundary. |
| One PSI/free-RAM threshold decides cause/action | REJECTED | LMKD/AOSP ambiguity + distinct MemoryLimiter/policy/freezer causes. |
| Continuous app-level recorder is universal truth | REJECTED | cached freezer/background quotas interrupt ordinary app execution; observer overhead. |
| Freeze apps to relieve memory | REJECTED mechanism | freezer retains memory; also has Binder failure semantics. |
| Second generic userspace OOM killer on retail Android | REJECTED | duplicates/fights LMKD, MemoryLimiter and vendor controllers. |
| Hard-code cgroup/sysfs/vendor paths | REJECTED | Android task-profile/vendor overrides; target-specific. |
| Direct cgroup/DAMON/MGLRU writes in M1/M2 | REJECTED | strong/risky controls; target ownership/safety unverified. |
| Delete/disable Huawei system-management packages | REJECTED | undocumented/destructive; no supported contract; can destabilize device. |
| Treat Huawei PerfGenius as global optimizer | REJECTED | vendor SDK is integrated app-scoped performance API. |
| User-space page-hotness controller | REJECTED stock design | MGLRU/kernel reclaim owns page-level feedback on capable systems. |
| Predictive continuity ranking directly kills apps | REJECTED initial production | research shows prediction/calibration limitations; background semantics and target causality unresolved. |
| AppFlow/Ariadne copied into stock app | REJECTED feasibility | reported gains require framework/kernel implementation. |
| Persistent root daemon on day one | REJECTED | unnecessary for incident-first M2 and increases safety/recovery cost. |
