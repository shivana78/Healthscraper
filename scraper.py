import os
import pandas as pd
import numpy as np
import re

# Setting variables to be used in format string command below
tweet_count = 1000
text_query = "canada health insurance"
since_date = "2020-12-01"
until_date = "2021-02-28"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date))
