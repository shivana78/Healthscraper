import os
import pandas as pd
import numpy as np
from textblob import TextBlob

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)
# Remove all except one column
tweets_df2 = tweets_df2[['content']]
#TextBlob polarity
tweets_df2['sentiment'] = tweets_df2['content'].apply(lambda tweet: TextBlob(tweet).sentiment)
print(tweets_df2['sentiment'])
#the upper code Sentiment returns a namedtuple of the form Sentiment(polarity, subjectivity).
#now its time for Csv
tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)
