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



def main():
    big_data = pd.read_csv('data_deliverable/data/housing_merged.csv')
    print("Chi-Square Independence Test Results:")
    tstats, pvalue = chisquared_independence_test(big_data, "status", "income_level")


