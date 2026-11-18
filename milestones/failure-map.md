# Failure map through M3

This map revisits every risk in the [original proposal](M1.md#failure-map).
An observed failure is evidence that a mechanism can fail; one occurrence does
not establish its frequency. Source-checked analyses and provisional model audits
are not human quality labels.

| M1 risk | Evidence and current status | Response and next measurement |
|---|---|---|
| Abstract hype hides weak support. | Not directly measured. [F06](../data/failures/F06.json) demonstrates the related problem of turning partial evidence into a paper-wide conclusion. | Check central claims against methods/results and counterevidence; human coverage labels must inspect the full snapshot. |
| Parsing corrupts tables, formulas, or results. | Known text-only limitation. The T17 diagnostic below reproduces failed quotation repair in 3/10 native attempts; it does not demonstrate incorrect scientific conclusions. | Keep snapshots frozen; mark missing visual evidence as uncertainty and separate extraction failures from reasoning errors. |
| Rubric favors a topic or paper type. | Unmeasured. The M2 convenience sample and selected M3 assessment tasks cannot establish fairness across fields or types. | Keep task tracks separate and retain source-paper groupings. Broader human labels by field and paper type are still needed to evaluate rubric bias. |
| Scores fluctuate or inflate in weak batches. | M3 repeats agent and baseline attempts on frozen inputs and separates model identities. The T17 completed-score range alone is 0.68–0.72 across seven completions; failed attempts are excluded only from that score spread. | Report repetition variation before method gaps in the [M3 results](M3-results/README.md). Fixed-task repetitions do not resolve future provider drift or validate rating accuracy. |
| Close-score review forces changes or wastes reads. | The planned batch-level close-score review was not implemented in M2. M3 adds a selection pilot with explicit ties and abstention, but its rule-derived acceptable choices do not validate reading-club preference. | Report acceptable-choice and tie-set agreement separately; human preference labels and a controlled memory ablation remain future work. |
| Plausible assessment cites unsupported evidence. | [F01](../data/failures/F01.json) expands an interface requirement into a transfer restriction; [F06](../data/failures/F06.json) misses a quantitative follow-up. M3 adds scope and already-reported-ablation errors below, including outputs with valid quotations. | Evaluate claim scope, evidence coverage, and defect-versus-uncertainty calibration separately from citation matching. Compare the deliberative variant's planned investigation and critic with both ReAct harnesses. |
| Reference scores reproduce model biases. | M2 has no human gold scores; [F07](../data/failures/F07.json) contains a judge arithmetic contradiction. M3 uses preserved human ReviewCritique labels and QASPER answers, plus programmatic controlled/selection references; these cover narrower judgments than overall review quality. | Report expert-label agreement and controlled correctness by track. Preserve disagreements for inspection; do not treat model judgments or reading-club preference proxies as human ground truth. |

## Substantive review failures

**Unsupported extrapolation (F01, archived prototype).** The Reflexion review
turns a requirement for a termination heuristic and binary reward into a claim
that transfer is restricted. The cited statement establishes the requirement;
it does not establish how difficult transfer is. This is an interpretation error,
independent of whether the quote can be located. A qualified open question would
be defensible. Its frequency in later versions is unknown.

**Coverage-driven overgeneralization (F06, integrated M2).** The AutoGen review
describes the math comparison as qualitative after reading pages 8–10. Page 11
contains an additional 12-problem quantitative comparison. The agent next reads
pages 15–17 and later submits the broader criticism. The valid quote from page 10
does not support dismissing the whole comparison as qualitative. The follow-up
is still small, so this example does not prove that the paper merits a higher
score. It demonstrates a materially incomplete rationale.

**Judge arithmetic contradiction (F07, integrated M2).** The evidence audit says
ReAct does not improve WebShop success over Act while citing 40.0% versus 30.1%.
The frozen table agrees with those numbers and the paper explicitly describes
an improvement. Other qualifications in the audited observation can still be
debated; this contradiction alone invalidates treating the judge's reasoning as
reliable human ground truth.

## Substantive disagreements in frozen M3 tests

These examples come from the first `gpt-6-luna` test repetition. They were
inspected after the implementation was frozen and were not used to tune it.
ReviewCritique examples compare an output with the dataset's existing expert
label; they are not new independent human annotations of the generated output.

**Untested performance treated as contradicted.** On
[CB-cedf9028d20e](../runs/m3-existing-20261118-luna6/r1/core/pyagent_react-r1/CB-cedf9028d20e/trace.jsonl#L15),
PyAgent correctly reads that only English was evaluated, but labels a claim of
higher accuracy in English, German, and Spanish `contradicted`. The
[controlled reference](../data/benchmark/v1/controlled/references/CB-cedf9028d20e.json)
is `insufficient`: the report supplies no German or Spanish accuracy, so it
establishes neither improvement nor its negation there. The quotation verifies;
the error is confusing absent evidence with incompatible evidence.

**Already-reported ablation dismissed as a harmless request.** On
RC-f94db276afa4, the
[native agent](../runs/m3-existing-20261118-luna6/r1/core/agent-r1/RC-f94db276afa4/trace.jsonl#L30)
accepts a request for an input-entity-only KALM ablation after reading evidence
about the general method. The supplied paper's blocks b0032 and b0037 explicitly
describe that ablation and give its results; the
[expert reference](../data/benchmark/v1/reviewcritique/references/RC-f94db276afa4.json)
labels the comment `deficient` for neglecting it. The
[full-text baseline](../runs/m3-existing-20261118-luna6/r1/core/baseline-r1/RC-f94db276afa4/trace.jsonl#L4)
actually cites the appendix, yet also returns `reliable` because the comment is
phrased as a question. Both outputs have verified quotations. They expose two
different problems: incomplete coverage, and treating question wording as
sufficient to excuse overlooking an already-reported experiment.

**Possible explanations mistaken for deeper analysis.** On
[RC-f5097b168055](../runs/m3-existing-20261118-luna6/r1/core/baseline-r1/RC-f5097b168055/trace.jsonl#L4),
the baseline rejects a criticism that entity abstraction lacks deeper analysis
by citing possible explanations such as noisy labels and task dependence. The
review's supplied context already acknowledges those possibilities and asks
for analysis that distinguishes them. The
[expert reference](../data/benchmark/v1/reviewcritique/references/RC-f5097b168055.json)
labels this criticism `reliable`. This disagreement concerns the strength of
the evidence required for an explanation; the existence of plausible
discussion does not establish a causal account. Some quotations also fail
literal matching, which is a separate defect.

## Operational failures and frequency

[F02](../data/failures/F02.json) and [F03](../data/failures/F03.json) document wrong
pages and edited quotations in archived runs. Page-specific observations and
citation rejection address these mechanics, but later verified completion does
not establish review quality. [F04](../data/failures/F04.json) documents a literal
search query contract mismatch and a wasted read, followed by recovery.

For [F05](../data/failures/F05.json), the integrated M2 T17 run exhausts its decision
budget after four rejected submissions. The
[M3 native diagnostic](../runs/m3-t17-native-r10/README.md) repeats T17 ten times
with the frozen paper, `gpt-6-luna`, five reading actions, and eight decisions.
Seven attempts complete with verified citations; three exhaust the decision
budget (3/10). Every first submission fails citation checking, including those
that later recover. The three failed attempts have distinct final states:

| Repeat | Rejected submissions | Reading actions used / allowed | Final observed blocker |
|---|---:|---:|---|
| [2](../runs/m3-t17-native-r10/agent-r2/T17/README.md) | 4 | 4/5 | [Step 8](../runs/m3-t17-native-r10/agent-r2/T17/trace.jsonl#L40) still joins line-hyphenated words in the performance and limitations quotations; both checks return `hyphenation_ambiguous`. |
| [3](../runs/m3-t17-native-r10/agent-r3/T17/README.md) | 4 | 4/5 | [Step 8](../runs/m3-t17-native-r10/agent-r3/T17/trace.jsonl#L40) repairs the other citations but retains `errors` where the extracted source has `er-` followed by a line break and `rors`; the last check remains `hyphenation_ambiguous`. |
| [5](../runs/m3-t17-native-r10/agent-r5/T17/README.md) | 3 | 5/5 | [Step 8](../runs/m3-t17-native-r10/agent-r5/T17/trace.jsonl#L43) fixes an earlier page mismatch but leaves two edited quotations `not_found`, including inconsistent handling of `sub-tasks`, `ac-cording`, and `aver-age` line wraps. |

Reading actions include searches. In repeats 2 and 3, a reading action remains,
but no model decision remains to use it. The checker preserves line-end
hyphens and reports a candidate instead of silently deleting them. These traces
establish a repeated repair-budget failure involving both model edits and that
conservative rule; they do not isolate either one's causal contribution or show
that the underlying scientific observations are false. The 3/10 rate describes
this native diagnostic only, not the other methods or a stable future rate.
Replays of a fixed decision prefix test conditional recovery, not end-to-end
failure frequency.

The earlier [M3 development smoke](../runs/m3-smoke-20261118/README.md) also contains
a native T17 repair-budget exhaustion, while PyAgent and baseline return reviews.
Those development attempts remain separate from the ten-attempt diagnostic and
the frozen comparison grid.

**API history replay failures.** The
[offline API audit](../runs/m3-existing-20261118-luna6/api-400-analysis.md)
finds four native HTTP 400 failures in primary-model core round 1, each on the
first request replaying a returned reasoning item. The audit verifies matched
tool-call/output pairs, unique IDs, and unchanged replay order. Fourteen native
failures in secondary-model M2 round 1 show the same trigger. Provider
compatibility with the returned reasoning representation is a hypothesis; the
redacted errors do not establish which field caused rejection. These attempts
remain failures in completion and content denominators, with incurred usage
retained. They measure operational reliability, not the substantive quality of
an assessment that was never returned.

The [human quality protocol](../data/quality/README.md) defines independent labels
for the substantive failures. It does not supply or imply completed annotation.
