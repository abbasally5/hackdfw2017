import re
import tweepy
import json
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):

    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):

        '''
        Class constructor or initialization method.
        '''

        # keys and tokens from the Twitter Dev Console
        consumer_key = 'cV4wnecpl9WIMZgocjeWfaCLa'
        consumer_secret = 'owmk5cH8emocNZVQM7OyH99zszWjwhvucrfp7qUgtvls4Uzlar'
        access_token = '1043044687-lXvSx8xRCC21RUmUtCjfiZHlOKt3idJfd5zef4T'
        access_token_secret = 'iIitJeVgPYktg8akrC89MUolsHBnoYHjaQtJox5tfckSi'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        
        except:
            print("Error: Authentication Failed")
    
    def clean_tweet(self, tweet):

        '''
        Utility function to clean tweet text by removing links, special 
        characters using simple regex statements.
        '''

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |" +\
            "(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
   
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''

        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return analysis.sentiment.polarity
        elif analysis.sentiment.polarity == 0:
            return analysis.sentiment.polarity
        else:
            return analysis.sentiment.polarity

    def get_tweet_polarity(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis.sentiment.polarity

    def get_tweets(self, query, lang='en', count=100):
        
        '''
        Main function to fetch tweets and parse them.
        '''
       
        # sentiment scores (+, n, -) 
        scores = [(0, 0), 0, (0, 0)]

        try:
            # call twitter api to fetch tweets
            fetched_tweets = [tweet._json for tweet in 
                tweepy.Cursor(self.api.search, q=query, 
                count=count, lang=lang).items(count)]
            
            # parsing tweets one by one and get its polarity
            for tweet in fetched_tweets:
                score = self.get_tweet_polarity(tweet['text'])
                if score > 0:
                    scores[0][0] += 1       # increment positive
                    scores[0][1] += score   # add score (+)
                elif score == 0:
                    scores[1] += 1          # number of neutral ++
                else:
                    scores[2][0] += 1       # increment negative
                    scores[2][1] += score   # add score (-)

            # return parsed tweets
            return scores

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
