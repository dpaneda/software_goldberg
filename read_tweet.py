#!/usr/bin/python2
import tweepy
import time

api = tweepy.API()

while not api.search('#softwaregoldberg'):
    time.sleep(3)
        
print "Tweet received"
