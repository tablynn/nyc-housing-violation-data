import pandas as pd
import json as json

housing_merged =  pd.read_csv('data/housing_merged.csv')
income_classification = pd.read_csv('data/income_classification_zipcode.csv')
income_classification = income_classification.set_index('NAME')

#print(income_classification.head())
zipcode = housing_merged.iloc[0, 3]
print(type(zipcode))
print('zipcode', zipcode)
#print(income_classification.loc[str(zipcode), "2011"])
print(housing_merged.iloc[3])

#income_classification[housing_merged['zipcode']][housing_merged['year_of_violation']]

def classification(x) -> int:
  # print("zip", x["zipcode"])
  print(type(str(x[3])))
  #print(type(x[9]))
  return income_classification.loc[10457, str(x[9])]


housing_merged['rich'] = housing_merged.apply(lambda x: classification(x), axis=1)

#print(housing_merged.head())

