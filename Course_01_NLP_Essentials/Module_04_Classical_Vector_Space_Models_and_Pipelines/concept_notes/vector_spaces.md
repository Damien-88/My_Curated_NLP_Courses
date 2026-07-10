# Day 10: Bag-of-Words (BoW) & Vector Space Dimensionality

### Learning Objective
Understand the transition from sequential string structures to high-dimensional geometric vector spaces, implement a 
deterministic Bag-of-Words (BoW) feature extraction matrix, and analyze spatial dimensionality constraints.

## Core Concepts

### 1. The Bag-of-Words (BoW) Paradigm
Up to this point, our models have relied heavily on sequential ordering ($N$-grams). The **Bag-of-Words (BoW)** model 
discards word order and syntactic structure, representing each document solely by the frequency of its vocabulary 
terms. Instead, it treats a document as an unstructured "bag" of individual tokens.

The underlying feature representation is a simple frequency count of how often each unique vocabulary term appears in a
given document.

### 2. High-Dimensional Vector Spaces
When we vectorize a document collection, the global vocabulary size $|V|$ forms the literal dimensions of our geometric 
space.
* Every unique word in the training corpus is assigned a fixed index.
* A single document is represented as a dense or sparse numerical vector $\mathbf{x} \in \mathbb{R} ^{|V|}$.

### 3. The Sparsity Bottleneck
In real-world production systems, your unique vocabulary size $|V|$ can easily exceed 50k+ terms. However, a typical 
short document might only contain 10 or 15 unique words.
* This leaves the vast majority of positions in any given document vector filled with zeros.
* Storing these long, mostly empty arrays as dense NumPy structures wastes significant system RAM and processing cycles,
which introduces severe computational bottlenecks into downstream linear engines.