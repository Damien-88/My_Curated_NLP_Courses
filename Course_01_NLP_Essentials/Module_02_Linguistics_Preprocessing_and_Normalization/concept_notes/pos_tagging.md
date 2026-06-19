# Day 6: Part-of-Speech (POS) Tagging and Noun Chunking

### Learning Objective
Understand how sequence models assign grammatical tags to tokens, analyze the structure of the Penn Treebank tagset, 
and implement dependency-based noun chunking to isolate base noun phrases for information extraction.

## Core Concepts

### 1. Fine-Grained vs. Coarse-Grained POS Tags
Linguistic pipelines assign two distinct layers of Part-of-Speech classifications to tokens:
* **Coarse-Grained (Universal POS)**: Broad, high-level categories that apply across almost all languages 
  (e.g., `NOUN`, `VERB`, `ADJ`, `ADV`)
* **Fine-Grained (Penn Treebank Tagset)**: Specific grammatical subdivisions that capture tense, plurality, and case
  configurations for English text.

For example:
* `NN`: Noun, singular or mass (*wall*)
* `NNS`: Noun, plural (*flies*)
* `VB`: Verb, base form (*sit*)
* `VBZ`: Verb, 3rd person singular present (*flies*)

### 2. Dependency Graph Parsing
Tokens do not sit in a vacuum; they exist in a hierarchical dependency tree. Every sentence contains a "root" token 
(typically the main finite verb or predicate head of the sentence) that governs the structural relationships among 
surrounding subjects, objects, and modifiers.

### 3. Noun Phrase (NP) Chunking
In raw text processing, single words often fail to capture semantic concepts. For example, in the phrase *"The advanced
multi-threaded processing engine"*, looking at the word *"engine"* by itself strips out the core context.
* **Noun Chunking** can be performed using either POS-pattern chunking or dependency parsing. In dependency-based 
  approaches, noun phrases are extracted by identifying a head noun and its syntactic dependents (such as determiners, 
  adjectives, and compound modifiers).
* This provides clean, non-overlapping phrases that capture complete structural concepts.