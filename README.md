# Tokenizer
initialize the lib 
# Step 1 
pip install spacy
python -m spacy download xx_ent_wiki_sm
# Step 2
now we have the run the python tokenizer
give the text :
రియల్ ఎస్టేట్: ఏఐ వాడకం వల్ల రియల్ ఎస్టేట్ రంగంలో నిర్మాణ ఖర్చులు తగ్గుతాయని, ప్రాజెక్ట్ సమయం సగానికి తగ్గుతుందని మరియు జాప్యాలు తగ్గుతాయని ఒక వార్త నివేదించింది. ఇది గృహ కొనుగోలుదారులకు ప్రయోజనం చేకూరుస్తుంది.

# Final output
we can see that the spaCy tokenizer has differentiated it.

# BPE_learner

# Step 1 
Enter your text (press Enter twice to finish):
low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

# Step 2:
Enter number of merges to learn (default 10): 3

# BPE_L3

# Step 1
Enter your text paragraph (4-6 sentences):
Press Enter twice when finished:
The quick brown fox jumps over the lazy dog. Natural language processing 
is amazing with subword tokenization. This demonstrates BPE algorithm 
effectiveness for various NLP tasks.
# Step 2
Enter number of merges to learn (default 30): 25
# Step 3
Enter 5 words to segment (one per line):
Include one rare word and one inflected form:
Word 1: tokenization
Word 2: jumps
Word 3: processing
Word 4: effectiveness
Word 5: algorithm