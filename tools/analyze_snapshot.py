#!/usr/bin/env python3
"""Conservative host-side FixHUA M0.2 snapshot summarizer.

Arm B adds read-only capability observations for newer Android mechanisms. This is
not an incident-attribution engine and never recommends or executes system tuning.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

PSI_RE = re.compile(r"^(some|full)\s+(.*)$")
KV_RE = re.compile(r"([a-zA-Z0-9_]+)=([0-9.]+)")
MEM_RE = re.compile(r"^([A-Za-z0-9_()]+):\s+([0-9]+)\s*(kB)?")
PROP_RE = re.compile(r"^\[([^]]+)\]:\s*\[(.*)\]$")
LIMITER_KV_RE = re.compile(r"\b(monitoring|visibleMem|visibleSwap|notVisibleMem|notVisibleSwap|started|watched|watch-failed|events|processes|process-hwm)=([^\s]+)")

def parse_psi(text: str):
    out={}
    for line in text.splitlines():
        m=PSI_RE.match(line.strip())
        if not m: continue
        vals={k: float(v) if k!='total' else int(float(v)) for k,v in KV_RE.findall(m.group(2))}
        out[m.group(1)]=vals
    return out

def parse_meminfo(text: str):
    out={}
    for line in text.splitlines():
        m=MEM_RE.match(line.strip())
        if m: out[m.group(1)] = int(m.group(2)) * 1024
    return out

def parse_props(text: str):
    out={}
    for line in text.splitlines():
        m=PROP_RE.match(line.strip())
        if m: out[m.group(1)] = m.group(2)
    return out

def parse_memory_limiter_status(text: str):
    """Parse only documented key=value fields; raw prose is not a stable semantic API."""
    return {k:v for k,v in LIMITER_KV_RE.findall(text)}

def read(path: Path):
    try: return path.read_text(errors='replace')
    except OSError: return ''

def status_map(root: Path):
    out={}
    for line in read(root/'command_status.tsv').splitlines():
        parts=line.split('\t',1)
        if len(parts)==2: out[parts[0]]=parts[1]
    return out

def ok(status, key):
    return status.get(key,'').startswith('OK')

def analyze(root: Path):
    status=status_map(root)
    props=parse_props(read(root/'props.txt'))
    pressure={r:parse_psi(read(root/f'pressure_{r}.txt')) for r in ('memory','cpu','io')}
    mem=parse_meminfo(read(root/'proc_meminfo.txt'))
    available=mem.get('MemAvailable'); total=mem.get('MemTotal')
    swap_free=mem.get('SwapFree'); swap_total=mem.get('SwapTotal')
    mem_summary={'memTotalBytes':total,'memAvailableBytes':available,'memAvailableFraction':(available/total if available is not None and total else None),'swapTotalBytes':swap_total,'swapFreeBytes':swap_free,'swapUsedFraction':((swap_total-swap_free)/swap_total if swap_total and swap_free is not None else None)}
    observed=[]
    for resource,p in pressure.items():
        if p: observed.append(f'{resource}_psi')
    if total is not None: observed.append('meminfo')
    missing=[k for k in ('pressure_memory','pressure_cpu','pressure_io','proc_meminfo','thermalservice') if not ok(status,k)]
    nonzero=[]
    for resource,p in pressure.items():
        some=p.get('some',{}); full=p.get('full',{})
        if any(float(some.get(k,0.0))>0.0 for k in ('avg10','avg60')) or any(float(full.get(k,0.0))>0.0 for k in ('avg10','avg60')): nonzero.append(resource)
    if not observed: candidate='UNKNOWN_OR_MIXED'
    elif len(nonzero)==0: candidate='NORMAL_OR_UNDETERMINED'
    else: candidate='PRESSURE_SIGNAL_PRESENT'
    sdk_raw=props.get('ro.build.version.sdk')
    try: sdk=int(sdk_raw) if sdk_raw is not None else None
    except ValueError: sdk=None
    cgroup_text=read(root/'cgroup_controllers.txt').strip()
    limiter_text=read(root/'memory_limiter_status.txt') if ok(status,'memory_limiter_status') else ''
    mglru_text=read(root/'mglru_enabled.txt').strip() if ok(status,'mglru_enabled') else ''
    perfetto_text=read(root/'perfetto_version.txt').strip() if ok(status,'perfetto_version') else ''
    capabilities={'androidSdk':sdk,'memoryLimiterStatus':{'observed':bool(limiter_text.strip()),'adapter':'AM_MEMORY_LIMITER_STATUS_DOCUMENTED_FIELDS_ONLY' if limiter_text.strip() else None,'fields':parse_memory_limiter_status(limiter_text)},'cgroupV2Controllers':{'observed':bool(cgroup_text),'controllers':cgroup_text.split() if cgroup_text else []},'mglruEnabledFile':{'observed':bool(mglru_text),'raw':mglru_text or None},'perfettoVersion':{'observed':bool(perfetto_text),'raw':perfetto_text.splitlines()[0] if perfetto_text else None},'procSwapsObserved':ok(status,'proc_swaps')}
    return {'schemaVersion':2,'reportType':'CAPABILITY_PRESSURE_SNAPSHOT_NOT_INCIDENT_ATTRIBUTION','truthState':'OBSERVATION_SUMMARY_NOT_CAUSAL_DIAGNOSIS','observability':{'status':status,'observed':observed,'missingOrDenied':missing},'platformCapabilities':capabilities,'pressure':pressure,'memory':mem_summary,'candidateState':candidate,'pressureSignalsWithRecentNonzeroPsi':nonzero,'limitations':['This report is not an incident attribution and does not authorize a system write.','A documented Android mechanism is not target capability proof unless its probe/API succeeds on this build.','Nonzero PSI is contextual evidence, not a universal cause; direct exit/start/limiter/freezer/policy evidence should be preferred for an incident.','MemoryLimiter command output and other human-readable text may change; only version-qualified adapters may promote parsed semantics.','Huawei/Android background-policy restrictions can mimic resource-pressure symptoms.','Target-specific benefit and safe actuation remain UNKNOWN until controlled device experiments.']}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('snapshot',type=Path); ap.add_argument('--out',type=Path); args=ap.parse_args(); report=analyze(args.snapshot); text=json.dumps(report,indent=2,sort_keys=True)
    if args.out: args.out.write_text(text+'\n')
    else: print(text)
if __name__=='__main__': main()
