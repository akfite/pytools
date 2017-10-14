#!/usr/bin/python3.5
from bs4 import BeautifulSoup
import requests
import sys

args = sys.argv

if len(args) < 2:
    print("Provide a stock ticker symbol to get the last traded price.")
    exit()
else:
    for stock in args[1:]:
        # try to load the msn page for the stock
        msn_url = 'http://www.msn.com/en-us/money/indexdetails/'
        page = requests.get(msn_url + stock.upper())
        soup = BeautifulSoup(page.content, 'html.parser')

        # look for the stock quote value
        currentvalue = soup.find("div", {"class": "precurrentvalue"})
        currentvalue = currentvalue.text.replace('\n', '')

        if currentvalue:
            # if currentvalue is found, assume we can find the pctchange
            pctchange = soup.find("div", {"data-role": "percentchange"})
            pctchange = pctchange.next

            # print the result
            quote = currentvalue + " (" + pctchange + ")"
            print(stock.upper() + " is currently trading at " + quote)
        else:
            print("Unable to find a quote for " + stock.upper())
