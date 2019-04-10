import CompanyProfiler
import MakePrediction

class Game:
    def __init__(self,company,pctIncrease,pctDecrease,investment):
        self.CoName = company
        self.CoProfile = CompanyProfiler.Profiler(company,investment)
        # self.CoProfile = CompanyProfiler.Profiler("AAPL")
        # self.initCoProfile()
        self.stockFile = "C:/Users/psalm/Documents/S&P500Data_Start/"+company+"_DailyData.txt"
        # self.stockFile = "C:/Users/psalm/Documents/S&P500Data_Start/AAPL_DailyData.txt"
        self.stockData = []
        self.stockPrice = 0
        self.stockTradeFee = 7.0
        self.initStockPrice()
        self.Pred = 0
        self.CoProfile.updateMoneyIn(self.stockPrice)
        self.CoProfile.updateHighLow(self.stockPrice)
        self.pctIncrease = pctIncrease*.01
        self.pctDecrease = pctDecrease*.01
        #update high/low values in companyProfiler

    # def initCoProfile(self):
    #     self.CoProfile = CompanyProfiler.Profiler("AAPL")
    #     self.CoProfile.getCurrentProfile()

    def initStockPrice(self):
        stockFile = open(self.stockFile,"r")
        data = stockFile.readlines()
        self.stockData = data[:]
        top = len(data)-1
        stockLine = data[top]
        price = stockLine.split("|")[1]
        price = price.replace(",","")
        self.stockPrice = float(price)

    def potentialStockCount(self):
        if self.CoProfile.pool >= self.CoProfile.startInvestment:
            return int(self.CoProfile.startInvestment / self.stockPrice)
        else:
            return int(self.CoProfile.pool / self.stockPrice)

    def projectedValue(self):
        if self.CoProfile.low == 0.0:
            self.CoProfile.low = self.CoProfile.getStockValue()
            self.CoProfile.writeProfile()

        #get 5 day prediction here
        # predictor = MakePrediction.Prediction("AAPL")
        predictor = MakePrediction.Prediction(self.CoName,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        predictor.loadData()
        predictor.initCLF()
        predictor.buildPredSet()
        predictor.Pred = predictor.clf.predict(predictor.XPredSet)[0]
        self.Pred = predictor.Pred
        stockCount = self.CoProfile.numStocks
        # print(self.CoName)
        # print("Predicted Price: ", predictor.Pred, " and Current Price ",self.stockPrice)
        if self.CoProfile.onTimeout is False:
            return ((stockCount * predictor.Pred) - (stockCount * self.stockPrice))
        else:
            potStock = self.potentialStockCount()
            return ((potStock * predictor.Pred) - (potStock * self.stockPrice))
        # print(predictor.Pred)

    def play(self):
        projVal = self.projectedValue()
        # print("projected value: ",projVal)
        # print(self.CoProfile.onTimeout)
        if self.CoProfile.onTimeout is False and projVal < 0:
            numStk = self.CoProfile.numStocks
            high = self.CoProfile.high
            potVal = ((numStk * self.Pred) - (numStk * high))
            stkValDecrease = self.Pred - self.CoProfile.high
            # print potVal
            print("Stock value decrease is ", abs(stkValDecrease), " and value to beat is ",self.stockPrice*self.pctDecrease)
            if potVal < 0 and abs(potVal) > self.stockTradeFee and abs(stkValDecrease) > (self.stockPrice*self.pctDecrease):
                print(self.CoName + " Selling Out!")
                self.CoProfile.sellOut(self.stockPrice)
                self.CoProfile.writeProfile()
        if self.CoProfile.onTimeout is True and projVal > 0:
            potStockCnt = self.potentialStockCount()
            low = self.CoProfile.low
            potVal = ((potStockCnt * self.Pred) - (potStockCnt * low))
            stkValIncrease = self.Pred - self.CoProfile.low
            # print(potStockCnt * self.Pred)
            # print(potStockCnt * low)
            # print(potVal)
            if potVal > 0 and abs(potVal) > self.stockTradeFee and stkValIncrease > (self.stockPrice*self.pctIncrease):
                print(self.CoName + " Buying In!")
                self.CoProfile.buyIn(self.stockPrice, potStockCnt)
                self.CoProfile.writeProfile()



# stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
# file = open(stkNames,"r")
# names = file.readlines()
# for n in names:
#     shrtName = n.split("|")[0].rstrip()
#     game = Game(shrtName)
#     game.play()

# testGameMSFT = Game("MSFT")
# testGameMSFT.play()


# testGame = Game("AAPL")
# print(testGame.projectedValue())
# testGame.play()
# print(testGame.projectedValue())
# print()
# print(testGame.stockPrice)
# print(testGame.potentialStockCount())
# testGame.CoProfile.printProfile()
# print(testGame.getStockPrice())
