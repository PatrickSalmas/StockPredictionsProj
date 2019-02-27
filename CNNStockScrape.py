import bs4
from bs4 import BeautifulSoup
import requests


print "Began Scraping CNN Stocks"

#Go through each page of CNN S&P 500 index and extract each company name
urlBaseStr = "https://money.cnn.com/data/markets/sandp/?page="

def getStockList(soupContent):
    return soupContent.select("div tbody tr")

def getStkShortName(stockCols):
    return stockCols[0].find('a').get_text()

def getStkFullName(stockCols, shortName):
#     return stockCols[0].get_text().partition(' ')[0]
    return stockCols[0].get_text()[len(shortName)+1:]



shtNameList = []
lngNameList = []
priceList = []
changeList = []
pctChangeList = []
PEList = []
volumeList = []
ytdList = []
stocksFile = open("S&P500Stocks.txt","w")

#S&P 500 has 1-34 pages
for p in range(1,35):
    urlStr = urlBaseStr + str(p)
    stockPage = requests.get(urlStr)
    print(urlStr," ",stockPage.status_code)
    stockContent = BeautifulSoup(stockPage.content, 'html.parser')
    stockList = getStockList(stockContent)
    for s in range(0,len(stockList)):
        stockColumns = stockList[s].find_all('td')
        shortName = getStkShortName(stockColumns)
        longName = getStkFullName(stockColumns,shortName)
        shtNameList.append(shortName)
        lngNameList.append(longName)

        print shortName, " | ",longName
        stocksFile.write(shortName+ " | "+longName+'\n')
        # print shortName," ",longName
        # print shortName, " | ",longName," | ",stockColumns[1].get_text()," | ",stockColumns[2].get_text()," | ",stockColumns[3].get_text()," | ",stockColumns[4].get_text()," | ",stockColumns[5].get_text()," | ",stockColumns[6].get_text(),'\n'
        # stocksFile.write(shortName+ " | "+longName+" | "+stockColumns[1].get_text()+" | "+stockColumns[2].get_text()
        #         +" | "+stockColumns[3].get_text()+" | "+stockColumns[4].get_text()+" | "+stockColumns[5].get_text()+
        #         " | "+stockColumns[6].get_text()+'\n')
        # print(getStkShortName(stockColumns), " ", len(getStkShortName(stockColumns)))

        #INSTEAD OF PRINTING, SHOULD WRITE TO FILE