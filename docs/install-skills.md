# Installation and packaging

Python 3.11+ is required. These commands run from the **modified AntiRLHF repository root**. Skills in the same installation share sibling-relative references.

Validate source references and entries:

```bash
python scripts/validate.py
```

Build a portable ZIP containing the five core Skills, Constitution and installation notes:

```bash
python scripts/package_skills.py --out dist/AntiRLHF-skills.zip
```

Include the optional project setup / CI / release Skill:

```bash
python scripts/package_skills.py --with-project-workflows --out dist/AntiRLHF-skills-full.zip
```

For a chosen harness, specify its actual skill directory and persistent instruction file. The installer preserves unrelated instruction text and installed Skills:

```bash
python scripts/install.py --skills-dir ~/.codex/skills --instructions-file ~/.codex/AGENTS.md --dry-run
python scripts/install.py --skills-dir ~/.codex/skills --instructions-file ~/.codex/AGENTS.md
```

Use `--with-project-workflows` when that optional Skill is needed. Use `--replace` to replace existing matching Skills. Each replaced directory is renamed to `<name>.backup` instead of being deleted; an existing backup must be resolved before another replacement. Do not install individual core Skills without their siblings if they contain relative links to each other.

A ZIP created by `package_skills.py` can also be extracted into a harness's skill root manually. Install the bundled Constitution in the harness's persistent custom instruction location according to its supported mechanism. Use the actual harness documentation to determine the location and confirm it discovers and reads the Skills.

The `project-workflows` entry is optional to invoke and optional to distribute. Ordinary code work uses Exec, not a project setup workflow.
