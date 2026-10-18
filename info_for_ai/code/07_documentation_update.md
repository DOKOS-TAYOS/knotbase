# Repository documentation update

## Activation

Use this module when creating, materially changing, stabilizing, or preparing a repository for publication. The goal is for users and maintainers to understand and operate it without superfluous documentation.

## Minimum coverage

Check and update the following, reusing the existing structure when reasonable:

1. **What it is and how to start:** purpose, intended audience, scope and limits, requirements, installation, and quick start. For scientific experiments or papers, include the exact commands, data, seeds, environment, and order needed for reproduction.
2. **How to use it:** features, public API or CLI, configuration, inputs and outputs, complete examples, and common errors.
3. **How to maintain it:** operational architecture, testing, quality, debugging, versions, deployment or packaging when applicable, and what to inspect when something fails or changes.
4. **Algorithms:** algorithms, assumptions, complexity, limitations, references, and numerical or data decisions that affect results.
5. **Repository map:** the architecture and relevant directories and files needed to locate code manually or with AI. Do not enumerate generated artifacts, caches, or trivial details.

## Procedure

1. Inventory existing documentation, entry points, APIs, tests, configuration, and user flows. Identify gaps and contradictions.
2. Choose the most natural location: README for quick start, `docs/` for extensive material, and references near code when they reduce ambiguity. Do not create a file merely to satisfy a list when a clear section in an existing document is enough.
3. Write copyable commands and run them or mark them explicitly as unverified. Do not invent results, datasets, or performance claims.
4. Keep links, file names, APIs, and examples synchronized with code and manifests.
5. Finish with a coverage matrix showing where each minimum item is documented and what remains pending.
