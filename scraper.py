
from bs4 import BeautifulSoup, NavigableString
import requests
import os
import json

MOST_ACTIVE_STOCKS_URL = "https://www.rubmaps.ch/search-s33"

spas_list = [] 


for a in range(1, 212): 
    if a == 1:
        page = requests.get(MOST_ACTIVE_STOCKS_URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        container = soup.find(id = "container")

        rows = container.find_all("div", class_ = "main-row")

        for i in rows:
            first = i.find("div")
            name_div = first.a
            name = [x.strip() for x in name_div.contents if isinstance(x, NavigableString)][0].upper()
            #print(first.a)
            contents = [x.strip() for x in first.contents if isinstance(x, NavigableString)]
            address = contents[2]
            zip_code = contents[3].split(', ')[2]
          
            spa = {}
            spa['name'] = name
            spa['address'] = address
            spa['zip_code'] = int(zip_code)
            spas_list.append(spa)  

    else:
        #print(str(a))
        page = requests.get(MOST_ACTIVE_STOCKS_URL + "-p" + str(a))
        soup = BeautifulSoup(page.content, 'html.parser')
        container = soup.find(id = "container")

        rows = container.find_all("div", class_ = "main-row")

        for i in rows:
            first = i.find("div")
            name_div = first.a
            name = [x.strip() for x in name_div.contents if isinstance(x, NavigableString)][0].upper()
            #print(first.a)
            contents = [x.strip() for x in first.contents if isinstance(x, NavigableString)]
            address = contents[2]
            try:
                zip_code = contents[3].split(', ')[2]
            except IndexError:
                if a == 20 and name == 'GOOD GIRLS':
                    zip_code = '10001'

          
            spa = {}
            spa['name'] = name
            spa['address'] = address
            spa['zip_code'] = int(zip_code)
            spas_list.append(spa)      
    

#print(spas['GOOD GIRLS'])
print(len(spas_list))

if not os.path.exists("data"):
   os.makedirs("data")

with open('data/all_spas.json', 'w') as outfile:
    json.dump(spas_list, outfile, indent=4)

