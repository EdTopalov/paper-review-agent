# QASPER-8eefa116e3c3

agent · repeat 1 · ok

4 API calls · 10210 input tokens · 431 output tokens · estimated USD 0.0006995650000000001

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0023",
      "quote": "Table TABREF33 gives an overview of the standard data sets we use for training. The GENIA Corpus BIBREF3 contains biomedical abstracts from the PubMed database. We use GENIA technical term annotations 3.02, which cover linguistic expressions to entities of interest in molecular biology, e.g. proteins, genes and cells. CoNLL2003 BIBREF14 is a standard NER dataset based on the Reuters RCV-1 news corpus. It covers named entities of type person, location, organization and misc."
    },
    {
      "document_id": "P1",
      "block_id": "b0024",
      "quote": "For testing the overall annotation performance, we utilize CoNLL2003-testA and a 50 document split from GENIA. Additionally, we test on the complete KORE50 BIBREF21 , ACE2004 BIBREF22 and MSNBC data sets using the GERBIL evaluation framework BIBREF23 ."
    }
  ],
  "explanation": "The paper names GENIA and CoNLL2003 as the standard datasets used for training, and lists additional evaluation sets.",
  "answer": "The standard training datasets were GENIA (technical term annotations 3.02) and CoNLL2003. Tests also used CoNLL2003-testA, a 50-document GENIA split, KORE50, ACE2004, and MSNBC."
}
```
