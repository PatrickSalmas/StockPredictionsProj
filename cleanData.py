#Script for removing all the commas from current data sets
import os
import BuildTrainSet
import TrainData
import FeatClasses
import TopBottomStocks
import ColumnDesigner


topBottom = TopBottomStocks.TopBottomStocks(100)
stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
SP500_fName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/SP500_DailyData.txt"
lines = open(SP500_fName,"r").readlines()
file = open(stkNames,"r")
print(len(lines))
names = file.readlines()
#for adding to first line of each file
for n in names:
    shrtName = n.split("|")[0].rstrip()
    fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/" + shrtName + "_DailyData.txt"
    data = open(fileName,"r").readlines()
    fileCo = open(fileName,"w")
    for d in range(0,len(data)-1):
        fileCo.write(data[d])
    # fileCo.write(data[:len(data)-1])
    # print(data[:len(data)-1])
    # break
#     stockData = data[:]
#     top = len(data) - 2
#     stockLine = data[top]
#     print(shrtName)
#     print(stockLine)
    # price = stockLine.split("|")[1]
    # colDesign = ColumnDesigner.ColumnDesigner(fileName)
    # print(colDesign.getColumn("last",5))
    # print(shrtName)
    # print(colDesign.getColumn(0,11))
    # colDesign.deleteColumn(0,11)
    # colDesign.appendColumn(0,str(0))
    # colDesign.appendColumn(0,str(0))
#
# for l in range(1,len(lines)+5):
#     print("iteration ",l)
#     for n in range(0,len(names)):
#         shrtName = names[n].split("|")[0].rstrip()
#         fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shrtName + "_DailyData.txt"
#         data = open(fileName,"r").readlines()
#         colDesign = ColumnDesigner.ColumnDesigner(fileName)
#         key = shrtName
#         valueToday = colDesign.getColumn(len(data)-l,1)
#         valueYester = colDesign.getColumn(len(data)-l-1,1)
#         if valueToday == "null" or valueYester == "null": continue
#         value = (float(valueToday) - float(valueYester)) / float(valueYester)
#         topBottom.addItem(key,value)
#
#     topBottom.calculate()
#     for n in names:
#         shrtName = n.split("|")[0].rstrip()
#         fileName = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/" + shrtName + "_DailyData.txt"
#         fileNameStart = "C:/Users/psalm/Documents/StockProj/S&P500Data_Start/" + shrtName + "_DailyData.txt"
#
#         data = open(fileName,"r").readlines()
#         colDesign = ColumnDesigner.ColumnDesigner(fileName)
#         colDesignStart = ColumnDesigner.ColumnDesigner(fileNameStart)
#         # print(shrtName)
#         if topBottom.queryTop(shrtName) == 1:
#             colDesign.appendColumn(len(data)-l,str(1))
#             colDesignStart.appendColumn(len(data)-l+4,str(1))
#         else:
#             colDesign.appendColumn(len(data)-l,str(0))
#             colDesignStart.appendColumn(len(data)-l+4,str(0))
#         if topBottom.queryBottom(shrtName) == 1:
#             colDesign.appendColumn(len(data)-l,str(1))
#             colDesignStart.appendColumn(len(data)-l+4,str(1))
#         else:
#             colDesign.appendColumn(len(data)-l,str(0))
#             colDesignStart.appendColumn(len(data)-l+4,str(0))
#

# print(topBottom.topN)
# print(topBottom.bottomN)
    # print(shrtName)
    # print(colDesign.getColumn(len(data)-1,1))






stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
totalDiff = 0
#
# for n in range(0,len(names)):
#     shrtName = names[n].split("|")[0].rstrip()
#     # print("STOCK: ", shrtName)
#     # top = [tb1.queryTop(shrtName),tb2.queryTop(shrtName),tb3.queryTop(shrtName),tb4.queryTop(shrtName),tb5.queryTop(shrtName)]
#     # bottom = [tb1.queryBottom(shrtName),tb2.queryBottom(shrtName),tb3.queryBottom(shrtName),tb4.queryBottom(shrtName),tb5.queryBottom(shrtName)]
#     # tempBuild = BuildTrainSet.TrainBuilder(shrtName, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#     #                                        [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11,12,13,14,15])
#     tempBuild = BuildTrainSet.TrainBuilder(shrtName, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#                                            [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11,12,13,14,15],
#                                            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
#     tempBuild.loadData()
#     tempBuild.buildTrainSet()
#
#     train = TrainData.Trainer(shrtName)
#     train.loadData()
#     train.buildSets()
#     train.fitPredict()
#     # print(top)
#     # print bottom
#     # print("Average difference of ", train.calcAvgDiff())
#     totalDiff += train.calcAvgDiff()
#
# print(totalDiff/len(names))

# testBuild = TrainBuilder("AAPL",4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# testBuild.loadData()
# testBuild.buildTrainSet()

# stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
# file = open(stkNames,"r")
# names = file.readlines()
# dayPred = [1,2,3,4,5]
#
# for dp in dayPred:
#     print("Prepending "+str(dp) + " Day Predictions")
#     investmentList = [500,600,700,800,900,1000]
#     for i in investmentList:
#         original_totalInvestment = [0, 0, 0, 0, 0]
#         currentTotalValue = [0, 0, 0, 0, 0]
#         print(i, " STOCKS")
#         for n in names:
#         #     # stkProfile = open("C:/Users/psalm/Documents/S&P500_Profiles/"+n+".txt")
#             for j in range(0,5):
#                 shrtName = n.split("|")[0].rstrip()
#                 CoProfile = CompanyProfiler.Profiler(shrtName,dp,i,j,j)
#                 original_totalInvestment[j] += CoProfile.startInvestment
#                 currentTotalValue[j] += CoProfile.liquidVal
#                 # if i == 1000 and j == 4:
#                 #     print(shrtName + ": " + str(CoProfile.liquidVal))
#                 profilePath = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(dp)+"DayPred/"+str(i)+"/"+str(j)+"_"+str(j)+"/CoProf"
#                 if not os.path.exists(profilePath):
#                     os.makedirs(profilePath)
#                 profilePath = profilePath+"/"+shrtName+".txt"
#                 CoReport = open(profilePath,"a+")
#                 CoReport.write(dateStamp+": "+str(CoProfile.liquidVal)+"\n")
#
#
#
#         # print("Original Total Investment: "+str(original_totalInvestment))
#         # print("Total Current Value: "+str(currentTotalValue))
#
#         for j in range(0,5):
#             overallPath = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(dp)+"DayPred/"+str(i)+"/"+str(j)+"_"+str(j)
#             if not os.path.exists(overallPath):
#                 os.makedirs(overallPath)
#             overallProfile = overallPath+"/Overall.txt"
#             overallFile = open(overallProfile,"a+")
#             # if(j != 1):
#             # overallFile.write("Initial Total Investment: "+ str(original_totalInvestment[j])+"\n")
#             overallFile.write(dateStamp + " " + str(currentTotalValue[j])+"\n")
#
#
#
# print isUnique("jimm")