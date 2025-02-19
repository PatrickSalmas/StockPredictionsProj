import bs4
from bs4 import BeautifulSoup
import requests
import datetime
import PlayGame          #for TEMP SYSTEM
import CompanyProfiler   #for TEMP SYSTEM
import BuildTrainSet     #for TEMP SYSTEM
import TrainData         #for TEMP SYSTEM


urlBaseStr = "https://money.cnn.com/data/markets/sandp/?page="
d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

def getStockList(soupContent):
    return soupContent.select("div tbody tr")

def getStkShortName(stockCols):
    return stockCols[0].find('a').get_text()

def getStkFullName(stockCols, shortName):
#     return stockCols[0].get_text().partition(' ')[0]
    return stockCols[0].get_text()[len(shortName)+1:]


#Scrape data for S&P500 overall
page = requests.get("https://money.cnn.com/data/markets/sandp/?page=1")
soup = BeautifulSoup(page.content, 'html.parser')

select = soup.select("body tr span")
overallVal = select[0].get_text()
overallVal = overallVal.replace(",","")
select = soup.select("div.wsod_fLeft td.wsod_quoteDataPoint")
tdVolume = select[4].get_text()
tdVolume = tdVolume.replace(",","")
avgVolume = select[5].get_text()
avgVolume = avgVolume.replace(",","")
avgPE = select[6].get_text()
ytdChg = select[7].get_text()

if d.hour < 12:
    SP500_fName = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/SP500_DailyData.txt"
else:
    SP500_fName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/SP500_DailyData.txt"


SP500_file = open(SP500_fName,"a+")
SP500_file.write(dateStamp+" | "+overallVal+" | "+tdVolume+" | "+avgVolume+" | "+avgPE+" | "+ytdChg+'\n')


#Scrape for all individual company stocks in S&P500
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


        if d.hour < 12:
            fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/"+shortName + "_DailyData.txt"
        else:
            fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shortName + "_DailyData.txt"

        stocksFile = open(fileName,"a+")


        # fileName = "D:/Users/psalmas/Documents/S&P500Data/"+longName + "_DailyData.txt"

        stockValue = stockColumns[1].get_text()
        stockValue = stockValue.replace(",","")
        print shortName, " | ",longName," | ",stockValue," | ",stockColumns[2].get_text()," | ",stockColumns[3].get_text()," | ",stockColumns[4].get_text()," | ",stockColumns[5].get_text()," | ",stockColumns[6].get_text(),'\n'


        stocksFile.write(dateStamp+" | "+stockValue+" | "+stockColumns[4].get_text()+" | "+
                         stockColumns[5].get_text()+" | "+stockColumns[6].get_text()+'\n')


#Add appropiate data corresponding to whether or not each company was in top/bottom 10, 50, and 100 companies for the day
import AppendTopBottomData

if d.hour < 12:
    import RunMarket
    import RecordDailyGrowth



