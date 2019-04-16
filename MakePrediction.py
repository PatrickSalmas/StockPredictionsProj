import TrainData
import FeatClasses
import csv
import random
from sklearn import linear_model
import numpy
from sklearn import svm

#This is essentially where we calculate the actual prediction once our model has been created and trained
class Prediction:
    def __init__(self,company,co_featArr,sp_featArr):
        self.CoName = company
        self.Pred = 0
        self.clf = linear_model.Ridge(1.0, fit_intercept=False)
        self.CoEndFile = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/"+company+"_DailyData.txt"  # for now hard coding the endFile to retrieve data from
        self.SPEndFile = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/SP500_DailyData.txt"
        self.trainXs_loc = "C:/Users/psalm/Documents/StockProj/TrainS&P500_Xs/"+company+".txt"
        self.trainYs_loc = "C:/Users/psalm/Documents/StockProj/TrainS&P500_Ys/"+company+".txt"
        self.CoEndData = []
        self.SPEndData = []
        self.xVec = []
        self.XPredSet = []
        self.co_featArr = co_featArr
        self.sp_featArr = sp_featArr


    def loadData(self):
        endFile = open(self.CoEndFile,"r")
        spFile = open(self.SPEndFile,"r")
        lines = endFile.readlines()
        for l in lines:
            self.CoEndData.append(l)
        lines = spFile.readlines()
        for l in lines:
            self.SPEndData.append(l)

    def initCLF(self):
        trainer = TrainData.Trainer(self.CoName)
        trainer.loadData()
        trainer.buildSets()
        trainer.fitPredict()
        self.clf = trainer.clf


    def buildDataPoint(self,index,xFile,yFile):
        self.xVec = []
        for f in self.co_featArr:
            feat = FeatClasses.NDayPrev(f,self.CoEndData)
            self.xVec.append(feat.getValue(index))
        for f in self.sp_featArr:
            feat = FeatClasses.NDayPrev(f,self.SPEndData)
            self.xVec.append(feat.getValue(index-1))


    def clean_xVec(self,xVec):
        for xI in range(0,len(xVec)):
            xVec[xI] = xVec[xI].replace(',','')
            xVec[xI] = float(xVec[xI])

    def buildPredSet(self):
        i = len(self.CoEndData)-1
        Xs_file = 0
        Ys_file = 0
        self.buildDataPoint(i,Xs_file,Ys_file)
        self.clean_xVec(self.xVec)
        self.XPredSet.append(self.feature(self.xVec))

    def feature(self,datum):
        feat = datum
        feat.append(1)
        return feat
    # def buildFeatsOneDayPred(self):


# predMSFT = Prediction("MSFT", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# predMSFT.loadData()
# predMSFT.initCLF()
# predMSFT.buildPredSet()
# predMSFT.Pred = predMSFT.clf.predict(predMSFT.XPredSet)
# print("MSFT Prediction: ",predMSFT.Pred)












