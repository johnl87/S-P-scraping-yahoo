#importing libraries
import requests
from bs4 import BeautifulSoup
import json

#S&P500, S&P/TSX comp index, Nasdaq
listOfStocks = ['%5EGSPC', 'NQ%3DF', '%5EGSPTSE']
displayStocks = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    url = f'https://ca.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers= headers)
    #print(r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')
    #using stock dictionary
    stock = {
        'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
        'percentChange': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock


#runs a for each loop that iterates each item inside list of stocks and displays the stock details at the current time
for stocks in listOfStocks:
    displayStocks.append(getData(stocks))
    print('Obtaining... please wait', stocks)

#outputs the list of stock data in json format
with open ('yahooStocks.json', 'w') as f:
    json.dump(displayStocks, f)
