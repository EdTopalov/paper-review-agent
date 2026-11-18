# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 355 output tokens · estimated USD 0.00026772000000000005

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
      "quote": "Backoff to background model: We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK. Figure 1 depicts this scenario pictorially."
    },
    {
      "document_id": "P1",
      "block_id": "b0020",
      "quote": "Thus, it is best to train a precise foreground model on an in-domain corpus and focus on frequent words, and then to resort to a general-purpose background model for rare and unobserved words."
    }
  ],
  "explanation": "The paper describes three ways to handle an UNK prediction: pass the input through unchanged, replace it with a neutral word, or use a broader background recognizer.",
  "answer": "When the foreground recognizer predicts UNK, the system can (1) pass the possibly misspelled word through unchanged, (2) replace it with a neutral word such as “a,” or (3) send it to a general-purpose background recognizer trained on a larger, less-specialized corpus. The background model is intended for rare or unseen words; the paper also evaluates pass-through as a baseline."
}
```
