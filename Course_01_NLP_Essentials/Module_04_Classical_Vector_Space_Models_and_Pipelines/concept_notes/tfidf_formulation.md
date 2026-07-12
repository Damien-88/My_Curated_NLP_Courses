# Day 11: TF-IDF Mathematical Formulations

### Learning Objective
Deconstruct the mathematical theory behind Term Frequency-Inverse Document Frequency (TF-IDF), derive its components, \
and understand how log-scaling controls feature explosions in a vector space.

## Mathematical Architecture

### 1. Term Frequency (TF)
Term Frequency measures how often a specific word $t$ appears inside a single targeted document $d$. While there are \
multiple ways to scale this metric, we will stick to the standard raw frequency count representation:

$$\text{TF}(t, d) = C(t, d)$$

Where $C(t, d)$ is the raw frequency count of token $t$ inside document $d$.

### 2. Inverse Document Frequency (IDF)
Inverse Document Frequency measures how common or rare a word is across your entire document collection. If a word \
appears in every single document in your corpus, its predictive power drops to zero.

To account for this, we divide the total number of documents $M$ by the number of documents that contain the target \
term $t$. We then apply a base-e ($\ln$) or base-10 ($\log_{10}$) log transformation to prevent the metric from scaling \
linearly:

$$\text{IDF}(t, D) = \log \left(\frac{M}{1 + |\{d \in D:t \in d\}|} \right)$$

* $M$: Total number of documents in the corpus collection.

* $|\{d \in D : t \in d\}|$: The document frequency ($\text{DF}$), meaning the count of documents where term $t$ appears.

* **The $+1$ Smooth**: We add $1$ to the denominator to ensure the IDF remains well-defined when a term has a document \
frequency of zero, preventing division by zero.



### 3. The Combined Matrix Formula
The final TF-IDF weight is calculated by multiplying these two distinct components together:

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

A term achieves a high TF-IDF weight when it occurs frequently within a small subset of documents, making it highly \
descriptive for those specific texts.