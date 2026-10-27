#!/usr/bin/env python3
"""Build the GitHub release archive of the installable skill package."""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


ROOT_FILES = (
    ".version",
    "CONSTITUTION.zh-CN.md",
    "CONTENTS.zh-CN.md",
    "LICENSE",
    "README.md",
    "plugin.json",
)
SKIP_DIRECTORIES = {"__pycache__", ".pytest_cache", "tests"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}
SKIP_SUFFIXES = {".pyc", ".pyo"}


def version_text(root: Path) -> str:
    version = (root / ".version").read_text(encoding="utf-8").strip()
    if not version or any(part in version for part in ("/", "\\", "\n")):
        raise ValueError(f"Invalid version: {version!r}")
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("version") != version:
        raise ValueError(f"plugin.json version {manifest.get('version')!r} does not match {version}")
    return version


def package_files(root: Path) -> list[tuple[Path, Path]]:
    selected: list[tuple[Path, Path]] = []
    for name in ROOT_FILES:
        path = root / name
        if not path.is_file():
            raise ValueError(f"Required release file is missing: {name}")
        selected.append((path, Path(name)))
    installer = root / "tools" / "install.py"
    if not installer.is_file():
        raise ValueError("Required release file is missing: tools/install.py")
    selected.append((installer, Path("tools/install.py")))
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("This package contains no skill entrypoints.")
    for skill in skills:
        for path in sorted(skill.parent.rglob("*")):
            relative = path.relative_to(root)
            if path.is_symlink():
                raise ValueError(f"Unexpected symbolic link: {relative.as_posix()}")
            if not path.is_file() or any(part in SKIP_DIRECTORIES for part in relative.parts):
                continue
            if path.name in SKIP_NAMES or path.suffix in SKIP_SUFFIXES:
                continue
            selected.append((path, relative))
    return selected


def write_archive(output: Path, version: str, files: list[tuple[Path, Path]]) -> None:
    prefix = f"AntiRLHF-{version}"
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.with_name(output.name + ".partial")
    try:
        with zipfile.ZipFile(partial, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for source, relative in files:
                archive.write(source, arcname=f"{prefix}/{relative.as_posix()}")
        partial.replace(output)
    except Exception:
        partial.unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Release zip path. Defaults to dist/AntiRLHF-<version>.zip")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        version = version_text(root)
        files = package_files(root)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Release stopped: {exc}", file=sys.stderr)
        return 1
    output = args.output.expanduser().resolve() if args.output else (root / "dist" / f"AntiRLHF-{version}.zip").resolve()
    if output.suffix.lower() != ".zip":
        parser.error("The release archive must be a .zip file.")
    dist = (root / "dist").resolve()
    inside_repo = output == root or root in output.parents
    inside_dist = output == dist or dist in output.parents
    if inside_repo and not inside_dist:
        parser.error("Write the archive to dist/ or outside this repository.")
    try:
        write_archive(output, version, files)
    except OSError as exc:
        print(f"Release stopped: {exc}", file=sys.stderr)
        return 1
    skills = sum(
        1
        for _, relative in files
        if len(relative.parts) == 3 and relative.parts[0] == "skills" and relative.name == "SKILL.md"
    )
    print(f"Created {output} ({len(files)} files, {skills} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
