import spacy

# Load the multi-language spaCy model
nlp = spacy.load("xx_ent_wiki_sm")

# Get text input from user at runtime
text = input("Enter the Telugu text to analyze: ")

# Manual tokenization (space-separated)
manual_tokens = text.split()

# spaCy tokenization
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

# Compare results
print(f"Manual token count: {len(manual_tokens)}")
print(f"spaCy token count: {len(spacy_tokens)}")
print()
print(f"Tokens that differ: {len(set(manual_tokens) ^ set(spacy_tokens))}")