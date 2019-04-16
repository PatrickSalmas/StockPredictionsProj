import datetime
d = datetime.datetime.today()
dateStamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

investList = [500,600,700,800,900,1000]
for i in investList:
    print
    print dateStamp," Investment Value: ",i
    for j in range(0,5):
        path = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/"+str(i)+"/"+str(j)+"_"+str(j)+"/Overall.txt"
        file = open(path,"r")
        data = file.readlines()
        initial = data[0].split()
        initial = float(initial[len(initial)-1])
        current = data[len(data)-1]
        currDate = current.split()[0]
        currValue = float(current.split()[1])
        yesterday = data[len(data)-2].split()
        yesterValue = float(yesterday[len(yesterday)-1])
        overallChange = currValue - initial
        yesterdayChange = currValue - yesterValue

        path = "C:/Users/psalm/Documents/StockProj/S&P500_GrowthProfiles/" + str(i) + "/" + str(j) + "_" + str(j) + "/SBCount.txt"
        file = open(path,"r")
        data = file.readlines()
        todayStkCnt = data[len(data)-1].split()

        bought = int(todayStkCnt[1])
        sold = int(todayStkCnt[2])
        transactionCosts = 0
        buyCosts = bought*7
        sellCosts = sold*7
        transactionCosts += buyCosts
        transactionCosts += sellCosts
        stockYield = yesterdayChange + transactionCosts
        # if yesterdayChange < 0:
        #     stockYield = yesterdayChange + transactionCosts
        # else:
        #     stockYield = yesterdayChange - transactionCosts

        # print("Percent Increase:",str(j),"Percent Decrease:",str(j),"Overall Change:", overallChange,
        #       "Yesterday Change:", yesterdayChange)

        print("Percent Increase:",str(j),"Percent Decrease:",str(j),"Overall Change:", overallChange,
              "Yesterday Change:", yesterdayChange,"Stock Yield:",stockYield, "Transaction Costs:",transactionCosts, "Bought:", bought, "Sold:", sold)
        # print overallChange
        # print currDate
        # print current
        # print initial
        # print lines