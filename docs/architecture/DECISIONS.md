# Architecture Decision Records

## ADR-001 — Select evidence-gated supervisor
**Status:** ACTIVE  
**Context:** Similar Huawei/Android symptoms can originate from multiple resource and policy mechanisms.  
**Alternatives:** static tweak pack; aggressive root autotuner; diagnostics-only; evidence-gated supervisor.  
**Choice:** FH-A1 evidence-gated supervisor.  
**Evidence:** AOSP LMKD/PSI/cgroup/freezer/thermal docs and Huawei background-policy docs in `docs/evidence/SOURCES.md`.  
**Assumptions:** useful observables exist on the target, at least via explicit shell/root read access.  
**Consequences:** diagnosis and shadow evaluation precede writes; architecture remains useful even if zero write actuators qualify.  
**Risks:** observer overhead; classification uncertainty; controller conflict.  
**Reopen if:** target evidence shows observability is too weak or a simpler architecture achieves the same outcomes.  

## ADR-002 — First useful build is observation-first
**Status:** ACTIVE  
**Choice:** ship/use a read-only capability/pressure snapshot path before Android privileged control.  
**Why:** it produces high information gain, validates assumptions, and cannot destabilize system policy through writes.  
**Reopen if:** the target denies enough observability that the snapshot is not decision-useful.

## ADR-003 — Multi-signal state estimation; UNKNOWN is allowed
**Status:** ACTIVE  
**Choice:** no single free-RAM, PSI, clock or thermal threshold may authorize control. Estimation combines available evidence and emits `UNKNOWN_OR_MIXED` when evidence conflicts or is incomplete.  
**Evidence:** AOSP 2026 LMKD correction shows a full-memory-PSI signal can be misleading under some memcg conditions.  
**Reopen if:** validated target telemetry establishes a stronger causal minimal signal set.

## ADR-004 — Typed privilege gateway; no arbitrary root endpoint
**Status:** ACTIVE  
**Choice:** UI/policy code cannot execute free-form root commands. Privileged writes, if ever admitted, are allowlisted typed actuators with preconditions, bounded parameters, verification, timeout and rollback.  
**Reopen if:** never for unrestricted root; typed implementation details may evolve.

## ADR-005 — No persistent boot-time modifications in first installable build
**Status:** ACTIVE  
**Choice:** first Android build is observation/reporting only; any privileged read helper is explicit-session and ephemeral.  
**Why:** firmware/device capability is unverified and persistent services add reliability/battery risk.  
**Reopen if:** daily-use evidence demonstrates a persistent observer is required and overhead/recovery tests pass.

## ADR-006 — Huawei documented settings before undocumented mutation
**Status:** ACTIVE  
**Choice:** diagnose App Launch/background/battery policy and guide the user through documented settings/deep links where possible; do not edit undocumented vendor state stores.  
**Reopen if:** Huawei exposes a documented programmable API suitable for the target.

## ADR-007 — Continuity allocator is experimental, non-destructive initially
**Status:** ACTIVE  
**Choice:** user-priority/reuse/cold-start-cost scoring may rank continuity value in shadow mode, but initial production does not kill/freeze arbitrary apps based on this score.  
**Reopen if:** E-003/E-005-style device experiments show safe, superior outcomes and protect background semantics.

## ADR-008 — Local-first evidence and redacted export
**Status:** ACTIVE  
**Choice:** sensitive device/app telemetry stays local by default; exports minimize fields and support identifier redaction. Public repository must never receive raw device reports automatically.  
**Reopen if:** user explicitly configures another privacy-preserving storage model.

## Rejected major alternatives
See `docs/evidence/REJECTED_IDEAS.md`; history is preserved rather than rewritten.
