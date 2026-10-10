# Implementation Blueprint

## Stages

### M0 — Reference diagnostic utility (current)
**Purpose:** validate repository-level evidence schemas and give a no-write first-use path.  
**Files:** `tools/device_probe.sh`, `tools/analyze_snapshot.py`, `tests/test_analyze_snapshot.py`, `schemas/*`.  
**Privilege:** shell read only; no root required by design, though some fields may be denied.  
**Exit:** local tests pass; probe has no write/tuning commands; analyzer handles missing signals conservatively.

### M1 — Target device evidence bootstrap (next)
**Dependencies:** actual Huawei device + ADB or equivalent explicit shell access.  
**Work:** run probe, inventory accessible capabilities, capture representative problem episode, measure probe cost, record device-private results outside public repo.  
**Output:** evidence-backed sensor set, exact OS/build constraints, denied/unknown surfaces.  
**Exit:** E-001 result + E-002 preliminary overhead; Android observer requirements updated.

### M2 — First diagnostic Android APK
**Purpose:** installable local UX without privileged writes.  
**Planned modules:** `app`, `core-model`, `capability`, `observer`, `evidence-store`, `report`, `huawei-assistant`.  
**Interfaces:** IF-001/002/003/006/007/008.  
**State:** DeviceProfile, samples/windows, estimates, user policy, audits.  
**Concurrency:** UI thread only renders; probes/storage on structured worker/coroutine scopes; one recorder writer per stream.  
**Privilege:** APP by default; optional explicit shell/root **read** adapter only after M1 determines necessity.  
**Errors:** missing signal → annotated UNKNOWN, not app failure.  
**Build:** Android toolchain versions selected/locked during M1/M2 bootstrap; see runbook.  
**Tests:** unit parsers/classifier, schema migration, UI degraded states, build/install smoke, E-002 overhead.  
**Exit:** APK installs, first-run profile works, incident report works, no system write, device smoke passes.

### M3 — Daily-use observer + Huawei assistant
Add low-overhead lifecycle, retention, symptom capture, documented settings guidance and privacy-redacted export. Establish device-specific overhead budget and stability regression suite.  
**Exit:** representative daily workload shows acceptable observer overhead and crash-free operation; background semantics preserved.

### M4 — Shadow policy engine
Implement CMP-005 with offline/replay decisions only. Candidate actions are explanation/guidance/capture requests first; write candidates cannot execute.  
**Algorithm:** `estimate -> guard exclusions -> enumerate typed candidates -> check qualification -> score expected value/risk -> apply hysteresis/cooldown -> emit NO_OP or shadow candidate + explanation`.
**Exit:** replay tests show stable/no-chatter behavior and explicit UNKNOWN/no-op.

### M5 — Privilege gateway + first actuator research
Implement CMP-006 boundary and transaction journal **without admitting a write actuator initially**. Add one candidate only after E-005 proves exact device/firmware semantics, rollback and measurable benefit.  
**Concurrency:** single serialized actuator transaction; cancellation cannot skip rollback.  
**Exit:** failure injection passes; gateway cannot execute arbitrary command strings; target canary qualifies or rejects actuator.

### M6 — Experimental continuity allocator
Shadow-only first. Compare continuity ranking against observed reload/resume cost and user intent. No destructive automation until a separate safety/benefit admission review.

## Parallelizable work
After M1 sensor set is known, Android UI/state store, parser fixtures, Huawei guidance catalog, report/redaction and CI can proceed in parallel. Privilege write work cannot proceed in parallel past qualification gates because it depends on target evidence and rollback tests.

## Device-specific unknowns that must not be fabricated
Exact kernel/cgroup hierarchy, LMKD properties, SELinux access, shell/root broker, Perfetto data sources, Huawei setting intent paths, thermal sensor visibility and any writable control. M1 discovers them; absent evidence remains UNKNOWN.
