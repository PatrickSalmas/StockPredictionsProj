import TopBottomStocks
import ColumnDesigner
import datetime

d = datetime.datetime.today()
hour = d.hour

stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
if hour >= 12:
    tb10 = TopBottomStocks.TopBottomStocks(10)
    tb50 = TopBottomStocks.TopBottomStocks(50)
    tb100 = TopBottomStocks.TopBottomStocks(100)
    for n in names:
        shrtName = n.split("|")[0].rstrip()
        fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shrtName + "_DailyData.txt"
        # data = open(fileName,"r").readlines()
        colDes = ColumnDesigner.ColumnDesigner(fileName)
        todayVal = colDes.getColumn("last",1)
        yesterVal = colDes.getColumn("yesterday",1)
        weightChange = (float(todayVal) - float(yesterVal)) / float(yesterVal)
        print(shrtName)
        print(weightChange)
        tb10.addItem(shrtName,weightChange)
        tb50.addItem(shrtName,weightChange)
        tb100.addItem(shrtName,weightChange)

    tb10.calculate()
    tb50.calculate()
    tb100.calculate()
    for n in names:
        shrtName = n.split("|")[0].rstrip()
        fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shrtName + "_DailyData.txt"
        colDes = ColumnDesigner.ColumnDesigner(fileName)
        if tb10.queryTop(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
        if tb10.queryBottom(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
        if tb50.queryTop(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
        if tb50.queryBottom(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
        if tb100.queryTop(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
        if tb100.queryBottom(shrtName): colDes.appendColumn("last",str(1))
        else: colDes.appendColumn("last",str(0))
else:
    for n in names:
        shrtName = n.split("|")[0].rstrip()
        fileNameEnd = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shrtName + "_DailyData.txt"
        fileNameStart = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/" + shrtName + "_DailyData.txt"
        colDesEnd = ColumnDesigner.ColumnDesigner(fileNameEnd)
        colDesStart = ColumnDesigner.ColumnDesigner(fileNameStart)
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",11))
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",12))
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",13))
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",14))
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",15))
        colDesStart.appendColumn("last",colDesEnd.getColumn("last",16))


# print(tb10.topN)
# print(tb50.topN)
# print(tb100.topN)
