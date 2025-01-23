# Literature Review: Root Cause Analysis for Textual Embeddings
The following review explore methods for identifying and diagnosing failures and weaknesses in the utilization of textual embeddings. 
**The accompanying README file serves as a navigation panel to the various topics covered in this literature review.**

Please note that in the existing literature, root cause analysis (or failure analysis) is predominantly associated with production processes, with almost no mention of language models failures.
Therefore, we tried to use variouse of alternative terms. 

## Low Performance Areas
Definition: concecuenses in which embeddings fail to meet expected performance metrics. 
The focus is on specific measurable shortcomings in predefined benchmarks or tasks (e.g., classification, clustering coherence, analogy tests).

Purpose: Identify areas where embeddings underperform relative to established standards or baselines.

Examples from Document: Intrinsic evaluation metrics (e.g., WordSim-353) identify poor dimensional coherence.
Downstream task errors (e.g., sentiment analysis misclassifications) highlight application-specific failures.
Cluster coherence scoring reveals semantic groupings that are not well-defined.

<u>Emphasis:<u> Quantitative analysis and comparisons to known standards or task-specific requirements.

## Weaknesses
Definition: Weaknesses refer to intrinsic properties or vulnerabilities in embeddings, such as their inability to handle rare terms, adversarial inputs, or polysemous words. 
These are fundamental flaws in the embedding model's representation capabilities.

Purpose: Uncover underlying issues that may lead to failure across multiple areas or tasks.
Examples from Document:
Cosine similarity distribution checks detect anomalies in semantic distances.
Adversarial example testing exposes embeddings' inability to generalize against minor variations (e.g., typos or synonyms).
Linguistic property probing examines encoding accuracy for specific attributes (e.g., syntax, semantics).

Emphasis: Qualitative diagnostics that focus on improving the model's robustness and adaptability.
Key Difference

Scope: Low performance areas are task-specific and quantitative, while weaknesses are model-intrinsic and qualitative.
Objective: Low performance areas aim to optimize embeddings for specific tasks; weaknesses aim to improve the model’s general robustness and versatility.

Methods: Low performance focuses on benchmarks and performance logs, whereas weaknesses explore structural and distributional properties of embeddings.
By addressing both, a comprehensive root cause analysis ensures that textual embeddings are both task-efficient and inherently robust.

---
Let's start with a schematic diagram illustrating few potential causes of textual embeddings failures, at various stages where textual embeddings are involved.

![Literature Review Overview](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/diagram.svg)


## Mapping the failure diagnostics methods covered in this literature review.
![Literature Review Overview](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/Methods_map.png)

## Navigation panel:

**1. Introduction**

&nbsp;&nbsp;&nbsp;&nbsp;- [1. Introduction](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/1.%20Introduction/1.%20Introduction.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [2. Types of Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/1.%20Introduction/2.%20Types%20of%20Embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [3. Evaluation Metrics](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/1.%20Introduction/3.%20Evaluation%20Metrics.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [4. Datasets](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/1.%20Introduction/4.%20Datasets.md)

**2. Clustering**

&nbsp;&nbsp;&nbsp;&nbsp;- [Advanced clustering techniques (applicable across levels)](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/2.%20Clustering/Advanced%20clustering%20techniques%20(applicable%20across%20levels).md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering Methods for Document Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/2.%20Clustering/Clustering%20Methods%20for%20Document%20Embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering Methods for Sentence Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/2.%20Clustering/Clustering%20Methods%20for%20Sentence%20Embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering methods for Word Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/2.%20Clustering/Clustering%20methods%20for%20Word%20Embeddings.md)

**3. Segmentation**

&nbsp;&nbsp;&nbsp;&nbsp;- [Segmentation Methods for Document Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/3.%20Segmentation/Segmentation%20Methods%20for%20Document%20Embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Segmentation Methods for Sentence Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/3.%20Segmentation/Segmentation%20Methods%20for%20Sentence%20Embeddings.md)

**4. Search Methodes**

&nbsp;&nbsp;&nbsp;&nbsp;**1. Fairness and Bias Assessment**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Bias and Fairness Quantification](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/1.%20Fairness%20and%20Bias%20Assessment/Bias%20and%20Fairness%20Quantification.md)

&nbsp;&nbsp;&nbsp;&nbsp;**2. Linguistic and Contextual Analysis**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Contextual issues](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/2.%20Linguistic%20and%20Contextual%20Analysis/Contextual%20issues.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Cross-language testing](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/2.%20Linguistic%20and%20Contextual%20Analysis/Cross-language%20testing.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [linguistic analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/2.%20Linguistic%20and%20Contextual%20Analysis/linguistic%20analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Out-of-Domain](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/2.%20Linguistic%20and%20Contextual%20Analysis/Out-of-Domain.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Out-of-Vocabulary (OOV) words](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/4.%20Search%20Methodes/2.%20Linguistic%20and%20Contextual%20Analysis/Out-of-Vocabulary%20(OOV)%20words.md)

&nbsp;&nbsp;&nbsp;&nbsp;**3. Statistical and Information-Theoretic Analysis**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Divergence Metrics](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/3.%20Statistical%20and%20Information-Theoretic%20Analysis/Divergence%20Metrics.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Entropy and Information-Theoretic Metrics](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/3.%20Statistical%20and%20Information-Theoretic%20Analysis/Entropy%20and%20Information-Theoretic%20Metrics.md)

&nbsp;&nbsp;&nbsp;&nbsp;**4. Dimensionality and Topological Analysis**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Dimensionality Reduction Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/4.%20Dimensionality%20and%20Topological%20Analysis/Dimensionality%20Reduction%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Latent Space Topology Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/4.%20Dimensionality%20and%20Topological%20Analysis/Latent%20Space%20Topology%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Manifold Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/4.%20Dimensionality%20and%20Topological%20Analysis/Manifold%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;**5. Robustness and Sensitivity Testing**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Advanced Adversarial Testing Methods](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Advanced%20Adversarial%20Testing%20Methods.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Adversarial testing](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Adversarial%20testing.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Few-shot and zero-shot learning](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Few-shot%20and%20zero-shot%20learning.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Probing Task Metrics](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Probing%20Task%20Metrics.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Sensitivity and Robustness Tests](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Sensitivity%20and%20Robustness%20Tests.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Temporal drift detection](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Temporal%20drift%20detection.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Transfer Learning Evaluation](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/5.%20Robustness%20and%20Sensitivity%20Testing/Transfer%20Learning%20Evaluation.md)

&nbsp;&nbsp;&nbsp;&nbsp;**6. Error Analysis**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Error Distribution Analysis (EDA)](4.%20Search%20Methodes/6.%20Error%20Analysis//Error%20Distribution%20Analysis%20(EDA).md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Error Surface Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/6.%20Error%20Analysis/Error%20Surface%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;**7. Feature and Vector-Level Metrics**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Feature importance scores](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/7.%20Feature%20and%20Vector-Level%20Metrics/Feature%20importance%20scores.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Similarity and Distance Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/7.%20Feature%20and%20Vector-Level%20Metrics/Similarity%20and%20Distance%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Vector density](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/7.%20Feature%20and%20Vector-Level%20Metrics/Vector%20density.md)

&nbsp;&nbsp;&nbsp;&nbsp;**8. Model and Loss Surface Analysis**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Loss Landscape Analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/8.%20Model%20and%20Loss%20Surface%20Analysis/Loss%20Landscape%20Analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Normalization and Comparison](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/8.%20Model%20and%20Loss%20Surface%20Analysis/Normalization%20and%20Comparison.md)

&nbsp;&nbsp;&nbsp;&nbsp;**9. Outlier and Anomaly Detection**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Locality-Sensitive Hashing (LSH)](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/9.%20Outlier%20and%20Anomaly%20Detection/Locality-Sensitive%20Hashing%20(LSH).md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Outlier Detection](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/9.%20Outlier%20and%20Anomaly%20Detection/Outlier%20Detection.md)

&nbsp;&nbsp;&nbsp;&nbsp;**10. Dataset and Cross-Validation Metrics**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Cross-Validation Metrics](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/10.%20Dataset%20and%20Cross-Validation%20Metrics/Cross-Validation%20Metrics.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Dataset analysis](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/10.%20Dataset%20and%20Cross-Validation%20Metrics/Dataset%20analysis.md)

&nbsp;&nbsp;&nbsp;&nbsp;**11. Visualization Techniques**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Visualization techniques](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/4.%20Search%20Methodes/11.%20Visualization%20Techniques/Visualization%20techniques.md)

**5. Real-Time**

&nbsp;&nbsp;&nbsp;&nbsp;- [Real-Time Investigation to Find Low Performance Areas](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/5.%20Real-Time/Real-Time%20Investigation%20to%20Find%20Low%20Performance%20Areas.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Real-Time Investigation to Find Weaknesses](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/5.%20Real-Time/Real-Time%20Investigation%20to%20Find%20Weaknesses.md)

**6. Summary Tables**

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering Methods for Analyzing Weaknesses in Word Embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Clustering%20Methods%20for%20Analyzing%20Weaknesses%20in%20Word%20Embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering Methods of finding weaknesses in sentence embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Clustering%20Methods%20of%20finding%20weaknesses%20in%20sentence%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering Methods to find weaknesses in Paragraph and Document embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Clustering%20Methods%20to%20find%20weaknesses%20in%20Paragraph%20and%20Document%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Clustering: Advanced Techniques](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Clustering:%20Advanced%20Techniques.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Datasets for Paragraph and Document Embeddings Quality Evaluation](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Datasets%20for%20Paragraph%20and%20Document%20Embeddings%20Quality%20Evaluation.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Datasets for Sentence Embeddings Quality Evaluation](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Datasets%20for%20Sentence%20Embeddings%20Quality%20Evaluation.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Datasets for Word Embeddings Quality Evaluation](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Datasets%20for%20Word%20Embeddings%20Quality%20Evaluation.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Real-Time methods to find low performance areas in textual embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Real-Time%20methods%20to%20find%20low%20performance%20areas%20in%20textual%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Real-Time methods to find weaknesses in textual embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Real-Time%20methods%20to%20find%20weaknesses%20in%20textual%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Segmentation methods to identify weaknesses in Paragraph and Document embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Segmentation%20methods%20to%20identify%20weaknesses%20in%20Paragraph%20and%20Document%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;- [Segmentation methods to Identify weaknesses in sentence embeddings](https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/6.%20Summary%20Tables/Segmentation%20methods%20to%20Identify%20weaknesses%20in%20sentence%20embeddings.md)

&nbsp;&nbsp;&nbsp;&nbsp;
