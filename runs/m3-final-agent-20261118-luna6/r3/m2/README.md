# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 19/20 | 19/20 | 5.60 | 5.55 | 4.10 | 5.60 | 31208.3 | 816.2 | $0.002007 | 12.70 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 19/20 | 19/20 | 5.60 | 31208.3/816.2 | $0.002007 | 12.70 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 19 / 0 / 1 | k=1: 0.950 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T02 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T03 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T04 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T05 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T07 | 1/1 | 1/1 | 0.7900 | unavailable | [0.79, 0.79] |
| agent | T08 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T09 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| agent | T10 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T11 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| agent | T12 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T15 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| agent | T16 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| agent | T17 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T18 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.79 | 0 | yes | not audited | 5 | 24618/603 | $0.001501 | 11.58 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 35738/588 | $0.003162 | 11.39 |
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.78 | 2 | no | not audited | 7 | 40432/1423 | $0.002069 | 18.20 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 39119/749 | $0.003072 | 13.25 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.77 | 0 | yes | not audited | 5 | 23131/614 | $0.001259 | 12.41 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.76 | 1 | no | not audited | 6 | 45138/1080 | $0.002338 | 15.42 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 20003/562 | $0.001522 | 9.12 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.76 | 1 | no | not audited | 6 | 35766/1105 | $0.001919 | 15.54 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.75 | 2 | no | not audited | 7 | 51042/1484 | $0.002494 | 20.03 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.74 | 0 | yes | not audited | 6 | 23500/635 | $0.002070 | 12.22 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.73 | 0 | yes | not audited | 5 | 28889/635 | $0.001670 | 10.25 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 29452/615 | $0.002387 | 11.00 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 33500/1067 | $0.001765 | 13.12 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 23056/600 | $0.001409 | 9.52 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 25934/986 | $0.001563 | 13.02 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.69 | 0 | yes | not audited | 4 | 19208/594 | $0.001306 | 10.24 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 30569/697 | $0.002483 | 10.92 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.67 | 0 | yes | not audited | 5 | 26176/587 | $0.001543 | 10.98 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.66 | 1 | no | not audited | 7 | 49860/998 | $0.003148 | 14.93 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | error | — | 1 | no | not audited | 5 | 19035/703 | $0.001466 | 10.92 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
