import tweepy as tweepy
from textblob import TextBlob
import json

consumer_key = '08KAZsaUX3EKXIMTWnYAJT5AT'
consumer_secret = 'eSJ4Lvw42jnRx7RYFbbM51cixXrfI5Rbjdd4yLXn7Y8dSmw1VW'

access_token = '842936456771461120-Ce5haijVorq2MmLylALSx15EChD7nu9'
access_token_secret = 'hGwRzIRjTKmG69bOczgHdzL4iqugMr3Yagc70Dh736fGc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(input("Tema:"))

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    data = {'Tweet':tweet.text, 'hasPolarity':(analysis.sentiment.polarity != 0.0), 'Sentiment': analysis.sentiment}
    data_string = json.dumps(data)
    print(data_string)
    '''
    print(tweet.text)
    if (analysis.sentiment.polarity != 0.0):
        print(analysis.sentiment)
    else:
        print('(It not could do sentiment analysis)')'''
    print('--------------------------------------------------------------------')
