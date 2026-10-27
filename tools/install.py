#!/usr/bin/env python3
"""Install the skill set and merge the managed constitution into an instruction file."""
from __future__ import annotations

import argparse
import importlib.util
import os
import re
import shutil
import sys
from pathlib import Path


BEGIN = "<!-- BEGIN_AntiRLHF_Constitution -->"
END = "<!-- END_AntiRLHF_Constitution -->"


def merge_constitution(existing: str, constitution: str) -> str:
    if (BEGIN in existing) != (END in existing):
        raise ValueError("Incomplete AntiRLHF managed block")
    block = f"{BEGIN}\n{constitution.rstrip()}\n{END}"
    if BEGIN in existing:
        start = existing.index(BEGIN)
        end = existing.index(END, start) + len(END)
        return existing[:start] + block + existing[end:]
    return block + "\n\n" + existing


def waiver_pattern(source: Path) -> re.Pattern[str]:
    path = source / "skills/direct-writing/scripts/check/governance_prose.py"
    spec = importlib.util.spec_from_file_location("antirlhf_install_prose", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Waiver syntax cannot be loaded: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    sys.dont_write_bytecode = True
    spec.loader.exec_module(module)
    pattern = getattr(module, "WAIVER_RE", None)
    if not isinstance(pattern, re.Pattern):
        raise RuntimeError(f"Waiver syntax is missing: {path}")
    return pattern


def remove_waivers_from_line(body: str, pattern: re.Pattern[str]) -> str | None:
    matches = list(pattern.finditer(body))
    if not matches:
        return body
    pieces: list[str] = []
    cursor = 0
    for match in matches:
        pieces.append(body[cursor:match.start()])
        pieces.append("\ue000")
        cursor = match.end()
    pieces.append(body[cursor:])
    cleaned = "".join(pieces)
    result: list[str] = []
    index = 0
    while index < len(cleaned):
        if cleaned[index] != "\ue000":
            result.append(cleaned[index])
            index += 1
            continue
        had_space = False
        while result and result[-1] in " \t":
            result.pop()
            had_space = True
        index += 1
        while index < len(cleaned) and cleaned[index] in " \t":
            had_space = True
            index += 1
        left = bool(result)
        right = index < len(cleaned) and cleaned[index] != "\ue000"
        if left and right and had_space:
            result.append(" ")
    text = "".join(result)
    if not text.strip():
        return None
    return text


def strip_waivers(text: str, pattern: re.Pattern[str]) -> str:
    if pattern.search(text) is None:
        return text
    rewritten: list[str] = []
    for line in text.splitlines(keepends=True):
        ending = ""
        body = line
        for suffix in ("\r\n", "\n", "\r"):
            if body.endswith(suffix):
                body = body[: -len(suffix)]
                ending = suffix
                break
        cleaned = remove_waivers_from_line(body, pattern)
        if cleaned is None:
            continue
        rewritten.append(line if cleaned == body else cleaned + ending)
    return "".join(rewritten)


def strip_installed_waivers(root: Path, pattern: re.Pattern[str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        cleaned = strip_waivers(text, pattern)
        if cleaned != text:
            path.write_bytes(cleaned.encode("utf-8"))


def personal_targets(home: Path) -> list[tuple[Path, Path]]:
    """Pair each installed harness with the skills directory and instruction file it already uses."""
    codex_home = Path(os.environ["CODEX_HOME"]).expanduser() if os.environ.get("CODEX_HOME") else home / ".codex"
    claude_home = Path(os.environ["CLAUDE_CONFIG_DIR"]).expanduser() if os.environ.get("CLAUDE_CONFIG_DIR") else home / ".claude"
    agents_skills = home / ".agents" / "skills"
    codex_skills = codex_home / "skills"
    claude_present = claude_home.exists()
    codex_present = codex_home.exists() or (home / ".agents").exists() or not claude_present
    targets: list[tuple[Path, Path]] = []
    if codex_present:
        skills = agents_skills if agents_skills.is_dir() or not codex_skills.is_dir() else codex_skills
        targets.append((skills, codex_home / "AGENTS.md"))
    if claude_present:
        targets.append((claude_home / "skills", claude_home / "CLAUDE.md"))
    return targets


def skill_sources(source: Path) -> list[Path]:
    skills = sorted(path.parent for path in (source / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("This package contains no skill entrypoints.")
    return skills


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, help="Skill directory. Omit to use the existing personal harness.")
    parser.add_argument("--instruction", type=Path, help="Persistent instruction file. Omit together with --target.")
    args = parser.parse_args()
    if (args.target is None) != (args.instruction is None):
        parser.error("Pass both --target and --instruction, or neither.")
    source = Path(__file__).resolve().parents[1]
    try:
        sources = skill_sources(source)
    except ValueError as exc:
        parser.error(str(exc))
    if args.target is None:
        targets = personal_targets(Path.home())
    else:
        targets = [(args.target.expanduser().absolute(), args.instruction.expanduser().absolute())]
    constitution = source / "CONSTITUTION.zh-CN.md"
    if not constitution.is_file():
        parser.error("The constitution file is missing.")
    pattern = waiver_pattern(source)
    prepared: list[tuple[Path, Path, str]] = []
    for target, instructions in targets:
        if target.is_symlink() or any(parent.is_symlink() for parent in target.parents):
            parser.error(f"Choose a skill directory without symbolic-link path components: {target}")
        if instructions.is_symlink() or any(parent.is_symlink() for parent in instructions.parents):
            parser.error(f"Choose an instructions file without symbolic-link path components: {instructions}")
        resolved = target.resolve()
        scratch = (source / "temp").resolve()
        in_package = resolved == source or source in resolved.parents
        in_scratch = resolved == scratch or scratch in resolved.parents
        if in_package and not in_scratch:
            parser.error("Choose a skill directory outside this source package.")
        if target.exists() and not target.is_dir():
            parser.error(f"The skill path exists and is not a directory: {target}")
        if instructions.exists() and not instructions.is_file():
            parser.error(f"The instructions path exists and is not a file: {instructions}")
        if instructions.resolve() == constitution.resolve():
            parser.error("The instructions file cannot replace the source constitution.")
        for src in sources:
            destination = target / src.name
            if destination.is_symlink():
                parser.error(f"Refusing to replace a symbolic link: {destination}")
            if destination.exists() and not destination.is_dir():
                parser.error(f"The skill destination exists and is not a directory: {destination}")
            if any(path.is_symlink() for path in src.rglob("*")):
                parser.error(f"Unexpected symbolic link inside package skill: {src.name}")
        existing = instructions.read_text(encoding="utf-8") if instructions.is_file() else ""
        try:
            merged = merge_constitution(existing, strip_waivers(constitution.read_text(encoding="utf-8"), pattern))
        except ValueError as exc:
            parser.error(f"{instructions}: {exc}")
        prepared.append((target, instructions, merged))
    for target, instructions, merged in prepared:
        try:
            target.mkdir(parents=True, exist_ok=True)
            for src in sources:
                destination = target / src.name
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.copytree(src, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                strip_installed_waivers(destination, pattern)
            instructions.parent.mkdir(parents=True, exist_ok=True)
            instructions.write_text(merged, encoding="utf-8")
        except OSError as exc:
            print(f"Installation stopped: {exc}. Already copied directories remain at {target}.", file=sys.stderr)
            return 1
        print(f"Installed {len(sources)} skills into {target}")
        print(f"Managed constitution: {instructions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
