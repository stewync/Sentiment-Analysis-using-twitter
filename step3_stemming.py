# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:43:16 2017

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.


import nltk
import json
#saving all kinds of stopwords


from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()

stopwords = nltk.corpus.stopwords.words('english')+['"rt','trump','donald','amp','uddf',
'"trump','"en','url','pbs','lang','null','"id','false','udc','trump"','spi','admin','https',
'thi',' trump','trump ','trump\"','trump\",','ud','udc','ude','uddf','lik','know']

infile = open("processed_tweets.json",'r')
content = infile.read().split()

real_words = []
for word in content:
    real_words.append(ls.stem(word))
infile.close() 
      
[word.lower() for word in real_words]
non_stopwords = []

for each_word in real_words:
    if each_word not in stopwords and each_word not in str('/,"realdonaldtrump",/,') and len(each_word) > 2:
        non_stopwords.append(each_word)
 
with open("wordcloud_tweets.json",'w') as outfile:
    json.dump(non_stopwords,outfile,indent=4)   

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
     
