#!/usr/bin/env python3
import json,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve(); required=['AGENTS.md','README.md','PROJECT_STATE.json','KNOWLEDGE_GRAPH.json','IMPLEMENTATION_MAP.json','VISUAL_TRACEABILITY.json','docs/project/00_START_HERE.md','docs/architecture/ARCHITECTURE.md','docs/architecture/DECISIONS.md','docs/architecture/COMPONENT_CONTRACTS.md','docs/implementation/BUILD_RUNBOOK.md','docs/implementation/TEST_MATRIX.md','docs/visual/ARCHITECTURE.mmd','docs/visual/RUNTIME_NORMAL.mmd','docs/visual/RUNTIME_INCIDENT.mmd','docs/visual/DEPENDENCY_BUILD.mmd','docs/visual/PRODUCT_FLOW.mmd']; errors=[]
for rel in required:
 if not (root/rel).is_file(): errors.append(f'missing {rel}')
for rel in ['PROJECT_STATE.json','KNOWLEDGE_GRAPH.json','IMPLEMENTATION_MAP.json','VISUAL_TRACEABILITY.json','schemas/device_snapshot.schema.json','schemas/diagnosis_report.schema.json']:
 p=root/rel
 if p.exists():
  try:json.loads(p.read_text())
  except Exception as e:errors.append(f'invalid json {rel}: {e}')
probe=(root/'tools/device_probe.sh').read_text() if (root/'tools/device_probe.sh').exists() else ''
for forbidden in ['settings put','settings delete','echo 1 > /proc','echo 1 > /sys','setprop persist.']:
 if forbidden in probe:errors.append(f'probe contains forbidden write pattern: {forbidden}')
try: state=json.loads((root/'PROJECT_STATE.json').read_text())
except Exception: state={}
if state and state.get('buildState',{}).get('androidApk') not in {'NOT_IMPLEMENTED',None}: errors.append('state may overclaim Android APK')
if errors: print('FAIL\n'+'\n'.join(errors)); sys.exit(1)
print('PASS: repository structural/json/no-write guard checks')
