# Day 12: Text Classification and Linear Models

### Learning Objective
Understand how high-dimensional sparse representations feed downstream statistical learning engines, derive basic \
gradient optimizations for binary classification, and baseline an end-to-end processing pipeline.

## Machine Learning Foundations

### 1. The Logistic Regression Classifier
To classify a document vector $\mathbf{x}$, we compute a weighted sum of its features plus a bias term. We then pass \
this value through the activation function $\sigma(z)$ to squash it into a valid probability range between $0$ and $1$:

$$z = \mathbf{w} \cdot \mathbf{x} + b$$

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

* $\mathbf{w} \in \mathbb{R}^{|V|}$: The weight vector matching your vocabulary size.
* $b$: The system intercept bias.

### 2. Gradient Descent Optimization
To train the model parameters, we minimize the binary cross-entropy loss function ($L$) using gradient descent:

$$L = -\frac{1}{M} \sum_{i=1}^{M} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

In each training iteration, the weights are adjusted by calculating the gradient of the loss function with respect to \
the weights:

$$\mathbf{w} \leftarrow \mathbf{w} - \eta \frac{\partial L}{\partial \mathbf{w}}$$

Where $\eta$ is the learning rate parameter controlling optimization step size.