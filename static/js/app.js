function Tweet(text, sentiment, polarity, favorites, retweets) {
    this.text = text;
    this.sentiment = sentiment;
    this.polarity = polarity;
    this.favorites = favorites;
    this.retweets = retweets;
}

function Stats(sentimentArr, polarityArr) {
    this.numPos = sentimentArr['positive']; 
    this.numNeg = sentimentArr['negative']; 
    this.numNeut = sentimentArr['neutral']; 
    this.avgPos = polarityArr['positive'];
    this.avgNeg = polarityArr['negative'];
    this.avgNeut = polarityArr['neutral'];
}





var hashtag_success = function(json) {
    //alert(json.tweets[0].text);
    //alert(json.tweets[0].sentiment);
    //alert(json.tweets[0]['text']);
    //alert(JSON.stringify(json.tweets));
    //alert(JSON.stringify(json));
    //var arr = JSON.stringify(json.tweets);
    var arr = json.tweets;
    //alert(arr);
    //alert(json['tweets']);
    var data = json['tweets'];
    $('#tweets').empty();
    var sentArr = {'positive': 0,
                   'negative': 0,
                   'neutral': 0}; 
    var polarArr = {'positive': 0,
                    'negative': 0,
                    'neutral': 0}; 
     
    for (var i = 0; i < json.tweets.length; i++) {
        var tweet = new Tweet(
            json.tweets[i].text,
            json.tweets[i].sentiment,
            json.tweets[i].polarity,
            json.tweets[i].favorites,
            json.tweets[i].retweets);
        if (tweet.sentiment == 'positive') {
            sentArr['positive'] += 1;
            polarArr['positive'] += tweet.polarity;
        } 
        else if (tweet.sentiment == 'negative') {
            sentArr['negative'] += 1;
            polarArr['negative'] += tweet.polarity;
        }
        else if (tweet.sentiment == 'neutral') {
            sentArr['neutral'] += 1;
            polarArr['neutral'] += tweet.polarity;
        }
        //console.log(json.tweets[i].text);
        $('#tweets').append('<p>' + tweet.text + '</p>');
        $('#tweets').append('<p>' + tweet.sentiment+ '</p>');
        $('#tweets').append('<p>' + tweet.polarity+ '</p>');
        $('#tweets').append('</br>');

    }
    polarArr['positive'] /= sentArr['positive'];
    polarArr['negative'] /= sentArr['negative'];
    polarArr['neutral'] /= sentArr['neutral'];
    var stats = new Stats(sentArr, polarArr);
    console.log(stats);
    $('#stats').empty();
    $('#stats').append('<p>Num Pos: ' + stats.numPos + '</p>');
    $('#stats').append('<p>Num Neg: ' + stats.numNeg + '</p>');
    $('#stats').append('<p>Num Neut: ' + stats.numNeut + '</p>');
    $('#stats').append('<p>Avg Pos: ' + stats.avgPos + '</p>');
    $('#stats').append('<p>Avg Neg: ' + stats.avgNeg + '</p>');
    $('#stats').append('<p>Avg Neut: ' + stats.avgNeut + '</p>');
    return true;
}

$('#hashtag_form').submit(function(e) {
    e.preventDefault();
    $.ajax({
        url: '/hashtag',
        type: "POST",
        datatype: "json",
        data: {
            'hashtag': $("#hashtag_input").val()
              },
        success: hashtag_success
    });
    
});
