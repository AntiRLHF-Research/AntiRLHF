#!/usr/bin/env python3
"""Validate native AntiRLHF Skills and build a relocatable installation ZIP."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import sys
import zipfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CORE = ("antirlhf-plan", "antirlhf-exec", "antirlhf-review", "refactoring", "documentation")
OPTIONAL = ("project-workflows",)
SKIP_NAMES = {"__pycache__", ".pytest_cache", ".DS_Store", ".git", "dist", "tests", ".venv"}
SKIP_EXTENSIONS = {".pyc", ".pyo"}
FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)|!\[[^\]\n]*\]\(([^)]+)\)")


class PackageError(ValueError):
    pass


def names(include_project: bool) -> tuple[str, ...]:
    return CORE + OPTIONAL if include_project else CORE


def source_files(root: Path, include_project: bool):
    for name in names(include_project):
        skill = root / "skills" / name
        if not (skill / "SKILL.md").is_file():
            raise PackageError(f"missing Skill entry: {skill / 'SKILL.md'}")
        for p in sorted(skill.rglob("*")):
            if p.is_file() and not any(x in SKIP_NAMES for x in p.relative_to(skill).parts) and p.suffix not in SKIP_EXTENSIONS:
                yield p, Path(name) / p.relative_to(skill)


def check_frontmatter(text: str, expected: str, path: Path) -> None:
    m = FRONT.match(text)
    if not m:
        raise PackageError(f"missing frontmatter: {path}")
    values = dict((k.strip(), v.strip().strip('\"\'')) for k, v in
                  (line.split(":", 1) for line in m[1].splitlines() if ":" in line))
    if values.get("name") != expected or not values.get("description"):
        raise PackageError(f"invalid Skill identity or description: {path}")


def markdown_links(content: str):
    in_fence = False
    visible = []
    for line in content.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if not in_fence:
            visible.append(re.sub(r"`[^`\n]*`", "", line))
    for m in LINK.finditer("\n".join(visible)):
        yield (m.group(1) or m.group(2)).split(maxsplit=1)[0].strip("<>")


def validate_files(files: dict[Path, bytes]) -> None:
    for entry, raw in files.items():
        if entry.suffix != ".md":
            continue
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError as ex:
            raise PackageError(f"invalid UTF-8: {entry}") from ex
        if entry.name in {"SKILL.md", "SKILL.zh-CN.md"} and len(entry.parts) == 2:
            check_frontmatter(content, entry.parts[0], entry)
        for url in markdown_links(content):
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = Path(entry.parent, unquote(parts.path))
            # Resolve traversal against the logical zip directory, not the host FS.
            import posixpath
            resolved = Path(posixpath.normpath(target.as_posix()))
            if resolved not in files:
                raise PackageError(f"broken Skill link {entry} -> {url} (expected {resolved})")


def staged_files(root: Path, include_project: bool) -> dict[Path, bytes]:
    contents = {dst: src.read_bytes() for src, dst in source_files(root, include_project)}
    contents[Path("CONSTITUTION.md")] = (root / "CONSTITUTION.md").read_bytes()
    contents[Path("CONSTITUTION.zh-CN.md")] = (root / "CONSTITUTION.zh-CN.md").read_bytes()
    contents[Path("VERSION")] = (root / ".version").read_bytes()
    contents[Path("INSTALL.md")] = (root / "docs" / "install-skills.md").read_bytes()
    validate_files(contents)
    return contents


def make_archive(root: Path, output: Path, include_project: bool) -> str:
    files = staged_files(root, include_project)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, payload in sorted(files.items()):
            info = zipfile.ZipInfo(name.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, payload, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    sha = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(f"{sha}  {output.name}\n", encoding="utf-8")
    return sha


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--out", type=Path, default=ROOT / "dist" / "AntiRLHF-skills.zip")
    ap.add_argument("--with-project-workflows", action="store_true", help="include optional CI/release Skill")
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.check_only:
            files = staged_files(args.root, args.with_project_workflows)
            print(f"Checked {len(files)} packaged files across {len(names(args.with_project_workflows))} Skills")
        else:
            sha = make_archive(args.root, args.out, args.with_project_workflows)
            print(f"Created {args.out} SHA256={sha}")
    except (OSError, PackageError) as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
