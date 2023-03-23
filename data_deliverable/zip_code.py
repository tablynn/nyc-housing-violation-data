from urllib import response
import requests
from pyspark import SparkContext
import os
import json
import argparse
import pandas as pd
from pandas.io.json import json_normalize

ZIPCODE_DEMOGRAPHICS = \
    "https://data.cityofnewyork.us/resource/kku6-nxdu.json"

def scrape(link):
    req = requests.get(link)
    return req.json()

if not os.path.exists("data"):
        os.makedirs("data")

with open('data/zipcode_demographics.json', 'w') as outfile:
    json.dump(scrape(ZIPCODE_DEMOGRAPHICS), outfile, indent=4)


df1 = pd.read_json('data/all_spas.json')
df2 = pd.read_json('data/zipcode_demographics.json')
zipcode_merge_df = pd.merge(df1, df2, on='jurisdiction_name', how='left')
print(zipcode_merge_df)
# for col in zipcode_merge_df.columns:
#     print(col)
zipcode_merge_df.to_json(r'data/merged_zipcodes.json')