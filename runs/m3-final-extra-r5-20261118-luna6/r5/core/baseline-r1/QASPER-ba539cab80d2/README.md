# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 323 output tokens · estimated USD 0.00025172

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
  "explanation": "The paper describes three strategies used when the foreground recognizer predicts UNK, including pass-through as a comparison strategy.",
  "answer": "When the foreground recognizer predicts UNK, the system can pass the possibly misspelled word through unchanged, replace it with a fixed neutral word such as “a,” or send it to a more generic recognizer trained on a larger corpus. The paper favors a precise in-domain foreground model for frequent words and a background model for rare or unseen words."
}
```
