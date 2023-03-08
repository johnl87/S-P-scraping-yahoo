
import requests
from bs4 import BeautifulSoup

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    url = f'https://ca.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers= headers)
    #print(r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
        'percentChange': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock
    #price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    #change = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text

print(getData('%5EGSPC'))