#!/usr/bin/python3.5
from bs4 import BeautifulSoup
import requests
import sys

# parse args for the desired quote
args = sys.argv

if len(args) < 2:
    print("Provide a stock ticker to get the last traded price.")
    exit()
else:
    for stock in args[1:]:
        # get the webpage html and parse it out
        msn_url = 'http://www.msn.com/en-us/money/indexdetails/'
        page = requests.get(msn_url + stock.upper())
        soup = BeautifulSoup(page.content, 'html.parser')

        # look for the stock quote value
        currentvalue = soup.find("div", {"class": "precurrentvalue"})
        currentvalue = currentvalue.text.replace('\n', '')

        if currentvalue:
            # print the result
            print(stock.upper() + " is currently trading at " + currentvalue)
        else:
            print("Unable to find a quote for " + stock.upper())
