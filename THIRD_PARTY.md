# Sources, dependencies, and licenses

The agent/harness code in this repository was written for this project. No agent
framework implementation or paper-review dataset code was copied.

- ReAct supplies the architectural idea of alternating model decisions and tool
  observations: Yao et al., [ReAct](https://arxiv.org/abs/2210.03629), CC BY 4.0.
  It is cited in `src/paper_review/runner.py`; this is an independent implementation.
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

Token pricing was checked on 26 October 2026 against the official
[GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) model page:
standard text input $0.10/M, cached input $0.01/M, cache writes $0.125/M,
output $0.50/M. The runner records these rates and usage in every trace. Rates are
estimates for the specified service tier, not an invoice or a future price promise.
