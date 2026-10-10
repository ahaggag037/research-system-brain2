import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "tools" / "device_probe.sh"


class DeviceProbeTests(unittest.TestCase):
    def test_manifest_is_valid_json_and_tsv_split_is_correct(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "snapshot"
            subprocess.run(
                ["sh", str(SCRIPT), str(out)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            manifest = json.loads((out / "manifest.json").read_text())
            self.assertEqual(manifest["schemaVersion"], 1)
            self.assertGreater(len(manifest["files"]), 0)
            allowed = {"OK", "MISSING", "DENIED", "ERROR"}
            for item in manifest["files"]:
                self.assertNotIn("\t", item["name"])
                self.assertIn(item["status"], allowed)
                self.assertEqual(item["source"], item["name"] + ".txt")


if __name__ == "__main__":
    unittest.main()
