import stkFunc

#Let's go through thr stock-trend hit list and observe the value of that particular stock



#print stocks that have at least a single hit, and the amount change in stock price, and change in stock price pct
file = open("stock-trend_titleHits.txt","r")
stkDataFile = open("S&P500Stocks.txt","r")
lines = file.readlines()
linesData = stkDataFile.readlines()
for l in range(0,len(lines)):
    if int(stkFunc.getStk_trend_titleHits(lines[l])) > 0:
        print stkFunc.getLongName(lines[l])," ",stkFunc.getStk_trend_titleHits(lines[l]).rstrip()," with changes ",stkFunc.getChange(linesData[l])," and ",stkFunc.getPctChange(linesData[l])