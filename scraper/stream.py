import tweepy
from auth import keys

auth = tweepy.AppAuthHandler(keys['api_key'], keys['api_secret'])
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)

#below is broken doesn't work. Look at https://www.youtube.com/watch?v=qhLVAXcFsao
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

def streamtweets():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['python'])

streamtweets()