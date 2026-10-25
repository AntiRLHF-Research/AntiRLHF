# AntiRLHF Index

[中文](INDEX.zh-CN.md)

AntiRLHF combines a persistent Constitution with five core Skills and one optional project-workflow Skill. Start with the [introduction](README.en.md), then [install the bundle](docs/install-skills.md).

## Structure

| Entry                                          | Role                                                                                |
| ---------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Constitution](CONSTITUTION.md)                | Shared principles, kept in persistent user instructions.                            |
| [Plan](skills/antirlhf-plan/SKILL.md)          | Research, judgment, architecture, and specifications.                               |
| [Exec](skills/antirlhf-exec/SKILL.md)          | Implementation, debugging, verification, and delivery.                              |
| [Refactoring](skills/refactoring/SKILL.md)     | Responsibility boundaries, data flow, structural simplification, and test redesign. |
| [Documentation](skills/documentation/SKILL.md) | Reader-facing writing, documentation structure, and language/navigation checks.     |
| [Bundle version](.version)                     | Version shared by the integrated Skills.                                            |

Plan and Exec load their own `references/` by task. Refactoring and Documentation provide focused task methods. Documentation owns the reusable [prose scanner](skills/documentation/scripts/check/governance_prose.py), [navigation checker](skills/documentation/scripts/check/doc_graph.py), and [scanner configuration](skills/documentation/scripts/.config/scanner.toml).

## Additional skills and installation

- [Review](skills/antirlhf-review/SKILL.md): independent read-only diagnosis with actionable findings.
- [Project Workflows](skills/project-workflows/SKILL.md): optional setup, CI and release workflows.
- [Skill architecture](docs/skill-architecture.md): direct roles, specialist methods, and source ownership.
- [Installation](docs/install-skills.md): standalone packaging and installation.

## Background

- [Research archive](docs/README.en.md): field observations, behavioral hypotheses, prompt strategies, and source notes.
- [Archive](archive/README.en.md): historical JDD, TED, and COST documents.

Packaging and installation are controlled by this repository's `scripts/` directory.

## Navigation

- [Introduction](README.en.md)
- [Installation](docs/install-skills.md)
- [AntiRLHF introduction](README.en.md)
- [Research notes](docs/README.en.md)
