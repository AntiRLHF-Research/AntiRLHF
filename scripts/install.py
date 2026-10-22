#!/usr/bin/env python3
"""Install AntiRLHF Skills and merge the managed Constitution into a chosen instruction file."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys
import tempfile

from package_skills import CORE, OPTIONAL, ROOT, staged_files

BEGIN = "<!-- BEGIN AntiRLHF managed Constitution -->"
END = "<!-- END AntiRLHF managed Constitution -->"


def install(root: Path, skills_dir: Path, instructions_file: Path, include_project: bool, replace: bool, dry_run: bool):
    staged_files(root, include_project)  # validate complete source and resolved dependencies
    role_names = CORE + (OPTIONAL if include_project else ())
    conflicts = [skills_dir / name for name in role_names if (skills_dir / name).exists()]
    if conflicts and not replace:
        raise ValueError("Existing Skills require --replace: " + ", ".join(p.name for p in conflicts))
    if replace:
        blocked = [skills_dir / f"{p.name}.backup" for p in conflicts if (skills_dir / f"{p.name}.backup").exists()]
        if blocked:
            raise ValueError("Existing backups must be resolved before replacement: " + ", ".join(map(str, blocked)))
    old = instructions_file.read_text(encoding="utf-8") if instructions_file.exists() else ""
    if (BEGIN in old) != (END in old):
        raise ValueError(f"Incomplete AntiRLHF managed block: {instructions_file}")
    constitution = (root / "CONSTITUTION.md").read_text(encoding="utf-8").rstrip()
    new_block = f"{BEGIN}\n{constitution}\n{END}"
    if BEGIN in old:
        start = old.index(BEGIN)
        end = old.index(END, start) + len(END)
        new = old[:start] + new_block + old[end:]
    else:
        new = new_block + "\n\n" + old
    if dry_run:
        print(f"Would install {', '.join(role_names)} to {skills_dir}")
        print(f"Would merge Constitution into {instructions_file}")
        return
    skills_dir.mkdir(parents=True, exist_ok=True)
    # Stage the new directories before touching installed Skills.
    with tempfile.TemporaryDirectory(prefix="antirlhf-install-", dir=skills_dir) as temp:
        stage = Path(temp)
        for name in role_names:
            shutil.copytree(root / "skills" / name, stage / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "tests", ".pytest_cache"))
            (stage / name / ".version").write_text((root / ".version").read_text(encoding="utf-8"), encoding="utf-8")
        # Old user Skills are retained in named backups when replacement is explicit.
        for name in role_names:
            target = skills_dir / name
            if target.exists():
                backup = skills_dir / f"{name}.backup"
                if backup.exists():
                    raise ValueError(f"Backup already exists; resolve first: {backup}")
                target.rename(backup)
            (stage / name).rename(target)
    instructions_file.parent.mkdir(parents=True, exist_ok=True)
    instructions_file.write_text(new, encoding="utf-8")
    print(f"Installed {len(role_names)} Skills; managed Constitution: {instructions_file}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--skills-dir", type=Path, required=True)
    ap.add_argument("--instructions-file", type=Path, required=True)
    ap.add_argument("--with-project-workflows", action="store_true")
    ap.add_argument("--replace", action="store_true", help="back up existing matching Skill directories and replace them")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    try:
        install(args.root, args.skills_dir, args.instructions_file, args.with_project_workflows, args.replace, args.dry_run)
    except (OSError, ValueError) as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
