function Tweet(text, sentiment, polarity, favorites, retweets) {
    this.text = text;
    this.sentiment = sentiment;
    this.polarity = polarity;
    this.favorites = favorites;
    this.retweets = retweets;
}


var hashtag_success = function(json) {
    alert(json.tweets[0].text);
    alert(json.tweets[0].sentiment);
    //alert(json.tweets[0]['text']);
    //alert(JSON.stringify(json.tweets));
    //alert(JSON.stringify(json));
    //var arr = JSON.stringify(json.tweets);
    var arr = json.tweets;
    //alert(arr);
    //alert(json['tweets']);
    var data = json['tweets'];
    for (var i = 0; i < json.tweets.length; i++) {
        var tweet = new Tweet(
            json.tweets[i].text,
            json.tweets[i].sentiment,
            json.tweets[i].polarity,
            json.tweets[i].favorites,
            json.tweets[i].retweets);
        console.log(json.tweets[i].text);
        $('#tweets').append('<p>' + tweet.text + '</p>');
        $('#tweets').append('<p>' + tweet.sentiment+ '</p>');
        $('#tweets').append('</br>');

    }
    /*
    for (tweet in arr) {
        console.log(tweet.text);
        console.log(tweet.sentiment);
        console.log(tweet.polarity);
        console.log(tweet.retweets);
        console.log(tweet.favorites);
        $('#tweets').append('<p>' + tweet.text + '</p>');
    }
    */
    //$('#tweets').text(json['tweet']);
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
