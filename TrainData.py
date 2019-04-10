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
        self.XData = []
        self.YData = []
        self.XTrainSet = []
        self.YTrainSet = []
        self.predTrain = []
        self.clf = linear_model.Ridge(1.0, fit_intercept=False)

    def loadData(self):
        XFile = open(self.XTrainFile,"r")
        YFile = open(self.YTrainFile,"r")
        XLines = XFile.readlines()
        YLines = YFile.readlines()
        for x in XLines:
            self.XData.append(x)
        for y in YLines:
            y = y.replace(",","")
            self.YTrainSet.append(float(y.rstrip()))
            self.YData.append(y)


    def buildSets(self):
        for x in self.XData:
            xArr = x.split("|")
            xArr = xArr[:len(xArr)-1]
            for xI in range(0,len(xArr)):
                xArr[xI] = xArr[xI].replace(',','')
                xArr[xI] = float(xArr[xI])
            self.XTrainSet.append(self.feature(xArr))


    def feature(self,datum):
        feat = datum
        feat.append(1)
        return feat

    def fitPredict(self):
        self.clf.fit(self.XTrainSet, self.YTrainSet)
        theta = self.clf.coef_
        self.predTrain = self.clf.predict(self.XTrainSet)


    def calcAvgDiff(self):
        sum = 0.0
        for i in range(0,len(self.predTrain)):
            print("Prediction of: ", self.predTrain[i]," and real value of: ", self.YTrainSet[i])
            subSum = self.predTrain[i]-self.YTrainSet[i]
            subSum = abs(subSum)
            sum += subSum

        return sum/len(self.predTrain)


# testTrain = Trainer("MSFT")
# testTrain.loadData()
# testTrain.buildSets()
# testTrain.fitPredict()
# print("Average difference of ", testTrain.calcAvgDiff())
