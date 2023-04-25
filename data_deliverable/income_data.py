import pandas as pd
import json as json

folder_path = "data/income_data/median_income/"
med_2011 = pd.read_csv(folder_path+"2011.csv")
med_2012 = pd.read_csv(folder_path+"2012.csv")
med_2013 = pd.read_csv(folder_path+"2013.csv")
med_2014 = pd.read_csv(folder_path+"2014.csv")
med_2015 = pd.read_csv(folder_path+"2015.csv")
med_2016 = pd.read_csv(folder_path+"2016.csv")
med_2017 = pd.read_csv(folder_path+"2017.csv")
med_2018 = pd.read_csv(folder_path+"2018.csv")
med_2019 = pd.read_csv(folder_path+"2019.csv")
med_2020 = pd.read_csv(folder_path+"2020.csv")
med_2021 = pd.read_csv(folder_path+"2021.csv")
df_list = [med_2011]

nyc_median = [49461, 50895, 52223, 52996, 55752, 58856, 60869, 63799, 69407, 67046, 67997]

def convert_zip(zip):
    new_zip = zip.split(" ")[1]
    return new_zip 

def main():
    main_df = med_2011[['NAME','S1901_C01_012E']].iloc[1: , :]
    main_df['NAME'] = main_df['NAME'].apply(convert_zip)

    for df in df_list:
        new_df = df[['NAME','S1901_C01_012E']].iloc[1: , :]

        main_df.merge(new_df, how='inner', on='NAME')

    main_df.to_csv('data/zipcode_median_income.csv', index = False)

    # with open('data/zipcode_median_income.json', 'w') as outfile:
    #     json.dump(json_df, outfile, indent=4)

def convert_zip(zipcode):
    new_zip = zipcode.split()[1]
    return new_zip 


if __name__ == '__main__':
    main()
    





