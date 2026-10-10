# Problem and Success — FH-A2

## Product problem
A Huawei/Android user can experience reloads, exits, slow resumes, jank or background discontinuity for mechanically different reasons: LMKD/global pressure, Android 17 MemoryLimiter, cached freezer/Binder behavior, background-policy quotas, Huawei launch/battery policy, crash/ANR, CPU/I/O contention, thermal throttling, or the app's own memory footprint. Treating all symptoms as “not enough RAM” or “Huawei killed it” produces unsafe and often useless tweaks.

FixHUA must turn a symptom into a provenance-bearing incident explanation and only escalate measurement/control when the evidence warrants it.

## Success hierarchy
### Diagnostic success
- incident attributed to a supported direct cause or honestly `UNKNOWN_OR_MIXED`;
- evidence source/version/access and contradictions visible;
- no hidden assumption that continuous telemetry was available.

### User-outcome success
On repeated target workflows, reduce one or more of:
- avoidable cold relaunches/reloads;
- relaunch latency / TTID / TTFD where measurable;
- recurrence of policy-limited background failures;
- jank/thermal instability associated with tested intervention;
while not worsening crashes, battery/thermal behavior, important background semantics or data integrity.

### Safety/reliability success
- observer cost within measured target budget;
- no unqualified privileged writes;
- rollback verified before promotion;
- firmware changes invalidate device-specific qualifications;
- private evidence does not leak into public repo/package.

## Non-goals
- maximizing “free RAM”;
- forcing max clocks or disabling thermal throttling;
- replacing Android LMKD/MemoryLimiter/MGLRU with another generic killer;
- bypassing Android/Huawei security/integrity/banking/DRM controls;
- guaranteeing that all apps stay resident;
- claiming a platform feature exists on the target because AOSP documents it.
