# hackdfw2017

Live Demo: http://107.23.94.58

## Inspiration
It has become increasingly important to be informed about what is going on in the world. However, actively searching out world views on the internet can be very time consuming. Therefore, we decided to give a WorldView of any topic at a glance.

## What it does
The user can search for a twitter hashtag and the data visualization shows the general twitter sentiment of the hashtag to the user. The green, blue, and white colors correspond to a positive, negative, and neutral sentiment of the hashtag.

How we built it
We used three.js to power the front end data visualization and used flask, python, the Twitter API, and the library tweepy to power the backend and TextBlob for the sentiment analysis.

## How to install

You will require a twitter api key

Replace the lines in test.py
```
consumer_key = TWITTER_CONSUMER_KEY
consumer_secret = TWITTER_CONSUMER_SECRET
access_token = TWITTER_ACCESS_TOKEN
access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
```
with your key and you should be set!

This project requires python2 and pip

To install requirements, run
```
**$** pip freeze > requirements.txt
```
and to run the app, run
```
**$** python app.py
```

## Contributors
This project was made by ([Nathan Chin (nathan-chin)](https://github.com/nathan-chin)), ([Avi Minocha (tr8009)](https://github.com/tr8009)), ([Jin Yeom (jinyeom)](https://github.com/jinyeom)), ([Carlos L. Barahona (Sapulsic)](https://github.com/Sapulsic)), ([Abbas Ally (abbasally5)](https://github.com/abbasally5)) at Earthack 2017
