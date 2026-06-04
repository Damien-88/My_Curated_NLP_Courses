"""
Day 1: Character Encodings, Bytes, and UTF-8 Verification Script
This script demonstrates byte-level differences between text encodings and explores
how data corruption occurs when handling files with incorrect encoding assumptions.
"""

def inspect_character(char):
    # Prints the unicode code point and byte layout of a single character
    code_point = f"U+{ord(char):04X}"

    # Get byte layouts
    try:
        utf8_bytes = char.encode('utf-8')
        utf8_hex = utf8_bytes.hex().upper()
        utf8_bin = " ".join(f"{b:08b}" for b in utf8_bytes)

    except UnicodeEncodeError:
        utf8_hex, utf8_bin = "N/A", "N/A"

    try:
        ascii_bytes = char.encode('ascii')
        ascii_hex = ascii_bytes.hex().upper()

    except UnicodeEncodeError:
        ascii_hex = "Incompatible (Out of ASCII Range)"

    print(f"Character:  {char}")
    print(f"Code Point: {code_point}")
    print(f"ASCII Hex:  {ascii_hex}")
    print(f"UTF-8 Hex:  {utf8_hex}")
    print(f"UTF-8 Bin:  {utf8_bin}")
    print("-" * 50)


def demonstrate_corruption():
    # Simulates a pipeline crash/corruption when assuming the wrong encoding
    original_text = "Resumé processing for AI engines."
    print(f"Original Text: {original_text}\n")
    
    # Encode text explicitly as Latin-1 (Windows-1252 historical alternative)
    encoded_latin1 = original_text.encode('latin-1')
    print(f"Raw Bytes (encoded as Latin-1): {encoded_latin1}")
    
    # Try to decode those exact bytes using UTF-8 (Common NLP pipeline error)
    try:
        corrupted_decode = encoded_latin1.decode('utf-8')
        print(f"Decoded as UTF-8: {corrupted_decode}")

    except UnicodeDecodeError as e:
        print(f"Decoded as UTF-8: FAILED! (Caught Expected Error: {e})")
        print(" -> Insight: UTF-8 parser rejected invalid structural continuation bits.")


if __name__ == "__main__":
    print(" 1. Core Variable-Length Byte Inspection ")
    # 1-Byte ASCII Character
    inspect_character("A")
    
    # 2-Byte Cyrillic Character
    inspect_character("Д")
    
    # 3-Byte Currency Symbol
    inspect_character("€")
    
    # 4-Byte Emoji
    inspect_character("🐍")

    print(" 2. Simulating Pipeline Mismatches ")
    demonstrate_corruption()