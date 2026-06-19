# Day 8: Maximum Likelihood Estimation (MLE) and Chain Rule

### Learning Objective
Derive the mathematical formulation for Maximum Likelihood Estimation ($MLE$) in sequence modeling, understand the 
conditional probability chain rule, and calculate sentence-level probabilities from a statistical frequency matrix.

## Mathematical Architecture

### 1. The Chain Rule of Probability
The joint probability of a sequence of tokens $w_1, w_2, \dots, w_n$ is computed via the chain rule:

$$P(w_1, w_2, \dots, w_n) = \prod_{i=1}^{n} P(w_i \mid w_1, w_2, \dots, w_{i-1})$$

To make this computationally tractable, the **Markov Assumption** posits that the probability of a word depends only on
the immediately preceding history window.
* **Unigram Model (Zero-order)**: $P(w_i)$
* **Bigram Model (First-order)**: $P(w_i \mid w_{i-1})$

### 2. Maximum Likelihood Estimation Formulation
To estimate the bigram parameter $P(w_i \mid w_{i-1})$ from a corpus, we divide the count of a specific bigram sequence
by the total frequency of its history state (prefix unigram):

$$P_{MLE}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}$$

Where $C(w_{i-1}, w_i)$ is the bigram frequency count, and $C(w_{i-1})$ is the unigram count of the historical context 
token.

## Computational Bottlenecks: Underflow
When Calculating the joint probability of a long sentence, multiplying values between $0$ and $1$ continuously drops
the product toward zero exponentially:

$$P(S) = P(w_1) \times P(w_2 \mid w_1) \times \dots \times P(w_n \mid w_{n-1})$$

This quickly causes floating-point **arithmetic underflow** in code. To solve this, pipelines operate within 
**log space**. By converting probabilities to log-probabilities, we transform fractional multiplications into stable 
additions:

$$\log P(S) = \sum_{i=1}^{n} \log P(w_i \mid w_{i-1})$$

>**Rule**: Higher log-probability sums mean the sentence structure matches the training data more closely 
>(e.g., $-12.5$ is more likely than $-45.2$).