#!/usr/bin/env python

import logging
import json
import sys
import tweepy

from datetime import datetime, date
from apscheduler.schedulers.blocking import BlockingScheduler
from time import gmtime, strftime, sleep
from tweepy import OAuthHandler

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#---------------------

# WOEID (http://www.woeidlookup.com/)
WOEID = 23424977 # USA

def fetch_tweets():
	now1 = datetime.now().time() # Get current time
	print "Started at: " + str(now1)
	
	# Get trending topics for a specific WOEID
	trends1 = api.trends_place(WOEID)
	trends = set([trend['name'] for trend in trends1[0]['trends']])
	trendsList = list(trends)
	
	filename = strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + '_favorites.txt'
	with open(filename, 'a') as f:
		f.write('Trending topics in the USA: \n')
		
		# From trending topics, get Tweets
		for t in trendsList:
			print ('Retrieving tweets for :{}'.format(t.encode('utf-8'))) 
			sys.stdout.flush()
			
			for tweet in tweepy.Cursor(api.search, q=t, rpp=100, lang="en").items(1000):
				f.write(json.dumps([tweet._json], indent=1))
				f.write('\n')
        			sleep(0.5)
			
	now2 = datetime.now().time()
	elapsedTime = datetime.combine(date.today(), now2) - datetime.combine(date.today(), now1)
	print "Ended with elapsed time of: " + str(elapsedTime)

try:
	fetch_tweets()
	logging.basicConfig()
	scheduler = BlockingScheduler()
	scheduler.add_job(fetch_tweets, 'interval', hours=7, end_date='2018-04-22 19:00:00')
	scheduler.start()
	#scheduler.shutdown()
except:
    print('An error occured!')
