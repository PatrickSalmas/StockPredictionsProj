import schedule
import time

def job(t):
    import StocksDailyScrape
    return


schedule.every().day.at("06:35").do(job,'morning Scrape')
schedule.every().day.at("13:05").do(job,'afternoon Scrape')


#American stocks open at 6:30 AM and close at 1 PM PST


while True:
    schedule.run_pending()
    # print "let's wait a minute here"
    time.sleep(55)