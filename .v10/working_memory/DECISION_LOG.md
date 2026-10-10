# DECISION LOG

## D-001 — Clean-room canonical workspace
DECISION_ID: D-001
STATUS: ACTIVE
DATE/SEQUENCE: Initialization
CONTEXT: Mission package requires blind independent genesis in one dedicated repository.
OPTIONS: Use only authorized repo; inspect predecessor work; keep state only in chat.
DECISION: Use only `ahaggag037/research-system-brain2` on `main` as canonical workspace; use public research only when independent; persist consequential state to GitHub.
EVIDENCE: V10.3-B `00_CONTROL_PLANE.md`, `00B_CLEAN_REPOSITORY_BOUNDARY.md`; GitHub repository metadata.
ASSUMPTIONS: GitHub connector remains writable.
CONSEQUENCES: Prior user repositories are intentionally unavailable as evidence; cold-start repository quality is mandatory.
RISKS: Accidental contamination; mitigated by strict repository/search scoping.
REOPEN_IF: Mission contract changes or repository becomes inaccessible.
SUPERSEDES: None
SUPERSEDED_BY: None

## D-002 — Discovery remains architecture-neutral
DECISION_ID: D-002
STATUS: PROVISIONAL
DATE/SEQUENCE: Initialization
CONTEXT: Early ideas should not lock the product category.
OPTIONS: Commit now to optimizer/tweak app; remain product-category neutral until evidence converges.
DECISION: Remain architecture-neutral through Discovery; treat adaptive measurement-driven control as a hypothesis, not a fact.
EVIDENCE: Engineering Constitution §§1,7 and Control Plane mission definition.
ASSUMPTIONS: Public research and first-principles reasoning can narrow mechanisms sufficiently.
CONSEQUENCES: No implementation category is privileged before evidence.
RISKS: Discovery sprawl; controlled by diminishing marginal information value and convergence criteria.
REOPEN_IF: Discovery Protocol prescribes a stronger constraint.
SUPERSEDES: None
SUPERSEDED_BY: None
