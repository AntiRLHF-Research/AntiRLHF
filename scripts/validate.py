#!/usr/bin/env python3
"""Validate the AntiRLHF source's installable Skill relationships."""
from __future__ import annotations
from pathlib import Path
from package_skills import staged_files

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    for optional in (False, True):
        files = staged_files(root, optional)
        print(f"{'Full' if optional else 'Core'} bundle: {len(files)} files, references verified")
