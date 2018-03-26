# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 01:04:59 2017
Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

from __future__ import division, print_function
#from gensim import corpora, models, similarities, matutils
from pprint import pprint

import nltk
from sklearn.feature_extraction.text import CountVectorizer

#logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
#logging.root.level = logging.INFO  # ipython sometimes messes up the logging setup; restore

infile = open("processed_tweets.json","r")   
content = infile.readlines()

from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()

stopwords = nltk.corpus.stopwords.words('english')+['"rt','trump','donald','amp','uddf',
'"trump','"en','url','pbs','lang','null','"id','false','udc','trump"','spi','admin','https',
'thi',' trump','trump ','trump\"','trump\",','ud','udc','ude','uddf','lik','know']





fnl_tweets= []
for tweet in content:
    tweet = tweet.lower()
    cln=[]
    for word in tweet.split():
      if word not in stopwords :
          cln.append(ls.stem(word))
    tweet_fnl=''
    for word in cln:tweet_fnl+=' {}'.format(word)
    
    fnl_tweets.append(tweet_fnl)

corpus = fnl_tweets

#data  = eval(open('processed_tweets.json', 'r').read())

    
#print (corpus)
#data.pop()
#dat = [tweet for tweet in data if len(tweet) != 0]
#corpus = [str(tweet) for tweet in data]
from gensim import corpora
#print (corpus[:10])
corpus2 = [text.split() for text in corpus]

dic = corpora.Dictionary(corpus2)
#print (dic)

print(type(corpus), len(corpus))

corpus1 = [dic.doc2bow(text) for text in corpus2]

#for corp in corpus1:
 #   print(len(corp), corp[:10])
           
from gensim import models
tfidf = models.TfidfModel(corpus1)
print(type(tfidf))
 
corpus_tfidf = tfidf[corpus1]
print(type(corpus_tfidf))

NUM_TOPICS = 5
model = models.ldamodel.LdaModel(corpus_tfidf, num_topics=NUM_TOPICS, id2word=dic, 
                                 update_every=1, passes=500)

print("LDA model")
topics_found = model.print_topics(10)
counter = 1
for t in topics_found:
    print("Topic #{} {}".format(counter, t))
    counter += 1
print('********')

print(model.log_perplexity(corpus1))
print('********')
#model = models.lsimodel.LsiModel(corpus_tfidf,id2word=dic, num_topics=NUM_TOPICS)
with open("outputCAL5_500.txt", "w") as output:
    output.write('{}'.format(model.print_topics(10)))
    output.write("\n{}".format(model.log_perplexity(corpus1)))
    

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

