"""
Day 9: Smoothed Bigram Language Model
This script implements Laplace and Lidstone smoothing to eliminate negative 
infinity metrics caused by structural data sparsity.
"""

import math
from collections import Counter

class SmoothedLanguageModel:

    def __init__(self, unigram_counts, bigram_counts, vocabulary_size):
        self.unigrams = unigram_counts
        self.bigrams = bigram_counts
        self.vocab_size = max(1, vocabulary_size)

    def calculate_lidstone_probability(self, context, word, alpha):
        """Computes Add-Alpha (Lidstone/Laplace) smoothed bigram probability."""
        bigram = (context, word)
        bigram_count = self.bigrams.get(bigram, 0)
        context_count = self.unigrams.get(context, 0)

        # Mathematical Equation implementation
        numerator = bigram_count + alpha
        denominator = context_count + (alpha * self.vocab_size)

        return numerator / denominator
    
    def score_sentence(self, sentence_tokens, alpha):
        """Scores a token chain using log space transformations."""
        log_prob_sum = 0.0

        for i in range(len(sentence_tokens) - 1):
            context = sentence_tokens[i]
            word = sentence_tokens[i + 1]

            probability = self.calculate_lidstone_probability(
                          context, word, alpha
                          )
            
            if probability <= 0.0:
                continue
            
            log_prob_sum += math.log2(probability)


        return log_prob_sum
    
    def perplexity(self, sentence_tokens, alpha):
        """
        Computes perplexity of a sentence: perplexity = 2^(-1/N * log_prob_sum)
        """

        n = len(sentence_tokens) - 1

        if n <= 0:
            return float("inf")
        
        log_prob = self.score_sentence(sentence_tokens, alpha)

        return 2 ** (-log_prob / n)
    
if __name__ == "__main__":

    from build_ngrams import StatisticalNGramCounter
    
    corpus = "The data engine runs. The data pipeline fails. Clean data creates a clean engine."
    
    counter = StatisticalNGramCounter()
    uni_counts, bi_counts = counter.generate_counts(corpus)
    
    # Extract unique vocabulary size (|V|)
    unique_vocabulary = set(uni_counts.keys())
    vocab_size = len(unique_vocabulary)
    
    # Instantiate smoothed parameters model
    model = SmoothedLanguageModel(uni_counts, bi_counts, vocab_size)
    
    # Re-testing the problematic sequence that failed under raw MLE on Day 8
    unseen_sequence = ["<s>", "clean", "pipeline", "fails", "</s>"]
    
    print("Smoothed Bigram Language Model Evaluation\n")
    print(f"Vocabulary Size (|V|): {vocab_size}")
    print(f"Test Sequence: {unseen_sequence}\n")

    # Laplace smoothing
    laplace_log = model.score_sentence(unseen_sequence, alpha=1.0)
    laplace_ppl = model.perplexity(unseen_sequence, alpha=1.0)

    print(f"Laplace (α=1.0) Log-Score:   {laplace_log:.4f}")
    print(f"Laplace (α=1.0) Perplexity:  {laplace_ppl:.4f}")

    # Lidstone smoothing
    lidstone_log = model.score_sentence(unseen_sequence, alpha=0.1)
    lidstone_ppl = model.perplexity(unseen_sequence, alpha=0.1)

    print(f"\nLidstone (α=0.1) Log-Score:  {lidstone_log:.4f}")
    print(f"Lidstone (α=0.1) Perplexity: {lidstone_ppl:.4f}")