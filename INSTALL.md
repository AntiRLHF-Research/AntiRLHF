# Experimental use

[中文](INSTALL.zh-CN.md)

This repository is not installed into a personal daily environment. `scripts/install.py` is only for the task environment chosen by the experiment runner.

The experiment runner reads the Constitution and five core skills from the repository root, freezes them into a batch, and places them in the task environment:

- Condition C: install them so the host can discover the skills. The user request does not name AntiRLHF. Add `project-workflows` only when the task explicitly asks for setup, CI, or release.
- Condition B: generate static rule text from the same files and supply it with the request.
- Condition A: install nothing from this repository.

Link checks and packaging do not install anything into a personal environment:

```bash
python scripts/validate.py
python scripts/package_skills.py --with-project-workflows --out dist/AntiRLHF-skills-full.zip
```

`docs/` and `archive/` do not enter the subject environment.

A freeze records `.version`, the Git commit, and file digests. A frozen batch does not pick up later edits.
