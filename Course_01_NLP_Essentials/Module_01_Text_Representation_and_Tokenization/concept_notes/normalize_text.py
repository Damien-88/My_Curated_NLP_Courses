"""
Day 2: Unicode Normalization (NFC vs. NFD) Verification Script
This script isolates the exact byte and code-point differences between composed 
and decomposed text strings.Demonstrating why normalization is critical.
"""

import unicodedata

def analyze_normalization_forms(input_word):
    """Deconstructs a string into NFC and NFD states to show byte and code-point differences."""
    # Force input string into explicit NFC and NFD forms
    nfc_form = unicodedata.normalize('NFC', input_word)
    nfd_form = unicodedata.normalize('NFD', input_word)

    print(f"Analysis for base word input: '{input_word}'")
    print("=" * 60)

    # Analyze Composed State (NFC)
    print(f"NFC Form (Composed):    {nfc_form}")
    print(f"NFC String Length:      {len(nfc_form)} characters")
    print(f"NFC Code Points:        {[f'U+{ord(c):04X}' for c in nfc_form]}")
    print(f"NFC UTF-8 Bytes (Hex):  {nfc_form.encode('utf-8').hex().upper()}")
    print("-" * 60)

    # Analyze Decomposed State (NFD)
    print(f"NFD Form (Decomposed):  {nfd_form}")
    print(f"NFD String Length:      {len(nfd_form)} characters")
    print(f"NFD Code Points:        {[f'U+{ord(c):04X}' for c in nfd_form]}")
    print(f"NFD UTF-8 Bytes (Hex):  {nfd_form.encode('utf-8').hex().upper()}")
    print("=" * 60)

if __name__ == "__main__":
    # Test using the French word for summary: 'résumé'
    # We explicitly define it with unicode literals to prevent terminal/editor stripping
    target_word = "r\u00e9sum\u00e9"  # 'résumé' with composed characters
    analyze_normalization_forms(target_word)