"""
Day 5: Rule-Based Stemming Engine Comparison (Fixed)
This script implements and benchmarks the Porter and Lancaster stemming
algorithms using NLTK to map out over-stemming and under-stemming anomalies.
"""
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer

def execute_stemming_suite():
    # Explicitly initialize the stemming objects
    porter = PorterStemmer()
    lancaster = LancasterStemmer()

    # Target word categories designed to expose rule-based flaws
    test_vocabulary = [
        # Morphological variations
        "connect", "connected", "connecting", "connection",
        # Over-stemming test targets (Distinct words that shouldn't match)
        "organization", "organize", "organs",
        # Under-stemming test targets (Related words that should match but fail)
        "alumnus", "alumni", "alumnae"
    ]

    print(f"{'Raw Input Word':<16} | {'Porter Stem':<15} | {'Lancaster Stem':<15}")
    print("-" * 55)

    for word in test_vocabulary:
        # We ensure the word is passed as a string explicitly
        p_stem = porter.stem(str(word))
        l_stem = lancaster.stem(str(word))
        print(f"{word:<16} | {p_stem:<15} | {l_stem:<15}")
        
    print("=" * 55)
    print("=== Pipeline Structural Anomalies ===")
    
    # Isolate a visual example of Lancaster's hyper-aggressive destruction
    sample = "destabilize"
    print(f"Raw: '{sample}' -> Porter: '{porter.stem(sample)}' "
          f"| Lancaster: '{lancaster.stem(sample)}'")


if __name__ == "__main__":
    # Ensure dependencies are available before running
    try:
        execute_stemming_suite()
    except Exception as e:
        print(f"Error encountered: {e}")
        print("Attempting to fix environment and re-run...")
        nltk.download('punkt')
        execute_stemming_suite()