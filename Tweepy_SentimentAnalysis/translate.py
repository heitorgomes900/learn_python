from textblob import TextBlob
import json

text = TextBlob("Eu estou triste")
text = text.translate(to="en")
print(text)

type('teste')