# Architecture Decision Records

## Historical FH-A1 decisions

### ADR-001 — Select evidence-gated supervisor
**Status:** SUPERSEDED_BY_ADR-009  
FH-A1 was selected in V10.3-B. Arm B external research retained its evidence-gating invariant but superseded its observation/state-estimator-centered topology. Historical rationale remains in Git history and `ARCHITECTURE_REEVALUATION_ARM_B.md`.

### ADR-002 — First useful build is observation-first
**Status:** REVISED_BY_ADR-010  
Read-only capability discovery remains correct; “observation-first” is now refined to **incident/direct-history first, minimum evidence escalation second**.

### ADR-003 — Multi-signal state estimation; UNKNOWN is allowed
**Status:** REVISED_BY_ADR-011  
UNKNOWN remains active, but direct version-qualified platform incident records outrank generic multi-signal inference.

### ADR-004 — Typed privilege gateway; no arbitrary root endpoint
**Status:** ACTIVE / RETAINED  
No evidence justified weakening this boundary.

### ADR-005 — No persistent boot-time modifications in first installable build
**Status:** ACTIVE / STRENGTHENED_BY_ADR-010  
Android freezer/background restrictions and observer self-interference further reduce the case for an always-on privileged daemon in M2.

### ADR-006 — Huawei documented settings before undocumented mutation
**Status:** SUPERSEDED_BY_ADR-012  
The safety principle survives; the component is generalized to Android + vendor/version policy adapters.

### ADR-007 — Continuity allocator is experimental, non-destructive initially
**Status:** REVISED_BY_ADR-014  
The module remains experimental but is narrowed away from page-hotness/reclaim duplication toward user value and relaunch outcomes.

### ADR-008 — Local-first evidence and redacted export
**Status:** ACTIVE / RETAINED  
Arm B produced no reason to externalize raw cross-app telemetry.

## Active FH-A2 decisions

### ADR-009 — Select FH-A2 Incident-Centric Evidence Escalation Supervisor
**Status:** ACTIVE  
**Question:** Does FH-A1 remain the strongest design after mandatory current external research?  
**Evidence:** S-017..S-044 and `EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`.  
**Decision:** Select FH-A2. Start from incidents/direct platform records, then escalate evidence only as needed. Preserve evidence gating, typed privilege and target qualification.  
**Why:** Android now exposes distinct MemoryLimiter/freezer/background-policy/start/exit mechanisms; continuous app-level observation is lifecycle-constrained.  
**Rejected:** preserving FH-A1 for sunk-cost reasons; diagnostics-only as end state; second OOM killer; custom kernel architecture as stock-device product.  
**Reopen if:** M1 shows direct incident evidence is unusable and continuous privileged telemetry is both necessary and low-risk, or another simpler architecture demonstrates equal diagnostic/control value.

### ADR-010 — Tiered incident capture replaces continuous Flight Recorder as default
**Status:** ACTIVE  
**Evidence:** S-022..S-026, S-044.  
**Decision:** Tier 0 platform history → Tier 1 cheap snapshot → Tier 2 triggered Perfetto → Tier 3 explicit privileged reads. Persistent foreground/privileged monitoring is not default.  
**Consequence:** A2-004 owns escalation and observer budget. Deep tracing must be bounded and justified.

### ADR-011 — Direct version-qualified incident evidence outranks generic state inference
**Status:** ACTIVE  
**Evidence:** S-017..S-021, S-043.  
**Decision:** A2-003 first uses reliable direct exit/start/limiter/freezer/policy evidence. Multi-signal PSI/memory/thermal inference is fallback/context.  
**Important caveat:** `ApplicationExitInfo` reason support and cross-UID history vary; absence never proves the event did not occur. Description strings are not stable machine contracts.  
**Consequence:** cause records carry source, version, access method and confidence.

### ADR-012 — Generalize Huawei Assistant to versioned Platform Policy Adapter
**Status:** ACTIVE  
**Evidence:** S-024, S-025, S-031..S-034.  
**Decision:** A2-007 models Android baseline Doze/standby/background limits and vendor/version adapters, starting with Huawei EMUI/HarmonyOS documented controls.  
**Consequence:** no undocumented vendor DB mutation; PerfGenius is treated as app-scoped capability, not a global optimizer.

### ADR-013 — Experiments promote outcomes, not proxy metrics
**Status:** ACTIVE  
**Evidence:** S-036, S-037, S-043.  
**Decision:** A2-005 uses paired/repeated physical-device trials where practical, thermal/control-condition annotation, and user outcomes (cold/warm/hot, relaunch latency/continuity, recurrence).  
**Consequence:** free RAM, clocks or one PSI sample cannot establish benefit.

### ADR-014 — Continuity research uses relaunch/user value; kernel hotness stays kernel-owned
**Status:** ACTIVE  
**Evidence:** S-027, S-038..S-041.  
**Decision:** A2-009 may learn user-priority/relaunch-distance/cost rankings in shadow mode; it does not duplicate page-hotness/reclaim policy. Kernel/framework innovations are a separate future custom-system research track.  
**Consequence:** no arbitrary killing/freezing from learned rankings in stock production.

### ADR-015 — Observer self-interference is a first-class safety constraint
**Status:** ACTIVE  
**Evidence:** S-021, S-036, S-044.  
**Decision:** every capture mode declares/records expected overhead; optional probes are shed under observer stress. A supported app memory budget may be experimentally used only after a measured safe baseline.  
**Consequence:** measurement quality includes cost-of-measurement evidence.

### ADR-016 — Merge evidence store and report/export boundary
**Status:** ACTIVE  
**Reason:** FH-A1 CMP-008 and CMP-009 shared one provenance/privacy lifecycle; a separate report component did not earn unique concurrency/privilege/recovery ownership.  
**Decision:** A2-008 owns versioned evidence persistence plus redacted reporting/export.  
**Consequence:** one less production component while preserving export/redaction tests.
