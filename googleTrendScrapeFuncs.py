from bs4 import BeautifulSoup
import requests

#PRIVATE FUNC SECTION
def getShortName(line):
    names = line.split("|")
    return names[0]

def getLongName(line):
    names = line.split("|")
    return names[1]




#Extract text from given url
def getText(urlArg):
    if urlArg is None: return ["No_text"]
    # storyPage = requests.get(urlArg)
    try:
        storyPage = requests.get(urlArg, allow_redirects=False)
    except requests.exceptions.ConnectionError:
        return ["No_text"]
    if storyPage.status_code != 200: return ["No_text"]
    storyContent = BeautifulSoup(storyPage.content, 'html.parser')
    storyBody = storyContent.find_all('p')
    # storyBody_PTags = storyContent.find_all('p')
    # storyBody = storyBody_PTags[:]
    # for s in range(0,len(storyBody)):
    #     storyBody[s] = storyBody[s].get_text()

    return storyBody

# #Need a func that creates a list of associated stories for a, or each given company.
# #This logic is in HitGoogleTrends.py
# def get