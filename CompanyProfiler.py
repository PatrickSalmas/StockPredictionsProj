import os

class Profiler:
    def __init__(self,company):
        self.CoName = company
        self.money_in = 0
        # self.liquidVal = 0        #line0       total value in stocks  + pool(leftover/remainder)
        self.numStocks = 0        #line1
        self.onTimeout = True     #line3
        self.high = 0     #line4
        self.low = 0   #line5
        self.pool = 0             #line2
        self.startInvestment = 0  #line6
        self.liquidVal = 0
        self.profileFile = "C:/Users/psalm/Documents/S&P500_Profiles/"+company+".txt"
        self.stockFile = "C:/Users/psalm/Documents/S&P500Data_End/"+company+"_DailyData.txt"
        self.CoEndData = []
        self.stockTradeFee = 7
        self.getCurrentProfile()
        #Maybe need to create something so that everytime a profile is loaded, it's liquidVal is updated based
        #upon current stock price, for now being done from PlayGame.py

    def writeProfile(self):
        file = open(self.profileFile,"w+")
        # file.write("Liquid Value: " + str(self.liquidVal) + '\n')
        file.write("Number of Stocks: " + str(self.numStocks) + '\n')
        file.write("Money In: " + str(self.money_in) + '\n')
        file.write("Pool Money: " + str(self.pool) + '\n')
        file.write("On Time Out: " + str(self.onTimeout) + '\n')
        file.write("High Value: " + str(self.high) + '\n')
        file.write("Low Value: " + str(self.low) + '\n')
        file.write("Starting Investment: " + str(self.startInvestment) + '\n')
        file.write("Liquid Value: " + str(self.money_in + self.pool) + '\n')

    def updateMoneyIn(self,stockPrice):
        # self.liquidVal = (stockPrice * self.numStocks) + self.pool
        self.money_in = (stockPrice * self.numStocks)
        self.writeProfile()

    def updateHighLow(self,stockPrice):
        if stockPrice < self.low:
            self.low = stockPrice
        if stockPrice > self.high:
            self.high = stockPrice

    def getCurrentProfile(self):
        exists = os.path.isfile(self.profileFile)
        if exists:
            file = open(self.profileFile,"r")
            lines = file.readlines()
            arr = lines[0].split(' ')
            self.numStocks = float(arr[len(arr)-1])
            arr = lines[1].split(' ')
            self.money_in = float(arr[len(arr)-1])
            arr = lines[2].split(' ')
            self.pool = float(arr[len(arr)-1])
            arr = lines[3].split(' ')
            if arr[len(arr)-1].rstrip() == "True":
                self.onTimeout = True
            else:
                self.onTimeout = False
            arr = lines[4].split(' ')
            self.high = float(arr[len(arr)-1])
            arr = lines[5].split(' ')
            self.low = float(arr[len(arr)-1])
            arr = lines[6].split(' ')
            self.startInvestment = float(arr[len(arr)-1])
            arr = lines[7].split(' ')
            self.liquidVal = float(arr[len(arr)-1])
        else:
            #create new file
            self.initNewProfile()

    def initNewProfile(self):
        self.startInvestment = 1500   #for now hardcoded
        self.pool = 1500
        # self.liquidVal = 1500


    def printProfile(self):
        # print(self.liquidVal)
        print(self.numStocks)
        print(self.pool)
        print(self.money_in)
        print(self.onTimeout)
        print(self.high)
        print(self.low)
        print(self.startInvestment)

    def setInvestment(self,value):
        self.startInvestment = value
        # self.liquidVal = value

    def getStockValue(self):
        file = open(self.stockFile,"r")
        lines = file.readlines()
        top = len(lines)-1
        data = lines[top].split("|")
        data[1] = data[1].replace(',','')
        return float(data[1])

    # def potentialStockCount(self):
    #     if self.pool >= self.startInvestment:
    #

    def buyIn(self,stockPrice,stockCount):
        self.high = stockPrice
        # numStock = self.startInvestment/stockPrice
        self.numStocks = int(stockCount)
        self.pool -= (self.numStocks * stockPrice)
        self.pool -= self.stockTradeFee
        self.money_in = self.numStocks * stockPrice
        self.onTimeout = False

    def sellOut(self,stockPrice):
        self.low = stockPrice
        self.pool += (self.numStocks * stockPrice)
        self.pool -= self.stockTradeFee
        self.money_in = 0
        self.numStocks = 0
        self.onTimeout = True



#something wrong with liquid value calculation and all that

# TestProfiler = Profiler("AAPL")
# TestProfiler.writeProfile()
# # print(TestProfiler.getStockValue())
# TestProfiler.setInvestment(1500)
# TestProfiler.buyIn()
# # TestProfiler.writeProfile()
# # print()
# TestProfiler.sellOut()
# TestProfiler.writeProfile()

# TestProfiler.getCurrentProfile()
# TestProfiler.printProfile()