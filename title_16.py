# file for title_16.json
# Nancy
# feb 24

import sys
import types
import json
#import  nltk
from pprint import pprint
from collections import defaultdict
from math import log


# function to retrieve value from dictionary
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

# function to read a given subsection from dictionary


def readMyFile(dictionary, chapterNum, subchapterNum, partNum, sectionNum):
    chapterKey = "chapter" + " " + chapterNum
    subchapterKey = "subchapter" + " " + subchapterNum
    partKey = "part" + " " + partNum
    sectionKey = "section" + " " + sectionNum
    return dictionary[chapterKey][subchapterKey][partKey][sectionKey]

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

# function to convert dictionary to list


def convertDicToString(dicty):
    listy = []
    for key, value in dicty.items():
        if 'text' in key.lower() and type(value) is dict:
            for value1 in recursive_items(value):
                listy.append(value1)
    return listy

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

# load the file

with open('title_16.json') as json_data:
    d = json.load(json_data)
    json_data.close()

# collect the text in each subsection
mylist = []
for value in recursive_items(d):
    if value is not None:
        mylist.extend(value)

mystring = convertListToString(mylist)
# pprint(mystring)
# #read a given subsection from the given file
# target = readMyFile(d, "ii", "a", "1000", "1")

# #convert the target from a dictionary to a string
# subsection = convertDicToString(target)
# #pprint(content)

# #tokenize the text as follows:
# # a. for each subsection, split the text into a list of sentences.
# # method1: self-defined method
sentences = []
# # while subsection.split('.') is not ' ':
sentences.extend(mystring.split('.'))
#pprint (sentences)

# # method2:use NLTK
# #print ('\n-----\n'.join(tokenizer.tokenize(subsection)))

# # b. For each sentence, split the string into a list of tokens or ngrams
tokens = []
tokens.extend(mystring.split(' '))
#pprint (tokens)
#print(len(tokens))

# 2. combine all ngrams into a corpus
# it is already done in part 1, the corpus is given by mystring

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
#pprint(ngram_frequency)

# b. The probability of each ngram in the corpus
# c. The entropy of each ngram in the corpus
ngram_prob = {}
ngram_entropy = {}

for ngram in ngram_frequency:
    ngram_prob[ngram] = ngram_frequency[ngram] / len(tokens)
    ngram_entropy [ngram] = -ngram_prob[ngram] * log2(ngram_prob[ngram])

#pprint(ngram_prob)
#pprint(ngram_entropy)

#print (len(mylist[2][1]))
#chapterOne = []
# for value in mylist.items():
# chapterOne.append(value.split('.'))
# elif type(value) is tuple:
#     list(value)
#     chapterOne.append(value.split('.'))

#print (chapterOne)
