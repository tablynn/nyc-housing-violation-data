import pandas as pd
import os
import json
import requests


rubmaps_df = None
dob_df = None
maintainance_df = None
with open('data/dob_df.json') as json_file:
    data = json.load(json_file)
    dob_df = pd.DataFrame.from_dict(data)

with open('data/rubmaps_df.json') as json_file:
    data = json.load(json_file)
    rubmaps_df = pd.DataFrame.from_dict(data).dropna()


NYC_MAINTAIN_API = "https://data.cityofnewyork.us/resource/wvxf-dwi5.csv"

maintainance_data = requests.get(NYC_MAINTAIN_API)

maintainance_df = pd.read_csv()
print(maintainance_df.columns.values)

merged_dob = rubmaps_df.merge(dob_df,on=['lat','lon'])
merged_maintainence = rubmaps_df.merge(maintainance_df,left_on=['lat','lon'], right_on=['latitude','longitude'])

#print(merged)
merged_dict = merged_dob.to_dict('records')


with open('data/merge_rub_dob.json', 'w') as outfile:
    json.dump(merged_dict, outfile, indent=4)


merged_maintainence_dict = merged_maintainence.to_dict('records')
with open('data/merge_rub_maintain.json', 'w') as outfile:
    json.dump(merged_maintainence_dict, outfile, indent=4)

#convert violations to a dataframe that has lat and lon as columns

'''
data = json.load(open('data/merge_rub_dob.json'))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in data]
}


output = open("data/merge_geojson.json", 'w')
json.dump(geojson, output)


rubmaps = json.load(open('data/rubmaps_df.json'))

rubmaps_geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in rubmaps]
}
output = open("data/rubmaps_geojson.json", 'w')
json.dump(rubmaps_geojson, output)

dob = json.load(open('data/dob_df.json'))
dob_geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in dob]
}
output = open("data/dob_geojson.json", 'w')
json.dump(dob_geojson, output)
'''
