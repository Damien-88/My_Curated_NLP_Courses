"""
Day 11: Term Frequency - Inverse Document Frequency Engine
This script constructs a mathematically sound TF-IDF matrix completely from
scratch, handling document frequency tracking and log-scaled weighting.
"""
import math
import re

class ManualTFIDFVectorizer:
    """ A manual implementation of the TF-IDF vectorizer."""
    def __init__(self):
        self.vocabulary = {}
        self.idf_dict = {}
        self.token_pattern = re.compile(r'\w+')

    def tokenize(self, text):
        """Tokenizes input text into lowercase word tokens."""
        return self.token_pattern.findall(text.lower())
    
    def fit(self, raw_documents):
        """Learns the vocabulary and calculates global IDF values"""
        total_docs = len(raw_documents)
        unique_tokens = set()

        # Phase 1: Establish vocabulary indices
        for doc in raw_documents:
            unique_tokens.update(self.tokenize(doc))

        for index, token in enumerate(sorted(unique_tokens)):
            self.vocabulary[token] = index

        # Phase 2: Calculate Document Frequency (DF) for each term
        for term in self.vocabulary:
            docs_with_term = sum(
                1 for doc in raw_documents if term in self.tokenize(doc)
                )
            
            # Mathematical IDF with smooth padding to prevent division errors
            self.idf_dict[term] = math.log10(total_docs / (1 + docs_with_term))

    def transform(self, raw_documents):
        """Transforms documents into dense TF-IDF statistical vectors."""
        matrix = []
        vocab_size = len(self.vocabulary)

        for doc in raw_documents:
            vector = [0.0] * vocab_size
            tokens = self.tokenize(doc)

            # Simple count mapping
            for token in tokens:
                if token in self.vocabulary:
                    vector[self.vocabulary[token]] += 1.0

            # Apply individual weights using pre-calculates IDF matrix values
            for token in set(tokens):
                if token in self.vocabulary:
                    idx = self.vocabulary[token]
                    raw_tf = vector[idx]
                    vector[idx] = round(raw_tf * self.idf_dict[token], 4)

            matrix.append(vector)

        return matrix
    
if __name__ == "__main__":
    training_corpus = [
        "The data engine runs cleanly.",
        "The automated pipeline fails.",
        "Clean raw data feeds the pipeline engine."
    ]

    tfidf = ManualTFIDFVectorizer()
    tfidf.fit(training_corpus)
    tfidf_matrix = tfidf.transform(training_corpus)

    print("Production TF-IDF Geometric Vector Engine\n")
    print("Calculated Global Inverse Document Frequency (IDF) Metrics:\n")

    for term, val in sorted(tfidf.idf_dict.items(), key=lambda x: x[1]):
        print(f"\tTerm: {term:<15} | Log IDF Score: {val:.4f}")

    print("\nGenerated Document-Term Matrix (TF-IDF Weighting):\n")

    for i, vector in enumerate(tfidf_matrix):
        print(f"\tDocument {i + 1} Vector: {vector}")