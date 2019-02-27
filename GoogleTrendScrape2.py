# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import codecs
import googleTrendScrapeFuncs


#Scrape from categories, "sci/tech" and "sports"
catList = ["t","s"]
urlBase = "https://trends.google.com/trends/trendingsearches/realtime?geo=US&category="
fileBase = "googleTrends_"

for cat in catList:
    urlStr = urlBase + cat
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/psalm/Documents/chromedriver.exe')
    driver.get(urlStr)
    myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='title']"))))
    #
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='feed-load-more-button'][@ng-click=\"ctrl.loadMoreFeedItems()\"]"))).click()
            WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements_by_xpath("//div[@class='title']")) > myLength)
            # titles = driver.find_elements_by_xpath("//div[@class='title']")           #this is the actual webscraping!
            # myLength = len(titles)
        except TimeoutException:
            break

    titles = driver.find_elements_by_xpath("//div[@class='title']")  # this is the actual webscraping!
    summaries = driver.find_elements_by_xpath(
        "//div[@class='details-bottom']/div[@class='subtitles-text-wrapper visible']/div[@class='summary-text']/a[@ng-href]")
    urls = []
    for s in summaries:
        url = s.get_attribute("href")
        urls.append(url)
    # print "Urls set"

    storyTexts = []
    for u in urls:
        st = googleTrendScrapeFuncs.getText(u)
        storyTexts.append(st)

    myLength = len(titles)


    count = 0
    #write all trending titles to file
    fileName = fileBase + cat + "_Titles.txt"
    with codecs.open(fileName,"w",encoding='utf-8') as titleFile:
        titleFile.writelines("%s\n" % title.text for title in titles)

    fileNameText = fileBase + cat + "_Text.txt"
    with codecs.open(fileNameText,"w",encoding='utf-8') as textFile:
        textFile.writelines("%s\n" % text for text in storyTexts)

    driver.quit()