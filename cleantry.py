# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:39:59 2017
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
Reference: #http://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet


"""

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
#http://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet
import re
import json
import HTMLParser 
import string
from nltk.corpus import stopwords                              
html_parser = HTMLParser.HTMLParser()

infile = open("tweet_stream_trump_cal nev.json",'r')
content = infile.readlines()


#Removing links from tweets
wourl_tweets = []

for each_line in content:
      url_tweet = re.sub('http.://\w+.*', " ", each_line)
      wourl_tweets.append(url_tweet)


    

#content = html_parser.unescape(content)
processed_tweets = []
for each_line in wourl_tweets:
    a = string.punctuation
    b = string.digits
    c = string.maketrans(a, len(a)*" ")
    d = string.maketrans(b, len(b)*" ")

    tweets = str(each_line).translate(c)
    tweets = str(tweets).translate(d)
    processed_tweets.append(tweets.strip().encode('utf-8'))

infile.close()

with open("processed_tweets.json","w") as outfile:
    json.dump(processed_tweets,outfile,indent=4)

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
#http://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet
        
        
