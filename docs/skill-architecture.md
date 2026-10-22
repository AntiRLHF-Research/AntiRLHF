# AntiRLHF Skill architecture

AntiRLHF keeps objective and decision principles in the persistent `CONSTITUTION.md`. Native Skills expose the actual task contract and progressively load domain methods. The harness selects an entry by the required deliverable; AntiRLHF does not add an obligatory router or supervisory review process.

| Entry | Primary deliverable | Specialist knowledge |
| --- | --- | --- |
| `antirlhf-plan` | Decision, research, architecture, implementable Spec | Architecture, judgment, research, actual library choice |
| `antirlhf-exec` | Working feature, fix, verification and delivery | Root cause, consumers, direct implementation, permissions |
| `antirlhf-review` | Independent read-only code/architecture/PR diagnosis | Material defects, actual baseline, actions at responsible owner |
| `refactoring` | Structural replacement, deletion and test restructuring | Owner and data path, active consumers and migration |
| `documentation` | Reader-facing prose and maintained documentation | Authorial voice, facts and source ownership, prose checks |
| `project-workflows` (optional) | Requested installation, CI or publication | Platform-specific project lifecycle and external effects |

The first three entries are roles defined by the requested output; Refactoring and Documentation can also be invoked directly for specialist work. `project-workflows` remains an optional independent Skill. A request may use more than one entry where the actual work spans them. There is no routine requirement to run Plan before Exec or Review after every change.

Shared principles stay in Constitution. A task technique lives with its semantic owner; other Skills link to that technique. When an implementation changes behavior that another domain owns, the executing Agent loads that related guidance at the point of need. The source is authoritative, the distribution mirrors the source Skill directories under one shared skills root, keeping relative references between sibling Skills valid.

## Source integration

The previous `ai-agent-governance` shared rules inform concrete methods here:

- Engineering selection and implementation feed Plan's technology-selection reference and Exec's implementation reference.
- Change impact, root-cause siblings, complete removal, active compatibility and verification feed Exec and Refactoring references.
- Knowledge ownership and correction cleanup feed Documentation's reference.
- Independent read-only review becomes `antirlhf-review`.
- Setup, CI and release become optional `project-workflows`.

`academic-writing` contributed the proven division between directly invocable role entrypoints, one semantic source for each rule, and links to progressively disclosed references. Its thesis-specific writing rules were not imported into generic Agent governance.

## Research status

The conceptual target remains local defensibility optimization and loss of attention to the full task objective. Skill structure is an engineering intervention. An effect on model decisions remains a research question, as described in `docs/research/`.
