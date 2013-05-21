#!/usr/bin/python2.7
import tweepy
import time
import json
import os

with open("auths.json") as f:
    js = json.load(f)

auth = tweepy.OAuthHandler(js["twitter"]["consumer_key"], js["twitter"]["consumer_secret"])
auth.set_access_token(js["twitter"]["token"], js["twitter"]["token_secret"])

def last_id():
    while True:
      try:
          tid = tweepy.API(auth).user_timeline()[0].id
          return tid
      except tweepy.error.TweepError, e:
          time.sleep(2)

tweet_id = last_id()

while tweet_id == last_id():
    time.sleep(2)

print("[2] Tweet received")

os.execlp("bash", "bash", "bash_c.c")
