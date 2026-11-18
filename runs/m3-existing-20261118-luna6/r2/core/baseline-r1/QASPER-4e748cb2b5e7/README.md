# QASPER-4e748cb2b5e7

baseline · repeat 1 · ok

1 API calls · 7818 input tokens · 283 output tokens · estimated USD 0.00021994999999999998

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0008",
      "quote": "Computational linguists have previously addressed this problem using rule based and statistical techniques, that make use of : (a) Unigrams and Pragmatic features ... (b) Stylistic patterns and patterns related to situational disparity and (c) Hastag interpretations."
    },
    {
      "document_id": "P1",
      "block_id": "b0009",
      "quote": "Most of the previously done work on sarcasm detection uses distant supervision based techniques (ex: leveraging hashtags) and stylistic/pragmatic features (emoticons, laughter expressions such as “lol” etc)."
    },
    {
      "document_id": "P1",
      "block_id": "b0026",
      "quote": "The features enlisted under lexical,implicit incongruity and explicit incongruity are borrowed from various literature ... Two additional textual features viz. readability and word count of the text are also taken under consideration."
    }
  ],
  "explanation": "The paper describes its traditional/textual feature set in broad categories, with additional readability and word-count features. The supplied text does not give the detailed individual features listed in the referenced feature table.",
  "answer": "They used unigram/lexical, pragmatic and stylistic features, including cues such as emoticons and laughter expressions, plus features for implicit and explicit incongruity. They also included readability and word count."
}
```
