# Day 9: Laplace (Add-One) and Lidstone (Add-$\alpha$) Smoothing

### Learning Objective
Understand the mathematical mechanics of smoothing frequency estimates, derive the formulations for Laplace (Add-One) 
and Lidstone (Add-$\alpha$) configurations, and analyze how probability mass shifts to handle vocabulary sparsity.

## Mathematical Architecture

### 1. Laplace Smoothing
To prevent any transition from evaluating to zero, Laplace smoothing adds a pseudocount of $1$ to every single 
possibility count in the bigram transition space.

To maintain proper mathematical probability constraints (ensuring that all conditional probabilities for a given context 
word sum to $1.0$), the denominator must scale by the total size of your model's unique vocabulary, $|V|$:

$$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + |V|}$$

* $C(w_{i-1}, w_i)$: Raw bigram frequency.
* $C(w_{i-1})$: Raw context unigram frequency.
* $|V|$: Total count of unique vocabulary words across the training corpus (including boundary markers like `<s>` and 
  `</s>`).

### 2. Lidstone Smoothing
While Laplace removes the zero-probability failure mode, adding a full $1$ to every single unseen state redistributes 
too much probability mass from observed events to unseen events, a problem known as over-smoothing.

Lidstone smoothing introduces a tuning parameter, $\alpha$ (typically a fraction like $0.1$ or $0.05$), to scale the 
smoothing adjustment:

$$P_{\text{Lidstone}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + \alpha}{C(w_{i-1}) + \alpha |V|}$$

## Vocabulary Size Significance
The denominator metric $|V|$ acts as a critical anchor parameter. It must reflect the total pool of unique words known 
to the overall vocabulary. If the vocabulary size $|V|$ is inconsistently defined when estimating or applying the 
smoothed probabilities, the resulting distribution may become improperly normalized, violating the requirement that 
conditional probabilities sum to $1.0$, introducing systemic errors into downstream models.