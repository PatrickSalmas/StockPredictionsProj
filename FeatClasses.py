class NDayPrev:
    def __init__(self,n,fileData):
        self.data = fileData
        self.n = n

    def getValue(self,anchorIndex,colNum):
        if anchorIndex - self.n < 0: return "null"
        # print(anchorIndex-self.n," ",self.data[anchorIndex-self.n])
        cols = self.data[anchorIndex-self.n].split("|")
        if colNum >= len(cols): return 0
        return cols[colNum].rstrip()
        # return self.data[anchorIndex-1]
