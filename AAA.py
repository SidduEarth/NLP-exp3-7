
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
