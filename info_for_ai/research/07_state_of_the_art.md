# State of the art (SOTA)

## Activation

Use this module to identify the most competitive techniques, algorithms, and work in a specific line and compare an existing or proposed solution with the current frontier. Also apply `01_deep_research.md` for its search design, coverage disclosure, and thematic-synthesis method. Reuse its standalone output structure only where it is applicable; do not emit its optional reading path, additional-sources section, importance labels, or research-possibility sections merely because this SOTA module depends on its method.

## Additional SOTA method

1. Define comparison conditions, metrics, datasets, resource constraints, and what "best" means. Never combine results from incompatible protocols into a single ranking.
2. For each candidate, extract its method, assumptions, experimental environment, benchmarks, metrics, computational cost, reproducibility, and evidence of generalization.
3. Contrast performance claims with reproduction studies or independent evaluations when available.
4. Separate consolidated results from isolated records, recent preprints, and improvements that depend on incomparable resources.

## Additional SOTA output

Within the applicable deep-research structure:

- In the **summary**, state which methods lead under which conditions and classify the field as emerging, rapidly advancing, consolidated, or near saturation, with justification.
- For each method or family, add **advantages** supported by evidence and **limitations** covering assumptions, failures, cost, reproducibility, missing comparisons, and conditions where it is not competitive.
- Include benchmarks, repositories, implementations, challenges, and reviews needed for reproduction or context when they materially support the comparison; use a separate **additional sources** section only when that section is useful.
- Add **improvement opportunities**: unresolved weaknesses, missing comparisons, practical limits, scientifically or industrially relevant questions, and concrete evaluations that could demonstrate a real advance.
