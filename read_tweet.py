#!/usr/bin/python2.7
import tweepy
import time

def last_id():
  return tweepy.API().search('#softwaregoldberg')[0].id

tweet_id = last_id()

while tweet_id != last_id():
    time.sleep(3)
        
print "Tweet received"
