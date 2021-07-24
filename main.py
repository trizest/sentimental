import tweepy


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

consumer_key = "1WAb1n7WXDvXzLE56atSx2c2B"
consumer_secret = "QiOBYavcO7up3fSZ2WU2lDPDbUkIMKTtehuz7a9e8rZpSsIZpg"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKDARAEAAAAACwk7lxC4ivJu4PHi%2BwAqgY7Dy5E%3DQwYiem4k9izFiyGoIuR5nBGyXF5jjKpZPogrhJw4MrBr3KmXsP"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search, q='BTC').items(10):
    print(tweet.text)
