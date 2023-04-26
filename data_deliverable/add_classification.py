import pandas as pd
import json as json

housing_merged =  pd.read_csv('data/housing_merged.csv')
income_classification = pd.read_csv('data/income_classification_zipcode.csv')
income_classification = income_classification.set_index('NAME')

#print(income_classification.head())
zipcode = housing_merged.iloc[0, 3]
print('zipcode', zipcode)
print(income_classification.loc[zipcode, "2011"])

#income_classification[housing_merged['zipcode']][housing_merged['year_of_violation']]

def classification(x) -> int:
  # print("zip", x["zipcode"])
  print(type(x[3]))
  print(type(x[9]))
  return income_classification.loc[str(x[3]), x[9]]


housing_merged['rich'] = housing_merged.apply(lambda x: classification(x), axis=1)

#print(housing_merged.head())

