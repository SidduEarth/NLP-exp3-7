import nltk
from nltk import ngrams, word_tokenize

nltk.download('punkt')
text = "The quick brown fox jumps over the lazy dog."
for g in ngrams(word_tokenize(text), 3):
    print(g)
