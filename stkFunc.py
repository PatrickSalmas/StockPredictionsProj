#Used for S&P500Stocks.txt OR stock-trend_titleHits.txt
def getShortName(line):
    names = line.split("|")
    return names[0]

#Used for S&P500Stocks.txt OR stock-trend_titleHits.txt
def getLongName(line):
    names = line.split("|")
    return names[1]

#Used for stock-trend_titleHits.txt ONLY
def getStk_trend_titleHits(line):
    list = line.split("|")
    return list[2]

#Used for S&P500Stock.txt ONLY
def getPrice(line):
    list = line.split("|")
    return list[2]

#Used for S&P500Stock.txt ONLY
def getChange(line):
    list = line.split("|")
    return list[3]

#Used for S&P500Stock.txt ONLY
def getPctChange(line):
    list = line.split("|")
    return list[4]

#Used for S&P500Stock.txt ONLY
def getPE(line):
    list = line.split("|")
    return list[5]

#Used for S&P500Stock.txt ONLY
def getVolume(line):
    list = line.split("|")
    return list[6]

#Used for S&P500Stock.txt ONLY
def getYTDChange(line):
    list = line.split("|")
    return list[7]
