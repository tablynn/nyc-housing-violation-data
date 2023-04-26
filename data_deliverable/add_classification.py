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
  print(x[3])
  #print(type(x[9]))
  year = x[9]
  try:
    if (year < 2022):
      return income_classification.loc[x[3], str(year)]
    else:
      return income_classification.loc[x[3], '2021']
  except:
      return -1


housing_merged['rich'] = housing_merged.apply(lambda x: classification(x), axis=1)

income_and_housing = housing_merged.to_csv('data/housing_income_merged.csv')

print(housing_merged.head())

