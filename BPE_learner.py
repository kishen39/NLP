import re
from collections import defaultdict, Counter

class BPELearner:
    def __init__(self):
        self.merges = []
        self.vocab_size_history = []
        
    def get_stats(self, vocab):
        """Get frequency of adjacent symbol pairs"""
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pair = (symbols[i], symbols[i+1])
                pairs[pair] += freq
        return pairs
    
    def merge_vocab(self, pair, vocab):
        """Merge the most frequent pair in the vocabulary"""
        first, second = pair
        new_vocab = {}
        pattern = re.compile(r'(?<!\S)' + re.escape(first) + r' ' + re.escape(second) + r'(?!\S)')
        
        for word, freq in vocab.items():
            new_word = pattern.sub(first + second, word)
            new_vocab[new_word] = freq
        
        return new_vocab
    
    def learn(self, text, num_merges=10):
        """Learn BPE merges from input text"""
        if not text.strip():
            print("Error: No text provided!")
            return []
        
        # Pre-tokenize: split into words and then into characters
        words = text.split()
        vocab = Counter()
        
        for word in words:
            tokenized_word = ' '.join(list(word))
            vocab[tokenized_word] += 1
        
        print(f"Initial vocabulary size: {len(vocab)}")
        self.vocab_size_history = [len(vocab)]
        
        for i in range(num_merges):
            stats = self.get_stats(vocab)
            if not stats:
                print("No more pairs to merge!")
                break
                
            most_frequent = max(stats, key=stats.get)
            freq = stats[most_frequent]
            
            print(f"\nStep {i+1}:")
            print(f"Top pair: '{most_frequent[0]}' + '{most_frequent[1]}' (frequency: {freq})")
            
            vocab = self.merge_vocab(most_frequent, vocab)
            self.merges.append(most_frequent)
            
            print(f"Vocabulary size after merge: {len(vocab)}")
            self.vocab_size_history.append(len(vocab))
        
        return self.merges
    
    def encode_word(self, word):
        """Encode a single word using learned BPE merges"""
        tokens = list(word)
        
        for pair in self.merges:
            i = 0
            while i < len(tokens) - 1:
                if tokens[i] == pair[0] and tokens[i+1] == pair[1]:
                    tokens[i] = pair[0] + pair[1]
                    tokens.pop(i+1)
                else:
                    i += 1
        
        return tokens

def main():
    print("=" * 60)
    print("Mini BPE Learner")
    print("=" * 60)
    
    # Get text input from user
    print("\nEnter your text (press Enter twice to finish):")
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    text = " ".join(lines).strip()
    
    if not text:
        print("No text provided. Using default example.")
        text = "low low low low low low lowest lowest new newer newer newest widest widest wider wider"
        print(f"Using default text: {text}")
    
    # Get number of merges from user
    try:
        num_merges = int(input("\nEnter number of merges to learn (default 10): ") or "10")
    except ValueError:
        num_merges = 10
    
    print("\n" + "=" * 60)
    print("Learning BPE merges...")
    print("=" * 60)
    
    # Learn BPE
    bpe = BPELearner()
    merges = bpe.learn(text, num_merges)
    
    print("\n" + "=" * 60)
    print("Learning Complete!")
    print("=" * 60)
    
    print(f"\nTotal merges learned: {len(merges)}")
    print(f"Vocabulary size history: {bpe.vocab_size_history}")
    
    print("\nLearned merges in order:")
    for i, (first, second) in enumerate(merges, 1):
        print(f"{i:2d}. '{first}' + '{second}' -> '{first}{second}'")
    
    # Test encoding
    print("\n" + "=" * 60)
    print("Test Encoding")
    print("=" * 60)
    
    test_word = input("Enter a word to encode (or press Enter to skip): ").strip()
    if test_word:
        encoded = bpe.encode_word(test_word)
        print(f"Encoded '{test_word}': {encoded}")

if __name__ == "__main__":
    main()