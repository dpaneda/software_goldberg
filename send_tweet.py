#!/usr/bin/python2.7
import tweepy
import json
import random

with open("auths.json") as f:
    js = json.load(f)

auth = tweepy.OAuthHandler(js["twitter"]["consumer_key"], js["twitter"]["consumer_secret"])
auth.set_access_token(js["twitter"]["token"], js["twitter"]["token_secret"])


api = tweepy.API(auth)

rand_str = str(random.randint(1, 10000000))

api.update_status('#softwaregoldberg Guru meditation 0x' + rand_str)

print "Tweet sent"
