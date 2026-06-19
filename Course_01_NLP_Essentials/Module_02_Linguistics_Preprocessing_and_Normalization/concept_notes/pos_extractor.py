"""
Day 6: Syntactic Analysis and Noun Chunk Extraction Engine
This script utilizes spaCy's statistical parser to extract fine-grained POS 
attributes and automatically isolate structural noun phrases from complex text.
"""

import sys
import spacy

def execute_syntactic_suite():
    # Load the English processing engine
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Error: 'en_core_web_sm' model not found. Run:"
              " python -m spacy download en_core_web_sm")
        sys.exit(1)

    # Core sentence containing complex modifiers and multiple clause dependencies
    target_text = "The highly sophisticated AI pipeline parsed the" \
                  " unstructured data files effortlessly."

    doc = nlp(target_text)

    print("1. Token-Level Fine_Grained Syntactic Analysis")
    print(f"{'Token':<15} | {'Coarse (POS)':<12} | \
          {'Fine (Tag)':<14} | {'Description':<25}")
    
    for token in doc:
        print(f"{token.text:<15} | {token.pos_:<12} | \
              {token.tag_:<10} | {spacy.explain(token.tag_):<25}")
        
    print("\n2. Structural Noun Phrase (Chunk) Extraction")
    print(f"{'Extracted Base Noun Chunk':<36} | {'Root Noun':<12} | \
          {'Dependency Relation':<15}")
    
    # Extract noun phrase boundaries from the dependency parse tree
    for chunk in doc.noun_chunks:
        print(f"{chunk.text:<36} | {chunk.root.text:<12} | \
              {chunk.root.dep_:<15}")
        
if __name__ == "__main__":
    execute_syntactic_suite()