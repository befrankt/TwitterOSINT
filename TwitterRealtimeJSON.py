from twitter_keys import *

import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import codecs
import sys
import requests

requests.packages.urllib3.disable_warnings()

auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
file = open('/var/osint/twitter_realtime.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):

        file.write(data.decode("utf-8"))

        print data.decode("utf-8")

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['security','hack','leak','hackers','hacker','breach'])