"""
Day 7: Unigram and Bigram Frequency Generation Engine
This script splits text into sentence-bounded token streams and builds
complete, deterministic frequency distribution counters for unigrams and bigrams.
"""

from collections import Counter
import re

class StatisticalNGramCounter:
    def __init__(self):
        # Basic regex to isolate sentences by periods, exclamation marks, or question marks
        self.sentence_end = re.compile(r'[.!?]+\s*')
        # Isolate alphanumeric strings lowercased
        self.token_pattern = re.compile(r'\w+')

    def preprocess_to_sentences(self, raw_text):
        """Splits raw text into sentences and injects boundary tags."""
        
        clean_sentences = []
        raw_sentences = self.sentence_end.split(raw_text.strip())
        
        for sentence in raw_sentences:
            if not sentence:
                continue
            # Extract lowercase tokens
            tokens = self.token_pattern.findall(sentence.lower())
            if tokens:
                # Inject explicit structural padding boundaries
                bounded_tokens = ["<s>"] + tokens + ["</s>"]
                clean_sentences.append(bounded_tokens)
                
        return clean_sentences

    def generate_counts(self, raw_text):
        """Builds explicit unigram and bigram frequency tables from text."""

        sentences = self.preprocess_to_sentences(raw_text)
        
        unigrams = []
        bigrams = []
        
        for sentence in sentences:
            # 1. Collect Unigrams
            unigrams.extend(sentence)
            
            # 2. Collect Bigrams using an explicit sliding loop window
            for i in range(len(sentence) - 1):
                bigram_pair = (sentence[i], sentence[i+1])
                bigrams.append(bigram_pair)
                
        return Counter(unigrams), Counter(bigrams)


def run_ngram_analysis():
    engine = StatisticalNGramCounter()
    
    # Sample corpus containing repetitive structural phrase choices
    sample_corpus = (
        "The data engine runs. The data pipeline fails. "
        "Clean data creates a clean engine."
    )
    
    unigram_counts, bigram_counts = engine.generate_counts(sample_corpus)
    
    print("Production Frequency Distribution Engine\n")
    print(f"Raw Input Corpus:\n{sample_corpus}")
    
    # Print out Top Unigrams
    print("\nTop 5 Unigram Frequencies:")
    
    for token, count in unigram_counts.most_common(5):
        print(f"Token: {token:<12} | Frequency Count: {count}")
        
    # Print out Top Bigrams
    print("\nTop 5 Bigram Frequencies:")

    for pair, count in bigram_counts.most_common(5):
        pair_string = f"({pair[0]}, {pair[1]})"
        print(f"Sequence: {pair_string:<20} | Frequency Count: {count}")


if __name__ == "__main__":
    run_ngram_analysis()