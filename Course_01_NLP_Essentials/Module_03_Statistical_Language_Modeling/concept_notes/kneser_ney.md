# Day 9: Absolute Discounting and Kneser-Ney Smoothing

### Learning Objective
Derive the mathematical mechanics of Absolute Discounting and Kneser-Ney smoothing, understand the continuation \
probability formulation ($P_{\text{continuation}}$), and analyze how interpolation resolves unseen contexts without \
over-smoothing.

## Mathematical Architecture

### 1. Absolute Discounting
Instead of adding artificial counts like Laplace or Lidstone, Absolute Discounting subtracts a fixed absolute mass \
$d$ (where $0<d<1$) from all non-zero bigram counts. This subtracted mass is aggregated and redistributed to a \
lower-order distribution (unigrams for a bigram model):

$$P_{\text{Absolute}}(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})}$$

### 2. Kneser-Ney Smoothing (Interpolated)
Kneser-Ney Smoothing builds directly on absolute discounting but introduces a fundamental insight: lower-order histories \
should not track how frequent a unigram is, but rather how *versatile* it is as a continuation word.

For example, the word "Francisco" is highly frequent in text corpora containing "San Francisco", but it rarely occurs in \
any other context. A standard unigram model will assign it a high probability, making an error in an unseen context like \
`("clean", "Francisco")`. Kneser-Ney fixes this via the **Continuation Probability**:

$$P_{\text{continuation}}(w_i) = \frac{|\{w_{i-1} : C(w_{i-1}, w_i) > 0\}|}{\sum_{w'} |\{w_{i-1} : C(w_{i-1}, w') > 0\}|}$$

The complete Bigram Kneser-Ney interpolation formula reads:

$$P_{\text{KN}}(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})} + \lambda(w_{i-1}) P_{\text{continuation}}(w_i)$$

Where the weight parameter $\lambda(w_{i-1})$ is formulated as:

$$\lambda(w_{i-1}) = \frac{d}{C(w_{i-1})} \cdot |\{w : C(w_{i-1}, w) > 0\}|$$

* $d$: The absolute discount parameter (typically $0.75$).
* $|\{w : C(w_{i-1}, w) > 0\}|$: The unique count of word types that can legally follow the context word $w_{i-1}$.