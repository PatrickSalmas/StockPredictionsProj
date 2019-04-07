import csv
import random
from sklearn import linear_model
import numpy
from sklearn import svm

class Trainer:
    def __init__(self, company):
        self.CoName = company
        self.XTrainFile = "C:/Users/psalm/Documents/TrainS&P500_Xs/"+company+".txt"
        self.YTrainFile = "C:/Users/psalm/Documents/TrainS&P500_Ys/"+company+".txt"
        self.XTrainFile_5Day = "C:/Users/psalm/Documents/TrainS&P500_Xs_5Day/"+company+".txt"
        self.YTrainFile_5Day = "C:/Users/psalm/Documents/TrainS&P500_Ys_5Day/"+company+".txt"
        self.XData = []
        self.YData = []
        self.XData_5Day = []
        self.YData_5Day = []
        self.XTrainSet = []
        self.YTrainSet = []
        self.XTrainSet_5Day = []
        self.YTrainSet_5Day = []
        self.predTrain = []
        self.predTrain_5Day = []
        self.clf = linear_model.Ridge(1.0, fit_intercept=False)
        self.clf_5Day = linear_model.Ridge(1.0, fit_intercept=False)

    def loadData(self):
        XFile = open(self.XTrainFile,"r")
        YFile = open(self.YTrainFile,"r")
        XLines = XFile.readlines()
        YLines = YFile.readlines()
        for x in XLines:
            self.XData.append(x)
        for y in YLines:
            self.YTrainSet.append(float(y.rstrip()))
            self.YData.append(y)

    def loadData_5Day(self):
        XFile = open(self.XTrainFile_5Day,"r")
        YFile = open(self.YTrainFile_5Day,"r")
        XLines = XFile.readlines()
        YLines = YFile.readlines()
        for x in XLines:
            self.XData_5Day.append(x)
        for y in YLines:
            y = y.replace(",","")
            self.YTrainSet_5Day.append(float(y.rstrip()))

    def buildSets(self):
        for x in self.XData:
            xArr = x.split("|")
            xArr = xArr[:len(xArr)-1]
            for xI in range(0,len(xArr)):
                xArr[xI] = xArr[xI].replace(',','')
                xArr[xI] = float(xArr[xI])
            self.XTrainSet.append(self.feature(xArr))

    def buildSets_5Day(self):
        for x in self.XData_5Day:
            xArr = x.split("|")
            xArr = xArr[:len(xArr)-1]
            for xI in range(0,len(xArr)):
                xArr[xI] = xArr[xI].replace(',','')
                xArr[xI] = float(xArr[xI])
            self.XTrainSet_5Day.append(self.feature(xArr))

    def feature(self,datum):
        feat = datum
        feat.append(1)
        return feat

    def fitPredict(self):
        self.clf.fit(self.XTrainSet, self.YTrainSet)
        theta = self.clf.coef_
        self.predTrain = self.clf.predict(self.XTrainSet)

    def fitPredict_5Day(self):
        self.clf_5Day.fit(self.XTrainSet_5Day, self.YTrainSet_5Day)
        theta = self.clf_5Day.coef_
        self.predTrain_5Day = self.clf_5Day.predict(self.XTrainSet_5Day)


    def calcAvgDiff(self):
        sum = 0.0
        for i in range(0,len(self.predTrain)):
            print("Prediction of: ", self.predTrain[i]," and real value of: ", self.YTrainSet[i])
            subSum = self.predTrain[i]-self.YTrainSet[i]
            subSum = abs(subSum)
            sum += subSum

        return sum/len(self.predTrain)

    def calcAvgDiff_5Day(self):
        sum = 0.0
        for i in range(0,len(self.predTrain_5Day)):
            subSum = self.predTrain_5Day[i]-self.YTrainSet_5Day[i]
            subSum = abs(subSum)
            sum += subSum

        return sum/len(self.predTrain_5Day)


# testTrain = Trainer("AAPL")
# testTrain.loadData()
# testTrain.buildSets()
# testTrain.fitPredict()
# print("Average difference of ", testTrain.calcAvgDiff())

# testTrain = Trainer("MSFT")
# testTrain.loadData()
# testTrain.buildSets()
# testTrain.fitPredict()
# print("Average difference of ", testTrain.calcAvgDiff())
#
# testTrain_5Day = Trainer("AAPL")
# testTrain_5Day.loadData_5Day()
# testTrain_5Day.buildSets_5Day()
# testTrain_5Day.fitPredict_5Day()
# print("Average difference for 5Day is ",testTrain_5Day.calcAvgDiff_5Day())

# testMSFT_1Day = Trainer("MSFT")
# testMSFT_1Day.loadData()
# testMSFT_1Day.buildSets()
# testMSFT_1Day.fitPredict()
# print("Average difference for 1Day MSFT is ",testMSFT_1Day.calcAvgDiff())

# testMSFT_5Day = Trainer("MSFT")
# testMSFT_5Day.loadData_5Day()
# testMSFT_5Day.buildSets_5Day()
# testMSFT_5Day.fitPredict_5Day()
# print("Average difference for 5Day MSFT is ",testMSFT_5Day.calcAvgDiff_5Day())

# for i in range(0,len(testTrain.XTrainSet)):
#     print(testTrain.XTrainSet[i], " with lab ",testTrain.YTrainSet[i])
# for x in testTrain.XTrainSet:
#     print x
# print(testTrain.XData[0])
# print(testTrain.YData[0])