# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:12:00 2017

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

from textblob import TextBlob

infile = open("processed_tweets.json",'r')
content = infile.readlines()

sub_score = []
pol_score = []

for each_line in content:
    tb = TextBlob(each_line)
    sub_score.append(tb.sentiment.subjectivity)
    pol_score.append(tb.sentiment.polarity)

import matplotlib.pyplot as plot
plot.hist(sub_score, bins=15) #, normed=1, alpha=0.75)
plot.xlabel('subjectivity score')
plot.ylabel('sentence count (len of sentences)')
plot.grid(True)
plot.savefig('subjectivity_calnev_tweets.pdf')
plot.show()
    

plot.hist(pol_score, bins=20) #, normed=1, alpha=0.75)
plot.xlabel('polarity score')
plot.ylabel('sentence count (len of sentences)')
plot.grid(True)
plot.savefig('polarity_calnev_tweets.pdf')
plot.show()

print 'Average of Subjectivity Score =', sum(sub_score)/len(sub_score)
print 'Average of Polarity Score =', sum(pol_score)/len(pol_score)

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
