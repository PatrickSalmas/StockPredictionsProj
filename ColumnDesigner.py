#Is capable of creating and destroying specified columns in data files

class ColumnDesigner:
    def __init__(self,fileLoc):
        self.fileLoc = fileLoc


    #append item (value) as last column of specified data point (lineNum)
    def appendColumn(self,lineNum,value):
        fileIn = open(self.fileLoc,"r")
        allData = fileIn.readlines()
        fileIn.close()
        if lineNum == "last": lineNum = len(allData) - 1
        if lineNum >= len(allData): return 0
        if lineNum < 0: return 0
        data = allData[lineNum].rstrip()
        data = data + " | " + value + "\n"
        allData[lineNum] = data
        fileOut = open(self.fileLoc,"w")
        for d in allData:
            fileOut.write(d)

        fileOut.close()
        # print(data)

    #retrieves column number(colNum) of data entry specified by line number(lineNum)
    def getColumn(self,lineNum,colNum):
        fileIn = open(self.fileLoc,"r")
        allData = fileIn.readlines()
        fileIn.close()
        # print(lineNum, " " ,len(allData))
        # if lineNum > len(allData): return
        if lineNum == "last":
            data = allData[len(allData)-1]
            cols = data.split("|")
            # print cols
            return cols[colNum].rstrip()
        if lineNum == "yesterday":
            data = allData[len(allData)-2]
            cols = data.split("|")
            return cols[colNum].rstrip()
        if lineNum < 0: return "null"
        data = allData[lineNum]
        cols = data.split("|")
        return cols[colNum].rstrip()

    #delete specified column number (colNum) of data entry specified by line number (lineNum)
    def deleteColumn(self,lineNum,colNum):
        fileIn = open(self.fileLoc,"r")
        allData = fileIn.readlines()
        fileIn.close()
        if lineNum < 0: return 0
        data = allData[lineNum]
        cols = data.split("|")
        del cols[colNum]
        newEntry = ""
        for c in cols:
            newEntry = newEntry + c.rstrip() + " | "

        newEntry = newEntry[0:len(newEntry)-2]    #delete extra " | " at end
        newEntry = newEntry+"\n"
        allData[lineNum] = newEntry
        fileOut = open(self.fileLoc,"w")
        for d in allData:
            fileOut.write(d)

        fileOut.close()




# tester = ColumnDesigner("C:/Users/psalm/Documents/StockProj/TestDir/AAP_DailyData.txt")
# lines = open("C:/Users/psalm/Documents/StockProj/TestDir/AAP_DailyData.txt","r").readlines()
# for i in range(0,len(lines)):
#     print(tester.getColumn(i,5)," ",tester.getColumn(i,6))