import yahoo_fin as yh
from bs4 import BeautifulSoup
import requests
url = 'https://www.google.com/finance/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


def getHeaderData():
    div_elements = soup.findChildren('html')
    return soup.prettify()
