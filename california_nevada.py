# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:48:24 2017

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.


from twython import TwythonStreamer
import sys
import json
import requests
 
tweets = []
 
class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''
 
    # overriding
    def on_success(self, data):
        if 'lang' in data and data['lang'] == 'en':
            if "trump" in data['text'].lower():  
                tweets.append(data['text'])
                print 'CAL NEV received tweet #', len(tweets), data['text']
 
        if len(tweets) >= 10000:
            self.store_json()
            self.disconnect()
 
    # overriding
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
 
    def store_json(self):
        with open('tweet_stream_{}_{}.json'.format(keyword, 'cal nev'), 'w') as f:
            json.dump(tweets, f, indent=4)
 
 
if __name__ == '__main__':
 
    #with open('your_twitter_credentials.json', 'r') as f:
    with open('caston_credentials_twitter.json', 'r') as f:
        credentials = json.load(f)
 
    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
 
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'trump'
 
    
    try: 
        stream.statuses.filter(locations='-124.1,32.34,-114.3,42.07') #cal nev
    except:
                        #e = sys.exc_info()[0]  #Get exception info (optional)
                        #print 'ERROR:',e  #Print exception info (optional)
        stream.store_json()

        
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
