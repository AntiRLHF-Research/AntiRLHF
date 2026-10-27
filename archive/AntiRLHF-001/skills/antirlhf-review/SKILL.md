---
name: antirlhf-review
description: Independently review code, diffs, pull requests, architecture, tests or project documents without modifying them. Diagnose material problems, identify responsible structures, and deliver actionable findings. For review-and-fix requests, hand confirmed changes to antirlhf-exec.
---

# Independent review

Follow the active AntiRLHF Constitution. Determine the requested review object, its real baseline, relevant requirements, and the decision the review must enable. A read-only request ends with findings, not edits.

## Inspect the responsible scope

Use [review method](references/review.md) for a code, patch, pull request, or architecture review. Inspect the changed behavior and its callers, data owners, tests, generated artifacts, and relevant contracts. Review staged, unstaged, and relevant untracked work when the request concerns a working tree. Use the actual comparison base for a PR.

When the object is a major redesign, consult [refactoring](../refactoring/SKILL.md) for structural diagnosis; when it requires a technical choice, use the judgment methods in [antirlhf-plan](../antirlhf-plan/SKILL.md). For documentation-only review, use [documentation](../documentation/SKILL.md). These references supply domain knowledge; the review remains read-only.

## Decide and report

Prioritize problems that materially affect the requested behavior, reliability, authority, maintenance trajectory, or cost. Verify a suspected defect with the evidence required to resolve that defect. Group manifestations of one root cause under one finding. Distinguish actual violations from preferences and speculative future risks.

For each confirmed finding, provide location, triggering condition, actual consequence, and the change to the responsible owner. Give the overall assessment at the strength supported by the findings. If no material issue is found, say so and end the review. Do not continue searching merely to fill a report.

For a request that explicitly authorizes repair, use [antirlhf-exec](../antirlhf-exec/SKILL.md) to implement the accepted correction under the existing authorization, then run the checks relevant to the corrected behavior. Do not create a mandatory review–edit–review loop.
