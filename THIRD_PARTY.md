# Sources, dependencies, and licenses

The M2 agent/harness code in this repository was written for this project. V2
imports the PyAgent ReAct implementation as a dependency; no framework source or
paper-review dataset code is vendored.

The unified implementation incorporates the team's citation checker and page
reading design from [commit 39d760f](https://github.com/EdTopalov/paper-review-agent/commit/39d760f2e47b66d074de34397101dcc66e53ead1).
The original team commit remains in Git history. `citations.py` extends its
exact/normalized/wrong-page categories with conservative handling of case,
mathematical notation, and ambiguous line-break hyphens. The shared package is
`src/paper_review`; the OpenAI Responses API is the default model backend.

- ReAct supplies the architectural idea of alternating model decisions and tool
  observations: Yao et al., [ReAct](https://arxiv.org/abs/2210.03629), CC BY 4.0.
  It is cited in `src/paper_review/runner.py`; this is an independent implementation.
- V2 uses `pyagent-patterns==0.3.0` from
  [pyagent-core/pyagent](https://github.com/pyagent-core/pyagent), MIT licensed.
  Its `ReAct` loop is imported in `src/paper_review/pyagent_runner.py`; the project
  adapter handles evidence validation, accepted-review stopping and API accounting.
  This is the [pyagent.org](https://pyagent.org/) project, distinct from the
  unrelated `pyagent-harness` package.
- Evidence memory uses structured notes and context recitation as an architectural
  idea, described in [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  `context_memory.py` is an original implementation; no article or framework
  source code is copied. The selection pilot composes the existing reviewers with
  one independent structured comparison call.
- API integration follows the official [OpenAI function-calling documentation](https://developers.openai.com/api/docs/guides/function-calling).
- The OpenAI Python SDK is Apache-2.0 licensed; `pypdf` is BSD-3-Clause;
  `python-dotenv` is BSD-3-Clause; `requests` is Apache-2.0;
  `beautifulsoup4`, `jsonschema`, and `pytest` are MIT licensed.
  Dependencies are installed rather than vendored; their package distributions
  retain the authoritative license notices, including transitive dependencies.
- The 20 evaluation paper text snapshots retain their source authors' **CC BY 4.0**
  license. Each snapshot records its title, authors, versioned source and PDF URLs,
  license URL, PDF hash, and the modification (page-wise text extraction).
  Figures and layout are omitted. This dependency list does not relicense papers.
- `data/dev/toy.json` is an original synthetic fixture, clearly marked as such.
- Private reading-club pilot notes are ignored by Git and are not published with
  this implementation or treated as approved evaluation labels.

Luna token pricing was checked on 18 November 2026 against the official
[GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) model page:
standard text input $0.10/M, cached input $0.01/M, cache writes $0.125/M,
output $0.50/M. The runner records these rates and usage in every trace.
The [GPT-5.6 Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
page lists input $0.20/M, cached input $0.02/M, output $1.20/M, and cache writes
at 1.25 times input ($0.25/M). Both models double input/cache rates and multiply
output rates by 1.5 beyond 272K input tokens. These are estimates based on
published standard rates; regional/provider charges may differ.
