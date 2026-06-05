# Day 2: Unicode Normalization (NFC vs. NFD)

### Learning Objective
Understand the difference between canonical equivalence paradigms (NFC and NFD), analyze how single characters can have multiple unique byte-level representations, and implement structural normalization to prevent token duplication in NLP models.


## Core Concepts

### 1. The Multi-Representation Problem
In Unicode, certain accented or modified characters can be constructed in two distinct ways:
1. **Precomposed Character**: A single unique code point that represents the combined symbol.
2. **Decomposed Character Sequence**: A base character code point followed immediately by a separate combining diacritic mark code point.

Visually, these look identical on a monitor, but computationally, their underlying byte streams are completely different.

### 2. Canonical Equivalence Standards (NFC vs. NFD)
To fix this variance, the Unicode Consortium defined normalization standards to force text into a single consistent structural state:

* **NFD (Normalization Form Canonical Decomposition)**: Translates all characters into their maximally decomposed components (splits them up).
* **NFC (Normalization Form Canonical Composition)**: Translates characters into their decomposed states first, then recombines them into precomposed code points wherever possible (glues them together).



### 3. Linguistic Impact Matrix
Consider the character `é` (as seen in words like *café* or *resumé*):
```text
|           Feature           |    NFC (Composition)    |                   NFD (Decomposition)                     |
|             :---            |          :---           |                          :---                             |
|    **Visual Appearance**    |            é            |                            é                              |
|     **Code Points Used**    | `U+00E9` (Single point) | `U+0065` (Letter `e`) + `U+0301` (Combining Acute Accent) |
|      **String Length**      |       1 Character       |                     2 Characters                          |
|     **UTF-8 Hex Bytes**     |    `C3 A9` (2 bytes)    |                 `65 CC 81` (3 bytes)                      |
```

## Why This Matters in NLP Pipelines
If your raw training data contains a mix of un-normalized text, a NLP model will treat the NFC version of a word and the NFD version of the exact same word as two completely unique vocabulary terms. 

This artificially inflates vocabulary size, dilutes word frequency counts, splits semantic weights, and reduces downstream model accuracy.