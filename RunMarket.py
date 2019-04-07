import PlayGame
import BuildTrainSet
import TrainData



stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
for n in names:
    shrtName = n.split("|")[0].rstrip()
    build_5Day = BuildTrainSet.TrainBuilder(shrtName)
    build_5Day.loadData()
    build_5Day.buildTrainSet_5Day()

    game = PlayGame.Game(shrtName)
    game.play()

# testBuild_5Day = BuildTrainSet.TrainBuilder("AAPL")
# testBuild_5Day.loadData()
# testBuild_5Day.buildTrainSet_5Day()
#
# testGame = PlayGame.Game("MSFT")
# testGame.play()