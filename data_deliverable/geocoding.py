from bs4 import BeautifulSoup, NavigableString
import requests
import os
import json
import pandas as pd

GOOGLE_API_KEY = "AIzaSyBSJZzp_BCaoCcDPteg6SY2eA42DmpodNE"

MOST_ACTIVE_STOCKS_URL = "https://www.rubmaps.ch/search-s33"

spas_list = [] 

def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return lat, lng
addresses = []
address_df = []
geo_dictionary = []
dob_dictionary = []

with open('data/all_spas.json') as json_file:
    data = json.load(json_file)
    spa_df = pd.DataFrame.from_dict(data)
 
    # for reading nested data [0] represents
    # the index value of the list
     
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for spa in data:
        ad = {}
        #address_df['address'] = spa['address']
        address = spa['address'] + " " + str(spa['jurisdiction_name'])
        addresses.append(address)
        lat,lon = extract_lat_long_via_address(address)
        #geo_dictionary.append(lat,lon)

        ad['name'] = spa['name']
        ad['address'] = spa['address']
        try:
            ad['lat'] = round(lat,5)
            ad['lon'] = round(lon,5)
        except:
            ad['lat'] = lat
            ad['lon'] = lon
        address_df.append(ad)


with open('data/dob_violations2.json') as json_file:
    data = json.load(json_file)

    for i in data:
        
        # these addresses have borough instead of zipcode
        address = i['house_number'] + " " + i['street'] + " " + i['boro']
        vio_count = i['total_housing_maintenance_code_violations']
        vio_list = i['list of violations']
        vio_years = i['years_of_violations']
        lat,lon = extract_lat_long_via_address(address)

        loc = {}
        try:
            loc['lat'] = round(lat,5)
            loc['lon'] = round(lon,5)
        except:
            loc['lat'] = lat
            loc['lon'] = lon
        loc['violation_count'] = vio_count
        loc['list_of_violations'] = vio_list
        loc['years_of_violations'] = vio_years
        dob_dictionary.append(loc)

with open('data/rubmaps_df.json', 'w') as outfile:
    #dictionary form of rubmaps df
    json.dump(address_df, outfile, indent=4)


with open('data/dob_df.json', 'w') as outfile:
    #dictionary form of dobviolations2 df
    json.dump(dob_dictionary, outfile, indent=4)



    

#print(len(addresses))
#print(len(geo_dictionary))
#print(geo_dictionary)
print(address_df)
rubmaps_df = pd.DataFrame.from_dict(address_df)
#dob_df = pd.DataFrame.from_dict(dob_dictionary)
#print(dob_df.head())
#print(spa_df)

#write geodictionary to a json with lat and lon
#make a dataframe w name and lat and lon?
#do same conversion of geocoding for housing violations after 2000
#start with just DOB violations
#join to dataframe w the housing violations and then merge on lat/lon

#name
#total violations, list of violations, year number
#(lat,lon), [rest]