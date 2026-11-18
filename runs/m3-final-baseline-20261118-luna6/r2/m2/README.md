# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | 20/20 | 10/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 603.3 | $0.000550 | 7.06 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| baseline | 1 | 20/20 | 10/20 | 1.00 | 24778.5/603.3 | $0.000550 | 7.06 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| baseline | 10 / 0 / 10 | k=1: 0.500 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| baseline | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T02 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T03 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T05 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T06 | 1/1 | 0/1 | 0.7300 | unavailable | [0.73, 0.73] |
| baseline | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T09 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T10 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T11 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T12 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T13 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T14 | 1/1 | 0/1 | 0.7300 | unavailable | [0.73, 0.73] |
| baseline | T15 | 1/1 | 0/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T16 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 0/1 | 0.7100 | unavailable | [0.71, 0.71] |
| baseline | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 0/1 | 0.6600 | unavailable | [0.66, 0.66] |
| baseline | T20 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 30789/503 | $0.000560 | 6.08 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 16657/693 | $0.000513 | 7.69 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 38684/679 | $0.000727 | 7.84 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 27075/745 | $0.000644 | 7.95 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 23863/545 | $0.000511 | 6.21 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 1 | 36934/405 | $0.000572 | 5.11 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.73 | 0 | no | not audited | 1 | 35056/487 | $0.000594 | 6.18 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.73 | 0 | no | not audited | 1 | 24226/486 | $0.000486 | 6.37 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/690 | $0.000706 | 8.08 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 26994/540 | $0.000540 | 6.04 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.71 | 0 | no | not audited | 1 | 18064/694 | $0.000528 | 8.35 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.69 | 0 | yes | not audited | 1 | 16572/690 | $0.000511 | 7.63 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 30099/537 | $0.000570 | 6.21 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 17424/732 | $0.000541 | 8.94 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.66 | 0 | no | not audited | 1 | 33041/510 | $0.000586 | 5.85 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.66 | 0 | yes | not audited | 1 | 13497/752 | $0.000511 | 9.10 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 14416/728 | $0.000508 | 8.23 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 23878/667 | $0.000573 | 7.61 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.62 | 0 | no | not audited | 1 | 8838/483 | $0.000330 | 6.01 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 23392/500 | $0.000484 | 5.83 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
