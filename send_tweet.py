#!/usr/bin/python2

import tweepy
import json

with open("auths.json") as f:
    js = json.load(f)

auth = tweepy.OAuthHandler(js["twitter"]["consumer_key"], js["twitter"]["consumer_secret"])
auth.set_access_token(js["twitter"]["token"], js["twitter"]["token_secret"])

api = tweepy.API(auth)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status('#softwaregoldberg Hello world!')

print "Tweet sent"
