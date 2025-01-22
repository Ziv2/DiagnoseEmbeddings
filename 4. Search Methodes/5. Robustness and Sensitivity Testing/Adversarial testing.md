# Adversarial Perturbations testing

This method involves introducing slight perturbations to text inputs to uncover weaknesses in text models. These weaknesses often manifest in how embeddings encode information and handle adversarial variations. 

---

### How Adversarial Perturbations Testing is Done

1. **Generate Perturbations**: Slight alterations are made to the text, such as synonym replacements, paraphrasing, or introducing typographical errors. These changes are carefully designed to preserve semantics while potentially misleading the embedding model.

2. **Evaluate Model Responses**: Models are tested on the perturbed text to see if their outputs, such as classification or similarity metrics, change drastically compared to unaltered inputs.

3. **Embedding Space Analysis**: The embeddings of original and perturbed inputs are visualized or measured to assess the model's robustness in retaining semantic similarity.

4. **Adversarial Training**: Identified weaknesses are used to retrain the model with adversarial examples, enhancing robustness.

5. **Metrics for Robustness**: Metrics such as Word Mover’s Distance (WMD) and cosine similarity are often used to evaluate how close the perturbed and original embeddings are.

---

### Key Insights from Research

1. **Gradient-Based Attacks**: Zhu et al. proposed a gradient-based word-level adversarial attack to find optimal substitutions in the embedding space, revealing vulnerabilities in text classifiers [(Zhu et al., 2021)](https://consensus.app/papers/wordlevel-textual-adversarial-attack-in-the-embedding-zhu-gu/458e93e6bcf756bea0940693b82068d5/?utm_source=chatgpt).

2. **Embedding Space Alignment**: Bagdasarian et al. showed that adversarial perturbations could align embeddings across modalities, misleading multimodal systems without requiring knowledge of downstream tasks [(Bagdasarian et al., 2023)](https://consensus.app/papers/adversarial-illusions-in-multimodal-embeddings-bagdasarian-jha/97af0fdf2746542a90d7d83caddfdcdd/?utm_source=chatgpt).

3. **Embedding Augmentation**: Kim and Kang introduced adversarial embeddings generated using Projected Gradient Descent (PGD) to retrain models and prevent overfitting on small datasets [(Kim & Kang, 2022)](https://consensus.app/papers/text-embedding-augmentation-based-on-retraining-with-kim-kang/a8de88c295e75eb8848690f99649a04a/?utm_source=chatgpt).

4. **Reconstructing Perturbations**: Gong et al. adapted gradient-based adversarial attacks from images to text by searching in the embedding space and reconstructing adversarial examples via nearest neighbors [(Gong et al., 2018)](https://consensus.app/papers/adversarial-texts-with-gradient-methods-gong-wang/79e7eb8075c45356a1b59adcf51577d5/?utm_source=chatgpt).

5. **Defensive Techniques**: Zhou et al. developed a perturbation discriminator that restores original embeddings by estimating likely perturbations, effectively countering adversarial attacks [(Zhou et al., 2019)](https://consensus.app/papers/learning-to-discriminate-perturbations-for-blocking-zhou-jiang/a461c1da8c7f549c856d139d4127eaf0/?utm_source=chatgpt).

---

### Practical Resources

- **Codebase for Adversarial Attacks**:
  - [TextAttack](https://github.com/QData/TextAttack): A Python framework for adversarial attacks in NLP.
  - [AllenNLP Interpret](https://github.com/allenai/allennlp-interpret): Tools for generating adversarial perturbations and model interpretability.
  - [OpenAttack](https://github.com/thunlp/OpenAttack): Open-source framework for adversarial text attacks.
