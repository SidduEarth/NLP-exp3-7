### Exp 3a
```
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
```
---
### Exp 3b
```
import random
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(5):
    length = random.randint(5, 10)
    word = "".join(random.choice(letters) for j in range(length))
    print("Random Word:", word)

```
---
### Exp 7b
```import nltk
from nltk import ngrams, word_tokenize

nltk.download('punkt')
text = "The quick brown fox jumps over the lazy dog."
for g in ngrams(word_tokenize(text), 3):
    print(g)

```
---
### Exp 8
```
import speech_recognition as sr
from gtts import gTTS
import os

# Create recognizer object
recognizer = sr.Recognizer()

# Load the audio file
path = r"C:\Users\Lenovo\Downloads\harvard.wav"
audio = sr.AudioFile(path)

# Convert Audio to Text
with audio as source:
    data = recognizer.record(source)

# Recognize text using Google Web Speech API
extract = recognizer.recognize_google(data)

# Print the extracted text
print("Extracted Text:", extract)

# Convert Text to Audio
text = "We are using NLTK. We are in NLP lab."
speech = gTTS(text=text, lang='en')
speech.save("output.mp3")

# Play the audio file (use 'start' on Windows, 'xdg-open' on Linux, 'open' on macOS)
os.system("start output.mp3")
```
---

