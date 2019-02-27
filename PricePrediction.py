import pricePredFuncs

nDayPriceLs = [1,2,3]
# oneDayPrevLs = []


def getShortName(line):
    names = line.split("|")
    return names[0]

def getLongName(line):
    names = line.split("|")
    return names[1]


#Training function goes here (refer to CSE158 HW1)
#Returns a theta list

#Prediction function goes here (refer to CSE158 HW1)
#takes in thetaList and XIn (for now, XIn will consist of look back 1, 2, and 3 days and build list on that)
#returns a single prediction



file = open("S&P500Stocks.txt","r")
shtNames_Stks = []
lngNames_Stks = []
stks_hitScore = []
lines = file.readlines()
for line in lines:
    shtNames_Stks.append(getShortName(line))
    lngNames_Stks.append(getLongName(line))
    stks_hitScore.append(0)

SP500EndFiles = []
SP500EndData = []

#create the file list of CNNStock data based on short names
baseFileLoc = "D:/Users/psalmas/Documents/S&P500Data_End/"

for n in shtNames_Stks:
    fileLoc = baseFileLoc + n.rstrip() + "_DailyData.txt"
    file = open(fileLoc,"r")
    SP500EndData.append(file.readlines())
    # SP500EndFiles.append(file)
    # print fileLoc

trainSizeNDayPrices = []

for data in SP500EndData:
    nDaySize = pricePredFuncs.getTrainSize_nDayPrice(nDayPriceLs,data)
    trainSizeNDayPrices.append(nDaySize)
    # print pricePredFuncs.getTrainSize_nDayPrice(nDayPriceLs,d)

SP500_labList = []

for n in range(0,len(trainSizeNDayPrices)):
    # print shtNames_Stks[n]
    labList = pricePredFuncs.getNLabels(trainSizeNDayPrices[n],SP500EndData[n])
    SP500_labList.append(labList)

priceFeatList = []
for n in range(0,len(trainSizeNDayPrices)):
    # print ()
    # print shtNames_Stks[n]
    retList = pricePredFuncs.getPrevPriceDayLists(trainSizeNDayPrices[n],nDayPriceLs,SP500EndData[n])
    # print SP500_labList[n]
    # print retList
    priceFeatList.append(retList)


#now let's actually set up the training set
# yTrain = []
for n in range(0,len(SP500_labList)):
    yTrain = []
    XTrain = []
    for labNum in range(0,len(SP500_labList[n])):
        yTrain.append(SP500_labList[n][labNum])
        XTrain.append([])   #a feature list for every label


    for i in range(0,len(XTrain)):
        print i
        for pfl in priceFeatList[n]:
            print pfl
            XTrain[i].append(pfl[i])

    #Now we have correctly lined up the labels with corresponding features vecs
    #time to make predictions
    #Should simply fead them in or something

    print()
    print yTrain
    print XTrain
    # for num in nDayPriceLs:

    # for priceFeat in priceFeatList[n]:


# XTrain = []
# for n in range(0,len(nDayPriceLs)):



#using short names let's go through each file

#let's somehow define the features we want beforehand



