#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
errors=[]
required=['AGENTS.md','README.md','PROJECT_STATE.json','KNOWLEDGE_GRAPH.json','IMPLEMENTATION_MAP.json','VISUAL_TRACEABILITY.json','REQUIREMENT_TRACEABILITY.md','docs/project/00_START_HERE.md','docs/project/FUTURE_MODEL_PROTOCOL.md','docs/project/ARM_B_CHANGELOG.md','docs/architecture/ARCHITECTURE.md','docs/architecture/ARCHITECTURE_REEVALUATION_ARM_B.md','docs/architecture/DECISIONS.md','docs/architecture/COMPONENT_CONTRACTS.md','docs/architecture/INTERFACES_AND_RUNTIME.md','docs/architecture/DATA_STATE_MODEL.md','docs/architecture/PRIVILEGE_AND_SAFETY.md','docs/architecture/FAILURE_RECOVERY_MATRIX.md','docs/evidence/EVIDENCE_AND_EXPERIMENTS.md','docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md','docs/evidence/SOURCES.md','docs/evidence/RISK_TRANSMUTATION.md','docs/evidence/REJECTED_IDEAS.md','docs/implementation/IMPLEMENTATION_BLUEPRINT.md','docs/implementation/FIRST_BUILD_CRITICAL_PATH.md','docs/implementation/BUILD_RUNBOOK.md','docs/implementation/CODEBASE_MAP.md','docs/implementation/TEST_MATRIX.md','docs/implementation/READINESS_DEFINITIONS.md','docs/implementation/INTEGRATION_PROOF.md','docs/visual/ARCHITECTURE.mmd','docs/visual/RUNTIME_NORMAL.mmd','docs/visual/RUNTIME_INCIDENT.mmd','docs/visual/DEPENDENCY_BUILD.mmd','docs/visual/PRODUCT_FLOW.mmd','tools/device_probe.sh','tools/analyze_snapshot.py','tools/validate_repo.py','tests/test_analyze_snapshot.py','tests/test_device_probe.py','schemas/device_snapshot.schema.json','schemas/diagnosis_report.schema.json']
for rel in required:
    if not (root/rel).is_file(): errors.append(f'missing:{rel}')
for p in list(root.glob('*.json'))+list((root/'schemas').glob('*.json')):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f'invalid-json:{p.relative_to(root)}:{e}')
ledger=(root/'.v10/working_memory/REQUIREMENT_LEDGER.md').read_text()
ids=re.findall(r'^\| (R-\d{3}) \|',ledger,re.M)
if ids != [f'R-{i:03d}' for i in range(1,107)]: errors.append('requirement-ledger-id-gap')
g=json.loads((root/'KNOWLEDGE_GRAPH.json').read_text())
if g.get('requirementIds') != [f'R-{i:03d}' for i in range(1,107)]: errors.append('knowledge-graph-requirement-id-gap')
vt=json.loads((root/'VISUAL_TRACEABILITY.json').read_text())
visual_text='\n'.join(p.read_text() for p in (root/'docs/visual').glob('*.mmd'))
for n in vt.get('nodes',[]):
    vid=n.get('visual')
    if vid and vid not in visual_text: errors.append(f'visual-id-not-found:{vid}')
for p in root.rglob('*'):
    rel=p.relative_to(root).as_posix()
    if rel.startswith('_human/') or '/_human/' in rel: errors.append(f'forbidden-human-path:{rel}')
    if rel.startswith('private-device-snapshots/'): errors.append(f'raw-device-snapshot-present:{rel}')
secret_patterns=[re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b'),re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'),re.compile(r'AIza[0-9A-Za-z_-]{20,}')]
for p in root.rglob('*'):
    if not p.is_file() or p.suffix.lower() in {'.zip','.pyc'}: continue
    try: text=p.read_text(errors='ignore')
    except Exception: continue
    for pat in secret_patterns:
        if pat.search(text): errors.append(f'secret-pattern:{p.relative_to(root)}:{pat.pattern}')
probe=(root/'tools/device_probe.sh').read_text()
for forbidden in ['settings put','settings delete','setprop persist.','> /sys/','> /proc/','cmd package suspend','am force-stop']:
    if forbidden in probe: errors.append(f'probe-write-pattern:{forbidden}')
state=json.loads((root/'PROJECT_STATE.json').read_text())
if state.get('buildState',{}).get('androidApk')!='NOT_IMPLEMENTED': errors.append('apk-overclaim')
if state.get('testState',{}).get('targetDevice')!='NOT_RUN_NO_DEVICE': errors.append('target-test-overclaim')
if state.get('architecture',{}).get('id')!='FH-A2': errors.append('active-architecture-not-fh-a2')
research=(root/'docs/evidence/EXTERNAL_RESEARCH_EXPANSION_ARM_B.md').read_text()
for q in range(1,13):
    if f'## Q{q} ' not in research: errors.append(f'missing-armb-question:Q{q}')
for sid in range(17,45):
    if f'S-{sid:03d}' not in (root/'docs/evidence/SOURCES.md').read_text(): errors.append(f'missing-armb-source:S-{sid:03d}')
if 'FH-A2' not in (root/'docs/architecture/ARCHITECTURE.md').read_text(): errors.append('fh-a2-architecture-missing')
if 'A2-001' not in visual_text or 'A2-009' not in visual_text: errors.append('fh-a2-visual-range-missing')
if state.get('researchExpansion',{}).get('status') not in {'COMPLETE_RECONVERGED','COMPLETE_RECONVERGED_AUDITED'}: errors.append('armb-research-not-reconverged')
if state.get('phase') == 'ARM_B_FINAL_AUDIT_COMPLETE':
    if state.get('auditState',{}).get('requirementsSatisfied') != 106: errors.append('terminal-requirements-not-106')
    if state.get('auditState',{}).get('blockedMissionMust') != 0: errors.append('terminal-blocked-must-nonzero')
    if state.get('testState',{}).get('hostUnit') != 'TESTED_8_OF_8_PASS_IN_MISSION_CONTAINER': errors.append('terminal-host-test-count-mismatch')
    if state.get('package',{}).get('status') != 'CREATED_AND_VALIDATED_IN_MISSION_CONTAINER': errors.append('terminal-package-not-validated')
if errors:
    print('FAIL'); print('\n'.join(errors)); raise SystemExit(1)
print('PASS: final structural/truth/visual/secret/no-write checks')
