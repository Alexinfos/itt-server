import tweepy

import credentials

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.text)
        print("---")

printer = IDPrinter(credentials.bearerToken)


# @TAG_InfoTrafic: 2338153482
printer.add_rules(tweepy.StreamRule("from:2338153482"))
printer.filter()