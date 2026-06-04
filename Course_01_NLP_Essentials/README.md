# Course 1: Natural Language Processing Essentials

This directory houses all theoretical frameworks, mathematical derivations, and deterministic Python implementations for foundational computational linguistics. The focus is on understanding text at the byte, character, token, and statistical frequency levels before introducing deep neural architectures.

## Directory Structure

```text
Course_1_NLP_Essentials/
│
├── README.md               # This file (Course tracking and local system documentation)
│
├── concept_notes/          # Core algorithmic frameworks, math bounds, and Python scripts
│   ├── encodings.md
│   ├── encoding_tests.py
│   └── ... [Other daily concept files]
│
└── language_logs/          # Script executions and analysis across different linguistic typologies
    ├── tokenization_tests.md
    └── regex_tokenizer.py

## Technical Specifications & Environment

To maintain deterministic execution across all scripts, the code files inside this course utilize standard library Python engines paired with pinned scientific computing and NLP distributions:

* **Runtime Environment**: Python 3.11+
* **Core NLP Framework**: spaCy v3.7+ (utilizing the en_core_web_sm model)
* **Vectorization & Matrix Operations**: scikit-learn v1.4+

## Daily Curriculum Checklist

### Module 1: Text Representation & Tokenization
- [ ] **Day 1: Character Encodings, Bytes, and UTF-8** *Files*: `concept_notes/encodings.md`, `concept_notes/encoding_tests.py`
- [ ] **Day 2: Unicode Normalization (NFC vs. NFD)** *Files*: `concept_notes/unicode_normalization.md`, `concept_notes/normalize_text.py`
- [ ] **Day 3: Whitespace vs. Deterministic Regex Tokenizers** *Files*: `language_logs/tokenization_tests.md`, `language_logs/regex_tokenizer.py`

### Module 2: Linguistic Preprocessing & Normalization
- [ ] **Day 4: Structural Noise Stripping (HTML/JSON) & Case-Folding** *Files*: `concept_notes/noise_removal.md`, `concept_notes/clean_pipeline.py`
- [ ] **Day 5: Rule-Based Stemming (Porter & Lancaster)** *Files*: `concept_notes/stemming_analysis.md`, `concept_notes/stemmer_benchmarks.py`
- [ ] **Day 6: Morphological Lemmatization via spaCy** *Files*: `language_logs/morphology_comparison.md`, `language_logs/spacy_lemmatizer.py`
- [ ] **Day 7: Part-of-Speech (POS) Tagging & Noun Chunking** *Files*: `concept_notes/pos_tagging.md`, `concept_notes/pos_extractor.py`

### Module 3: Statistical Language Modeling
- [ ] **Day 8: Building Unigram and Bigram Frequency Distributions** *Files*: `concept_notes/ngram_matrices.md`, `concept_notes/build_ngrams.py`
- [ ] **Day 9: Maximum Likelihood Estimation (MLE) for Sequences** *Files*: `concept_notes/mle_math.md`, `concept_notes/mle_estimator.py`
- [ ] **Day 10: Laplace (Add-One) & Lidstone Smoothing Mechanics** *Files*: `concept_notes/laplace_smoothing.md`, `concept_notes/laplace_smoother.py`
- [ ] **Day 11: Absolute Discounting & Kneser-Ney Smoothing Theory** *Files*: `concept_notes/kneser_ney.md`, `concept_notes/kneser_ney_baseline.py`

### Module 4: Classical Vector Space Models & Pipelines
- [ ] **Day 12: The Bag-of-Words (BoW) Vector Space Model** *Files*: `concept_notes/bag_of_words.md`, `concept_notes/vector_bow.py`
- [ ] **Day 13: Term Frequency-Inverse Document Frequency (TF-IDF) Math** *Files*: `concept_notes/tfidf_formulation.md`, `concept_notes/matrix_tfidf.py`
- [ ] **Day 14: End-to-End Classification Pipelines** *Files*: `concept_notes/classification_pipeline.py`