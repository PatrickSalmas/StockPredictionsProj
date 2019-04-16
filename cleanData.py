#Script for removing all the commas from current data sets
import os

# SP500_fNameStart = "C:/Users/psalm/Documents/S&P500Data_Start_temp/SP500_DailyData.txt"
# SP500_fNameEnd = "C:/Users/psalm/Documents/S&P500Data_End_temp/SP500_DailyData.txt"
#
# fileStart = open(SP500_fNameStart,"r")
# fileEnd = open(SP500_fNameEnd,"r")
#
# startData = fileStart.readlines()
# endData = fileEnd.readlines()
# fileWriteStart = open("C:/Users/psalm/Documents/S&P500Data_Start/SP500_DailyData.txt","w+")
# fileWriteEnd = open("C:/Users/psalm/Documents/S&P500Data_End/SP500_DailyData.txt","w+")
# for d in startData:
#     d = d.replace(",","")
#     fileWriteStart.write(d)
#
# for d in endData:
#     d = d.replace(",","")
#     fileWriteEnd.write(d)


# stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
# namesFile = open(stkNames,"r")
# names = namesFile.readlines()
# for n in names:
#     shrtName = n.split("|")[0].rstrip()
#     startLoc = "C:/Users/psalm/Documents/S&P500Data_Start/" + shrtName + "_DailyData.txt"
#     endLoc = "C:/Users/psalm/Documents/S&P500Data_End/" + shrtName + "_DailyData.txt"
#
#     startFile = open(startLoc,"r")
#     endFile = open(endLoc,"r")
#     startData = startFile.readlines()
#     endData = endFile.readlines()
#
#
#     startWriteLoc = "C:/Users/psalm/Documents/S&P500Data_Start_clean/" + shrtName + "_DailyData.txt"
#     endWriteLoc = "C:/Users/psalm/Documents/S&P500Data_End_clean/" + shrtName + "_DailyData.txt"
#     startWriteFile = open(startWriteLoc, "w+")
#     endWriteFile = open(endWriteLoc, "w+")
#     for d in startData:
#         d = d.replace(",","")
#         startWriteFile.write(d)
#         # print(d)
#
#     for d in endData:
#         d = d.replace(",","")
#         endWriteFile.write(d)

#
# profilePath = "C:/Users/psalm/Documents/Test/test1/some.txt"
# if not os.path.exists(profilePath):
#     os.makedirs(profilePath)
#
# for j in range(0,5):
#     print j

#500, 600, 700, 800, 900, 1000
buys = []
sells = []
for i in range(0,6):
    buys.append([0,0,0,0,0])

print buys