class NDayPrev:
    def __init__(self,n,fileData):
        self.data = fileData
        self.n = n

    def getValue(self,anchorIndex):
        if anchorIndex - self.n < 0: return "null"
        return self.data[anchorIndex-self.n].split("|")[1]
        # return self.data[anchorIndex-1]

