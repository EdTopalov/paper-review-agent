# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 338 output tokens · estimated USD 0.00025922

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0017",
      "quote": "Pass-through: word-recognizer passes on the (possibly misspelled) word as is."
    },
    {
      "document_id": "P1",
      "block_id": "b0018",
      "quote": "Backoff to neutral word: Alternatively, noting that passing UNK-predicted words through unchanged exposes the downstream model to potentially corrupted text, we consider backing off to a neutral word like `a', which has a similar distribution across classes."
    },
    {
      "document_id": "P1",
      "block_id": "b0019",
      "quote": "Backoff to background model: We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK."
    },
    {
      "document_id": "P1",
      "block_id": "b0020",
      "quote": "Thus, it is best to train a precise foreground model on an in-domain corpus and focus on frequent words, and then to resort to a general-purpose background model for rare and unobserved words."
    }
  ],
  "explanation": "The paper describes three strategies used when the foreground recognizer predicts UNK, including pass-through as a baseline.",
  "answer": "When the foreground recognizer predicts UNK, the strategies are: pass-through, which leaves the possibly misspelled word unchanged; neutral-word backoff, which substitutes a fixed neutral word such as “a”; and background-model backoff, which uses a more general recognizer trained on a larger, less-specialized corpus. The paper recommends a precise in-domain foreground model for frequent words and the background model for rare or unseen words."
}
```
