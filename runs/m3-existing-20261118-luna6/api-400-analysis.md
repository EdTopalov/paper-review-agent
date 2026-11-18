# Native agent API 400 failures

This offline audit examines four native-agent failures in round 1 of the
`gpt-6-luna` core benchmark. All four failed immediately after the first request
that replayed a Responses API `reasoning` item. This is a common trigger, not a
confirmed root cause: saved API errors contain only `BadRequestError` and HTTP
status 400, because raw exception messages can contain sensitive values.

| Task | Trace | Response containing reasoning | Failed request | API error | Matched tool pairs |
| --- | --- | ---: | ---: | ---: | ---: |
| QASPER-8db6f8714bda | [trace](r1/core/agent-r1/QASPER-8db6f8714bda/trace.jsonl) | 13 | 17 | 18 | 3 |
| RC-59408ce4ca25 | [trace](r1/core/agent-r1/RC-59408ce4ca25/trace.jsonl) | 18 | 22 | 23 | 4 |
| RC-ae631d292d42 | [trace](r1/core/agent-r1/RC-ae631d292d42/trace.jsonl) | 13 | 17 | 18 | 3 |
| RC-cc398745c3c8 | [trace](r1/core/agent-r1/RC-cc398745c3c8/trace.jsonl) | 13 | 17 | 18 | 3 |

Numbers are event `seq` values and physical JSONL line numbers. Requests use
prefix compression on disk; `paper_review.trace.read_events` reconstructs them.
Read physical file lines, since embedded Unicode line separators in paper text
are not JSONL record boundaries.

For every failed request, all `function_call` IDs have exactly one corresponding
`function_call_output`; call IDs and output-item IDs are unique. The preceding
request remains an unchanged prefix, and every item from the last successful
response is replayed unchanged and in order. Missing tool outputs, duplicate
calls, and an edited history prefix therefore do not explain these four cases.

Each replayed reasoning item has nonempty `encrypted_content` (1,912–2,616
characters), empty `summary` and `content` lists, and `status: null`. Encrypted
payload values are deliberately omitted here. The requests use `store: false`.
The installed OpenAI Python SDK is version 1.96.1. Its reasoning input type has
no `content` field and declares a supplied `status` as an enum without `null`;
its response type permits a missing status that serializes to `null`.

The leading hypothesis is incompatibility when replaying the returned reasoning
item through the configured provider, potentially involving the additional
`content` field, null status, or encrypted reasoning handling. The
[official reasoning guide](https://developers.openai.com/api/docs/guides/reasoning),
retrieved on 2026-11-18, says to preserve reasoning items and tool outputs in
their original order. It also says encrypted reasoning is returned by default
when `store` is false. The absence of an explicit `include` parameter is
therefore insufficient evidence of an error.

No live probes, retries, or source changes were made for this diagnosis. Keep
these failures in all-attempt completion and quality denominators. They measure
operational reliability; they cannot establish the quality of an assessment
that was never submitted. A future, separately versioned development experiment
can test valid input-item normalization and provider compatibility before
collecting a new evaluation grid.
