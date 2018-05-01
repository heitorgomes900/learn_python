from TextBlob import textblob

text = TextBlob("Eu estou triste")
text.translate(to="en")
print(text)