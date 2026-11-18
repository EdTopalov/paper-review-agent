# QASPER-8eefa116e3c3

baseline · repeat 1 · ok

1 API calls · 6543 input tokens · 278 output tokens · estimated USD 0.0002047

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0023",
      "quote": "Table TABREF33 gives an overview of the standard data sets we use for training. The GENIA Corpus BIBREF3 contains biomedical abstracts from the PubMed database. We use GENIA technical term annotations 3.02, which cover linguistic expressions to entities of interest in molecular biology, e.g. proteins, genes and cells. CoNLL2003 BIBREF14 is a standard NER dataset based on the Reuters RCV-1 news corpus."
    },
    {
      "document_id": "P1",
      "block_id": "b0024",
      "quote": "For testing the overall annotation performance, we utilize CoNLL2003-testA and a 50 document split from GENIA. Additionally, we test on the complete KORE50 BIBREF21 , ACE2004 BIBREF22 and MSNBC data sets using the GERBIL evaluation framework BIBREF23 ."
    }
  ],
  "explanation": "The paper names GENIA and CoNLL2003 as standard training datasets and also lists the evaluation datasets.",
  "answer": "The standard datasets were GENIA and CoNLL2003. For testing, the paper also used CoNLL2003-testA, a 50-document GENIA split, KORE50, ACE2004, and MSNBC."
}
```
