import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


postweets=[]
negtweets=[]
neutweets=[]


def analyse_tweets(tweets):
    
    for tweet in tweets:
        
        tweetblob=TextBlob(tweet)
        #print tweetblob.polarity
        if (tweetblob.polarity > 0):
            postweets.append(tweet)
        if (tweetblob.polarity == 0):
            neutweets.append(tweet)
        if (tweetblob.polarity < 0):
            negtweets.append(tweet)


def get_tweets(search,count):


    """ Chane to your credentials """"
    
    ckey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    csecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    atoken="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    asecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    try:
        auth=OAuthHandler(ckey,csecret)
        auth.set_access_token(atoken, asecret)
        api = tweepy.API(auth)

    except:
        print "Authentication Failed"

    data=[]
    raw_data=api.search(q = search, count = count)
    for eachtweet in raw_data:
        data.append(eachtweet.text)

    return data


def print_cat(tweets):
    for tweet in tweets[:10]:
        print tweet




print "Enter the search query:"
search=raw_input()

print "Number of tweets to fetch:"

num=raw_input()

fetched_tweets=get_tweets(search,num)
analyse_tweets(fetched_tweets)

print ''
print "----------------------------------------------------------------------------------------------------------------"
print("Positive tweets : {} %".format(100*len(postweets)/len(fetched_tweets)))

print("Negative tweets : {} %".format(100*len(negtweets)/len(fetched_tweets)))

print("Neutral tweets : {} %".format(100*len(neutweets)/len(fetched_tweets)))

print ''
print "----------------------------------------------------------------------------------------------------------------"
print "Positive tweets:\n"
print print_cat(postweets)

print ''
print "----------------------------------------------------------------------------------------------------------------"
print "Negative tweets:\n"
print print_cat(negtweets)

print ''
print "----------------------------------------------------------------------------------------------------------------"
print "Neutral tweets:\n"
print print_cat(neutweets)

    
    
        
    
