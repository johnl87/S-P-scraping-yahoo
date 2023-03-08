
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

url = 'https://ca.finance.yahoo.com/quote/%5EGSPC'

r = requests.get(url)
#print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print(price)