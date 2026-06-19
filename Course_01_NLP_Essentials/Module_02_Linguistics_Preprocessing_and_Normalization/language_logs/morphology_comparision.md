# Day 5b: Morphological Lemmatization via spaCy

### Learning Objective
Understand the core differences between heuristic stemming and contextual lemmatization, analyze how statistical 
lemmatization systems utilize Part-of-Speech tags to determine dictionary base forms (lemmas), and evaluate performance 
across complex morphologically rich words.

## Core Concepts

### 1. What is Lemmatization?
Unlike rule-based stemming, which blindly slices suffixes off words using a static list of rules, **Lemmatization** 
uses a full linguistic dictionary and morphological analysis to accurately return the true, grammatically correct base
form of a word-know as its **Lemma**.

### 2. Contextual Resolution via POS Tagging
A word can change its lemma entirely depending on how it functions in a sentence. 
For example, consider the word **flies**:
* Sentence A: *"The **flies** gathered on the wall."* $\rightarrow$ Here, "flies" is a **Noun** (plural). 
  The correct lemma is **"fly"**.
* Sentence B: *"Time **flies** when you are coding."* $\rightarrow$ Here, "flies" is a **Verb** (third-person singular). 
  The correct lemma is **"fly"**.

Modern engines (like `spaCy`) look at the surrounding tokens to assign a Part-of-Speech (POS) tag before running the 
lookup, ensuring the correct dictionary form is retrieved.

## Technical Comparison Matrix

|    Characteristic    |          Stemming (Porter/Lancaster)           |            Lemmatization (spaCy)           |
|         :---         |                      :---                      |                    :---                    |
|  **Operation Type**  |  Suffix truncation rules (heuristic strings).  | Dictionary lookup + Morphological analysis.|
|  **Context Aware?**  | No. Looks at the word completely in isolation. |     Yes. Considers surrounding syntax.     |
|  **Output Validity** |Often returns non-words (`destabil` / `alumnu`).| Typically returns a real dictionary word.  |
|**Computational Cost**|       Ultra-low (instant regex matches).       |Higher (requires loading linguistic models).|