# Review the outcome and its owner

## Recover the actual comparison

For a diff or PR, establish the user's requested outcome, the merge base, edited files and affected consumers. For a module or repository audit, select representative user-facing paths and follow their real dependencies. Use existing static tools, tests and documentation where they answer the issue; isolate any checks that would otherwise mutate the reviewed workspace.

## Find structural and behavioral defects

Start with behavior and responsibility, then assess code paths, state transitions, data ownership, tests, and documentation. Look for an incomplete capability, a fix applied at the wrong owner, duplicated authority, unnecessary compatibility, a stale generated consumer, or a test that protects an obsolete implementation. Explicitly preserve legitimate requirements such as public consumers, persistent data, a rollout dependency, and independently failing contracts.

Investigate a possible issue to the point where its triggering input and consequence are actionable. A long list of hypothetical edge cases is less useful than a confirmed mismatch between the actual requirement and the implemented path.

## Finish the review

Report the most consequential findings first. For each: exact place, relevant trigger, consequence, and direct corrective action. Consolidate related symptoms into one architectural finding when one structural change resolves them. If the reviewed solution already satisfies the user goal, report that result directly. Only move to implementation when the request authorizes it.
