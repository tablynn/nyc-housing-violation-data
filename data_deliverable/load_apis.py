from urllib import response
import requests
from pyspark import SparkContext
import os
import json
import argparse
import pandas as pd

HOUSING_MAINTENANCE_CODE_VIOLATIONS = \
    'https://data.cityofnewyork.us/resource/wvxf-dwi5.json'

DOB_VIOLATIONS = \
    "https://data.cityofnewyork.us/resource/3h2n-5cm9.json"


ZIPCODE_DEMOGRAPHICS = \
    "https://data.cityofnewyork.us/resource/kku6-nxdu.json"


def scrape(link):
    req = requests.get(link)
    return req.json()

def mapper_code_violation(record):
    return ((record['housenumber'].strip(' \t'), record['streetname'].strip(' \t')), list([record]))

def mapper_dob_violation(record1):
    try:
        yield ((record1['house_number'].strip(' \t'), record1['street'].strip(' \t')), list([record1]))
    except:
        return




def mapper2_code(record):
    housenum = record[0][0]
    street = record[0][1]
    zip_code = int(record[1][0]['zip'].strip(' \t'))
    lat = float(record[1][0]['latitude'].strip(' \t'))
    long = float(record[1][0]['longitude'].strip(' \t'))
    boro = record[1][0]['boro'].strip(' \t')
    
    return {'house_number': housenum, 'street': street, 'zipcode': zip_code, 'boro': boro, 'latitude': lat, \
        'longitude': long, 'type_of_violation': 'maintenance code violation', \
            'year_of_violation': int(record[1][0]['inspectiondate'][:4].strip())}

def mapper2_dob(record):
    housenum = record[0][0]
    street = record[0][1]
    boro = record[1][0]['boro'].strip(' \t')
    if boro == '1':
        boro = 'MANHATTAN'
    elif boro == '2':
        boro = 'BRONX'
    elif boro == '3':
        boro = 'BROOKLYN'
    elif boro == '4':
        boro == 'QUEENS'
    elif boro == '5':
        boro = 'STATEN ISLAND'
    return {'house_number': housenum, 'street': street, 'boro': boro, \
            'type_of_violation': 'DOB Violation', 'year_of_violation': int(record[1][0]['issue_date'][:4].strip())}
    


def filterer(record):
    return record['year_of_violation'] > 2010



def main():
    sc = SparkContext()

    code_violations = scrape(HOUSING_MAINTENANCE_CODE_VIOLATIONS)
    dob_violations = scrape(DOB_VIOLATIONS)


    code2 = sc.parallelize(code_violations, 128).map(mapper_code_violation).map(mapper2_code).filter(filterer).collect()
    dob = sc.parallelize(dob_violations, 128).flatMap(mapper_dob_violation).map(mapper2_dob).filter(filterer).collect()

    print(len(code2))
    print(len(dob))



    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/housing_code_violations.json', 'w') as outfile:
            json.dump(code_violations, outfile, indent=4)

    with open('data/dob_violations.json', 'w') as outfile:
        json.dump(dob_violations, outfile, indent=4)


    with open('data/housing_code_violations2.json', 'w') as outfile:
            json.dump(code2, outfile, indent=4)

    with open('data/dob_violations2.json', 'w') as outfile:
        json.dump(dob, outfile, indent=4)


if __name__ == '__main__':
    main()
    



    


