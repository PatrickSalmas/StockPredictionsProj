def splitLine(line):
    data = line.split("|")
    return data

def getDate(data):
    return data[0]

def getPrice(data):
    return data[1]

def getPE(data):
    return data[2]

def getVolume(data):
    return data[3]

def getYTD(data):
    return data[4]
