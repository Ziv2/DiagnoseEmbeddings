# Segmentation methods to identify weaknesses in text embeddings:



---

| **Method**                   | **Effective** | **How to Use**                                | **Resources Needed**                | **Efficiency** | **References**                                                                | **GitHub Resources**                                                                                 |
| ---------------------------- | ------------- | --------------------------------------------- | ----------------------------------- | -------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **LDA**                      | Yes           | Topic segmentation using LDA                  | Gensim, preprocessed text corpus    | Moderate       | [Blei et al., 2003](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)  | [Gensim](https://github.com/RaRe-Technologies/gensim)                                                |
| **NMF**                      | Yes           | Factorize document matrix                     | Scikit-learn                        | High           | [Lee & Seung, 1999](https://www.nature.com/articles/nn599)                    | [Scikit-learn NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html) |
| **BERTopic**                 | Yes           | Transformer-based topic modeling              | HuggingFace, BERTopic library       | High           | [Grootendorst, 2022](https://arxiv.org/abs/2203.05794)                        | [BERTopic Repository](https://github.com/MaartenGr/BERTopic)                                         |
| **TextRank**                 | Yes           | Graph-based segmentation                      | NetworkX, embeddings                | Moderate       | [Mihalcea & Tarau, 2004](https://www.aclweb.org/anthology/W04-3252/)          | [TextRank Python](https://github.com/davidadamojr/TextRank)                                          |
| **LexRank**                  | Yes           | Graph-based segmentation                      | Graph processing libraries          | Moderate       | [Erkan & Radev, 2004](https://www.jair.org/index.php/jair/article/view/10303) | [LexRank](https://github.com/crabcamp/lexrank)                                                       |
| **Sliding Window**           | Yes           | Rolling window cosine similarity              | NumPy, embeddings                   | High           | NA                                                                            | [UKP Lab Sentence Transformers](https://github.com/UKPLab/sentence-transformers)                     |
| **Event Detection**          | Yes           | Clustering embeddings for event detection     | Pre-trained models, Scikit-learn    | High           | [Aggarwal, 2012](https://link.springer.com/book/10.1007/978-1-4614-2804-2)    | NA                                                                                                   |
| **Dialogue Segmentation**    | Yes           | Turn-based sentence segmentation              | Labeled datasets, SpaCy             | Moderate       | [Ritter et al., 2010](https://www.aclweb.org/anthology/P10-1044/)             | NA                                                                                                   |
| **Summarization Clustering** | Yes           | Embedding clustering for extractive summaries | Summarization libraries, embeddings | High           | NA                                                                            | [Sumy Repository](https://github.com/miso-belica/sumy)                                               |


