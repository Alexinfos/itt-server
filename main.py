from re import split
import tweepy

import credentials

class TweetHandler(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print("---")
        print(tweet.text)
        

        test = tweet.text.split("\n")

        print("---Analyse:")
        for e in test:
            print(e)
            print("-")

handler = TweetHandler(credentials.bearerToken)


# @TAG_InfoTrafic: 2338153482
print("Listening for new tweets from @TAG_InfoTrafic")
handler.add_rules(tweepy.StreamRule("from:2338153482"))
handler.filter()
