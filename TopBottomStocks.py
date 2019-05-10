from heapq import nlargest, nsmallest

#Allows one to contruct a container that can return the highest N and lowest N values
#with their "keys". As well allows to query if a key is in the highest N or lowest N
class TopBottomStocks:
    def __init__(self,n):
        self.n = n
        self.container = dict()
        self.topN = dict()
        self.bottomN = dict()

    def addItem(self,key,value):
        self.container[key] = float(value)

    def calculate(self):
        self.topN = nlargest(self.n,self.container,key=self.container.get)
        self.bottomN = nsmallest(self.n,self.container,key=self.container.get)

    def queryTop(self,key):
        if key in self.topN: return 1
        return 0

    def queryBottom(self,key):
        if key in self.bottomN: return 1
        return 0

