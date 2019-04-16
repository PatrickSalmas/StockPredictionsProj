import CompanyProfiler
import datetime
import os
d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()

investmentList = [500,600,700,800,900,1000]
for i in investmentList:
    original_totalInvestment = [0, 0, 0, 0, 0]
    currentTotalValue = [0, 0, 0, 0, 0]
    print(i, " STOCKS")
    for n in names:
    #     # stkProfile = open("C:/Users/psalm/Documents/S&P500_Profiles/"+n+".txt")
        for j in range(0,5):
            shrtName = n.split("|")[0].rstrip()
            CoProfile = CompanyProfiler.Profiler(shrtName,i,j,j)
            original_totalInvestment[j] += CoProfile.startInvestment
            currentTotalValue[j] += CoProfile.liquidVal
            # print(shrtName + ": " + str(CoProfile.liquidVal))
            profilePath = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(i)+"/"+str(j)+"_"+str(j)+"/CoProf"
            if not os.path.exists(profilePath):
                os.makedirs(profilePath)
            profilePath = profilePath+"/"+shrtName+".txt"
            CoReport = open(profilePath,"a+")
            CoReport.write(dateStamp+": "+str(CoProfile.liquidVal)+"\n")



    # print("Original Total Investment: "+str(original_totalInvestment))
    # print("Total Current Value: "+str(currentTotalValue))

    for j in range(0,5):
        overallPath = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(i)+"/"+str(j)+"_"+str(j)
        if not os.path.exists(overallPath):
            os.makedirs(overallPath)
        overallProfile = overallPath+"/Overall.txt"
        overallFile = open(overallProfile,"a+")
        # if(j != 1):
        # overallFile.write("Initial Total Investment: "+ str(original_totalInvestment[j])+"\n")
        overallFile.write(dateStamp + " " + str(currentTotalValue[j])+"\n")
