# Course 1: Natural Language Processing Essentials

This directory contains the theoretical foundations, mathematical derivations, and deterministic Python implementations for
classical Natural Language Processing (NLP) and Computational Linguistics (CL). The curriculum progresses from text
representation and linguistic preprocessing through statistical language modeling and classical machine learning pipelines,
establishing the foundation required for later neural architectures.


## Technical Specifications & Environment

To ensure deterministic execution and reproducibility across all implementations, this course uses the following software stack:

- **Runtime Environment:** Python 3.11+
- **Core NLP Framework:** spaCy v3.7+ (`en_core_web_sm`)
- **Scientific Computing:** scikit-learn v1.4+


# Curriculum Checklist

## Module 1: Text Representation & Tokenization

- [x] **Day 1: Character Encodings, Bytes, and UTF-8**
  - **Files**
    - `concept_notes/encodings.md`
    - `code/encoding_tests.py`

- [x] **Day 2: Unicode Normalization (NFC vs. NFD)**
  - **Files**
    - `concept_notes/unicode_normalization.md`
    - `code/normalize_text.py`

- [x] **Day 3: Whitespace vs. Deterministic Regex Tokenizers**
  - **Files**
    - `concept_notes/tokenization_tests.md`
    - `code/regex_tokenizer.py`


## Module 2: Linguistic Preprocessing & Normalization

- [X] **Day 4: Structural Noise Stripping (HTML/JSON), Case-Folding & Stop-word Removal**
  - **Files**
    - `concept_notes/noise_removal.md`
    - `code/clean_pipeline.py`

- [X] **Day 5a: Rule-Based Stemming (Porter & Lancaster)**
  - **Files**
    - `concept_notes/stemming_analysis.md`
    - `code/stemmer_benchmarks.py`

- [X] **Day 5b: Morphological Lemmatization via spaCy**
  - **Files**
    - `concept_notes/morphology_comparison.md`
    - `code/spacy_lemmatizer.py`

- [X] **Day 6: Part-of-Speech (POS) Tagging & Noun Chunking**
  - **Files**
    - `concept_notes/pos_tagging.md`
    - `code/pos_extractor.py`


## Module 3: Statistical Language Modeling

- [X] **Day 7: Building Unigram, Bigram & Trigram Frequency Distributions**
  - **Files**
    - `concept_notes/n-gram_matrices.md`
    - `code/build_ngrams.py`

- [X] **Day 8: Maximum Likelihood Estimation (MLE) for N-gram Language Models**
  - **Files**
    - `concept_notes/mle_derivation.md`
    - `code/mle_predictor.py`

- [X] **Day 9a: Laplace (Add-One) & Lidstone Smoothing**
  - **Files**
    - `concept_notes/smoothing_theory.md`
    - `code/smoothed_predictor.py`

- [X] **Day 9b: Absolute Discounting & Kneser-Ney Smoothing**
  - **Files**
    - `concept_notes/kneser_ney.md`
    - `code/kneser_ney_baseline.py`


## Module 4: Classical Vector Space Models & Pipelines

- [X] **Day 10: The Bag-of-Words (BoW) Vector Space Model**
  - **Files**
    - `concept_notes/vector_spaces.md`
    - `code/bow_vectorizer.py`

- [X] **Day 11: Term Frequency-Inverse Document Frequency (TF-IDF)**
  - **Files**
    - `concept_notes/tfidf_formulation.md`
    - `code/matrix_tfidf.py`

- [X] **Day 12: End-to-End Text Classification Pipelines**
  - **Files**
    - `concept_notes/classification_pipeline.md`
    - `code/classification_pipeline.py`