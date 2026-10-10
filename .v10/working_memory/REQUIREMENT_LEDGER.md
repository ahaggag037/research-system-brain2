# REQUIREMENT LEDGER

> Canonical operational compliance ledger. This file is scratch/operational state, not a replacement for the mission contract.

| ID | Source | Priority | Requirement | Acceptance evidence | Artifact/path | Status | Blocker/notes |
|---|---|---|---|---|---|---|---|
| R-001 | 00_CONTROL_PLANE §0 | MUST | Design the strongest realistic FixHUA project for a Huawei-class Android phone from first principles. | Converged architecture + audit trace | docs/ARCHITECTURE.md | OPEN |  |
| R-002 | 00_CONTROL_PLANE §0 | MUST | Optimize for responsiveness, smoothness, multitasking continuity, fewer avoidable reloads/exits, resume quality, sustained stability, predictability, and intelligent management. | Outcome mapping and validation plan | docs/OUTCOMES_AND_METRICS.md | OPEN |  |
| R-003 | 00_CONTROL_PLANE §0 | MUST | Treat root as an available capability only when justified, not as the product definition. | Privilege policy and component contracts | docs/PRIVILEGE_AND_SAFETY.md | OPEN |  |
| R-004 | 00_CONTROL_PLANE §0 | SHOULD | Maintain a credible path to a useful installable/testable first build in hours of focused engineering where feasible. | MVP implementation map with buildable slices | docs/IMPLEMENTATION_MAP.md | OPEN |  |
| R-005 | 00_CONTROL_PLANE §0 | MUST | Use diminishing marginal value of new information as the research stopping rule. | Discovery convergence record | .v10/working_memory/CHECKPOINT.md | OPEN |  |
| R-006 | 00_CONTROL_PLANE §1 | MUST | Do not inspect predecessor FixHUA architecture, prompts, research, diagrams, prior design discussions, or _human/. | Blindness statement and contamination audit | FINAL_AUDIT.md | OPEN |  |
| R-007 | 00_CONTROL_PLANE §1 | MAY | Use independent public research on Android/Linux/Huawei/SoCs/OS/performance/open source/math and related fields. | Source index | .v10/working_memory/SOURCE_INDEX.md | OPEN |  |
| R-008 | 00_CONTROL_PLANE §3 | MUST | Execute states A→B→C→D continuously in one session with automatic transitions. | Checkpoint state transitions + final audit | .v10/working_memory/CHECKPOINT.md | OPEN |  |
| R-009 | 00_CONTROL_PLANE §3 | MUST | Read mission files only in staged order; do not preload later packaging contracts during discovery. | Checkpoint read log | .v10/working_memory/CHECKPOINT.md | OPEN |  |
| R-010 | 00_CONTROL_PLANE §3 | MUST | Write DESIGN_CONVERGED only after Discovery convergence criteria are met. | Convergence marker | .v10/working_memory/CHECKPOINT.md | OPEN |  |
| R-011 | 00_CONTROL_PLANE §5 | MUST | Use MISSION_COMPLETE only if Final Audit Protocol permits; otherwise MISSION_INCOMPLETE with blockers. | Final audit conclusion | FINAL_AUDIT.md | OPEN |  |
| R-012 | 00A §1-3 | MUST | Do not stop at plans, research, architecture, docs, diagrams, or milestones; continue through final audit and ZIP attempt. | Continuous checkpoint sequence + final artifacts | FINAL_AUDIT.md | OPEN |  |
| R-013 | 00A §4 | MUST | For genuine blockers: record them, define smallest recovery action, and continue independent work. | Ledger/checkpoint blocker entries | .v10/working_memory/REQUIREMENT_LEDGER.md | OPEN |  |
| R-014 | 00A §5 | MUST | Handle tool failures with bounded retry/alternatives, record limitations, and continue unaffected work. | Tool-limit notes/audit | FINAL_AUDIT.md | OPEN |  |
| R-015 | 00A §7 | MUST | Maintain working memory continuously and checkpoint at context-heavy transitions. | Working-memory files | .v10/working_memory/ | OPEN |  |
| R-016 | 00A §8 | MUST | If final audit finds defects, repair and re-audit within the same session. | Audit repair log | FINAL_AUDIT.md | OPEN |  |
| R-017 | 00A §9 | MUST | Complete cold-start audit, visual/document consistency audit, transfer package if tooling permits, and final handoff. | Final audit + transfer manifest | FINAL_AUDIT.md | OPEN |  |
| R-018 | 00B §1 | MUST | Perform all mission work only in ahaggag037/research-system-brain2 on main; do not inspect any other user repo. | Repository status proof | FINAL_AUDIT.md | OPEN |  |
| R-019 | 00B §2 | MUST | Do not use public search to retrieve cached/prior user FixHUA work. | Research-source audit | .v10/working_memory/SOURCE_INDEX.md | OPEN |  |
| R-020 | 00B §3 | MUST | Make GitHub repository the canonical continuation surface and ZIP a transport snapshot. | Canonical entry + repository proof | README.md | OPEN |  |
| R-021 | 00B §3 | MUST | Final repo must contain root AGENTS.md, canonical entry, machine-readable state, decisions, component contracts, implementation map, build/test/runbook, visual twin source, final audit, and handoff checkpoint. | Presence/content audit | FINAL_AUDIT.md | OPEN |  |
| R-022 | 00B §4 | MUST | Keep canonical scratch memory under .v10/working_memory/, public-safe and secret-free. | Repo tree + secret scan | .v10/working_memory/ | OPEN |  |
| R-023 | 00B §4 | MUST | At DESIGN_CONVERGED and before handoff, distill important scratch knowledge into canonical docs and mark scratch noncanonical. | Distillation notes + docs | docs/ | OPEN |  |
| R-024 | 00B §5 | SHOULD | Persist meaningful checkpoints in GitHub as work progresses rather than transient context only. | Git history/checkpoint files | Git history | OPEN |  |
| R-025 | 00B §6 | MUST | Keep main as canonical branch and reconcile any temporary workflow back to main. | Branch proof | FINAL_AUDIT.md | OPEN |  |
| R-026 | 00B §7 | MUST | If contamination occurs, stop consuming it, record exposure, exclude it as evidence, continue independently, and disclose it. | Contamination record/audit | .v10/working_memory/ACTIVE_NOTES.md | OPEN |  |
| R-027 | 00B §8 | MUST | Final repository must cold-start from GitHub alone and communicate conclusions, product, truth state, implementation state, architecture, build/test, unknowns, next task, and privilege safeguards. | GitHub cold-start validation | FINAL_AUDIT.md | OPEN |  |
| R-028 | 00B §9 | MUST | Record final repo name, branch, current commit SHA if available, package/version ID, cold-start result, unresolved blocker count, and next milestone. | Final repository status proof | FINAL_AUDIT.md | OPEN |  |
| R-029 | 01 §2-3 | MUST | Bound hazardous concepts by mechanism, magnitude/timing/persistence/interactions/uncertainty/recovery; keep unsafe-unbounded ideas research-only. | Risk register + safety contracts | docs/PRIVILEGE_AND_SAFETY.md | OPEN |  |
| R-030 | 01 §3 | MUST | Admit privileged production behavior only with evidence, bounded scope, measurable expected effect, abort conditions, rollback/recovery, uncertainty awareness, and validation path. | Privilege admission contract | docs/PRIVILEGE_AND_SAFETY.md | OPEN |  |
| R-031 | 01 §3 | MUST | Do not disable fundamental hardware safety protections or build account/banking/DRM/integrity/anti-tamper bypasses or unrestricted arbitrary-root command endpoints. | Explicit forbidden-actions policy + audit | docs/PRIVILEGE_AND_SAFETY.md | OPEN |  |
| R-032 | 01 §4-6 | MUST | Treat models as hypotheses, distinguish causality from correlation, and verify privileged controls exist/useful/safe before relying on them. | Evidence taxonomy + experiment plans | docs/EVIDENCE_AND_EXPERIMENTS.md | OPEN |  |
| R-033 | 01 §7 | MUST | Require every important subsystem to justify unique value, cost, overhead, risk, and why a simpler mechanism is insufficient. | Architecture decision records | docs/DECISIONS.md | OPEN |  |
| R-034 | 01 §8 | MUST | Optimize for real user value rather than free RAM, max clocks, synthetic benchmarks, or tweak count alone. | Outcome metric design | docs/OUTCOMES_AND_METRICS.md | OPEN |  |
| R-035 | 01 §9 | MUST | Classify consequential claims using explicit truth states and never promote hypotheses silently. | Truth-state legend + annotated docs/state | PROJECT_STATE.json | OPEN |  |
| R-036 | 01 §10-11 | MUST | Do not silently omit mandatory items; keep working memory operational rather than private-reasoning dumps. | Requirement audit + memory review | FINAL_AUDIT.md | OPEN |  |
| R-037 | 03 §1 | MUST | Create the eight canonical working-memory files from templates. | All eight files exist | .v10/working_memory/ | IN_PROGRESS | Requirement ledger created; remaining seven files staged for same initialization checkpoint. |
| R-038 | 03 §3-7 | MUST | Update memory on consequential facts/ideas/decisions/contradictions/requirements/experiments/risks/tool limits, checkpoint at transitions, and distill at convergence. | Working-memory history | .v10/working_memory/ | IN_PROGRESS |  |
| R-039 | 03 §5 | MUST | Recovery procedure must read checkpoint, ledger, decision log, needed memory, then reconcile with actual artifacts. | AGENTS recovery section | AGENTS.md | OPEN |  |
| R-040 | 03 §6 | SHOULD | Keep working memory compact via deduplication, supersession markers, and focused active notes. | Memory hygiene audit | .v10/working_memory/ACTIVE_NOTES.md | OPEN |  |
| R-041 | 04 §1 | MUST | Compile loaded mandatory instructions into atomic requirements with source, priority, acceptance evidence, status, artifact, and blockers. | Requirement ledger schema/population | .v10/working_memory/REQUIREMENT_LEDGER.md | SATISFIED | Initial loaded-contract compilation established; extend when later mission files are read. |
| R-042 | 04 §4 | MUST | Bind every MUST to concrete evidence or an explicit blocker. | Ledger review | .v10/working_memory/REQUIREMENT_LEDGER.md | IN_PROGRESS | Initial binding present; final evidence statuses pending. |
| R-043 | 04 §5-6 | MUST | Reopen affected requirements after architecture changes and record/resolve actual requirement conflicts. | Decision/contradiction logs | .v10/working_memory/CONTRADICTION_REGISTER.md | OPEN |  |
| R-044 | 04 §7-9 | MUST | Before completion every MUST is SATISFIED or BLOCKED with recovery path; run compact compliance reviews at prescribed checkpoints. | Final ledger audit | FINAL_AUDIT.md | IN_PROGRESS | Initialization compliance review completed. |

Statuses: OPEN / IN_PROGRESS / SATISFIED / PARTIALLY_SATISFIED / BLOCKED / SUPERSEDED / NOT_APPLICABLE_WITH_JUSTIFICATION
