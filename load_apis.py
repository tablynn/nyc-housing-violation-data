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

DOB_COMPLAINTS = \
    "https://data.cityofnewyork.us/resource/eabe-havv.json"

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

def mapper_complaints(record2):
    try:
        yield ((record2['house_number'].strip(' \t'), record2['house_street'].strip(' \t')), list([record2]))
    except:
        return

def reducer(a, b):
     return a + b


def mapper2_code(record):
    housenum = record[0][0]
    street = record[0][1]
    
    date_list = []
    violation_list = []
    num_violations = len(record[1])
    zip_code = record[1][0]['zip']
    for rec in record[1]:
        date_list.append(rec['inspectiondate'][:4])
        violation_list.append(('maintenance code violation', rec['ordernumber']))
    
    return [{'house_number': housenum, 'street': street, 'zipcode': zip_code, \
        'total_housing_maintenance_code_violations': num_violations, \
            'list of violations': violation_list, 'years_of_violations': date_list}]

def mapper2_dob(record):
    housenum = record[0][0]
    street = record[0][1]
    
    date_list = []
    violation_list = []
    num_violations = len(record[1])
    for rec in record[1]:
        date_list.append(rec['issue_date'][:4])
        violation_list.append(('DOB violation', rec['violation_type_code']))
    
    return [{'house_number': housenum, 'street': street, \
        'total_housing_maintenance_code_violations': num_violations, \
            'list of violations': violation_list, 'years_of_violations': date_list}]

def mapper2_complaints(record):
    housenum = record[0][0]
    street = record[0][1]
    
    date_list = []
    violation_list = []
    num_violations = len(record[1])
    zip_code = record[1][0]['zip_code']
    for rec in record[1]:
        violation_list.append(('DOB complaint', rec['complaint_category']))
        date_list.append(rec['date_entered'][-4:])
    
    return [{'house_number': housenum, 'street': street, 'zipcode': zip_code, \
        'total_housing_maintenance_code_violations': num_violations, \
            'list of violations': violation_list, 'years_of_violations': date_list}]



def main():
    sc = SparkContext()

    code_violations = scrape(HOUSING_MAINTENANCE_CODE_VIOLATIONS)
    dob_violations = scrape(DOB_VIOLATIONS)
    complaints = scrape(DOB_COMPLAINTS)


    code2 = sc.parallelize(code_violations, 128).map(mapper_code_violation).reduceByKey(reducer).flatMap(mapper2_code).collect()
    dob = sc.parallelize(dob_violations, 128).flatMap(mapper_dob_violation).reduceByKey(reducer).flatMap(mapper2_dob).collect()
    complaints2 = sc.parallelize(complaints, 128).flatMap(mapper_complaints).reduceByKey(reducer).flatMap(mapper2_complaints).collect()


    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/housing_code_violations.json', 'w') as outfile:
            json.dump(code_violations, outfile, indent=4)

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/dob_violations.json', 'w') as outfile:
        json.dump(dob_violations, outfile, indent=4)

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/dob_complaints.json', 'w') as outfile:
        json.dump(complaints, outfile, indent=4)



    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/housing_code_violations2.json', 'w') as outfile:
            json.dump(code2, outfile, indent=4)


    # with open('data/dob_complaints.json', 'w') as outfile:
    #     json.dump(scrape(DOB_COMPLAINTS), outfile, indent=4)

   

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/dob_violations2.json', 'w') as outfile:
        json.dump(dob, outfile, indent=4)

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/dob_complaints2.json', 'w') as outfile:
        json.dump(complaints2, outfile, indent=4)

if __name__ == '__main__':
    main()
    



    


