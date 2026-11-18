# QASPER attribution and licence

Source: [QASPER](https://huggingface.co/datasets/allenai/qasper), version 0.3.
The pinned dataset card identifies its licence as [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The complete upstream card and data-format README are preserved beside this file.

Attribution: Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A. Smith,
and Matt Gardner (2021), *A Dataset of Information-Seeking Questions and Answers
Anchored in Research Papers*, NAACL. https://arxiv.org/abs/2105.03011

Modifications: selected a text-only subset of the public upstream development
data, assigned deterministic benchmark splits, converted paragraphs/captions to
identified text blocks, and separated existing annotations from agent inputs.
Answer wording and paper paragraphs are retained. The source papers retain
their authors' rights and are identified by title and arXiv URL in each document.
This adapter does not relicense those papers or manufacture new human labels.
