import parseStkData

def getTrainSize_nDayPrice(nDayPriceList,dataList):
    nLarge = max(nDayPriceList)
    return len(dataList) - nLarge

def getNLabels(n,dataList):
    labelList = []
    dataList.reverse()
    for d in range(0,n):
        dataArr = parseStkData.splitLine(dataList[d])
        labelList.append(parseStkData.getPrice(dataArr))
        # print parseStkData.getPrice(dataArr)
    return labelList

def getPrevPriceDayLists(nLabels,nDayList,dataList):
    retList = []
    # dataList.reverse()   #dataList is the dataList of a specific company
    # for dat in dataList: print dat
    for num in nDayList:
        priceList = []
        for i in range(0,nLabels):
            dataArr = parseStkData.splitLine(dataList[i+num])
            price = parseStkData.getPrice(dataArr)
            priceList.append(price)
        retList.append(priceList)

    return retList
    # for num in nDayList:
    #     for data in dataList:
    #         for i in range(0,n):
