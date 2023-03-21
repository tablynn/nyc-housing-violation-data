from bs4 import BeautifulSoup, NavigableString
import requests
import sqlite3


MOST_ACTIVE_STOCKS_URL = "https://www.rubmaps.ch/search-s33"

page = requests.get(MOST_ACTIVE_STOCKS_URL)
soup = BeautifulSoup(page.content, 'html.parser')
container = soup.find(id = "container")
spas = {}

rows = container.find_all("div", class_ = "main-row")

for i in rows:
    first = i.find("div")
    name_div = first.a
    name = [x.strip() for x in name_div.contents if isinstance(x, NavigableString)][0].upper()
    #print(first.a)
    contents = [x.strip() for x in first.contents if isinstance(x, NavigableString)]
    address = contents[2]
    zip_code = contents[3].split(', ')[2]
    #print(name)
    #print(address)
    #print(zip_code)
    #print(type(name))
    spas[name] = {}
    spas[name]['address'] = address
    spas[name]['zip_code'] = zip_code
    

print(spas)