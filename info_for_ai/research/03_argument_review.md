# Argument and proof review

## Activation

Use this module to rigorously evaluate an argument, calculation, or proof supplied by the user. The priority is to locate the first invalid step, not merely state that the conclusion is wrong.

## Method

1. Restate the thesis, definitions, assumptions, and conclusion briefly. Identify ambiguity that prevents a validity decision.
2. Check every inference, including variable domains, quantifiers, dimensions, existence conditions, exchanged operation order, theorem use, and boundary cases.
3. Classify the result as correct, correct under explicit conditions, incomplete, partially incorrect, or incorrect. A plausible conclusion does not validate its argument.
4. If it fails, identify the first unjustified step and explain why; give a counterexample when that is the clearest demonstration.
5. If repair is possible, supply the missing assumption, lemma, calculation, or case split and show where it belongs. Otherwise explain what must be replaced.
6. When a correct presentation still needs explicit matrices, operators, indices, or bases—as in linear algebra, quantum theory, or tensor methods—provide the minimum necessary formulation.

## Output

- **Verdict:** classification and a one-sentence scope.
- **Step-by-step review:** each material step and its justification or defect.
- **Correction or completion:** repaired version, missing lemma, or counterexample.
- **Assumptions and limits:** necessary conditions and what remains unproved.
