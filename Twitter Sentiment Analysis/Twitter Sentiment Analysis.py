
# coding: utf-8

# In[10]:

import tweepy
from textblob import TextBlob


# In[11]:

consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[12]:

topic=input('Topic Search')
public_tweets = api.search(topic,result_type='recent')


# In[ ]:

positive_tweets=0
negative_tweets=0
netural_tweets=0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment[0]>0:
        positive_tweets+=1
    elif analysis.sentiment[0]<0:
        negative_tweets+=1
    else:
        netural_tweets+=1
    
print ('Total Tweets Scanned',len(public_tweets))
print ('Positive Tweets:',((positive_tweets/len(public_tweets))*100),'%')
print ('Negative Tweets:',((negative_tweets/len(public_tweets))*100),'%')
print ('Neutral Tweets:',((netural_tweets/len(public_tweets))*100),'%')


# In[ ]:



