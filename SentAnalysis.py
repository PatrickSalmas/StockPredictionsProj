import datetime
from collections import defaultdict
import string
import nltk
from nltk.stem.porter import *

punctuation = set(string.punctuation)
stemmer = PorterStemmer()
d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

#For now we are going to only concern ourself with the words that are in the lexicon,
#and for now we will not use any sort of weighting system (more simple to just get a feel for things)
lexFile = open("C:/Users/psalm/Documents/NRC-VAD-Lexicon.txt","r")
lexicon = {}
for l in lexFile:
    # print l
    ws = l.split()
    leng = len(ws)
    strKey = ''.join(ws[:leng-3])
    lexicon[strKey] = ws[leng-3:]

print len(lexicon)

lexList = []
lexCount = []
lexWordIndex = {}
for w in lexicon:
    lexList.append(w)
    lexCount.append(0)
    lexWordIndex[w] = lexList.index(w)


def getWordCount(text):
    wordCount = defaultdict(int)
    if text != "No_text":
        for w in text.split():
            wordCount[w] += 1

    return wordCount


#This should actually be our feature right here!!
def getStoryLexCount(wordCountDict):
    storyLexCount = lexCount[:]
    for w in wordCountDict:
        if w in lexWordIndex:
            i = lexWordIndex[w]
            storyLexCount[i] = wordCountDict[w]
            # storyLexList.insert(i,wordCountDict[w])

    storyLexCount.append(1)
    return storyLexCount


#for right now we are just going send Google Trend scrapes to a single location
#soon we are going to want to send specifically timed scrapes to specific folders
def writeFeatToFile(companyName,featList):
    coFile = open("D:/Users/psalmas/Documents/GoogleTrendScrape/"+companyName+"_GTScrape.txt","a+")
    # coFile.write(featList+'\n')
    strList = " ".join(str(x) for x in featList)
    coFile.write(dateStamp + " | " + strList+'\n')
#
# def feature(wordCountList):
#     feat = [0]*len(wordCountList)





