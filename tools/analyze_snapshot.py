#!/usr/bin/env python3
"""Conservative host-side FixHUA M0 snapshot summarizer. Never tunes the device."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
PSI_RE=re.compile(r"^(some|full)\s+(.*)$"); KV_RE=re.compile(r"([a-zA-Z0-9_]+)=([0-9.]+)"); MEM_RE=re.compile(r"^([A-Za-z0-9_()]+):\s+([0-9]+)\s*(kB)?")
def parse_psi(text):
 out={}
 for line in text.splitlines():
  m=PSI_RE.match(line.strip())
  if m: out[m.group(1)]={k:(int(float(v)) if k=='total' else float(v)) for k,v in KV_RE.findall(m.group(2))}
 return out
def parse_meminfo(text):
 out={}
 for line in text.splitlines():
  m=MEM_RE.match(line.strip())
  if m: out[m.group(1)]=int(m.group(2))*1024
 return out
def read(path):
 try:return path.read_text(errors='replace')
 except OSError:return ''
def status_map(root):
 out={}
 for line in read(root/'command_status.tsv').splitlines():
  parts=line.split('\t',1)
  if len(parts)==2: out[parts[0]]=parts[1]
 return out
def analyze(root):
 status=status_map(root); pressure={r:parse_psi(read(root/f'pressure_{r}.txt')) for r in ('memory','cpu','io')}; mem=parse_meminfo(read(root/'proc_meminfo.txt'))
 av=mem.get('MemAvailable'); total=mem.get('MemTotal'); sf=mem.get('SwapFree'); st=mem.get('SwapTotal')
 memory={'memTotalBytes':total,'memAvailableBytes':av,'memAvailableFraction':(av/total if av is not None and total else None),'swapTotalBytes':st,'swapFreeBytes':sf,'swapUsedFraction':((st-sf)/st if st and sf is not None else None)}
 observed=[f'{r}_psi' for r,p in pressure.items() if p]; observed+=['meminfo'] if total is not None else []
 missing=[k for k in ('pressure_memory','pressure_cpu','pressure_io','proc_meminfo','thermalservice') if not status.get(k,'').startswith('OK')]
 nonzero=[]
 for resource,p in pressure.items():
  some=p.get('some',{}); full=p.get('full',{})
  if any(float(some.get(k,0.0))>0.0 for k in ('avg10','avg60')) or any(float(full.get(k,0.0))>0.0 for k in ('avg10','avg60')): nonzero.append(resource)
 candidate='UNKNOWN_OR_MIXED' if not observed else ('NORMAL_OR_UNDETERMINED' if not nonzero else 'PRESSURE_SIGNAL_PRESENT')
 return {'schemaVersion':1,'truthState':'OBSERVATION_SUMMARY_NOT_CAUSAL_DIAGNOSIS','observability':{'status':status,'observed':observed,'missingOrDenied':missing},'pressure':pressure,'memory':memory,'candidateState':candidate,'pressureSignalsWithRecentNonzeroPsi':nonzero,'limitations':['This report does not establish root cause or authorize a system write.','Nonzero PSI can be workload-local or otherwise ambiguous; correlate with memory/thermal/process evidence and a controlled incident.','Huawei background-policy restrictions can mimic resource-pressure symptoms.','Target-specific control capability and benefit remain UNKNOWN until experiments are run.']}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('snapshot',type=Path); ap.add_argument('--out',type=Path); a=ap.parse_args(); text=json.dumps(analyze(a.snapshot),indent=2,sort_keys=True); a.out.write_text(text+'\n') if a.out else print(text)
if __name__=='__main__': main()
