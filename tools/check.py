#!/usr/bin/env python3
"""Inspect this authored package's local links, metadata and every UTF-8 file."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True


def load_scanner(root: Path):
    path = root / "skills/direct-writing/scripts/check/governance_prose.py"
    spec = importlib.util.spec_from_file_location("antirlhf_prose", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Scanner cannot be loaded: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def fence_lines(text: str) -> set[int]:
    inside: set[int] = set()
    marker = ""
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*(?:>\s*)?(`{3,}|~{3,})(.*)$", line)
        if marker:
            inside.add(number)
            if match and match[1][0] == marker[0] and len(match[1]) >= len(marker) and not match[2].strip():
                marker = ""
        elif match:
            marker = match[1]
            inside.add(number)
    return inside


# These are preserved source records, not operational instructions. Their text is
# still scanned and its hits remain visible in the report.
SOURCE_RECORDS = frozenset({
    "skills/direct-writing/references/cases/charter/AI-original.md",
    "skills/direct-writing/references/cases/charter/Revised.md",
    "skills/direct-writing/references/cases/charter/Revised-vs-AI-original.diff",
})


def package_files(root: Path):
    for directory, names, files in os.walk(root, followlinks=False):
        rel = Path(directory).resolve().relative_to(root.resolve()).as_posix()
        if rel == ".":
            rel = ""
        hidden = {".git", ".hg", ".svn", "__pycache__", "node_modules", "dist", ".venv", "venv", "archive", "temp"}
        names[:] = sorted(
            name for name in names
            if name not in hidden and not (rel == "docs" and name in {"charter", "research"})
        )
        for name in names:
            child = Path(directory) / name
            if child.is_symlink():
                yield child
        for name in sorted(files):
            yield Path(directory) / name


def is_source_record(relative: str, path: Path) -> bool:
    return relative in SOURCE_RECORDS or (
        relative.startswith("docs/authoring/upstream/")
        and (".original." in path.name or path.suffix == ".diff")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Write JSON outside the package, or print to stdout")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.expanduser().resolve() if args.output else None
    if output is not None and (output == root or root in output.parents):
        parser.error("Write the report outside the inspected package.")
    try:
        import yaml
    except ImportError:
        parser.error("Install the authoring dependency: python -m pip install -r tools/requirements.txt")
    scanner = load_scanner(root)
    config_path = root / "skills/direct-writing/scripts/.config/scanner.toml"
    config = scanner.load_config(config_path)
    files, assets, findings, intentional, waivers, errors = [], [], [], [], [], []
    skills = []
    report_note = "Regex-based language findings are listed separately from literal examples and rule definitions."
    for path in package_files(root):
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"Unexpected symlink: {rel}")
            continue
        if not path.is_file():
            continue
        raw = path.read_bytes()
        if raw.startswith(b"\x89PNG\r\n\x1a\n") or raw.startswith(b"\xff\xd8\xff"):
            kind = "png" if raw.startswith(b"\x89PNG") else "jpeg"
            assets.append({"path": rel, "bytes": len(raw), "kind": kind})
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Unrecognized non-UTF-8 file: {rel}")
            continue
        lines = text.splitlines()
        files.append({"path": rel, "bytes": len(raw), "lines": len(lines)})
        found, waived = scanner.scan_file(path, root, config)
        waivers.extend(waived)
        protected = {(f["line"], f["rule"], f["match"]) for f in found}
        for item in found:
            num = int(item["line"])
            literal = path == config_path and lines[num - 1].lstrip().startswith("regex =")
            source_quote = is_source_record(rel, path)
            if literal or source_quote:
                intentional.append({**item, "reason": "scanner pattern definition" if literal else "preserved source text or edit comparison"})
            else:
                findings.append(item)
        # A second raw pass also sees code fences, inline examples, and nonstandard text extensions.
        code = fence_lines(text) if path.suffix == ".md" else set()
        active = tuple(p for p in config.patterns if p.scope == "all" or scanner.is_ai_instruction(path))
        for pattern in active:
            for match in pattern.regex.finditer(text):
                num = text.count("\n", 0, match.start()) + 1
                if (num, pattern.key, match.group()) in protected:
                    continue
                if any(w["rule"] == pattern.key and w["line"] <= num <= w["end_line"] for w in waived):
                    continue
                if any(f["line"] <= num <= f["end_line"] and f["rule"] == pattern.key and match.group() in str(f["text"]) for f in found):
                    continue
                if lines[num - 1].lstrip().startswith("<!-- antirlhf:"):
                    continue
                item = {"path": rel, "line": num, "rule": pattern.key, "class": pattern.klass,
                        "match": match.group(), "text": lines[num - 1], "pass": "raw-text"}
                if path == config_path and lines[num - 1].lstrip().startswith("regex ="):
                    intentional.append({**item, "reason": "scanner pattern definition"})
                elif is_source_record(rel, path):
                    intentional.append({**item, "reason": "preserved source text or edit comparison"})
                else:
                    findings.append(item)
        if path.name == "SKILL.md":
            if not text.startswith("---\n") or "\n---\n" not in text[4:]:
                errors.append(f"Missing skill frontmatter: {rel}")
            else:
                front, body = text[4:].split("\n---\n", 1)
                try:
                    data = yaml.safe_load(front)
                except yaml.YAMLError as exc:
                    errors.append(f"Invalid skill metadata: {rel}: {exc}")
                    continue
                if not isinstance(data, dict):
                    errors.append(f"Invalid skill metadata: {rel}")
                    continue
                name, description = data.get("name"), data.get("description")
                if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name != path.parent.name:
                    errors.append(f"Invalid skill name: {rel}")
                if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                    errors.append(f"Invalid skill description: {rel}")
                skills.append({"name": name, "path": rel, "body_characters": len(body),
                               "references": len(list((path.parent / "references").glob("*.md")))})
        if path.suffix in {".yaml", ".yml"}:
            try:
                metadata = yaml.safe_load(text)
                if path.name == "openai.yaml" and path.parent.name == "agents":
                    interface = metadata.get("interface", {}) if isinstance(metadata, dict) else {}
                    expected = "$" + path.parent.parent.name
                    prompt = interface.get("default_prompt", "")
                    if not isinstance(prompt, str) or expected not in prompt:
                        errors.append(f"Agent prompt must reference {expected}: {rel}")
                    if not all(isinstance(interface.get(key), str) and interface[key].strip()
                               for key in ("display_name", "short_description")):
                        errors.append(f"Missing agent display metadata: {rel}")
            except yaml.YAMLError as exc:
                errors.append(f"Invalid YAML: {rel}: {exc}")
        if path.suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON: {rel}: {exc}")
        if path.suffix == ".md" and rel not in SOURCE_RECORDS:
            for number, line in enumerate(lines, 1):
                if number in code:
                    continue
                for match in re.finditer(r"\[[^\]\n]*\]\(([^\)\n]+)\)", line):
                    link = match[1].strip().split(' "', 1)[0]
                    if urlsplit(link).scheme or link.startswith("#"):
                        continue
                    target = (path.parent / unquote(link.split("#", 1)[0])).resolve()
                    if target != root and root not in target.parents:
                        errors.append(f"Link escapes package: {rel}:{number}: {link}")
                    elif not target.exists():
                        errors.append(f"Missing local link: {rel}:{number}: {link}")
    duplicates = [name for name, count in Counter(s["name"] for s in skills).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate skill names: {duplicates}")
    result = {"package": root.name, "note": report_note,
              "summary": {"files": len(files)+len(assets), "text_files_scanned": len(files), "assets": len(assets),
                          "skills": len(skills), "references": sum(s["references"] for s in skills),
                          "unresolved_language_findings": len(findings), "scoped_prose_waivers": len(waivers),
                          "intentional_literal_hits": len(intentional), "structure_errors": len(errors)},
              "source_records": sorted(SOURCE_RECORDS),
              "skills": skills, "findings": findings, "waivers": waivers,
              "intentional_literals": intentional, "errors": errors, "files": files, "assets": assets}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(json.dumps(result["summary"], ensure_ascii=False))
        print(f"Report: {output}")
    else:
        print(rendered, end="")
    return 1 if errors or findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
