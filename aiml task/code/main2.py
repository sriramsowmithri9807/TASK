from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
sentiments = [sia.polarity_scores(tweet) for tweet in tweet_data]