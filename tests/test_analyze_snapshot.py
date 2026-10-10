import importlib.util,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('analyze_snapshot',Path(__file__).parents[1]/'tools'/'analyze_snapshot.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class AnalyzeSnapshotTests(unittest.TestCase):
 def test_psi_parser_preserves_some_full(self):
  p=m.parse_psi('some avg10=1.25 avg60=0.50 avg300=0.10 total=42\nfull avg10=0.01 avg60=0.00 avg300=0.00 total=2\n'); self.assertEqual(p['some']['avg10'],1.25); self.assertEqual(p['full']['total'],2)
 def test_meminfo_bytes(self):
  x=m.parse_meminfo('MemTotal: 1000 kB\nMemAvailable: 250 kB\nSwapTotal: 500 kB\nSwapFree: 400 kB\n'); self.assertEqual(x['MemTotal'],1024000); self.assertEqual(x['MemAvailable'],256000)
 def test_missing_input_is_unknown(self):
  with tempfile.TemporaryDirectory() as d:
   r=m.analyze(Path(d)); self.assertEqual(r['candidateState'],'UNKNOWN_OR_MIXED'); self.assertIn('pressure_memory',r['observability']['missingOrDenied'])
 def test_nonzero_psi_is_signal_not_causal_diagnosis(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'command_status.tsv').write_text('pressure_memory\tOK\nproc_meminfo\tOK\n'); (p/'pressure_memory.txt').write_text('some avg10=2.0 avg60=1.0 avg300=0.2 total=9\nfull avg10=0.0 avg60=0.0 avg300=0.0 total=0\n'); (p/'proc_meminfo.txt').write_text('MemTotal: 1000 kB\nMemAvailable: 100 kB\n'); r=m.analyze(p); self.assertEqual(r['candidateState'],'PRESSURE_SIGNAL_PRESENT'); self.assertEqual(r['truthState'],'OBSERVATION_SUMMARY_NOT_CAUSAL_DIAGNOSIS')
 def test_zero_psi_does_not_claim_normal_root_cause(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'command_status.tsv').write_text('pressure_cpu\tOK\n'); (p/'pressure_cpu.txt').write_text('some avg10=0.0 avg60=0.0 avg300=0.0 total=0\n'); self.assertEqual(m.analyze(p)['candidateState'],'NORMAL_OR_UNDETERMINED')
if __name__=='__main__': unittest.main()
