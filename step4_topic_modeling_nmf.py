# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:27:53 2017
#Reference: Prof. Gene Lee's codes from Dropbox code files. Modified...

"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

import numpy as np  # a conventional alias
from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk

from sklearn import decomposition
stopwords = nltk.corpus.stopwords.words('english')+['"rt','trump','donald','amp','uddf',
'"trump','"en','url','pbs','lang','null','"id','false','udc','trump"','spi','admin','https',
'thi',' trump','trump ','trump\"','trump\",','ud','udc','ude','uddf','lik','know']

tweets = []

infile = open('processed_tweets.json', 'r')
content = infile.readlines()


fnl_tweets= []
for tweet in content:
    tweet = tweet.lower()
    cln=[]
    for word in tweet.split():
      if word not in stopwords and word not in str('/,"realdonaldtrump",/,') and len(word) > 2 :
          cln.append(ls.stem(word))
    tweet_fnl=''
    for word in cln:tweet_fnl+=' {}'.format(word)
    
    fnl_tweets.append(tweet_fnl)

corpus = fnl_tweets

print 'num of documents, num of unique words'

vectorizer = TfidfVectorizer(stop_words='english', min_df=2)

dtm = vectorizer.fit_transform(corpus)

print dtm.shape
print len(corpus)
vocab = vectorizer.get_feature_names() # list of unique vocab, we will use this later
print len(vocab), '# of unique words'
print vocab[-10:]
print vocab[:10]

num_topics = 10

clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)
print num_topics, clf.reconstruction_err_

topic_words = []
num_top_words = 5
for topic in clf.components_:
    #print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words] # get indexes with highest weights
    #print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    #print topic_words[-1]
    #print

print ("**" * 10)  
    
    
for t in range(len(topic_words)):
    print "Topic {}: {}".format(t, ' '.join(topic_words[t][:15]))
    
from sklearn import decomposition

print dtm.shape

for n in range(1, 10):    
    num_topics = 5*n
    num_top_words = 10
    clf = decomposition.NMF(n_components=num_topics, random_state=1)
    doctopic = clf.fit_transform(dtm)
    print num_topics, clf.reconstruction_err_

    
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
