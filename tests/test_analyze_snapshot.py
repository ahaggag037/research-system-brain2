import importlib.util, tempfile, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('analyze_snapshot', Path(__file__).parents[1]/'tools'/'analyze_snapshot.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class AnalyzeSnapshotTests(unittest.TestCase):
    def test_psi_parser_preserves_some_full(self):
        p=m.parse_psi('some avg10=1.25 avg60=0.50 avg300=0.10 total=42\nfull avg10=0.01 avg60=0.00 avg300=0.00 total=2\n')
        self.assertEqual(p['some']['avg10'],1.25); self.assertEqual(p['full']['total'],2)
    def test_meminfo_bytes(self):
        x=m.parse_meminfo('MemTotal: 1000 kB\nMemAvailable: 250 kB\nSwapTotal: 500 kB\nSwapFree: 400 kB\n')
        self.assertEqual(x['MemTotal'],1024000); self.assertEqual(x['MemAvailable'],256000)
    def test_missing_input_is_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            r=m.analyze(Path(d))
            self.assertEqual(r['candidateState'],'UNKNOWN_OR_MIXED')
            self.assertIn('pressure_memory',r['observability']['missingOrDenied'])
    def test_nonzero_psi_is_signal_not_causal_diagnosis(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'command_status.tsv').write_text('pressure_memory\tOK\nproc_meminfo\tOK\n')
            (p/'pressure_memory.txt').write_text('some avg10=2.0 avg60=1.0 avg300=0.2 total=9\nfull avg10=0.0 avg60=0.0 avg300=0.0 total=0\n')
            (p/'proc_meminfo.txt').write_text('MemTotal: 1000 kB\nMemAvailable: 100 kB\n')
            r=m.analyze(p)
            self.assertEqual(r['candidateState'],'PRESSURE_SIGNAL_PRESENT')
            self.assertEqual(r['truthState'],'OBSERVATION_SUMMARY_NOT_CAUSAL_DIAGNOSIS')
            self.assertEqual(r['schemaVersion'],2)
            self.assertIn('memory',r['pressureSignalsWithRecentNonzeroPsi'])
    def test_zero_psi_does_not_claim_normal_root_cause(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'command_status.tsv').write_text('pressure_cpu\tOK\n')
            (p/'pressure_cpu.txt').write_text('some avg10=0.0 avg60=0.0 avg300=0.0 total=0\n')
            r=m.analyze(p)
            self.assertEqual(r['candidateState'],'NORMAL_OR_UNDETERMINED')
    def test_parse_props_and_sdk(self):
        x=m.parse_props('[ro.build.version.sdk]: [37]\n[ro.product.manufacturer]: [HUAWEI]\n')
        self.assertEqual(x['ro.build.version.sdk'],'37')
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'command_status.tsv').write_text('props\tOK\n')
            (p/'props.txt').write_text('[ro.build.version.sdk]: [37]\n')
            r=m.analyze(p)
            self.assertEqual(r['platformCapabilities']['androidSdk'],37)
    def test_research_expanded_capabilities_are_observations_not_target_assumptions(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'command_status.tsv').write_text('memory_limiter_status\tOK\ncgroup_controllers\tOK\nmglru_enabled\tOK\nperfetto_version\tOK\nproc_swaps\tOK\n')
            (p/'memory_limiter_status.txt').write_text('Memory limiter\n  enabled monitoring=true visibleMem=1948MB notVisibleMem=974MB events=2\n')
            (p/'cgroup_controllers.txt').write_text('cpu memory pids\n')
            (p/'mglru_enabled.txt').write_text('0x0007\n')
            (p/'perfetto_version.txt').write_text('Perfetto v50\n')
            r=m.analyze(p)
            c=r['platformCapabilities']
            self.assertTrue(c['memoryLimiterStatus']['observed'])
            self.assertEqual(c['memoryLimiterStatus']['fields']['monitoring'],'true')
            self.assertIn('memory',c['cgroupV2Controllers']['controllers'])
            self.assertTrue(c['mglruEnabledFile']['observed'])
            self.assertEqual(c['perfettoVersion']['raw'],'Perfetto v50')
            self.assertEqual(r['reportType'],'CAPABILITY_PRESSURE_SNAPSHOT_NOT_INCIDENT_ATTRIBUTION')

if __name__=='__main__': unittest.main()
