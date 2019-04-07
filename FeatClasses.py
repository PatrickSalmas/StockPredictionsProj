class NDayPrev:
    def __init__(self,n,fileData):
        self.data = fileData
        self.n = n

    def getValue(self,anchorIndex):
        if anchorIndex - self.n < 0: return "null"
        # print(anchorIndex-self.n," ",self.data[anchorIndex-self.n])
        return self.data[anchorIndex-self.n].split("|")[1]
        # return self.data[anchorIndex-1]

