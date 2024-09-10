# Define the search query
query = '$AAPL'  # Example: Apple Inc.

# Scrape tweets
tweets = tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(1000)

# Store tweets in a list
tweet_data = []
for tweet in tweets:
    tweet_data.append(tweet.full_text)