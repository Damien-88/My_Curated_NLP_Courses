"""
Day 8: Maximum Likelihood Estimation (MLE) Sequence Predictor
This script build on top of the Day 7 frequency distributions to compute 
conditional bigram probablilites and evaluate sentence structure in log space.
"""

import math
from collections import Counter
import re

class MLELanguageModel:
    def __init__(self, unigram_counts: Counter, birgram_counts: Counter):
        self.unigrams = unigram_counts
        self.bigrams = birgram_counts

    def calculate_bigram_probability(self, context, word):
        """Computes the raw MLE parameterL C(w_{i-1}, w_i) / C(w_{i-1})"""

        bigram = (context, word)
        bigram_count = self.bigrams.get(bigram, 0)
        context_count = self.unigrams.get(context, 0)

        if context_count == 0:
            return 0.0
        
        return bigram_count / context_count
    
    def score_sentence(self, sentence_tokens):
        """Calculates total log probability sequence score to prevent undeflow"""
        
        log_prob_sum = 0.0

        for i in range(len(sentence_tokens) - 1):
            context = sentence_tokens[i]
            word = sentence_tokens[i+1]
            prob = self.calculate_bigram_probability(context, word)

            if prob == 0.0:
                # Assign negative infinity for completely unseen transitions
                # (Sparsity Failure)
                return float('-inf')
            
            log_prob_sum += math.log2(prob)

        return log_prob_sum
    
if __name__ == "__main__":
    # Import the clean counting mechanics from Day 7 directly
    from build_ngrams import StatisticalNGramCounter

    corpus = "The data engine runs. The data pipeline fails. Clean data " \
             "creates a clean engine."
    
    counter = StatisticalNGramCounter()
    uni_counts, bi_counts = counter.generate_counts(corpus)

    # Instantiate our model parameters
    model = MLELanguageModel(uni_counts, bi_counts)

    print("MAXIMUM LIKELIHOOD ESTIMATION MODEL BASELINE\n")

    # Samle 1: A highly predictable sequence based on training facts
    known_sequence = ["<s>", "the", "data", "engine", "runs", "</s>"]
    known_score = model.score_sentence(known_sequence)

    print(f"Sequence: {str(known_sequence):<50}")
    print(f"Log Probability Score: {known_score:.4f}\n")

    # Sample 2: A sequence with an unseen word transition (Sparsity Problem)
    unseen_sequence = ["<s>", "clean", "pipeline", "fails", "</s>"]
    unseen_score = model.score_sentence(unseen_sequence)

    print(f"Sequence: {str(unseen_sequence):<50}")
    print(f"Log Probability Score: {unseen_score:.4f}")