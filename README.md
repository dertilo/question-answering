# question-answering
### ideas
* pure bag-of-tokens based retrieval (done by haystack) is not sufficient! -> one needs an entity-linking/resolution giving feedback to the user, which entities the systems thinks that the user refers to
    + at least some "guidance" for retriever via NER (spacy?)
* big transformers like roberta might be too slow -> distillation?
* es + page-rank?

### DrQA wiki-data
* `GET drqa_wiki/_count` -> 5075182

## libraries
### extractive
* [DrQA](https://github.com/facebookresearch/DrQA.git)
* [haystack](https://github.com/deepset-ai/haystack)
* [FARM](https://github.com/deepset-ai/FARM)
* [huggingface-transformers](https://github.com/huggingface/transformers.git)