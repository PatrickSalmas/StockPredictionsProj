import re
import SentAnalysis

def getShortName(line):
    names = line.split("|")
    return names[0]

def getLongName(line):
    names = line.split("|")
    return names[1]



file = open("S&P500Stocks.txt","r")
shtNames_Stks = []
lngNames_Stks = []
stks_hitScore = []
lines = file.readlines()
for line in lines:
    shtNames_Stks.append(getShortName(line))
    lngNames_Stks.append(getLongName(line))
    stks_hitScore.append(0)
    # print getShortName(line)," ",getLongName(line)

businessTrends = []
entertainTrends = []
healthTrends = []
sci_techTrends = []
sportTrends = []

businessTrendsText = []
entertainTrendsText = []
healthTrendsText = []
sci_techTrendsText = []
sportTrendsText = []

baseTrend = "googleTrends_"
catList = ["b","e","m","t","s"]
trendList = [businessTrends, entertainTrends, healthTrends, sci_techTrends, sportTrends]
trendListText = [businessTrendsText, entertainTrendsText, healthTrendsText, sci_techTrendsText, sportTrendsText]
for c in range(0,len(catList)):
    trendCat = baseTrend + catList[c] + "_Titles.txt"
    trendCatText = baseTrend + catList[c] + "_Text.txt"
    file = open(trendCat,"r")
    fileText = open(trendCatText,"r")
    lines = file.readlines()
    linesText = fileText.readlines()
    for l in range(0,len(lines)):
        trendList[c].append(lines[l])
    for l in range(0,len(linesText)):
        trendListText[c].append(linesText[l])
    # for line in lines:
    #     trendList[c].append(line)


file = open("exceptionShtName.txt","r")
shtExceptions = []
lines = file.readlines()
for line in lines:
    # shtExceptions.append(line[0:len(line)-1])
    shtExceptions.append(line.rstrip())
    # print(len(line.rstrip()))
    # print line[0:len(line)-1]," ",len(line[0:len(line)-1])


#Now check each stock to see if they appear in one or more of the trends lists, any number of times
for n in range(0,len(shtNames_Stks)):
    for trendCat in range(0,len(trendList)):
        # for t in trendList[trend]:
        for t in range(0,len(trendList[trendCat])):
            if re.search(r'\b'+shtNames_Stks[n].rstrip()+r'\b',trendList[trendCat][t]) and shtNames_Stks[n].rstrip() not in shtExceptions:
                stks_hitScore[n] += 1
                wc = SentAnalysis.getWordCount(trendListText[trendCat][t])
                featLs = SentAnalysis.getStoryLexCount(wc)
                SentAnalysis.writeFeatToFile(shtNames_Stks[n],featLs)
                # print "Hit Shorty!! ", shtNames_Stks[n].rstrip()," in ",t.rstrip()," --- ",trend
            elif re.search(lngNames_Stks[n].rstrip(),trendList[trendCat][t]):
                stks_hitScore[n] += 1
                wc = SentAnalysis.getWordCount(trendListText[trendCat][t])
                featLs = SentAnalysis.getStoryLexCount(wc)
                SentAnalysis.writeFeatToFile(shtNames_Stks[n],featLs)
            #     print "Hit LONG!! ", lngNames_Stks[n].rstrip()," in ",t.rstrip()," --- ",trend


#Write all the "hit score" for each stock to file
#for now we are just looking to see if the company stock's short name or long name
#appears in the google trends titles (pretty niave)
file = open("stock-trend_titleHits.txt","w")
for n in range(0,len(shtNames_Stks)):
    file.write(shtNames_Stks[n].rstrip() + " | " + lngNames_Stks[n].rstrip() + " | " + str(stks_hitScore[n]) +'\n')
