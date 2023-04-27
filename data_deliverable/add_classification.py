import pandas as pd
import json as json

housing_merged =  pd.read_csv('data/housing_merged.csv')
income_classification = pd.read_csv('data/income_classification_zipcode.csv')
income_classification = income_classification.set_index('NAME')
zipcode_median_income = pd.read_csv('data/zipcode_median_income.csv')
zipcode_median_income = zipcode_median_income.set_index('NAME')

#print(income_classification.head())
zipcode = housing_merged.iloc[0, 3]
#print(type(zipcode))
#print('zipcode', zipcode)
#print(income_classification.loc[str(zipcode), "2011"])
print(housing_merged.iloc[3])

cpi_values = {
                '2011': 247.718, 
                '2012': 251.483, 
                '2013': 256.130, 
                '2014': 260.191, 
                '2015': 259.967, 
                '2016': 262.089, 
                '2017': 267.826, 
                '2018': 272.717, 
                '2019': 276.975, 
                '2020': 281.937, 
                '2021': 288.973
                }

#income_classification[housing_merged['zipcode']][housing_merged['year_of_violation']]

def classification(x) -> int:
  # print("zip", x["zipcode"])
  #print(x[3])
  #print(type(x[9]))
  year = x[10]
  try:
    if (year < 2022):
      return income_classification.loc[x[3], str(year)]
    else:
      return income_classification.loc[x[3], '2021']
  except:
      return -1
  
def median_income(x) -> int: 
  year = x[10]
  try:
    if (year < 2022):
      income = zipcode_median_income.loc[x[3], str(year)]
    else:
      income = zipcode_median_income.loc[x[3], '2021']
    indexer = cpi_values['2021']/cpi_values[str(year)]
    if (income == "250,000+"):
      return round((250000.0 * (indexer)), 2)
    else:
      return round((float(income) * (indexer)), 2)
  except:
    -1  


housing_merged['med_income'] = housing_merged.apply(lambda x: median_income(x), axis=1)
housing_merged['rich'] = housing_merged.apply(lambda x: classification(x), axis=1)

housing_merged = housing_merged.drop(housing_merged[housing_merged['rich']== -1].index)

income_and_housing = housing_merged.to_csv('data/housing_income_merged.csv')

data_sample = housing_merged.iloc[:100,:].to_csv('data/data_sample.csv')

