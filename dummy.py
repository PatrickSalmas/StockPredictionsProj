import selenium
# import scrapy
import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from collections import defaultdict
import string
import nltk
from nltk.stem.porter import *


#Selenium baby!!!!


# d = datetime.datetime.today()
# print d
# print d.year,"-",d.month,"-",d.day
# print d.hour
# dateStamp =




# -*- coding: UTF-8 -*-

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/psalm/Documents/chromedriver.exe')
# driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all")
# myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='title']"))))
# #
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     try:
#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='feed-load-more-button'][@ng-click=\"ctrl.loadMoreFeedItems()\"]"))).click()
#         WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements_by_xpath("//div[@class='title']")) > myLength)
#         titles = driver.find_elements_by_xpath("//div[@class='title']")
#         myLength = len(titles)
#     except TimeoutException:
#         break
# #
# count = 0
# for title in titles:
#     print title.text," ",count
#     count+=1
# driver.quit()

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
#
# driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/psalm/Documents/chromedriver.exe')
#
# element = driver.find_elements_by_css_selector("div[ng-click=\"ctrl.loadMoreFeedItems()\"]")
# element.click()


# page = requests.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=b")
# soup = BeautifulSoup(page.content, 'html.parser')
# print soup
# # selection = soup.select("div a")
# selection = soup.select("a")
# # print selection
# for i in selection:
#     print selection

#ST SOL1
# SOLUTION FOR EXTRACTING ALL GOOGLE TREND TITLES AND RETREIVING ALL OF THE LINKS OF ARTICLES
# JUST THE SOLUTION FOR THE FIRST PAGE OF GOOGLE TRENDS AND DOESN'T INCLUDE LOADING PROCESS
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/psalm/Documents/chromedriver.exe')
# driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=b")
# myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='title']"))))
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='feed-load-more-button'][@ng-click=\"ctrl.loadMoreFeedItems()\"]"))).click()
# WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements_by_xpath("//div[@class='title']")) > myLength)
# titles = driver.find_elements_by_xpath("//div[@class='title']")
# summaries = driver.find_elements_by_xpath("//div[@class='details-bottom']/div[@class='subtitles-text-wrapper visible']/div[@class='summary-text']/a[@ng-href]")
# #
# #
# #Extract text from given url
# def getText(urlArg):
#     if urlArg is None: return ["No_text"]
#     storyPage = requests.get(urlArg)
#     if storyPage.status_code != 200: return ["No_text"]
#     storyContent = BeautifulSoup(storyPage.content, 'html.parser')
#     storyBody = storyContent.find_all('p')
#     print "getText Success"
#     return storyBody
#     # for p in storyBody:
#     #     print p
# #
# #
# # #We have all the links now! We can now go through the articles and extract all the paragraphs
# urls = []
# for s in summaries:
#     url = s.get_attribute("href")
#     urls.append(url)
#     # print url
# #     print u.location
# #     print u.get_attribute("href")
# #     print()
# # print urls
#
# storyTexts = []
# for u in urls:
#     storyText = getText(u)
#     storyTexts.append(storyText)
#
# for text in storyTexts:
#     for p in text:
#         if p != "No_text":
#             print p.get_text()
#     print "<-------->"

#SOL 2: solution/logic for the "Sentiment Analysis Feature"
lexFile = open("C:/Users/psalm/Documents/NRC-VAD-Lexicon.txt","r")
lexicon = {}
for l in lexFile:
    # print l
    ws = l.split()
    leng = len(ws)
    str = ''.join(ws[:leng-3])
    lexicon[str] = ws[leng-3:]

lexList = []
lexCount = []
lexWordIndex = {}
for w in lexicon:
    lexList.append(w)
    lexCount.append(0)
    lexWordIndex[w] = lexList.index(w)


def getStoryLexCount(wordCountDict):
    storyLexList = lexCount[:]
    for w in wordCountDict:
        if w in lexWordIndex:
            i = lexWordIndex[w]
            storyLexList[i] = wordCountDict[w]
            # storyLexList.insert(i,wordCountDict[w])

    return storyLexList


def getWordCount(text):
    wordCount = defaultdict(int)
    for p in text:
        if p != "No_text":
            for w in p.get_text().split():
                wordCount[w] += 1

    return wordCount

# wordCount = defaultdict(int)
punctuation = set(string.punctuation)
stemmer = PorterStemmer()
print len(lexicon)

#Logic for each story pretty sure
for t in range(0,len(storyTexts)):
    # wcDict = getWordCount(text)
    wcDict = getWordCount(storyTexts[t])
    stryLexCnt = getStoryLexCount(wcDict)
    print(t, " ", stryLexCnt)
    # break

#END SOL 2

    # print len(getWordCount(text))
    # for p in text:
    #     if p != "No_text":
    #         for w in p.get_text().split():
    #             wordCount[w] += 1




# for w in wordCount:
#     print w," ",wordCount[w]
            # print p.get_text()
# print len(defDict)


# lexFile = open("C:/Users/psalm/Documents/Emoticon-AFFLEX-NEGLEX-unigrams.txt","r")
# lexFile = open("C:/Users/psalm/Documents/NRC-VAD-Lexicon.txt","r")
#
# # lexicon = []
# lexicon = {}
# for l in lexFile:
#     # print l
#     ws = l.split()
#     # print ws[0]
#     # print ws[1:]
#     leng = len(ws)
#     str = ''.join(ws[:leng-3])
#     lexicon[str] = ws[leng-3:]
#     # for w in ws:
#         # lexicon.append(w)
#         # print "adding ",w[0]
#         # lexicon[w[0]] = w[1:]
# for w in wordCount:
#     # print w
#     if w in lexicon:
#         # print w," ",wordCount[w]
#         print wordCount[w]," ",w," ", lexicon[w]


# print getText("https://www.cruiseindustrynews.com/cruise-news/20183-carnival-cruise-line-brings-style-to-rose-parade.html")


#Let's use scraped urls now
#END SOL1

driver.quit()

# page = requests.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=b")
# soup = BeautifulSoup(page.content, 'html.parser')
# selection = soup.select("div a")
# for i in selection:
#     print i

# for i in titles:
#     print i.text

# #Let's now extract the "value" of the S&P index, along with its YTD change, and its volume, and avgVolume???
# page = requests.get("https://money.cnn.com/data/markets/sandp/?page=1")
# soup = BeautifulSoup(page.content, 'html.parser')
# # select = soup.find_all('td', class_='wsod_last wsod_lastIndex')
# # select.
# # select = soup.select("tbody tr td span")
#
# # GETS THE OVERALL VALUE OF THE S&P500 INDEX
# select = soup.select("body tr span")
# print select[0].get_text()
#
# # select = soup.select("body tr")
# # select = soup.select("body tr ytdval")
# # select = soup.select("div.wsod_fLeft")
# # print select[3]
# print()
# # #Today's volume:                  index 4
# # #Average daily volume (3 months): index 5
# # #Average P/E:                     index 6
# # #1 year change:                   index 7
# select = soup.select("div.wsod_fLeft td.wsod_quoteDataPoint")
# # select = soup.select("div.wsod_fLeft")
# print select[4].get_text()
# print select[5].get_text()
# print select[6].get_text()
# print select[7].get_text()
# # # print select
# # # print soup
# # for i in range(0,len(select)):
# #     print i," ",select[i]

