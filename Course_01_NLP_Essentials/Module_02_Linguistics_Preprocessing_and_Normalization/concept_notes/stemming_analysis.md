# Day 5: Rule-Based Stemming (Porter & Lancaster)

### Learning Objective
Understand the mechanics of rule-based inflectional stripping, analyze the structural algorithms behind the Porter and 
Lancaster stemmers, and map the computational errors of over-stemming and under-stemming.


## Core Concepts

### 1. What is Stemming?
Stemming is an aggressive, heuristic process that chops off the ends of words to reduce them to a common base form 
(a "stem"). It relies entirely on structural string-matching rules and ignores grammatical context or part-of-speech 
attributes.

### 2. Algorithmic Implementations

* **The Porter Stemmer**: The industry-standard rule baseline. It applies a sequential series of 5 distinct algorithmic 
  phases. Each phase checks specific suffix rules and maps them to a smaller core block.
  * *Example Rule*: If a word ends in `sses`, replace with `ss` (e.g., `caresses` $\rightarrow$ `caress`).
  * *Design Philosophy*: Conservative and moderate. It tries to preserve recognizable base forms.

* **The Lancaster Stemmer**: A significantly more aggressive, cascading rule system. It applies a large set of 
  aggressive, iterative rules stored in a fixed rule set until no further reductions are possible.
  * *Design Philosophy*: Highly destructive. It optimizes purely for maximum vocabulary reduction, often leaving behind 
    non-word roots.


## Error Paradigms in Rule-Based Systems

Because stemmers do not use a linguistic dictionary, they frequently make two distinct structural errors:

### Over-stemming (False Positives)
When two linguistically distinct words with completely different semantic meanings are mistakenly chopped down to the 
exact same root stem.
* *Example*: `organization` and `organs` both stem to `organ`. A model would treat medical body parts and corporate 
  structures as identical tokens.

### Under-stemming (False Negatives)
When two words that are closely related semantically are left with completely different stems because their suffixes do 
not match standard structural rule phases.
* *Example*: `alumnus` stems to `alumnu`, while `alumni` stems to `alumni`. The model fails to link these singular and 
  plural forms together.