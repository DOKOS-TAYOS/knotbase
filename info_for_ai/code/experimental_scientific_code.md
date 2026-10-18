# Scientific experiment code minimalism

## Activation

Load this module only when generated or modified code is scientific or research code whose primary purpose is to run, inspect, or reproduce experiments rather than serve as production or application software.

## Contract

**Invariant:** Use the smallest implementation structure that correctly performs the experiment and its required verification.

- Optimize for legibility of the algorithm, data construction, numerical procedure, and experiment flow. Prefer direct functions, small modules or scripts, plain data structures, and explicit transformations.
- Do not introduce speculative or general-purpose infrastructure such as dataclasses, class hierarchies, factories, registries, dependency injection, service or repository layers, plugin systems, configuration frameworks, wrapper layers, elaborate CLIs, extensibility mechanisms, or generalized APIs unless they are concretely required by the current experiment, an existing repository contract, or an explicit user request.
- Add an abstraction only when it demonstrably reduces complexity in the current experimental code, removes real duplication, supports multiple required experiment variants, or is necessary for correctness, reproducibility, or validation.
- Within the changed surface, omit newly introduced helpers, classes, configuration layers, or indirection that can be removed without reducing correctness, reproducibility, testability, or required reuse. Do not use this rule to clean up unrelated existing architecture.
- This minimalism does not waive repository contracts, numerical correctness, reproducibility, validation, typing, or testing requirements. For application, production, or reusable product software, use architecture appropriate to that software instead of forcing experimental minimalism.
