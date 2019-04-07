import FeatClasses

class TrainBuilder:
    def __init__(self,company,co_featArr,sp_featArr):
        self.CoName = company
        self.CoEndFile = "C:/Users/psalm/Documents/S&P500Data_End/"+company+"_DailyData.txt"
        self.SPEndFile = "C:/Users/psalm/Documents/S&P500Data_End/SP500_DailyData.txt"
        self.CoEndData = []
        self.SPEndData = []
        self.trainXs_loc = "C:/Users/psalm/Documents/TrainS&P500_Xs/"+company+".txt"
        self.trainYs_loc = "C:/Users/psalm/Documents/TrainS&P500_Ys/"+company+".txt"
        self.trainXs_loc_5Day = "C:/Users/psalm/Documents/TrainS&P500_Xs_5Day/"+company+".txt"
        self.trainYs_loc_5Day = "C:/Users/psalm/Documents/TrainS&P500_Ys_5Day/"+company+".txt"
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


    def getLabel(self,index):
        datArr = self.CoEndData[index].split("|")
        return datArr[1]

    #Checks if the dataPoint is valid (has no null values)
    def isValid(self,xVec):
        for i in xVec:
            if i == "null":
                return False

        return True

    #Builds a data point with specified features and writes to endFile(s)
    def buildDataPoint_old(self,index,xFile,yFile):
        feat1Day = FeatClasses.NDayPrev(1,self.CoEndData)
        feat2Day = FeatClasses.NDayPrev(2,self.CoEndData)
        feat3Day = FeatClasses.NDayPrev(3,self.CoEndData)
        feat7Day = FeatClasses.NDayPrev(7,self.CoEndData)
        featSP1Day = FeatClasses.NDayPrev(1,self.SPEndData)
        featSP2Day = FeatClasses.NDayPrev(2,self.SPEndData)
        featSP3Day = FeatClasses.NDayPrev(3,self.SPEndData)
        featSP7Day = FeatClasses.NDayPrev(7,self.SPEndData)

        xVec = []
        yLab = self.getLabel(index)
        xVec.append(feat1Day.getValue(index))
        xVec.append(feat2Day.getValue(index))
        xVec.append(feat3Day.getValue(index))
        xVec.append(feat7Day.getValue(index))
        xVec.append(featSP1Day.getValue(index-1))
        xVec.append(featSP2Day.getValue(index-1))
        xVec.append(featSP3Day.getValue(index-1))
        xVec.append(featSP7Day.getValue(index-1))

        if self.isValid(xVec):
            # xFile.write(xVec)
            for x in xVec:
                xFile.write(x + " | ")
            xFile.write("\n")
            yFile.write(yLab+"\n")
            # print("Built Data point: ",xVec," ",yLab)

    def buildDataPoint(self,index,xFile,yFile):
        xVec = []
        yLab = self.getLabel(index)
        for f in self.co_featArr:
            feat = FeatClasses.NDayPrev(f,self.CoEndData)
            xVec.append(feat.getValue(index))
        for f in self.sp_featArr:
            feat = FeatClasses.NDayPrev(f,self.SPEndData)
            xVec.append(feat.getValue(index-1))        #may want to fix this off by one index error later on

        if self.isValid(xVec):
            # xFile.write(xVec)
            for x in xVec:
                xFile.write(x + " | ")
            xFile.write("\n")
            yFile.write(yLab+"\n")
            # print("Built Data point: ",xVec," ",yLab)



    def buildDataPoint_5Day(self,index,xFile,yFile):
        feat1Day = FeatClasses.NDayPrev(1, self.CoEndData)
        feat2Day = FeatClasses.NDayPrev(2, self.CoEndData)
        feat5Day = FeatClasses.NDayPrev(5,self.CoEndData)
        feat6Day = FeatClasses.NDayPrev(6,self.CoEndData)
        feat7Day = FeatClasses.NDayPrev(7,self.CoEndData)
        feat10Day = FeatClasses.NDayPrev(10,self.CoEndData)
        feat12Day = FeatClasses.NDayPrev(12,self.CoEndData)
        feat15Day = FeatClasses.NDayPrev(15,self.CoEndData)
        featSP1Day = FeatClasses.NDayPrev(1, self.SPEndData)
        featSP2Day = FeatClasses.NDayPrev(2, self.SPEndData)
        featSP5Day = FeatClasses.NDayPrev(5,self.SPEndData)
        featSP6Day = FeatClasses.NDayPrev(6,self.SPEndData)
        featSP7Day = FeatClasses.NDayPrev(7,self.SPEndData)
        featSP10Day = FeatClasses.NDayPrev(10,self.SPEndData)
        featSP12Day = FeatClasses.NDayPrev(12,self.SPEndData)
        featSP15Day = FeatClasses.NDayPrev(15,self.SPEndData)

        xVec = []
        yLab = self.getLabel(index)
        xVec.append(feat1Day.getValue(index))
        xVec.append(feat2Day.getValue(index))
        xVec.append(feat5Day.getValue(index))
        xVec.append(feat6Day.getValue(index))
        xVec.append(feat7Day.getValue(index))
        xVec.append(feat10Day.getValue(index))
        xVec.append(feat12Day.getValue(index))
        xVec.append(feat15Day.getValue(index))
        xVec.append(featSP1Day.getValue(index-1))
        xVec.append(featSP2Day.getValue(index-1))
        xVec.append(featSP5Day.getValue(index - 1))
        xVec.append(featSP6Day.getValue(index - 1))
        xVec.append(featSP7Day.getValue(index - 1))
        xVec.append(featSP10Day.getValue(index - 1))
        xVec.append(featSP12Day.getValue(index - 1))
        xVec.append(featSP15Day.getValue(index - 1))

        if self.isValid(xVec):
            # xFile.write(xVec)
            for x in xVec:
                xFile.write(x + " | ")
            xFile.write("\n")
            yFile.write(yLab+"\n")
            # print("Built Data point: ",xVec," ",yLab)


    def buildTrainSet_old(self):
        i = len(self.CoEndData)-1
        Xs_file = open(self.trainXs_loc,"w+")
        Ys_file = open(self.trainYs_loc,"w+")
        while i >= 0:
            self.buildDataPoint(i,Xs_file,Ys_file)
            i -= 1

    def buildTrainSet_5Day(self):
        i = len(self.CoEndData)-1
        Xs_file = open(self.trainXs_loc_5Day,"w+")
        Ys_file = open(self.trainYs_loc_5Day,"w+")
        while i >= 0:
            self.buildDataPoint_5Day(i,Xs_file,Ys_file)
            i -= 1

    def buildTrainSet(self):
        i = len(self.CoEndData)-1
        Xs_file = open(self.trainXs_loc,"w+")
        Ys_file = open(self.trainYs_loc,"w+")
        while i >= 0:
            self.buildDataPoint(i,Xs_file,Ys_file)
            i -= 1


# testBuild = TrainBuilder("Apple")
# testBuild.loadData()
# testBuild.buildTrainSet()
#

# testBuild = TrainBuilder("AAPL",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# testBuild.loadData()
# testBuild.buildTrainSet()

# testBuild = TrainBuilder("MSFT",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# testBuild.loadData()
# testBuild.buildTrainSet()

# testBuild_5Day = TrainBuilder("AAPL", [],[])
# testBuild_5Day.loadData()
# testBuild_5Day.buildTrainSet_5Day()
#
# # testMSFT_1Day = TrainBuilder("MSFT")
# # testMSFT_1Day.loadData()
# # testMSFT_1Day.buildTrainSet()
#
# testMSTF_5Day = TrainBuilder("MSFT")
# testMSTF_5Day.loadData()
# testMSTF_5Day.buildTrainSet_5Day()
# i = len(testBuild.CoEndData)-1
# Xs_file = open(testBuild.trainXs_loc, "w+")
# Ys_file = open(testBuild.trainYs_loc, "w+")
# while i >= 0:
#     testBuild.buildDataPoint(i,Xs_file,Ys_file)
#     i-=1




# print len(testBuild.CoEndData)
# for i in testBuild.CoEndData:
#     print i
# print testBuild.CoEndFile


# feat = FeatClasses.OneDayPrev("bob")
# print(feat.data)