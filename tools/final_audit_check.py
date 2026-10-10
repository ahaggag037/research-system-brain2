#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve(); errors=[]
required=['AGENTS.md','README.md','PROJECT_STATE.json','KNOWLEDGE_GRAPH.json','IMPLEMENTATION_MAP.json','VISUAL_TRACEABILITY.json','REQUIREMENT_TRACEABILITY.md','docs/project/00_START_HERE.md','docs/project/FUTURE_MODEL_PROTOCOL.md','docs/architecture/ARCHITECTURE.md','docs/architecture/DECISIONS.md','docs/architecture/COMPONENT_CONTRACTS.md','docs/implementation/BUILD_RUNBOOK.md','docs/implementation/TEST_MATRIX.md','docs/visual/ARCHITECTURE.mmd','docs/visual/RUNTIME_NORMAL.mmd','docs/visual/RUNTIME_INCIDENT.mmd','docs/visual/DEPENDENCY_BUILD.mmd','docs/visual/PRODUCT_FLOW.mmd','tools/device_probe.sh','tools/analyze_snapshot.py','tests/test_analyze_snapshot.py','tests/test_device_probe.py']
for rel in required:
    if not (root/rel).is_file(): errors.append('missing:'+rel)
for p in list(root.glob('*.json'))+list((root/'schemas').glob('*.json')):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f'invalid-json:{p.relative_to(root)}:{e}')
ledger=(root/'.v10/working_memory/REQUIREMENT_LEDGER.md').read_text()
if '90/90 SATISFIED' not in ledger: errors.append('requirement-gate-not-final')
vt=json.loads((root/'VISUAL_TRACEABILITY.json').read_text()); vis='\n'.join(p.read_text() for p in (root/'docs/visual').glob('*.mmd'))
for n in vt.get('nodes',[]):
    if n.get('visual') and n['visual'] not in vis: errors.append('visual-id-not-found:'+n['visual'])
for p in root.rglob('*'):
    rel=p.relative_to(root).as_posix()
    if rel.startswith('_human/') or '/_human/' in rel: errors.append('forbidden-human-path:'+rel)
    if rel.startswith('private-device-snapshots/'): errors.append('raw-snapshot:'+rel)
probe=(root/'tools/device_probe.sh').read_text()
for bad in ['settings put','settings delete','setprop persist.','> /sys/','> /proc/','am force-stop']:
    if bad in probe: errors.append('probe-write-pattern:'+bad)
state=json.loads((root/'PROJECT_STATE.json').read_text())
if state.get('buildState',{}).get('androidApk')!='NOT_IMPLEMENTED': errors.append('apk-overclaim')
if state.get('testState',{}).get('targetDevice')!='NOT_RUN_NO_DEVICE': errors.append('target-overclaim')
if errors:
    print('FAIL\n'+'\n'.join(errors)); raise SystemExit(1)
print('PASS: final structural/truth/visual/no-write checks')
