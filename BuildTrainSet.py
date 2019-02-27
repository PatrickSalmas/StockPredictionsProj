import FeatClasses

class TrainBuilder:
    def __init__(self,company):
        self.CoName = company
        self.CoFile = "C:/Users/psalm/Documents/S&P500Data_End/AAPL_DailyData.txt"   #for now hard coding the file to retrieve data from
        self.CoData = []
        self.trainXs_loc = "C:/Users/psalm/Documents/TrainS&P500_Xs/AAPL.txt"
        self.trainYs_loc = "C:/Users/psalm/Documents/TrainS&P500_Ys/AAPL.txt"

    def loadData(self):
        file = open(self.CoFile,"r")
        lines = file.readlines()
        for l in lines:
            self.CoData.append(l)

    def getLabel(self,index):
        datArr = self.CoData[index].split("|")
        return datArr[1]

    #Checks if the dataPoint is valid (has no null values)
    def isValid(self,xVec):
        for i in xVec:
            if i == "null":
                return False

        return True

    #Builds a data point with specified features and writes to file(s)
    def buildDataPoint(self,index,xFile,yFile):
        feat1Day = FeatClasses.NDayPrev(1,self.CoData)
        feat2Day = FeatClasses.NDayPrev(2,self.CoData)
        feat3Day = FeatClasses.NDayPrev(3,self.CoData)
        feat7Day = FeatClasses.NDayPrev(7,self.CoData)
        xVec = []
        yLab = self.getLabel(index)
        xVec.append(feat1Day.getValue(index))
        xVec.append(feat2Day.getValue(index))
        xVec.append(feat3Day.getValue(index))
        xVec.append(feat7Day.getValue(index))
        if self.isValid(xVec):
            # xFile.write(xVec)
            for x in xVec:
                xFile.write(x + " | ")
            xFile.write("\n")
            yFile.write(yLab+"\n")
            print("Built Data point: ",xVec," ",yLab)


    def buildTrainSet(self):
        i = len(self.CoData)-1
        Xs_file = open(self.trainXs_loc,"w+")
        Ys_file = open(self.trainYs_loc,"w+")
        while i >= 0:
            self.buildDataPoint(i,Xs_file,Ys_file)
            i -= 1



testBuild = TrainBuilder("Apple")
testBuild.loadData()
testBuild.buildTrainSet()
# i = len(testBuild.CoData)-1
# Xs_file = open(testBuild.trainXs_loc, "w+")
# Ys_file = open(testBuild.trainYs_loc, "w+")
# while i >= 0:
#     testBuild.buildDataPoint(i,Xs_file,Ys_file)
#     i-=1




# print len(testBuild.CoData)
# for i in testBuild.CoData:
#     print i
# print testBuild.CoFile


# feat = FeatClasses.OneDayPrev("bob")
# print(feat.data)