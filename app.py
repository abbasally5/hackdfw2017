import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify, Response

from test import *
import json

app = Flask(__name__)

#_demo = ['corgi']
_demo = []

@app.route("/")
def hello():
    return render_template('FlyZoom.html')


@app.route("/hashtag", methods=['POST'])
def hashtag():
    hashtag_text = request.form.get('hashtag', None)
    
    # if user input is from demo, 
    if hashtag_text in _demo:
        with open('data/' + hashtag_text + '.txt') as f:
            scores = [[0, 0], 0, [0, 0]]

            for line in f:
                json_form = {}
                _tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])" +\
                    " |(\w+:\/\/\S+)", " ", line).split())
                
                analysis = TextBlob(_tweet)
                if analysis.polarity>= 0:
                    scores[0][0] += 1                   # increment positive
                    scores[0][1] += analysis.polarity# add score (+)
                else:
                    scores[2][0] += 1                   # increment negative
                    scores[2][1] += analysis.polarity# add score (-)

            return jsonify(tweets=scores)

    else:
        api = TwitterClient()
        tweets_dict = api.get_tweets(query = hashtag_text, lang='en', count=1000)
        #tweets = [json.dumps(tweet) for tweet in tweets_dict]
        #print json.dumps(tweets_dict)
        return jsonify(tweets=tweets_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
