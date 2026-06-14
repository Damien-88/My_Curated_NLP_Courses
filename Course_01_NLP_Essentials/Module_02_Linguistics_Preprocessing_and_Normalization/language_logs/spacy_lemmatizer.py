"""
Day 6: Context-Aware Lemmatization Engine
This script utilizes spaCy to accurately extract dictionary base forms (lemmas)
and highlights how parsing context prevents the over-stemming bugs seen on day 5.
"""
import sys
import spacy

def execute_lemmatization_suite():
    # Load the optimized English pipeline
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Error: 'en_core_web_sm' model not found.")
        print(
            "Please run this command in your terminal first: " \
            "python -m spacy download en_core_web_sm"
        )
        sys.exit(1)

    # 1. Re-testing the specific words that broke the day 5 stemmers
    problematic_vocabulary = [
        "organization", "organs", "alumnus", "alumni", "alumnae"
    ]

    print("1. Resolving Historical Stemming Flaws")
    print(f"{'Raw Input Word:':<16} | {'spaCy Extracted Lemma':<22}")
    print("-" * 45)

    # Process words as an active sace-separated string to let spaCy build tokens
    vocab_doc = nlp(" ".join(problematic_vocabulary))
    for token in vocab_doc:
        print(f"{token.text:<16} | {token.lemma_:<22}")

    print("=" * 50)
    print("2. Tracking Contextual Sensitivity")

    # Context-switching test cases where identical words have different meanings
    context_samples = [
        "The stubborn flies sat on the clean kitchen wall.",
        "An arrow flies straight through the dark forest."
    ]

    for sentence in context_samples:
        print(f"\nRaw Sentence: {sentence}")
        doc = nlp(sentence)

        # Isolate and inspect the exact token "flies" in each sentence context
        for token in doc:
            if token.text.lower() == "flies":
                print(f"Token Found: '{token.text}'")
                print(f"Assigned POS Tag: {token.pos_} ({token.tag_})")
                print(f"Resolved Lemma: '{token.lemma_}'")

if __name__ == "__main__":
    execute_lemmatization_suite()