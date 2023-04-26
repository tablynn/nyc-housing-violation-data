import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency

def chisquared_independence_test(df, column_a_name, column_b_name):

    cross_table = pd.crosstab(df[column_a_name], df[column_b_name])

    chi2_result = chi2_contingency(cross_table)
    tstats = chi2_result[0]
    pvalue = chi2_result[1]
    
    print("T-statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)

    return tstats, pvalue

def one_sample_ttest(values, population_mean):
    tstats, pvalue = ttest_1samp(a=values, popmean=population_mean)
    print("T-statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)
    return tstats, pvalue

def two_sample_ttest(values_a, values_b):
    tstats, pvalue = ttest_ind(a=values_a, b=values_b)
    print("T-statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)
    return tstats, pvalue

def sum_violations(data, year):
    return len(data.drop(data[data['year_of_violation']==year].index))



def main():
    big_data = pd.read_csv('data_deliverable/data/housing_income_merged.csv')
    print("Chi-Square Independence Test Results:")
    tstats, pvalue = chisquared_independence_test(big_data, "status", "rich")
    print("One Sample T-Test Results:")
    tstat2, pval2 = one_sample_ttest(big_data['med_income'], 67997)
    rich_data = big_data.drop(big_data[big_data['rich']== 0].index)
    poor_data = big_data.drop(big_data[big_data['rich']== 1].index)
    rich_violate = []
    poor_violate = []

    for year in range(2011, 2022):
        rich_violate.append(sum_violations(rich_data, year))
        poor_violate.append(sum_violations(poor_data, year))
    
    two_sample_data = {
        "Rich": rich_violate,
        "Poor": poor_violate
    }
    two_sample_df = pd.DataFrame(two_sample_data)
    print("Two Sample T-Test Results:")
    tstats3, pvalue3 = two_sample_ttest(two_sample_df['Rich'].values, two_sample_df['Poor'].values)


if __name__ == '__main__':
    main()


