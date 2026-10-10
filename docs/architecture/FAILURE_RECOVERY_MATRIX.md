# FH-A2 Failure and Recovery Matrix

| Failure | Detection | Automatic response | Degraded/recovery mode | Verification |
|---|---|---|---|---|
| Direct history unavailable/permission denied | API/permission result | mark UNOBSERVABLE; request next evidence tier only if useful | no fabricated cause | profile + attribution gap |
| Exit reason unsupported/ambiguous | low-memory support flag/version/conflict | do not map SIGKILL blindly to LMK | use context/trace; UNKNOWN allowed | fixture + target incident |
| MemoryLimiter absent/disabled | status/capability probe | remove limiter cause/action assumptions | continue other causes | profile evidence |
| App frozen/background-restricted | lifecycle/policy evidence or interrupted capture | do not treat recorder gap as “healthy system” | after-the-fact history/T1 snapshot | incident timeline |
| Perfetto trigger unsupported/misconfigured | capability/test capture fails | fall back to T1/T3 if justified | preserve gap | bounded smoke test |
| Observer budget breach | measured memory/CPU/thermal/capture health | shed optional probes; stop deep capture | minimal Tier 0/1 only | overhead record |
| Vendor policy version unknown | adapter lookup mismatch | generic Android guidance + UNKNOWN vendor specifics | user-confirmed/manual docs path | target version check |
| Local state corruption | schema/transaction failure | quarantine affected records | conservative fresh state; never restore qualification by inference | reopen + validator |
| Firmware/update drift | fingerprint/full-SDK/vendor change | stale profile/adapters; invalidate qualifications | read-only re-profile | M1 subset |
| Contradictory direct vs heuristic evidence | attribution conflict | prefer qualified direct source but lower confidence if semantics uncertain | record contradiction | replay fixture/target |
| Failed intervention | read-back/canary regression | abort | typed rollback + suspend qualification | post-rollback window |
| Partial intervention/helper crash | transaction journal/timeout | stop writes | rollback; unresolved → all writes disabled | baseline restored |
| Thermal regression | thermal/canary guard | abort experiment/action | cool-down + rollback if applicable | stable thermal window |
| Controller fight | repeated reversal/oscillation | suspend actuator | no-op; restore owned baseline | no recurrence |
| Sensitive export risk | redaction scanner/preview | block/redact | source remains private | export test |
| Continuity model OOD/poor calibration | holdout/online shadow evidence | no ranking/action promotion | fallback explicit user priority/recency | experiment record |
