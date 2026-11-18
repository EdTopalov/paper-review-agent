# Paper-selection pilot

The scored [selection benchmark](benchmark-protocol.md) contains 12 synthetic
cases: four candidate sets in three orders. Each brief defines eligibility and
preferences; deterministic reference choices include abstention. Accuracy is
acceptable choices divided by all attempts, including failures. This track uses
the common benchmark controllers, 20 reads and 46 ordinary decisions plus one
forced final call at exhaustion (47 maximum). Ordinary citations gate submission;
forced non-null public answers complete with separate citation diagnostics.
Null, missing/invalid output and transport errors remain failures.

`paper-review select` is a separate workflow for local PDFs or paper snapshots.
It reviews each candidate independently with the requested agent, then makes one
chooser call over the brief, final reviews, citation diagnostics and failures.
Candidate reviews default to five reads and 16 ordinary decisions plus one forced
final call if needed. The chooser itself makes one comparative decision.
The chooser receives no additional paper text. All reviews stay in its context;
there is no persistent memory between runs. At least two reviews must complete,
and the decision must compare the chosen paper against every other completed candidate.

After [installation](../README.md#installation) with `requirements-m3.txt` and
`.env`, run this paid development example; replace its fixtures with real PDFs:

```shell
paper-review select data/dev/toy.json data/dev/selection-negative-result.json --variant deliberative_review --model gpt-6-luna --brief "Discuss experimental design, uncertainty, and useful follow-up studies" --out runs/scratch/selection-dev
```

| Output | Contents |
|---|---|
| `README.md` | Choice, comparisons, uncertainties and total usage. |
| `selection.json` | Structured decision, candidate outcomes and aggregate accounting. |
| `selection-trace.jsonl` | Chooser requests, responses and diagnostics, labelled by variant. |
| `reviews/<candidate-id>/` | Each candidate's ordinary review report and trace. |

Total API calls, tokens, estimated USD and elapsed time include all candidate
reviews and the chooser, including failed reviews, retries and forced calls. Unknown costs
remain unknown. The output preserves tied alternatives and failed candidates.

The benchmark measures compliance with an explicit synthetic policy. The CLI
pilot tests whether independently generated reviews support an auditable choice;
neither supplies human reading-club preference labels. Comparing a bounded
shortlist with all-review context remains a separate memory experiment.
