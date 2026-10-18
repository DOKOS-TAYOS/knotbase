# Readable refactoring

## Activation

Use this module to improve maintainability, readability, scalability, and internal efficiency without changing features or external contracts.

## Objective and limits

- Preserve public APIs, formats, observable results, documented errors, compatibility, and performance unless explicitly authorized otherwise.
- Prefer clear names, single-responsibility units, understandable module boundaries, consistent types, visible error handling, and simple data flow.
- Avoid patterns, layers, dependencies, or abstractions that only add complexity. Do not confuse a rewrite with refactoring.

## Procedure

1. Establish a baseline: use cases, existing tests, relevant metrics or profiles, and public contracts.
2. Locate the highest cognitive costs: long functions, coupling, repetition, implicit state, ambiguous names, scattered mutation, circular dependencies, or opaque error paths.
3. Propose a small ordered plan with risks and equivalence criteria. If a prior audit is requested, use the bug-audit or dead-code-audit module first.
4. Refactor incrementally. After each meaningful unit, run tests and compare behavior or performance with the baseline when critical paths are affected.
5. Update comments and documentation that no longer describe the actual design.

## Final report

Explain what was simplified, what was preserved, affected files, tests run, metrics compared, and remaining technical debt. Present any improvement that would change behavior as a separate proposal.
