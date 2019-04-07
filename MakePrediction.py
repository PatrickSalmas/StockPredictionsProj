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
        self.OneDayPred = 0
        self.FiveDayPred = 0
        self.clf = linear_model.Ridge(1.0, fit_intercept=False)
        self.clf_5Day = linear_model.Ridge(1.0, fit_intercept=False)
        self.CoEndFile = "C:/Users/psalm/Documents/S&P500Data_End/"+company+"_DailyData.txt"  # for now hard coding the endFile to retrieve data from
        self.SPEndFile = "C:/Users/psalm/Documents/S&P500Data_End/SP500_DailyData.txt"
        self.trainXs_loc = "C:/Users/psalm/Documents/TrainS&P500_Xs/"+company+".txt"
        self.trainYs_loc = "C:/Users/psalm/Documents/TrainS&P500_Ys/"+company+".txt"
        self.trainXs_loc_5Day = "C:/Users/psalm/Documents/TrainS&P500_Xs_5Day/"+company+".txt"
        self.trainYs_loc_5Day = "C:/Users/psalm/Documents/TrainS&P500_Ys_5Day/"+company+".txt"
        self.CoEndData = []
        self.SPEndData = []
        self.xVec = []
        self.XPredSet = []
        self.xVec_5Day = []
        self.XPredSet_5Day = []
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

    def initCLF_5Day(self):
        trainer = TrainData.Trainer(self.CoName)
        trainer.loadData_5Day()
        trainer.buildSets_5Day()
        trainer.fitPredict_5Day()
        self.clf_5Day = trainer.clf_5Day

    def buildDataPoint(self,index,xFile,yFile):
        self.xVec = []
        for f in self.co_featArr:
            feat = FeatClasses.NDayPrev(f,self.CoEndData)
            xVec.append(feat.getValue(index))
        for f in self.sp_featArr:
            feat = FeatClasses.NDayPrev(f,self.SPEndData)
            xVec.append(feat.getValue(index-1))



    def buildDataPoint_old(self,index,xFile,yFile):
        feat1Day = FeatClasses.NDayPrev(0,self.CoEndData)
        feat2Day = FeatClasses.NDayPrev(1,self.CoEndData)
        feat3Day = FeatClasses.NDayPrev(2,self.CoEndData)
        feat7Day = FeatClasses.NDayPrev(6,self.CoEndData)
        featSP1Day = FeatClasses.NDayPrev(0,self.SPEndData)
        featSP2Day = FeatClasses.NDayPrev(1,self.SPEndData)
        featSP3Day = FeatClasses.NDayPrev(2,self.SPEndData)
        featSP7Day = FeatClasses.NDayPrev(6,self.SPEndData)

        self.xVec = []
        # yLab = self.getLabel(index)
        self.xVec.append(feat1Day.getValue(index))
        self.xVec.append(feat2Day.getValue(index))
        self.xVec.append(feat3Day.getValue(index))
        self.xVec.append(feat7Day.getValue(index))
        self.xVec.append(featSP1Day.getValue(index-1))      #need to remove comma and convert to float for these!!
        self.xVec.append(featSP2Day.getValue(index-1))
        self.xVec.append(featSP3Day.getValue(index-1))
        self.xVec.append(featSP7Day.getValue(index-1))

    def buildDataPoint_5Day(self,index):
        feat1Day = FeatClasses.NDayPrev(0,self.CoEndData)
        feat2Day = FeatClasses.NDayPrev(1,self.CoEndData)
        feat5Day = FeatClasses.NDayPrev(4,self.CoEndData)
        feat6Day = FeatClasses.NDayPrev(5,self.CoEndData)
        feat7Day = FeatClasses.NDayPrev(6,self.CoEndData)
        feat10Day = FeatClasses.NDayPrev(9,self.CoEndData)
        feat12Day = FeatClasses.NDayPrev(11,self.CoEndData)
        feat15Day = FeatClasses.NDayPrev(14,self.CoEndData)
        featSP1Day = FeatClasses.NDayPrev(0,self.SPEndData)
        featSP2Day = FeatClasses.NDayPrev(1,self.SPEndData)
        featSP5Day = FeatClasses.NDayPrev(4,self.SPEndData)
        featSP6Day = FeatClasses.NDayPrev(5,self.SPEndData)
        featSP7Day = FeatClasses.NDayPrev(6,self.SPEndData)
        featSP10Day = FeatClasses.NDayPrev(9,self.SPEndData)
        featSP12Day = FeatClasses.NDayPrev(11,self.SPEndData)
        featSP15Day = FeatClasses.NDayPrev(14,self.SPEndData)

        self.xVec_5Day.append(feat1Day.getValue(index))
        self.xVec_5Day.append(feat2Day.getValue(index))
        self.xVec_5Day.append(feat5Day.getValue(index))
        self.xVec_5Day.append(feat6Day.getValue(index))
        self.xVec_5Day.append(feat7Day.getValue(index))
        self.xVec_5Day.append(feat10Day.getValue(index))
        self.xVec_5Day.append(feat12Day.getValue(index))
        self.xVec_5Day.append(feat15Day.getValue(index))
        self.xVec_5Day.append(featSP1Day.getValue(index-1))      #need to remove comma and convert to float for these!!
        self.xVec_5Day.append(featSP2Day.getValue(index-1))
        self.xVec_5Day.append(featSP5Day.getValue(index-1))
        self.xVec_5Day.append(featSP6Day.getValue(index-1))
        self.xVec_5Day.append(featSP7Day.getValue(index-1))
        self.xVec_5Day.append(featSP10Day.getValue(index-1))
        self.xVec_5Day.append(featSP12Day.getValue(index-1))
        self.xVec_5Day.append(featSP15Day.getValue(index-1))


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

    def buildPredSet_5Day(self):
        i = len(self.CoEndData)-1
        self.buildDataPoint_5Day(i)
        self.clean_xVec(self.xVec_5Day)
        self.XPredSet_5Day.append(self.feature(self.xVec_5Day))

    def feature(self,datum):
        feat = datum
        feat.append(1)
        return feat
    # def buildFeatsOneDayPred(self):



#
# pred = Prediction("AAPL")
# pred.loadData()
# print(len(pred.CoEndData))
# print(len(pred.SPEndData))
# pred.initCLF()
# pred.buildPredSet()
# print(pred.XPredSet)
# pred.OneDayPred = pred.clf.predict(pred.XPredSet)
# # pred.OneDayPred = pred.clf.predict(pred.xVec)
#
# print(pred.OneDayPred)
# print("\n")
#
# pred5Day = Prediction("AAPL")
# pred5Day.loadData()
# pred5Day.initCLF_5Day()
# pred5Day.buildPredSet_5Day()
# print(pred5Day.XPredSet_5Day)
# pred5Day.FiveDayPred = pred5Day.clf_5Day.predict(pred5Day.XPredSet_5Day)
# print(pred5Day.FiveDayPred)

# predMSFT = Prediction("MSFT")
# predMSFT.loadData()
# predMSFT.initCLF()
# predMSFT.buildPredSet()
# predMSFT.OneDayPred = predMSFT.clf.predict(predMSFT.XPredSet)
# print("MSFT One Day prediction: ",predMSFT.OneDayPred)
#
# predMSFT_5Day = Prediction("MSFT")
# predMSFT_5Day.loadData()
# predMSFT_5Day.initCLF_5Day()
# predMSFT_5Day.buildPredSet_5Day()
# predMSFT_5Day.FiveDayPred = predMSFT_5Day.clf_5Day.predict(predMSFT_5Day.XPredSet_5Day)
# print("MSFT Five Day prediction: ",predMSFT_5Day.FiveDayPred)

# for x in pred.xVec:
#     print x











