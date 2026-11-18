# Controlled scientific-appraisal pairs

These are original hypothetical reports with programmatically calculated reference
labels. They are not real papers or human-labelled review-quality examples.
Each pair changes exactly one decisive source block while keeping its assessment
statement fixed. Both conditions remain in the same split.

There are **4 development pairs (8 cases)** and **12 test pairs (24 cases)**.
Development families concern confidence intervals and total cost. Held-out
families concern evaluation independence, language scope, seed aggregation, and
quantitative counterevidence in an appendix. Entire scientific families are
separated between development and test. Labels are `supported`, `contradicted`,
or `insufficient`; a nonsignificant outcome does not prove a negative effect.
Language-scope claims concern the method's accuracy advantage in three languages.
An advantage measured only in English leaves the other languages unresolved;
it does not establish that the advantage is absent in those languages.

`inputs/` contains only the supplied report, statement, and common task
instructions. `references/` contains the separate answer key, decisive evidence
block IDs, study facts, and pair/family identities. `manifest.jsonl` binds every
input and reference to SHA-256 hashes. Agents must receive only public inputs.

Regenerate without model calls:

```shell
python scripts/prepare_controlled_benchmark.py --out runs/scratch/rebuilt-controlled
```

The generator is deterministic and refuses to replace a different frozen input or
reference. Text locations use block IDs, not PDF page numbers. Report per-case
verdict accuracy and pair accuracy (both cases in a pair correct), with failures
in the denominator. The 24 test cases are 12 pairs in four scientific families;
they are not 24 independent real papers. A blanket criticism strategy fails the
sound conditions. These cases measure bounded evidence interpretation, not
overall scientific merit or reading-club preference.

Original reports and structured records are dedicated to the public domain under
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). See `source.json`
for the generator version, counts, and manifest hash.
