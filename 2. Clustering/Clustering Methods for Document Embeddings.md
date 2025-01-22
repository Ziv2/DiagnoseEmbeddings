# Clustering Methods to find weaknesses in text embeddings

---

## **Partition-Based Methods**

### **K-Means and Its Variants**

- **Effective?**: Yes, widely used for text embeddings clustering.
- **How?**:
  - Clusters text embeddings by minimizing intra-cluster variance.
  - Variants include K-Harmonic Means (improves initialization sensitivity), Mini-Batch K-Means (optimized for large datasets), and Kernel K-Means (handles nonlinear cluster boundaries).
- **Resources Needed**:
  - Libraries: `scikit-learn`, `faiss`.
  - Computational resources: Moderate; Mini-Batch K-Means scales better for large datasets.
- **Efficiency**: Moderately efficient for small to medium datasets but struggles with sparse embeddings or high-dimensionality.
- **References and Links**:
  - [scikit-learn K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
  - [faiss GitHub](https://github.com/facebookresearch/faiss)

### **Gaussian Mixture Models (GMMs)**

- **Effective?**: Yes, for probabilistic clustering of overlapping embeddings.
- **How?**:
  - Uses probabilistic distributions to assign texts to clusters.
  - Adjusting covariance structures (full, tied, diagonal) improves fit.
- **Resources Needed**:
  - Libraries: `scikit-learn`.
  - Computational resources: Moderate to high for large datasets.
- **Efficiency**: Computationally intensive compared to K-Means.
- **References and Links**:
  - [scikit-learn GMM](https://scikit-learn.org/stable/modules/mixture.html)

---

## **Density-Based Methods**

### **DBSCAN**

- **Effective?**: Yes, dataset-specific.
- **How?**:
  - Groups embeddings with high density, identifying noise as outliers.
  - Parameters include `eps` (distance threshold) and `min_samples`.
- **Resources Needed**:
  - Libraries: `scikit-learn`, `hdbscan`.
  - Computational resources: Moderate to high for high-dimensional embeddings.
- **Efficiency**: Scales poorly with dimensionality.
- **References and Links**:
  - [scikit-learn DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan)

### **HDBSCAN**

- **Effective?**: Yes, extends DBSCAN for varying density clusters.
- **How?**:
  - Uses hierarchical density estimation.
  - Outputs hierarchical clusters.
- **Resources Needed**:
  - Libraries: `hdbscan`.
  - Computational resources: Moderate to high.
- **Efficiency**: More efficient than DBSCAN for large data.
- **References and Links**:
  - [HDBSCAN GitHub](https://github.com/scikit-learn-contrib/hdbscan)

### **Mean Shift**

- **Effective?**: Limited for text embeddings due to sensitivity to bandwidth parameter.
- **How?**:
  - Iteratively shifts points toward the mean of their neighborhood.
- **Resources Needed**:
  - Libraries: `scikit-learn`.
  - Computational resources: High for large datasets.
- **Efficiency**: Scales poorly with large datasets.
- **References and Links**:
  - [Mean Shift](https://scikit-learn.org/stable/modules/clustering.html#mean-shift)

---

## **Graph-Based Methods**

### **Spectral Clustering**

- **Effective?**: Yes, for embeddings with complex relationships.
- **How?**:
  - Converts embeddings into a similarity graph, clustering using eigenvalues of Laplacian matrices.
- **Resources Needed**:
  - Libraries: `scikit-learn`.
  - Computational resources: High due to eigen decomposition.
- **Efficiency**: Computationally expensive for large datasets.
- **References and Links**:
  - [Spectral Clustering](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)

### **Minimum Spanning Tree (MST)**

- **Effective?**: Yes, for clustering based on connected components.
- **How?**:
  - Forms a graph where embeddings are nodes; clusters based on MST distances.
- **Resources Needed**:
  - Libraries: `networkx`.
  - Computational resources: Moderate.
- **Efficiency**: Efficient for small datasets.
- **References and Links**:
  - [NetworkX Documentation](https://networkx.org/)

### **Affinity Propagation**

- **Effective?**: Yes, without requiring `k` specification.
- **How?**:
  - Finds exemplars within the embedding space to form clusters.
- **Resources Needed**:
  - Libraries: `scikit-learn`.
  - Computational resources: High for large datasets.
- **Efficiency**: Computationally expensive.
- **References and Links**:
  - [Affinity Propagation](https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation)

### **DeepWalk + Graph Embedding**

- **Effective?**: Yes, for embedding-based clustering on graphs.
- **How?**:
  - Represents relationships in embeddings as a graph, leveraging DeepWalk for node embeddings followed by clustering.
- **Resources Needed**:
  - Libraries: `stellargraph`, `deepwalk`.
  - Computational resources: Moderate to high.
- **Efficiency**: Moderately efficient.
- **References and Links**:
  - [DeepWalk GitHub](https://github.com/phanein/deepwalk)

---

## **Neural Network-Based Methods**

### **Autoencoder-Based Clustering**

- **Effective?**: Yes, for dimensionality reduction and clustering.
- **How?**:
  - Trains an autoencoder to encode embeddings; clustering is applied to the encoded space.
- **Resources Needed**:
  - Libraries: `TensorFlow`, `PyTorch`.
  - Computational resources: High (requires GPU for training).
- **Efficiency**: Effective but computationally intensive.
- **References and Links**:
  - [Autoencoder Example](https://github.com/keras-team/keras)

### **GCNN-Based Clustering**

- **Effective?**: Effective for graph-structured data.
- **How?**:
  - Learns embeddings and clusters them jointly using graph convolutional networks.
- **Resources Needed**:
  - Libraries: `PyTorch Geometric`.
  - Computational resources: High.
- **Efficiency**: Computationally intensive but effective for relational data.
- **References and Links**:
  - [PyTorch Geometric](https://github.com/pyg-team/pytorch_geometric)

### **Contrastive Learning-Based Clustering**

- **Effective?**: Yes, for learning discriminative embeddings for clustering.
- **How?**:
  - Learns representations by contrasting positive/negative pairs, clustering in latent space.
- **Resources Needed**:
  - Libraries: `SimCLR`, `PyTorch`.
  - Computational resources: High.
- **Efficiency**: Efficient for embeddings with clear contrasts.
- **References and Links**:
  - [SimCLR GitHub](https://github.com/google-research/simclr)

---

## **Hierarchical Methods**

### **Agglomerative Clustering**

- **Effective?**: Yes, for hierarchical relationships.
- **How?**:
  - Hierarchically merges embeddings into clusters using linkage metrics.
- **Resources Needed**:
  - Libraries: `scikit-learn`.
  - Computational resources: Moderate.
- **Efficiency**: Efficient for small to medium datasets.
- **References and Links**:
  - [Agglomerative Clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)

---

## **Topic-Based Clustering**

### **Latent Dirichlet Allocation (LDA)**

- **Effective?**: Partially, for topic modeling.
- **How?**:
  - Models topics in embeddings by fitting a generative model.
- **Resources Needed**:
  - Libraries: `Gensim`.
  - Computational resources: Moderate.
- **Efficiency**: Less suited for dense embeddings.
- **References and Links**:
  - [Gensim LDA](https://radimrehurek.com/gensim/)

### **BERTopic**

- **Effective?**: Yes, combines embedding and clustering seamlessly.
- **How?**:
  - Uses Sentence-BERT embeddings with clustering techniques (e.g., HDBSCAN).
- **Resources Needed**:
  - Libraries: `BERTopic`.
  - Computational resources: Moderate to high.
- **Efficiency**: Effective and efficient for large datasets.
- **References and Links**:
  - [BERTopic GitHub](https://github.com/MaartenGr/BERTopic)

## Summary Table
