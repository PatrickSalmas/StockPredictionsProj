import PlayGame
import BuildTrainSet
import TrainData
# import FeatClasses
import datetime
import os


d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
dayPred = [1,2,3,4,5]
for dp in dayPred:
    print(str(dp)+" Predictions")
    buys = []
    sells = []

    #build 2-d array for buying/selling scenarios
    for i in range(0,6):
        buys.append([0,0,0,0,0])
        sells.append([0,0,0,0,0])

    #For each company, train the data for that company
    #then for each investment value i, and each j (0-5), play game and add buy and sell
    #counts into 2d array
    for n in names:
        shrtName = n.split("|")[0].rstrip()
        # buildTrain = BuildTrainSet.TrainBuilder(shrtName,4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

        buildTrain = BuildTrainSet.TrainBuilder(shrtName,dp-1,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                                                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        buildTrain.loadData()
        buildTrain.buildTrainSet()
        investmentList = [500, 600, 700, 800, 900, 1000]
        for i in range(0,len(investmentList)):
            # print(str(investmentList[i])+" Investement")
            for j in range(0,5):
                game = PlayGame.Game(shrtName,dp,j,j,investmentList[i])
                if len(game.stockData) != 0:
                    res = game.play()
                    if res == "buy": buys[i][j] += 1
                    if res == "sell": sells[i][j] += 1


    #Go through 2d array and write the buy and sell data to each respective SBCount.txt
    #REFACTOR NOTE: this functionality is sort of out place (may require heavy change)
    investmentList = [500, 600, 700, 800, 900, 1000]
    for i in range(0,6):
        for j in range(0,5):
            basePath = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(dp)+"DayPred/"+str(investmentList[i])+"/"+str(j)+"_"+str(j)
            if not os.path.exists(basePath):
                os.makedirs(basePath)
            stkTransLoc = basePath+"/SBCount.txt"
            stkTransFile = open(stkTransLoc,"a+")
            stkTransFile.write(dateStamp + " " + str(buys[i][j]) + " " + str(sells[i][j])+"\n")


