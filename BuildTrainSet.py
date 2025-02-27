import FeatClasses

class TrainBuilder:
    # tb1 = FeatClasses.TopBottom(1)
    # tb2 = FeatClasses.TopBottom(2)
    def __init__(self,company,nDayPred,co_featArr,sp_featArr,co_tbArr):
        self.CoName = company
        self.CoEndFile = "C:/Users/psalm/Documents/StockProj/TestDir/"+company+"_DailyData.txt"
        self.SPEndFile = "C:/Users/psalm/Documents/StockProj/S&P500Data_End/SP500_DailyData.txt"
        self.CoEndData = []
        self.SPEndData = []
        self.trainXs_loc = "C:/Users/psalm/Documents/StockProj/TrainS&P500_Xs/"+company+".txt"
        self.trainYs_loc = "C:/Users/psalm/Documents/StockProj/TrainS&P500_Ys/"+company+".txt"
        self.co_featArr = co_featArr
        self.sp_featArr = sp_featArr
        self.co_tbArr = co_tbArr
        self.nDayPred = nDayPred


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


    def buildDataPoint(self,index,xFile,yFile):
        xVec = []
        yLab = self.getLabel(index)
        for f in self.co_featArr:
            feat = FeatClasses.NDayPrev(f+self.nDayPred,self.CoEndData)
            xVec.append(feat.getValue(index,1))
        for f in self.sp_featArr:
            feat = FeatClasses.NDayPrev(f+self.nDayPred,self.SPEndData)
            xVec.append(feat.getValue(index-1,1))        #may want to fix this off by one index error later on

        for f in self.co_tbArr:
            feat = FeatClasses.NDayPrev(f+self.nDayPred,self.CoEndData)
            xVec.append(feat.getValue(index,5))
            xVec.append(feat.getValue(index,6))
            xVec.append(feat.getValue(index,7))
            xVec.append(feat.getValue(index,8))
            xVec.append(feat.getValue(index,9))
            xVec.append(feat.getValue(index,10))


        # print(xVec,"\n")
        if self.isValid(xVec):
            # xFile.write(xVec)
            for x in xVec:
                xFile.write(str(x) + " | ")
            xFile.write("\n")
            yFile.write(yLab+"\n")
            # print("Built Data point: ",xVec," ",yLab)


    def buildTrainSet(self):
        i = len(self.CoEndData)-1
        Xs_file = open(self.trainXs_loc,"w+")
        Ys_file = open(self.trainYs_loc,"w+")
        while i >= 0:
            self.buildDataPoint(i,Xs_file,Ys_file)
            i -= 1


# testBuild = TrainBuilder("AAPL",4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# testBuild.loadData()
# testBuild.buildTrainSet()

# testBuild = TrainBuilder("MSFT",0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# testBuild.loadData()
# testBuild.buildTrainSet()
