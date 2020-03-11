import schedule
import time


# 1.simple task
def job():
    print("Reading time ....")

def coding():
    print("Coding time ....")

def playing():
    print("Playing time ....")

# set time
schedule.every(5).seconds.do(job)        # every 5 seconds do(run this function)
schedule.every(10).seconds.do(coding)    # for every 10 seconds
schedule.every().day.at("02:04").do(playing)    # using day.at() for particular time

while True:
    schedule.run_pending()    # this runs 
    time.sleep(1)




# 2. task
import requests


url = "https://www.coindesk.com/v1/bpi/currentprice.json"
page = requests.get(url)
data = page.json()

def fetch_bitcoin():
    print("Getting Bitcoin Price ....")
    result_US = data['bpi']['USD']
    print(result_US)

def fetch_bitcoin_currency(x):
    print("Getting Bitcoin Price ....", x)
    result_US = data['bpi'][x]
    print(result_US)


schedule.every(5).seconds.do(fetch_bitcoin)

schedule.every(5).seconds.do(fetch_bitcoin_currency, 'EUR')
schedule.every(5).seconds.do(fetch_bitcoin_currency, 'GBP')

while True:
    schedule.run_pending()
