# Change impact, parallel consumers, and complete removal

Use when a change affects a shared contract, a generated artifact, an indirect consumer, or a concept being removed. Start from the real changed behavior and follow the paths that can still observe the old behavior.

## Follow the impact chain

Begin at the changed definition and nearby uses. Expand when there is evidence of public exports, callers, registries, dependency injection, configuration keys, packaging manifests, derived files, or multiple entrypoints sharing one business invariant. Include dynamically registered and discovered consumers when their registry is part of the actual path.

The stopping condition is that the identified consumers and externally visible obligations of the affected behavior have been handled. A repository-wide keyword sweep can help locate residual names, but a matching word alone does not create a modification requirement. Treat a user-named file as a locator; honor an explicit editing-scope boundary as an authority boundary.

## Repair shared causes

When single-item and batch entrypoints share an expiry rule, inspect the same equality boundary in both. When a code generator emits a broken artifact, repair the canonical source and regenerate the affected outputs. When two implementations own one normalization policy, move it to its responsible owner instead of patching both branches indefinitely.

## Finish a deletion

For an approved complete removal, track the concept through implementation, aliases, names, registration, CLI, environment variables, tests, fixtures, examples, generated output, documentation, and packaged entrypoints that actually refer to it. Remove the obsolete support machinery together with the implementation. Update current documentation directly instead of leaving notices that commemorate the deleted option. Preserve genuine historical records in their own archive.

Verify retained user behavior and the actual registration/build/export paths that changed. An old name appearing in a release history or a research archive is not a live consumer. Preserve compatibility only when a real public contract, active data, or rollout needs a transition.

## Complete the original request

Before delivery inspect the whole change, not only the files from an initial plan. Resolve issues necessary for the authorized outcome; place unrelated findings with specific locations in the appropriate later-work channel. Do not manufacture a change just to fill a planned file list.
