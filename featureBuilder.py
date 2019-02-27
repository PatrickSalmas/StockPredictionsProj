import parseStkData


class featureBuilder:
    self.dateLs = []

    def __init__(self,coShortName):
        self.company = coShortName
        self.coSP500_openFile = open("D:/Users/psalmas/Documents/S&P500Data_Start/" + shortName + "_DailyData.txt")
        self.coSP500_closeFile = open("D:/Users/psalmas/Documents/S&P500Data_End/" + shortName + "_DailyData.txt")


    def nDayChange(self,n):

    # company =

#
# company = ""
# coSP500_openFile = ""
# coSP500_closeFile = ""
#
# def setCompany(shortName):
#     self.company = shortName
#     self.coSP500_openFile = open("D:/Users/psalmas/Documents/S&P500Data_Start/"+shortName + "_DailyData.txt")
#     self.coSP500_closeFile = open("D:/Users/psalmas/Documents/S&P500Data_End/" + shortName + "_DailyData.txt")
#
#
# company = setCompany("AAPL")
# print company
#
# # def nDayChange(n):
