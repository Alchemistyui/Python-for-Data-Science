# -*- coding: utf-8 -*- 

# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

import pdb

# import re

# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('stopwords'))
# print(len(stopwords))
# create your data structure here.  
wordcount={}

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation, 
# and use case demiliters. The functions lower() and split() will be useful!

def count_word():
    with open('98-0.txt', encoding='UTF-8-sig') as f:
        # print(f.readlines()[0])
        # lines = f.readlines()[0:2]
        lines = [x.strip() for x in f.readlines()]

    for l in lines:
        if l != '':
            words = l.replace(".", "").replace(",", "").replace('-', ' ').replace('"', '').split()
            for w in words:
                w = w.lower()
                if w not in stopwords:
                    if wordcount.get(w):
                        wordcount[w] += 1
                        # wordcount[w] = wordcount[w] + 1
                    else:
                        wordcount[w] = 1
count_word()
# print(wordcount)
# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.
count = collections.Counter(wordcount)

print(count.most_common(10))









