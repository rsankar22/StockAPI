import yahoo_fin as yh
from bs4 import BeautifulSoup
import requests
url = 'https://finance.yahoo.com/u/yahoo-finance/watchlists/most-watched'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
def getHeaderData():
    div_elements = soup.findChildren('td')
    return div_elements
