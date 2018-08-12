from textblob import TextBlob as tb
import json

text = tb("Eu estou triste")
print(text.sentiment)
text = text.translate(to="en")
print(text.sentiment.polarity)
print(text)

type('teste')