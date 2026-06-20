# My Curated NLP Courses

A comprehensive graduate-level repository documenting a ground-up, deterministic approach to Natural Language Processing 
(NLP) and Computational Linguistics (CL). This repository maps foundational statistical mechanics up to modern deep 
architectures, specifically viewed through the lens of cross-lingual structural analysis and multilingual scaling 
constraints.


## System Architecture & Repository Layout

This repository is strictly organized into modules matching the execution order of the curriculum blocks. Each course 
directory contains 4 module directory that contain two core folders: `concept_notes/` and `code`.


## Curriculum Blueprint & Tracking

### Course 1: Natural Language Processing Essentials
**Focus:** Foundational Linguistic Structure & Deterministic Pipelines

- [X] **Module 1: Text Representation & Tokenization**
  - [X] *The Text Lifecycle:* Strings, streams, Unicode normalization (NFC vs. NFD), and character encodings.
  - [X] *Tokenization Paradigms:* Whitespace vs. rule-based regex tokenization.
  - [X] *Implementation Mapping:* Building custom regex tokenizers vs. rule-based engines.
- [X] **Module 2: Linguistic Preprocessing & Normalization**
  - [X] *Noise Removal:* Stripping HTML/JSON, case folding, and stop-word removal strategies.
  - [X] *Stemming vs. Lemmatization:* Algorithmic truncation (Porter, Lancaster) vs. context-aware morphological analysis.
  - [X] *Part-of-Speech (POS) Tagging:* Penn Treebank conventions, dependency tracking, and noun chunk extraction.
- [ ] **Module 3: Statistical Language Modeling**
  - [X] *The $N$-gram Architecture:* Unigram, bigram, and trigram probability distributions.
  - [X] *Maximum Likelihood Estimation (MLE):* Math bounds for sentence generation and text completion.
  - [ ] *The Sparsity Problem:* Laplace (add-one), Lidstone, and Kneser-Ney smoothing equations.
- [ ] **Module 4: Classical Vector Space Models & Pipelines**
  - [ ] *Bag-of-Words (BoW):* Frequency counting and vector space dimensionality constraints.
  - [ ] *TF-IDF Matrix Generation:* Term Frequency-Inverse Document Frequency mathematical formulations.
  - [ ] *End-to-End Pipelines:* Text classifiers combining TF-IDF and Linear Models (Logistic Regression).

### Course 2: Advanced Tokenization and Sentiment Analysis
**Focus:** Subword Processing, Information Extraction, and Machine Learning Baselines

- [ ] **Module 1: Subword Tokenization Algorithms**
  - [ ] *The Out-of-Vocabulary (OOV) Solution:* Why traditional word-level models fail.
  - [ ] *Byte-Pair Encoding (BPE):* Frequency merges at the character/byte level.
  - [ ] *Alternative Tokenizers:* WordPiece (BERT) vs. SentencePiece (Unigram-based, language-agnostic).
- [ ] **Module 2: Named Entity Recognition (NER)**
  - [ ] *Sequence Labeling Frameworks:* IO, BIO, and BILOU tagging schemes.
  - [ ] *Statistical Models for NER:* Conditional Random Fields (CRFs) and transition matrices.
  - [ ] *Production Inference:* Evaluating pre-trained NER engines and custom entity rulers.
- [ ] **Module 3: Sentiment & Emotion Classification**
  - [ ] *Lexicon-Based Approaches:* Lexical analysis utilizing VADER and TextBlob.
  - [ ] *Supervised ML Pipelines:* Dense representations for multi-class/multi-label tasks.
  - [ ] *Metrics for Unbalanced Data:* Macro/Micro F1-scores, Precision-Recall curves, and Confusion Matrices.
- [ ] **Module 4: Real-World Data Processing & Modeling**
  - [ ] *Pipeline Orchestration:* Handling imbalanced classes, missing data, emojis, and slang.
  - [ ] *Model Optimization:* Hyperparameter tuning workflows to baseline classification systems.

### Course 3: Neural Models and Machine Translation
**Focus:** Deep Learning Architectures, Autoregressive Models, and Fine-Tuning

- [ ] **Module 1: Recurrent Architectures for Sequence Data**
  - [ ] *The Vanishing/Exploding Gradient Problem:* Mathematical limits of Vanilla RNNs over long sequences.
  - [ ] *Gated Architectures:* Long Short-Term Memory (LSTM) networks and Gated Recurrent Units (GRUs).
  - [ ] *Bidirectional Architectures:* Capturing sequential past and future context simultaneously.
- [ ] **Module 2: The Transformer Architecture**
  - [ ] *The Attention Revolution:* Breaking the sequential bottleneck of RNNs.
  - [ ] *Scaled Dot-Product & Multi-Head Self-Attention:* Formulating Query, Key, and Value ($Q, K, V$) matrices.
  - [ ] *Structural Mechanics:* Positional encodings, Layer Normalization, Residual Connections, and Feed-Forward Networks.
- [ ] **Module 3: Pre-trained Contextual Encoders**
  - [ ] *Masked Language Modeling (MLM):* Bidirectional encoders (BERT, RoBERTa).
  - [ ] *Downstream Adaptation:* Weights loading, classification heads, and Parameter-Efficient Fine-Tuning (PEFT/LoRA).
- [ ] **Module 4: Encoder-Decoder Models & Sequence-to-Sequence (Seq2Seq)**
  - [ ] *Autoregressive Models:* Classic Encoder-Decoder frameworks for cross-lingual tasks.
  - [ ] *Neural Machine Translation (NMT):* Sequence-to-sequence networks (MarianMT, T5).
  - [ ] *Generation Strategies:* Greedy Search, Beam Search, Temperature scaling, and Top-$k$/Top-$p$ (Nucleus) sampling.


## Global Reference System

The theoretical notes in this repository are cross-referenced directly with the following primary academic frameworks:
* **Textbook:** Daniel Jurafsky & James H. Martin, *Speech and Language Processing* (3rd Edition Draft).
* **Taxonomy Reference:** *World Atlas of Language Structures (WALS)* for structural/typological validation.
* **Testing Sandbox:** Hugging Face Model Hub Browser Widgets for non-code model output verification.