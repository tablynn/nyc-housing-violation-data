from urllib import response
import requests

import os
import json
import argparse


HOUSING_MAINTENANCE_CODE_VIOLATIONS = \
    'https://data.cityofnewyork.us/resource/wvxf-dwi5.json'

DOB_VIOLATIONS = \
    "https://data.cityofnewyork.us/resource/3h2n-5cm9.json"

DOB_COMPLAINTS = \
    "https://data.cityofnewyork.us/resource/eabe-havv.json"

ZIPCODE_DEMOGRAPHICS = \
    "https://data.cityofnewyork.us/resource/kku6-nxdu.json"


def scrape(link):
    req = requests.get(link)
    return req.json()





#stock_soup = BeautifulSoup(stocks_html, 'html.parser')
#stock_items = stock_soup.find("table").find_all("tr")

# Create connection to database

#Make sure you have the right path to data.db, in case you have any connection issues
#conn = sqlite3.connect('data.db')
#c = conn.cursor()

# Delete tables if they exist
#c.execute('DROP TABLE IF EXISTS "companies";')
#c.execute('DROP TABLE IF EXISTS "quotes";')

if not os.path.exists("data"):
   os.makedirs("data")

with open('data/housing_code_violations.json', 'w') as outfile:
        json.dump(scrape(HOUSING_MAINTENANCE_CODE_VIOLATIONS), outfile, indent=4)

if not os.path.exists("data"):
   os.makedirs("data")

with open('data/dob_violations.json', 'w') as outfile:
    json.dump(scrape(DOB_VIOLATIONS), outfile, indent=4)

if not os.path.exists("data"):
    os.makedirs("data")

with open('data/dob_complaints.json', 'w') as outfile:
    json.dump(scrape(DOB_COMPLAINTS), outfile, indent=4)

if not os.path.exists("data"):
    os.makedirs("data")

with open('data/zipcode_demographics.json', 'w') as outfile:
    json.dump(scrape(ZIPCODE_DEMOGRAPHICS), outfile, indent=4)
    



#TODO: Create tables in the database and add data to it. REMEMBER TO COMMIT
#c.execute('''CREATE TABLE companies(symbol varchar(140) not null, name text, 
  #   location text, PRIMARY KEY(symbol));''')
#c.execute('''CREATE TABLE quotes(symbol varchar(140) not null, prev_close int,
    # price float, avg_price int, volume int, change_pct float, 
   #  PRIMARY KEY(symbol) FOREIGN KEY (symbol) REFERENCES companies(symbol));''')

#for stock in stocks_list:
 #   c.execute('INSERT INTO companies VALUES (?, ?, ?)', (stock['Symbol'], \
  #      stock['Name'], stock['HQ (State)']))
   # c.execute('INSERT INTO quotes VALUES (?, ?, ?, ?, ?, ?)', \
    #    (stock['Symbol'], stock.get('Jan 20 closing'), stock['Price'], \
     #       stock.get('Average Price'), stock['Vol. '], stock['Ch. %']))

#conn.commit()

