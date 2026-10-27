# Full removal, active consumers, and migration

Start from the future architecture and its preserved external behavior. Use the real dependency graph to identify the owners, producers and consumers that must change together. For a feature being retired, inspect aliases, registries, package exports, dynamic discovery, configuration, documentation, generators, fixtures and tests attached to that retired concept. Remove support code and test machinery that no longer serves an active contract.

Distinguish a live external protocol, deployed reader, stored user data or phased rollout from an unused internal legacy path. Where active data or rolling deployment requires a transition, use the existing migration infrastructure with an explicit conversion order and recovery behavior. Otherwise replace the obsolete internal representation and affected consumers directly.

Rebuild verification around the new owner's operations and independently failing behaviors. Transfer meaningful old regression cases, then delete retired test groups and dedicated mocks together. Inspect production code, tests, adapters, scripts, and workflows when simplification is an explicit goal; avoid replacing one maintenance framework with another of equivalent size.

Exercise real entrypoints after replacement. The final result should consist of the new authoritative path and only the boundaries currently required by real consumers.
