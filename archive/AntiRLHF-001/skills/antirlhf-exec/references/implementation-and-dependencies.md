# Implement at the behavioral owner and reuse supported machinery

For a feature or change, trace the real user-facing entrypoint to the owner of state, policies and external effects. Find all consumers that rely on the same contract. Define the required input, operation and output, then implement that entire path. Prefer the project's existing dependencies and standard library for generic parsing, serialization, protocols, synchronization and other non-domain concerns.

Investigate a candidate third-party library's supported API, maintenance status, license, runtime fit, and relevant security properties when choosing a new dependency. Avoid creating a wrapper whose only purpose is to conceal a dependency the project is already free to use. Introduce an interface or adapter when multiple real protocols, domain boundaries or providers have distinct independent semantics.

Keep validation at trust boundaries. Let an internal invariant have one responsible owner. External input, network and file operations require meaningful failure behavior; retry only for an actual recoverable class of failures and with the appropriate idempotence and stop condition. Keep error messages useful for diagnosing the failed operation. Do not bury failure behind catch-all success values.

Run a check that distinguishes the required behavior from an incorrect implementation. When public installation, CLI, API, or generated output is part of the request, exercise that actual consumer path. Update callers, maintained usage examples and obsolete tests as the contract changes. Stop once the requested capability and its required checks work.
