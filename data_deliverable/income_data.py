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
df_list = [med_2012, med_2013, med_2014, med_2015, med_2016, med_2017, med_2018, med_2019, med_2020, med_2021]

nyc_median = [49461, 50895, 52223, 52996, 55752, 58856, 60869, 63799, 69407, 67046, 67997]

def convert_zip(zip):
    new_zip = zip.split(" ")[1]
    return new_zip 

def main():
    main_df = med_2011[['NAME','S1901_C01_012E']].iloc[1: , :]
    main_df['NAME'] = main_df['NAME'].apply(convert_zip)
    main_df.rename(columns={'S1901_C01_012E' : '2011'}, inplace = True)
    year = 2011
    index = 1
    for df in df_list:
        df = df[['NAME','S1901_C01_012E']].iloc[1: , :]
        df['NAME'] = df['NAME'].apply(convert_zip)

        df.rename(columns={'S1901_C01_012E' : str(index + 2011)}, inplace = True)
        index += 1

        main_df = pd.merge(main_df, df, on='NAME')

    main_df[main_df['2011'] != '-']

    main_df.to_csv('data/zipcode_median_income.csv', index = False)

    income_class_df = income_classification(main_df)

    income_class_df.to_csv('data/income_classification_zipcode.csv', index = False)
    print(income_class_df)

def income_classification(big_df):
    income = big_df.copy()

    income = income.replace("2,500-", -1)
    income = income.replace("-", -1)
    income = income.replace("(X)", -1)
    
    income = income.replace("250,000+", 250000)
   
    i = 0
    for col in income.iloc[:, 1:]:
        income[col] = income[col].apply(lambda x: 1 if int(x) > nyc_median[i] else (0 if x != -1 else -1))
        i+=1 

    return income



if __name__ == '__main__':
    main()
    





