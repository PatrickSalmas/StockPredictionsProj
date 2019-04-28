import CompanyProfiler
import MakePrediction

class Game:
    def __init__(self,company,pctIncrease,pctDecrease,investment):
        self.CoName = company
        self.CoProfile = CompanyProfiler.Profiler(company,investment,pctIncrease,pctDecrease)
        self.stockFile = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/"+company+"_DailyData.txt"
        self.stockData = []
        self.stockPrice = 0
        self.stockTradeFee = 7.0
        self.initStockPrice()
        self.Pred = 0
        self.CoProfile.updateMoneyIn(self.stockPrice)
        self.CoProfile.updateHighLow(self.stockPrice)
        self.pctIncrease = pctIncrease*.01
        self.pctDecrease = pctDecrease*.01

    #Get and initialize current price of stock
    #Stock price is based on recently scraped data (morning scrape)
    #REFACTOR NOTE: Currently self.stockData is soley set for the purpose
    #of haulting execution in RunMarket. Should seriously consider changing
    #this design so that there is a more effecient way of checking for this condition
    def initStockPrice(self):
        stockFile = open(self.stockFile,"r")
        data = stockFile.readlines()
        self.stockData = data[:]
        top = len(data)-1
        stockLine = data[top]
        price = stockLine.split("|")[1]
        # price = price.replace(",","")
        self.stockPrice = float(price)

    #Determines the potential number of stocks that can be purchased for a particular
    #company. Used for the case when a company doesn't currently have purchased stocks in market
    def potentialStockCount(self):
        if self.CoProfile.pool >= self.CoProfile.startInvestment:
            return int(self.CoProfile.startInvestment / self.stockPrice)
        else:
            return int(self.CoProfile.pool / self.stockPrice)

    #Makes a prediction based upon current data and calculates the potential future value
    #based on predictions
    #REFACTOR NOTE: May want to potentially split this up into Prediction function and
    #Potential value calculation function
    def projectedValue(self):
        if self.CoProfile.low == 0.0:
            self.CoProfile.low = self.CoProfile.getStockValue()
            self.CoProfile.writeProfile()

        predictor = MakePrediction.Prediction(self.CoName,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        predictor.loadData()
        predictor.initCLF()
        predictor.buildPredSet()
        predictor.Pred = predictor.clf.predict(predictor.XPredSet)[0]
        self.Pred = predictor.Pred
        stockCount = self.CoProfile.numStocks
        if self.CoProfile.onTimeout is False:
            return ((stockCount * predictor.Pred) - (stockCount * self.stockPrice))
        else:
            potStock = self.potentialStockCount()
            return ((potStock * predictor.Pred) - (potStock * self.stockPrice))


    #Detemines if a company will sell or buy based on set rules
    #REFACTOR NOTE: May want to think of renaming, or rethinking some logic
    #with projVal and potVal (little confusing)
    #REFACTOR NOTE: May want to rethink some way for rules to be checked either
    #in other function or other class. Think lego pieces
    def play(self):
        projVal = self.projectedValue()
        if self.CoProfile.onTimeout is False and projVal < 0:
            numStk = self.CoProfile.numStocks
            high = self.CoProfile.high
            potVal = ((numStk * self.Pred) - (numStk * high))
            stkValDecrease = self.Pred - self.CoProfile.high
            if potVal < 0 and abs(potVal) > self.stockTradeFee and abs(stkValDecrease) > (self.stockPrice*self.pctDecrease):
                print(self.CoName + " Selling Out!")
                self.CoProfile.sellOut(self.stockPrice)
                self.CoProfile.writeProfile()
                return "sell"
        if self.CoProfile.onTimeout is True and projVal > 0:
            potStockCnt = self.potentialStockCount()
            low = self.CoProfile.low
            potVal = ((potStockCnt * self.Pred) - (potStockCnt * low))
            stkValIncrease = self.Pred - self.CoProfile.low
            if potVal > 0 and abs(potVal) > self.stockTradeFee and stkValIncrease > (self.stockPrice*self.pctIncrease):
                print(self.CoName + " Buying In!")
                self.CoProfile.buyIn(self.stockPrice, potStockCnt)
                self.CoProfile.writeProfile()
                return "buy"

        return "nothing"




# testGameMSFT = Game("MSFT")
# testGameMSFT.play()


