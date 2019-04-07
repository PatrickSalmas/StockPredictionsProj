import CompanyProfiler
import datetime
d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

stkNames = "C:/Users/psalm/Documents/AI_Stocks/venv/S&P500Stocks.txt"
file = open(stkNames,"r")
names = file.readlines()
original_totalInvestment = 0
currentTotalValue = 0
for n in names:
    # stkProfile = open("C:/Users/psalm/Documents/S&P500_Profiles/"+n+".txt")
    shrtName = n.split("|")[0].rstrip()
    CoProfile = CompanyProfiler.Profiler(shrtName)
    original_totalInvestment += CoProfile.startInvestment
    currentTotalValue += CoProfile.liquidVal
    print(shrtName + ": " + str(CoProfile.liquidVal))
    CoReport = open("C:/Users/psalm/Documents/S&P500_GrowthProfiles/CoProf/"+shrtName+".txt","a+")
    CoReport.write(dateStamp+": "+str(CoProfile.liquidVal)+"\n")



# print("Original Total Investment: "+str(original_totalInvestment))
# print("Total Current Value: "+str(currentTotalValue))



overallProfile = "C:/Users/psalm/Documents/S&P500_GrowthProfiles/Overall.txt"
overallFile = open(overallProfile,"a+")
overallFile.write(dateStamp + " " + str(currentTotalValue)+"\n")
