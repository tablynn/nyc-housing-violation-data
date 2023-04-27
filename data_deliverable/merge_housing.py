from urllib import response
import requests
from pyspark import SparkContext
import os
import json
import argparse
import pandas as pd
import csv
import load_apis
import geocoding

load_apis
geocoding
housing_code_df = pd.read_json('data/housing_code_violations2.json')
dob_violate_df = pd.read_json('data/new_dob_zipcode_df.json')

frames = [housing_code_df, dob_violate_df]
merged_df = pd.concat(frames, ignore_index=True)
print(merged_df)
merged_json = merged_df.to_csv('data/housing_merged.csv')
