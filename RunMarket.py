import PlayGame
import BuildTrainSet
import TrainData
import datetime

d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)


stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
buys = []
sells = []
for i in range(0,6):
    buys.append([0,0,0,0,0])
    sells.append([0,0,0,0,0])

for n in names:
    shrtName = n.split("|")[0].rstrip()
    buildTrain = BuildTrainSet.TrainBuilder(shrtName,4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    buildTrain.loadData()
    buildTrain.buildTrainSet()
    # build_5Day = BuildTrainSet.TrainBuilder(shrtName)
    # build_5Day.loadData()
    # build_5Day.buildTrainSet_5Day()
    investmentList = [500, 600, 700, 800, 900, 1000]
    for i in range(0,len(investmentList)):
        for j in range(0,5):
            game = PlayGame.Game(shrtName,j,j,investmentList[i])
            if len(game.stockData) != 0:
                res = game.play()
                if res == "buy": buys[i][j] += 1
                if res == "sell": sells[i][j] += 1


        #This recodring of buys and sells needs to happen at the very end
        #Need two, two dimensional arrays to keep track of all buys and sells
        # for j in range(0,5):
        #     stkTansLoc = "C:/Users/psalm/Documents/S&P500_GrowthProfiles/"+str(i)+"/"+str(j)+"_"+str(j)+"/stockCount.txt"
        #     stkTransFile = open(stkTansLoc,"a+")
        #     stkTransFile.write(dateStamp + " " + str(buys[j]) + " " + str(sells[j])+"\n")

investmentList = [500, 600, 700, 800, 900, 1000]
for i in range(0,6):
    for j in range(0,5):
        stkTansLoc = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(investmentList[i])+"/"+str(j)+"_"+str(j)+"/SBCount.txt"
        stkTransFile = open(stkTansLoc,"a+")
        stkTransFile.write(dateStamp + " " + str(buys[i][j]) + " " + str(sells[i][j])+"\n")



# testBuild_5Day = BuildTrainSet.TrainBuilder("AAPL")
# testBuild_5Day.loadData()
# testBuild_5Day.buildTrainSet_5Day()
#
# testGame = PlayGame.Game("MSFT")
# testGame.play()