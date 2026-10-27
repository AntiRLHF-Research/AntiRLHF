---
name: project-workflows
description: Implement an explicitly requested repository setup, CI pipeline, release preparation, publication, or skill installation workflow. Use existing project and platform facilities; do not load for unrelated coding tasks.
---

# Project workflows

Follow the active AntiRLHF Constitution and the actual project requirements. Choose one method according to the user's authorized outcome:

- [Setup and skill integration](references/setup.md) for installation, project entrypoints, or maintenance of agent instructions.
- [CI](references/ci.md) for workflow and required-check changes.
- [Release](references/release.md) for versioning, changelog, packaging, deployment, and publication.

Read the relevant existing platform configuration and commands. Implement only the lifecycle the user requested. For significant software changes use [antirlhf-exec](../antirlhf-exec/SKILL.md), and use [documentation](../documentation/SKILL.md) for authored documentation. Review third-party credentials, public effects, and current user data at their actual trust boundaries.

Installations should make the selected Skills discoverable to the target harness; a successful copy is not sufficient when referenced material cannot be loaded. CI must exercise the project's real build and test paths. Publication must deliver the requested version and actual assets, or state a blocking issue that requires a user decision.

Do not make setup, CI, a review gate, or a release plan prerequisites for a normal implementation task unless an existing project contract requires them.
