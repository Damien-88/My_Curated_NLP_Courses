"""
Day 10: Deterministic Bag-of-Words Vectorization Engine
This script constructs a Document-Term Matrix entirely from scratch using 
standard Python utilities, highlighting vocabulary building and geometric vector 
generation.
"""

import re

class ManualBoWVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.token_pattern = re.compile(r'\w+')

    def tokenize(self, text):
        """Ensures lowercase token extraction uniform with preceding modules."""
        
        return self.token_pattern.findall(text.lower())
    
    def fit(self, raw_documents):
        """Builds the master vocabulary index mapping from training documents."""
        self.vocabulary.clear()
        unique_tokens = set()

        for doc in raw_documents:
            unique_tokens.update(self.tokenize(doc))

        # Explicitly sort to ensure absolute deterministic indexing across systems
        for index, token in enumerate(sorted(unique_tokens)):
            self.vocabulary[token] = index

    def transform(self, raw_documents):
        """Generates a raw Document-Term matrix based on the learned vocabulary."""

        matrix = []
        vocab_size = len(self.vocabulary)

        for doc in raw_documents:
            # Initialize a blank numerical vector matching dimensionality size
            vector = [0] * vocab_size
            tokens = self.tokenize(doc)

            for token in tokens:
                if token in self.vocabulary:
                    target_index = self.vocabulary[token]
                    vector[target_index] += 1

            matrix.append(vector)

        return matrix
    
if __name__ == "__main__":
    # Sample corpus mimicking structural server logs or document fragments
    training_corpus = [
        "The data engine runs cleanly.",
        "The automated pipeline fails.",
        "CLean raw data feeds the pipeline engine."
    ]

    vectorizer = ManualBoWVectorizer()
    vectorizer.fit(training_corpus)
    document_term_matrix = vectorizer.transform(training_corpus)

    print("\nProduction Bag-of-Words Vector Engine")

    print("\nLearned System Vocabulary Indexing:")
    print(vectorizer.vocabulary)
    
    rows = len(document_term_matrix)
    cols = len(vectorizer.vocabulary)

    print(f"\nGenerated Document-Term Matrix (Shape {rows} x {cols}):")
    
    for i, vector in enumerate(document_term_matrix):
        print(f"Document {i+1} Vector: {vector} -> Raw \"{training_corpus[i]}\"")