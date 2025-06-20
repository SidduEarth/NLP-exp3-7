import nltk, random
from nltk import pos_tag, FreqDist, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Downloads
for pkg in ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']:
    nltk.download(pkg)

text = "This is Python Programming. We are using NLTK."

tokens = word_tokenize(text)
filtered = [w for w in tokens if w.lower() not in stopwords.words('english')]

print("Tokens:", tokens)
print("Filtered:", filtered)
print("Stemmed:", [PorterStemmer().stem(w) for w in filtered])
print("Lemmatized:", [WordNetLemmatizer().lemmatize(w) for w in filtered])
print("POS Tags:", pos_tag(filtered))
print("Most Common:", FreqDist(filtered).most_common(5))
