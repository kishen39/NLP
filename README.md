This project shows:
- **spaCy Tokenizer** for word-level tokenization
- **BPE (Byte Pair Encoding)** for subword tokenization
- **Word_pair** of both outputs

---

# Tokenizer Example
### 1️⃣ Install & Download Model

pip install spacy
python -m spacy download xx_ent_wiki_sm

input : రియల్ ఎస్టేట్: ఏఐ వాడకం వల్ల రియల్ ఎస్టేట్ రంగంలో నిర్మాణ ఖర్చులు తగ్గుతాయని,ప్రాజెక్ట్ సమయం సగానికి తగ్గుతుందని మరియు జాప్యాలు తగ్గుతాయని ఒక వార్త నివేదించింది.ఇది గృహ కొనుగోలుదారులకు ప్రయోజనం చేకూరుస్తుంది.

### 🧮 Example Run

```python
import spacy

# Load the multi-language spaCy model
nlp = spacy.load("xx_ent_wiki_sm")

# Telugu input text
text = "రియల్ ఎస్టేట్: ఏఐ వాడకం వల్ల రియల్ ఎస్టేట్ రంగంలో నిర్మాణ ఖర్చులు తగ్గుతాయని, ప్రాజెక్ట్ సమయం సగానికి తగ్గుతుందని మరియు జాప్యాలు తగ్గుతాయని ఒక వార్త నివేదించింది."

# Manual tokenization (splitting by spaces)
manual_tokens = text.split()

# spaCy tokenization
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

# Compare results
print(f"Manual token count: {len(manual_tokens)}")
print(f"spaCy token count: {len(spacy_tokens)}")
print(f"Tokens that differ: {len(set(manual_tokens) ^ set(spacy_tokens))}")
```

# BPE Learner
### 🧮 Example Run
```python
input : low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

Enter number of merges to learn (default 10): 3
```

# BPE paragraph learner 
### 🧮 Example Run
```python

input : The quick brown fox jumps over the lazy dog. Natural language processing is amazing with subword tokenization.This demonstrates BPE algorithm effectiveness for various NLP tasks.

Enter number of merges to learn (default 30): 25

Enter : 
tokenization
jumps
processing
effectiveness
algorithm
```

# Word pair

### 🧮 Example Run
```python
source = "Sunday"
target = "Saturday"

# Model A: Equal cost for all operations
distA = min_edit_distance(source, target, 1, 1, 1)
print(f"Model A distance: {distA}")

# Model B: Higher cost for substitution
distB = min_edit_distance(source, target, 2, 1, 1)
print(f"Model B distance: {distB}")
```