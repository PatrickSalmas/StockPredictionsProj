import CompanyProfiler
import MakePrediction

class Game:
    def __init__(self,company):
        self.CoName = company
        self.CoProfile = CompanyProfiler.Profiler(company)
        # self.CoProfile = CompanyProfiler.Profiler("AAPL")
        # self.initCoProfile()
        self.stockFile = "C:/Users/psalm/Documents/S&P500Data_Start/"+company+"_DailyData.txt"
        # self.stockFile = "C:/Users/psalm/Documents/S&P500Data_Start/AAPL_DailyData.txt"
        self.stockData = []
        self.stockPrice = 0
        self.stockTradeFee = 7.0
        self.initStockPrice()
        self.FiveDayPred = 0
        self.CoProfile.updateMoneyIn(self.stockPrice)
        self.CoProfile.updateHighLow(self.stockPrice)
        #update high/low values in companyProfiler

    # def initCoProfile(self):
    #     self.CoProfile = CompanyProfiler.Profiler("AAPL")
    #     self.CoProfile.getCurrentProfile()

    def initStockPrice(self):
        stockFile = open(self.stockFile,"r")
        data = stockFile.readlines()
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
        if self.CoProfile.high == 0.0 and self.CoProfile.low == 0.0:
            self.CoProfile.low = self.CoProfile.getStockValue()
            self.CoProfile.writeProfile()

        #get 5 day prediction here
        # predictor = MakePrediction.Prediction("AAPL")
        predictor = MakePrediction.Prediction(self.CoName)
        predictor.loadData()
        predictor.initCLF_5Day()
        predictor.buildPredSet_5Day()
        predictor.FiveDayPred = predictor.clf_5Day.predict(predictor.XPredSet_5Day)[0]
        self.FiveDayPred = predictor.FiveDayPred
        stockCount = self.CoProfile.numStocks
        print(self.CoName)
        print("Predicted Price: ", predictor.FiveDayPred, " and Current Price ",self.stockPrice)
        if self.CoProfile.onTimeout is False:
            return ((stockCount * predictor.FiveDayPred) - (stockCount * self.stockPrice))
        else:
            potStock = self.potentialStockCount()
            # print(potStock)
            return ((potStock * predictor.FiveDayPred) - (potStock * self.stockPrice))
        # print(predictor.FiveDayPred)

    def play(self):
        projVal = self.projectedValue()
        # print("projected value: ",projVal)
        # print(self.CoProfile.onTimeout)
        if self.CoProfile.onTimeout is False and projVal < 0:
            numStk = self.CoProfile.numStocks
            high = self.CoProfile.high
            potVal = ((numStk * self.FiveDayPred) - (numStk * high))
            # print potVal
            if potVal < 0 and abs(potVal) > (self.stockTradeFee*.75):
                print(self.CoName + " Selling Out!")
                self.CoProfile.sellOut(self.stockPrice)
                self.CoProfile.writeProfile()
        if self.CoProfile.onTimeout is True and projVal > 0:
            potStockCnt = self.potentialStockCount()
            low = self.CoProfile.low
            potVal = ((potStockCnt * self.FiveDayPred) - (potStockCnt * low))
            # print(potStockCnt * self.FiveDayPred)
            # print(potStockCnt * low)
            # print(potVal)
            if potVal > 0 and abs(potVal) > (self.stockTradeFee*.75):
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
