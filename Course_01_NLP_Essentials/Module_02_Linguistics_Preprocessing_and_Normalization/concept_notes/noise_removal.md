# Day 4: Structural Noise Stripping (HTML/JSON) & Case-Folding

### Learning Objective
Implement deterministic data cleaners to strip structural syntax markup (HTML/JSON tags) from text streams, apply 
case-folding policies uniformly without losing semantic identity, and design an ordered text-cleansing pipeline.

## Core Concepts

### 1. Structural Markup Contamination
When harvesting text from production environments, datasets are rarely clean prose. They are typically wrapped in 
structural serialization formats (like JSON) or document styling markup (like HTML).
* Leaving markup intact forces tokenizers to index tags (e.g., `<div>`, `<a>`, `{"text": ...}`) as part of the core 
  vocabulary
* This pollutes downstream frequency distributions and skews semantic analysis.

### 2. The Regular Expression Stripping Engine
To discard structural tags without destroying the enclosed narrative text, we define strict match-and-replace patterns 
using lookarounds and non-greedy captures:
* **HTML Tag Pattern**: `<[^>]*>` identifies any block starting with a left angle bracket, containing zero or more
  non-right-bracket characters, and ending with a right angle bracket.
* **JSON/Key-Value Key Stripping**: Selective removal of metadata keys while preserving associated string values 
  (e.g., "message": "text" -> "text")

### 3. Case-Folding Frameworks
Case-Folding reduces the vocabulary footprint by converting all text to a uniform casing profile.
* **Standard `.lower()`**: Converts ASCII characters effectively (`"The"` $\rightarrow$ `"the"`).
* **Advanced Case-Folding (`.casefold()`)**: Designed for true multilingual normalization. It aggressively strips 
  structural casing differences unique to specific alphabets. For example, the German lowercase sharp "s" (`ß`)
  converts to `"ss"` under case-folding, allowing models to align accurately across dialects.

## The Preprocessing Pipeline Order of Operations

Text cleansing must follow a strict, logical sequence. Changing the order will corrupt the structural processing:

``` text
[Raw Input Stream] ---> [1. Strip HTML/JSON Markup] ---> [2. Apply Unicode Normalization] ---> 
[3. Uniform Case-Folding] ---> [Clean Tokenizable Text]
```