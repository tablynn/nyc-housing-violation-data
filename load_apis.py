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


def scrape(link):
    req = requests.get(link)
    return req.json()

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
    


