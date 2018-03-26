# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:25:24 2017
Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

"""
#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.

from wordcloud import WordCloud
import matplotlib.pyplot as plt
content = open("wordcloud_tweets.json",'r').read()


wordcloud = WordCloud(max_font_size=40).generate(content) 
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#Reference/Source: Prof. Gene Lee's codes from Dropbox code files.
