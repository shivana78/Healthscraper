import os
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import spacy
from nltk.corpus import stopwords
nltk.download('stopwords')

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)
# Remove all except one column
tweets_df2 = tweets_df2[['content']]
#list it all
tweets_df3 = tweets_df2.to_string()
df_split = tweets_df3.split()


#Removing Punctuation
df_split = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in df_split]

df_split2 = []
for word in df_split:
    if word != '':
        df_split2.append(word)

#This is stemming the words to their root
from nltk.stem.snowball import SnowballStemmer

# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')

stem = []
for word in df_split2:
    stem.append(s_stemmer.stem(word))

#Removing all Stop Words
stem2 = []

for word in stem:
    if word not in stopwords.words():
        stem2.append(word)
# Import module
from nrclex import NRCLex

# Assign list of strings
text = stem2
  
# Iterate through list
for i in range(len(text)):

    # Create object
    emotion = NRCLex(text[i])

    # Classify emotion
    print('\n\n', text[i], ': ', emotion.top_emotions)
