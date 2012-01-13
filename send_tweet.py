#!/usr/bin/python2.7
import tweepy
import json
import random
import time

with open("auths.json") as f:
    js = json.load(f)

auth = tweepy.OAuthHandler(js["twitter"]["consumer_key"], js["twitter"]["consumer_secret"])
auth.set_access_token(js["twitter"]["token"], js["twitter"]["token_secret"])

api = tweepy.API(auth)

rand_str = str(random.randint(1, 10000000))

while True:
  try:
    api.update_status('#softwaregoldberg Guru meditation 0x' + rand_str)
    break
  except tweepy.error.TweepError, e:
    time.sleep(1)

print "[1] Tweet sent"
