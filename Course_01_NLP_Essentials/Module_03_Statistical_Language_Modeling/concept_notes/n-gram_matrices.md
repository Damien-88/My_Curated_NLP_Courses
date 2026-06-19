# Day 7: Building Unigram and Bigram Frequency Distributions

### Learning Objective
Understand the mechanics of statistical sequencing, learn how to slice tokens into contiguous windows of length $N$, and
build frequency counting tables for unigrams and bigrams.

## Core Concepts

### 1. What is an $N$-gram?
An $N$-gram is a contiguous sequence of $N$ tokens extracted from a given stream of text.
* **Unigram ($N=1$)**: Individual tokens treated as sequences of length 1 (e.g., `["the", "cat", "sat", "on"]`).
* **Bigram ($N=2$)**: Pairs of adjacent tokens capturing local two-word context windows 
  (e.g., `["the", "cat"], ["cat", "sat"], ["sat", "on"]`).
* **Trigram ($N=3$)**: Three contiguous tokens (e.g., `["the", "cat", "sat"], ["cat", "sat", "on"]`).

### 2. Slicing with Sliding Windows
To construct an $N$-gram collection, a sliding window moves across a token sequence, stepping forward by exactly one 
token index per shift:

```text
Tokens: [ "the", "data", "pipeline", "runs" ]
          └─────┴─────┘  --> Bigram 1: ("the", "data")
                  └─────┴────────┘  --> Bigram 2: ("data", "pipeline")
                            └──────────┴──────┘  --> Bigram 3: ("pipeline", "runs")
```