import PlayGame
import BuildTrainSet
import TrainData



stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
for n in names:
    shrtName = n.split("|")[0].rstrip()
    buildTrain = BuildTrainSet.TrainBuilder(shrtName,4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    buildTrain.loadData()
    buildTrain.buildTrainSet()
    # build_5Day = BuildTrainSet.TrainBuilder(shrtName)
    # build_5Day.loadData()
    # build_5Day.buildTrainSet_5Day()
    investmentList = [500, 600, 700, 800, 900, 1000]
    for i in investmentList:
        game = PlayGame.Game(shrtName,1,1,i)
        if len(game.stockData) != 0:
            game.play()

# testBuild_5Day = BuildTrainSet.TrainBuilder("AAPL")
# testBuild_5Day.loadData()
# testBuild_5Day.buildTrainSet_5Day()
#
# testGame = PlayGame.Game("MSFT")
# testGame.play()