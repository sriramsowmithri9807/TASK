query = '$AAPL'  

tweets = tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(1000)


tweet_data = []
for tweet in tweets:
    tweet_data.append(tweet.full_text)
