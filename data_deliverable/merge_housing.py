from urllib import response
import requests
from pyspark import SparkContext
import os
import json
import argparse
import pandas as pd
import csv

housing_code_df = pd.read_json('data/housing_code_violations2.json')
dob_violate_df = pd.read_json('data/dob_violations2.json')
complaints_df = pd.read_json('data/dob_complaints2.json')

merged_df1 = pd.merge(housing_code_df, dob_violate_df, on=['house_number', 'street'], how='outer')
merged_df = pd.merge(merged_df1, complaints_df, on=['house_number', 'street'], how='outer')
print(merged_df)
merged_json = merged_df.to_json(path_or_buf='data/housing_merged.json', orient='index')
