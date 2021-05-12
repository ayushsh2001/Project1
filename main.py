import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob
import time

# all 4 authentication keys to access twitter API
# to connect as OAth handler or jump serever / revers proxy server
consumer_key = "Sxi4E6AKxIsSvJSqgEx6P7tnk"
consumer_sec = "M6JFg6UtawrnyOg5LtP8fNHcnCacI14mOhEi6rnL8DCxqDl52q"

# from proxy server we need to connect
access_token = "1391025710148440068-SjEd37frSvMel6TZ1Z68oY6q7U1hj3"
access_token_sec = "zOQS4PhLaOEiQndaaAAjkjnVQgZAnWLMSVfCL9OropYXu"

# tweepy explore
dir(tweepy)

# connected to jump server of twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_sec)

# now we can connect from jump server to web server of twitter
auth.set_access_token(access_token, access_token_sec)

# now we can connect to API storge server of twitter
api_connect = tweepy.API(auth)

# now you can search any topic on twitter
tweet_data = api_connect.search('Avengers', count=20)

pos = 0
neg = 0
neu = 0

# printing line by line
print("Show the recent tweets:")
i=1
for tweet in tweet_data:
    print(str(i) +') ' + tweet.text)
    i=i+1
    analysis = TextBlob(tweet.text)  # here it will apply NLP\
    print(analysis.sentiment)
    # now checking polarity only
    if analysis.sentiment.polarity > 0:
        print("posative \n")
        pos = pos + 1
    elif analysis.sentiment.polarity == 0:
        print("Neutral \n")
        neu = neu + 1
    else:
        print("Negative \n")
        neg = neg + 1

# ploting graphs
plt.xlabel("tags")
plt.ylabel("polarity")
plt.pie([pos, neg, neu], labels=['pos', 'neg', 'neu'], autopct="%1.1f%%")
plt.show()