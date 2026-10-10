# Rejected / Deferred Idea Memory

| Idea | Why it looked promising | What invalidated it | Rejection | Reopen condition |
|---|---|---|---|---|
| Universal static tweak pack | fast, simple, easy to demonstrate | device/version variance, multiple causal mechanisms, controller conflict, no feedback | core architecture REJECTED | only a specific tweak with target evidence becomes a typed actuator |
| Maximize free RAM | intuitive headroom metric | Android intentionally uses RAM for cached apps; free RAM does not express stalls/value | PERMANENT as objective | never as global objective; free memory may remain one observation |
| Force maximum clocks | immediate benchmark boost | thermal/power framework and sustained stability matter; safety bypass forbidden | REJECTED | bounded documented performance hints could be studied per app/device |
| Single PSI threshold controller | PSI is strong pressure signal | 2026 AOSP LMKD fix demonstrates full PSI can be misleading in some memcg cases | REJECTED | only if target experiment proves a narrowly scoped signal with guards |
| Freeze apps to solve memory pressure | keeps cached apps quiet | freezer reduces CPU activity but retains resident memory | REJECTED for memory relief | may be studied for CPU/wakeup behavior with safeguards |
| Pin/protect every user app | reduces cold starts | increases pressure and can harm foreground workload | REJECTED | user-value allocator may protect a bounded subset after experiments |
| Persistent root daemon from day one | easiest continuous control | unverified need, battery/reliability/security and recovery burden | DEFERRED | E-001/E-002 prove persistent access required and safe |
| Undocumented Huawei database edits | direct automation | unstable/version-specific, unsupported, hard to recover | REJECTED | documented supported API emerges |
| Continuous deep tracing | maximum observability | self-interference/storage/privacy | REJECTED | bounded triggered capture already preserves value |
