"""
Day 3: Deterministic Regex Tokenization Engine
This script constructs a rule-based tokenizer using regular expressions and 
benchmarks its performance against native whitespace splitting across various 
languages.
"""
import re

class DeterministicRegexTokenizer:
    def __init__(self):
        # A compiled regex pattern matching distinct tokens:
        # 1. Words with optional internal contractions/apostrophes (\w+(?:'\w+)?)
        # 2. Sequential non-whitespace symbols or isolated punctuation ([^\w\s])
        self.token_pattern = re.compile(r"[a-zA-Z0-9]+|['’]|[^\w\s]|\w")


    def tokenize(self, text):
        """Scans text and returns an array of matching token strings."""
        return self.token_pattern.findall(text)
    
def run_tokenizer_benchmarks():
    tokenizer = DeterministicRegexTokenizer()

    test_cases = {
        "Standard English Punctuation": "The data scientist's pipeline works flawlessly, doesn't it?",
        "Cluttered Log/Web Text": "Error: User_ID=1043 failed to connect to https://api.local/v1.",
        "Script-io Non-Space Language": "今天天气很好。"
    }

    print("NLP Tokenizer Benchmark Engine\n")

    for description, text in test_cases.items():
        print(f"Scenario: {description}")
        print(f"Raw Input: '{text}'\n")

        # Naive
        naive_output = text.split()
        print(f"Naive Whitespace [.split()]:")
        print(f" -> {naive_output}")
        print(f"Total Tokens: {len(naive_output)}\n")

        # Regex
        regex_output = tokenizer.tokenize(text)
        print(f"Deterministic Regex Tokenizer:")
        print(f" -> {regex_output}")
        print(f"Total Tokens: {len(regex_output)}\n")

if __name__ == "__main__":
    run_tokenizer_benchmarks()