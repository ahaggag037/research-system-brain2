# CONTRADICTION REGISTER — compact recovery view

| ID | Status | Contradiction | Resolution |
|---|---|---|---|
| C-001 | RESOLVED | keep apps warm vs real memory pressure | optimize valuable continuity under pressure; never pin everything |
| C-002 | RESOLVED | freezer preserves cached app vs need to free memory | freezer is not memory relief; no universal manual freeze policy |
| C-003 | RESOLVED | root observability/control vs stability | split privileged reads from typed qualified writes; no arbitrary shell API |
| C-004 | RESOLVED | M0 manifest claim vs nonportable TSV parsing | portable tab split + regression test |
| C-005 | RESOLVED | State-C 5-test metadata vs repaired suite | historical package fixed to 6/6 |
| C-006 | RESOLVED | nested analyzer test metadata stale | historical state repaired before V10.3-B package |
| C-007 | RESOLVED_BY_FH_A2 | continuous recorder vs cached freezer/background execution | incident history + tiered bounded capture; no continuous correctness dependency |
| C-008 | RESOLVED_BY_FH_A2 | generic MEMORY_PRESSURE vs Android 17 MemoryLimiter | separate `MEMORY_LIMITER` from LMK/global pressure; direct reason first |
| C-009 | RESOLVED_BY_SCOPE_REDUCTION | user-space page-hotness ideas vs kernel MGLRU | A2-009 focuses user/relaunch value; kernel owns page hotness |
| C-010 | RESOLVED_AS_CAPABILITY_BOUNDARY | direct start/exit APIs vs cross-UID/version permissions | A2-002 profiles access; A2-003 uses direct records only when qualified, else escalates/UNKNOWN |

Canonical rationale/evidence: `docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md`, active ADRs and FH-A2 architecture docs.
