# Selecting libraries, interfaces, and mechanisms

For a design or technology choice, inspect the current project's standard capabilities and installed dependencies first. Consult maintained upstream APIs and implementation when a specific library's actual semantics control the design. Compare a small number of materially different choices by ownership, lifecycle, runtime support, resource cost and future change coupling.

Choose one state and mutation owner for each business invariant. Keep adapters at actual boundaries such as multiple public protocols or external provider semantics. Where the project can replace an internal contract in one authorized change, migrate callers and delete the obsolete path; do not produce permanent old/new dual tracks.

Generic parsers, cryptographic primitives, protocols, migration engines and durable storage mechanics belong to suitable maintained libraries when they meet the requirements. The project should own its unique domain semantics, not reimplement generic machinery. Record the decision and the remaining condition that would genuinely reverse it, then deliver the chosen architecture or implementable specification.
