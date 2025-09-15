import re
from collections import defaultdict, Counter

class BPELearner:
    def __init__(self):
        self.merges = []
        self.vocab_size_history = []
        self.merge_frequencies = {}
        
    def preprocess_text(self, text):
        """Add end-of-word token (_) and split into words"""
        words = text.split()
        processed_words = [word + '_' for word in words]
        return ' '.join(processed_words)
    
    def get_stats(self, vocab):
        """Get frequency of adjacent symbol pairs"""
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pair = (symbols[i], symbols[i+1])
                pairs[pair] += freq
                self.merge_frequencies[pair] = freq
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
    
    def learn_bpe(self, text, num_merges=30):
        """Learn BPE merges from input text"""
        if not text.strip():
            return []
        
        # Preprocess text with end-of-word tokens
        processed_text = self.preprocess_text(text)
        words = processed_text.split()
        vocab = Counter()
        
        for word in words:
            chars = []
            i = 0
            while i < len(word):
                if word[i] == '_':
                    chars.append('_')
                    i += 1
                else:
                    chars.append(word[i])
                    i += 1
            tokenized_word = ' '.join(chars)
            vocab[tokenized_word] += 1
        
        self.vocab_size_history = [len(vocab)]
        
        for i in range(num_merges):
            stats = self.get_stats(vocab)
            if not stats:
                break
                
            most_frequent = max(stats, key=stats.get)
            freq = stats[most_frequent]
            
            vocab = self.merge_vocab(most_frequent, vocab)
            self.merges.append(most_frequent)
            self.vocab_size_history.append(len(vocab))
        
        return self.merges
    
    def segment_word(self, word):
        """Segment a word using learned BPE merges"""
        word_with_eow = word + '_'
        tokens = list(word_with_eow)
        
        for pair in self.merges:
            i = 0
            while i < len(tokens) - 1:
                if tokens[i] == pair[0] and tokens[i+1] == pair[1]:
                    tokens[i] = pair[0] + pair[1]
                    tokens.pop(i+1)
                else:
                    i += 1
        
        if tokens and tokens[-1] == '_':
            tokens.pop()
        
        segmented = "_".join(tokens)
        return tokens, segmented
    
    def get_most_frequent_merges(self, n=5):
        """Get the n most frequent merges"""
        sorted_merges = sorted(self.merge_frequencies.items(), 
                              key=lambda x: x[1], reverse=True)
        return sorted_merges[:n]
    
    def get_longest_subwords(self, n=5):
        """Get the n longest subword tokens"""
        all_subwords = set()
        for merge in self.merges:
            all_subwords.add(merge[0])
            all_subwords.add(merge[1])
            all_subwords.add(merge[0] + merge[1])
        
        sorted_subwords = sorted(all_subwords, key=len, reverse=True)
        return sorted_subwords[:n]

def get_user_input():
    """Get all required inputs from the user"""
    print("=" * 60)
    print("BPE TOKENIZATION LEARNER")
    print("=" * 60)
    
    # Get text input
    print("\nEnter your text paragraph (4-6 sentences):")
    print("Press Enter twice when finished:")
    lines = []
    while True:
        line = input().strip()
        if line == "":
            if len(lines) > 0:
                break
        else:
            lines.append(line)
    
    text = " ".join(lines)
    
    if not text:
        text = "The quick brown fox jumps over the lazy dog. Natural language processing is amazing with subword tokenization. This demonstrates BPE algorithm effectiveness."
        print("Using default text.")
    
    # Get number of merges
    try:
        num_merges = int(input("\nEnter number of merges to learn (default 30): ") or "30")
    except ValueError:
        num_merges = 30
    
    # Get words to segment
    print("\nEnter 5 words to segment (one per line):")
    print("Include one rare word and one inflected form:")
    words_to_segment = []
    for i in range(5):
        word = input(f"Word {i+1}: ").strip()
        if word:
            words_to_segment.append(word)
    
    if len(words_to_segment) < 5:
        words_to_segment = ["tokenization", "jumps", "processing", "amazing", "effectiveness"]
        print("Using default words.")
    
    return text, num_merges, words_to_segment

def main():
    # Get user input
    text, num_merges, words_to_segment = get_user_input()
    
    print("\n" + "=" * 60)
    print("PROCESSING YOUR INPUT...")
    print("=" * 60)
    
    # Initialize and train BPE
    bpe = BPELearner()
    merges = bpe.learn_bpe(text, num_merges)
    
    print(f"Learned {len(merges)} BPE merges")
    print(f"Final vocabulary size: {bpe.vocab_size_history[-1]}")
    
    # 1. Show five most frequent merges
    print("\n" + "=" * 60)
    print("1. FIVE MOST FREQUENT MERGES")
    print("=" * 60)
    frequent_merges = bpe.get_most_frequent_merges(5)
    for i, ((first, second), freq) in enumerate(frequent_merges, 1):
        print(f"{i}. '{first}' + '{second}' -> '{first+second}' (freq: {freq})")
    
    # 2. Show five longest subword tokens
    print("\n" + "=" * 60)
    print("2. FIVE LONGEST SUBWORD TOKENS")
    print("=" * 60)
    longest_subwords = bpe.get_longest_subwords(5)
    for i, subword in enumerate(longest_subwords, 1):
        print(f"{i}. '{subword}' ({len(subword)} chars)")
    
    # 3. Segment the words
    print("\n" + "=" * 60)
    print("3. WORD SEGMENTATION RESULTS")
    print("=" * 60)
    
    for word in words_to_segment:
        tokens, segmented = bpe.segment_word(word)
        print(f"Word: {word}")
        print(f"Subword sequence: {segmented}")
        print(f"Tokens: {tokens}")
        print()
    
    # 4. Reflection
    print("=" * 60)
    print("4. REFLECTION ON BPE TOKENIZATION")
    print("=" * 60)

if __name__ == "__main__":
    main()