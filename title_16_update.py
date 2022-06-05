# file for title_16.json
# Nancy
# feb 24

import sys
import types
import json
import re
#import  nltk
#from collections import defaultdict
from pprint import pprint
from math import log

# function to retrieve value from dictionary
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

# function to flatten a multidementional list
def flatten(list_to_flatten):
    if list_to_flatten is None:
        return []
    for elem in list_to_flatten:
        if isinstance(elem, (list, list)):
            for x in flatten(elem):
                yield x
        else:
            yield elem

# function to convert list to string
def convertListToString(listy):
    listy2 = []
    for elem in flatten(listy):
        if elem is not None:
            listy2.append(elem)
    return " ".join(listy2)

# function to compute base-2 logarithm
def log2(number):
    return log(number) / log(2)

# function to normalise the text
# replace all unwanted characters with space
cleaner = re.compile('[^a-z]+')
def clean(text):
    return cleaner.sub(' ',text)

# load the file
with open('title_16.json') as json_data:
    d = json.load(json_data)
    json_data.close()

# 1. collect the text in each subsection and convert them into a string
mylist = []
for value in recursive_items(d):
    if value is not None:
        mylist.extend(value)
mystring = convertListToString(mylist)
mystring = clean(mystring.lower().strip())      #clean the string

# #tokenize the text as follows:
# # a. for each subsection, split the text into a list of sentences.
# # method1: self-defined method
# An alternative way of tokenlizing is to use natural language toolkit. To remain consistency, I chose to use self-defined method for all tasks in this file.
sentences = []
# # while subsection.split('.') is not ' ':
sentences.extend(mystring.split('.')) 
#pprint (sentences)

# # b. For each sentence, split the string into a list of tokens or ngrams
tokens = []
tokens.extend(mystring.split(' '))
#print(len(tokens))
#pprint(tokens)

# 2. combine all ngrams into a corpus
with open ("ngrams.txt", "w") as text_file:
    print (mystring, file=text_file)

# and collect the following data:
# a. The frequency count for every ngram in the corpus
# b. The probability of each ngram in the corpus
# c. The entropy of each ngram in the corpus
ngram_frequency = {}
for ngram in tokens:
    if ngram in ngram_frequency:
        ngram_frequency[ngram] += 1
    else:
        ngram_frequency[ngram] = 1

#write ngram_frequency to a txt file
frequencyList = []
for key, value in recursive_items(ngram_frequency):
    if value is not None:
        frequencyList.extend( key+ ": "+ str(value)+ '\n')
frequencyString= convertListToString(frequencyList)
with open ("ngram_frequency.txt", "w") as text_file:
    print (frequencyString, file=text_file)         

# b. The probability of each ngram in the corpus
# c. The entropy of each ngram in the corpus
# one can also define entropy as the sum of entropy of each character contained in the ngram. For simplicity sake, I chose not to do so.
ngram_prob = {}
ngram_entropy = {}

for ngram in ngram_frequency:
    ngram_prob[ngram] = ngram_frequency[ngram] / len(tokens)
    ngram_entropy[ngram] = -ngram_prob[ngram] * log2(ngram_prob[ngram])

#pprint(ngram_prob)
#pprint(ngram_entropy)

#generate txt file for the probability of each ngram in the corpus
probabilityList = []
for key, value in recursive_items(ngram_prob):
    if value is not None:
         probabilityList.extend(key+ ": "+ str(value)+ '\n')
probabilityString= convertListToString(probabilityList)
with open ("ngram_probability.txt", "w") as text_file:
    print (probabilityString, file=text_file)   

#generate txt file for the entropy of each ngram in the corpus
entropyList = []
for key, value in recursive_items(ngram_entropy):
    if value is not None:
         entropyList.extend(key+ ": "+ str(value)+ '\n')
entropyString= convertListToString(entropyList)
with open ("ngram_entropy.txt", "w") as text_file:
    print (entropyString, file=text_file)   