"""
Day 9: Interpolated Kneser-Ney Bigram Language Model
Implements absolute discounting and continuation probability tracking from 
scratch to solve vocabulary sparsity using interpolated lower-order 
distributions.
"""
import math
from collections import Counter

class KneserNeyLanguageModel:
    def __init__(self, unigram_counts, bigram_counts, discount = 0.75):
        self.unigrams = unigram_counts
        self.bigrams = bigram_counts
        self.d = discount
        
        # Calculate denominator for continuation probability globally
        self.total_unique_bigram_types = len(self.bigrams)
        
        # Precompute continuation counts for all unique target words
        self.continuation_counts = Counter()

        # Precompute continuation counts for each context
        self.unique_extensions = Counter()
        
        for context, word in self.bigrams.keys():
            self.continuation_counts[word] += 1
            self.unique_extensions[context] += 1

    def get_continuation_probability(self, word):
        """
        P_continuation(w) = count of unique histories word completes / total 
        unique bigram types
        """
        num_histories = self.continuation_counts.get(word, 0)

        if self.total_unique_bigram_types == 0:
            return 0.0
        
        return num_histories / self.total_unique_bigram_types

    def calculate_kn_probability(self, context, word):
        """Computes the full Interpolated Kneser-Ney parameter for a bigram state."""
        context_count = self.unigrams.get(context, 0)
        p_cont = self.get_continuation_probability(word)
        
        # If the context has never been seen in training, fallback to 
        # continuation probability (simplification)
        if context_count == 0:
            return p_cont
            
        bigram = (context, word)
        bigram_count = self.bigrams.get(bigram, 0)
        
        # 1. Absolute Discounted Frequency Component
        assigned_mass = max(bigram_count - self.d, 0.0) / context_count
        
        # 2. Compute lambda interpolation weight
        # Count unique words that can follow this specific context token
        unique_extensions = self.unique_extensions.get(context, 0)
        lam = (self.d / context_count) * unique_extensions
        
        return assigned_mass + (lam * p_cont)

    def score_sentence(self, sentence_tokens):
        """Scores a complete token sequence in log space."""
        log_prob_sum = 0.0
        
        for i in range(len(sentence_tokens) - 1):
            context = sentence_tokens[i]
            word = sentence_tokens[i + 1]
            
            prob = self.calculate_kn_probability(context, word)

            # Protect against isolated absolute structural zero outcomes
            if prob <= 0.0:
                return float('-inf')
                
            log_prob_sum += math.log2(prob)
            
        return log_prob_sum


if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))
    from build_ngrams import StatisticalNGramCounter
    
    corpus = "The data engine runs. The data pipeline fails. Clean data creates " \
    "a clean engine."
    
    counter = StatisticalNGramCounter()
    uni_counts, bi_counts = counter.generate_counts(corpus)
    
    model = KneserNeyLanguageModel(uni_counts, bi_counts, discount=0.75)
    
    # Let's test the baseline sequence with the unseen token combination
    unseen_sequence = ["<s>", "clean", "pipeline", "fails", "</s>"]
    
    print("Interpolated Kneser-Ney Model Baseline")
    print(f"Target Sequence: {unseen_sequence}")
    
    kn_score = model.score_sentence(unseen_sequence)
    print(f"Kneser-Ney Log-Score: {kn_score:.4f}")
    
    # Calculate Perplexity to keep parsing tracking consistent
    n = len(unseen_sequence) - 1
    perplexity = 2 ** (-kn_score / n)
    print(f"Kneser-Ney Perplexity: {perplexity:.4f}")