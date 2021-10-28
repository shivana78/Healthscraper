from nltk.tokenize import word_tokenize
train["clean"] = train["Text"].apply(word_tokenize)

from nltk.stem import SnowballStemmer
snstem = SnowballStemmer('english') #create object of SnowbllStemmer
train['stem']=train['clean'].apply(lambda x : [snstem.stem(y) for y in x])

from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
train['stem']=train['clean'].apply(lambda x : [lemma.lemmatize(y) for y in x])

from nltk.corpus import stopwords
stoplist = stopwords.words('english') # config the language name
train['stem']=train['stem'].apply(lambda x : [y for y in x if y not in stoplist])
train['stem'].head(1)



# Remove all except one
tweets_df2 = tweets_df2[['content']]




# Displays first 5 entries from dataframe
print(tweets_df2.head(5))



tweets_df2=tweets_df2.filter(['content'])
tweets_df2=tweets_df2.values
tweets_df2=tweets_df2.reshape(1, -1)
tweets_df2=tweets_df2.ravel()
tweets_df2=tweets_df2.tolist( )
map(str.split, tweets_df2)
print(tweets_df2)


dataList = [] #empty list
for index, row in tweets_df2.iterrows():
    mylist = [row.content]
    dataList.append(mylist)

lines = list()
for line in dataList:
    words = line.split()
    for w in words:
       lines.append(w)


print(lines)
