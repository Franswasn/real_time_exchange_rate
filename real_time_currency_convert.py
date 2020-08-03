from bs4 import BeautifulSoup
import pandas as pd
import datetime
import requests
import winsound
import time
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def currencyTracker(currency):
    url = ('https://transferwise.com/de?sourceCurrency=EUR&targetCurrency='+currency)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    price = soup.find('span', {'class': 'tw-calculator-breakdown-rate__value'}).text
    return price


TrackList = ['INR']
while True:
    ExRate = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    for currency_name in TrackList:
        ExRate.append(currencyTracker(currency_name))
        ExchangeRate = currencyTracker(currency_name)
        # print("Current Euro to " + currency_name + " conversion rate is " + ExchangeRate)
        x = float(ExchangeRate)
        if x > 88:
            winsound.Beep(frequency, duration)
            continue
        else:
            continue
    col = [time_stamp]
    col.extend(ExRate)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('exchangerate.csv', mode = 'a', header = False)
    print(col)
    time.sleep(5)

