"""Packaging contracts for the installed AntiRLHF roles."""
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package_skills import CORE, OPTIONAL, make_archive, staged_files


class PackageTests(unittest.TestCase):
    def test_five_core_entries(self):
        files = staged_files(ROOT, False)
        for name in CORE:
            self.assertIn(Path(name) / "SKILL.md", files)
        self.assertNotIn(Path("project-workflows") / "SKILL.md", files)
        self.assertIn(Path("CONSTITUTION.md"), files)

    def test_optional_project_and_bilingual_entries(self):
        files = staged_files(ROOT, True)
        for name in CORE + OPTIONAL:
            self.assertIn(Path(name) / "SKILL.md", files)
            self.assertIn(Path(name) / "SKILL.zh-CN.md", files)
        self.assertIn(Path("antirlhf-review/references/review.md"), files)
        self.assertIn(Path("refactoring/references/removal-and-migration.md"), files)

    def test_archive_has_relocatable_references(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "skills.zip"
            make_archive(ROOT, path, True)
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                self.assertIn("antirlhf-review/SKILL.md", names)
                self.assertIn("documentation/scripts/check/governance_prose.py", names)
                self.assertIn("project-workflows/references/release.md", names)
                self.assertNotIn("docs/research/behavioral-mechanisms.md", names)
                self.assertNotIn("documentation/tests/test_governance_prose.py", names)


if __name__ == "__main__":
    unittest.main()
