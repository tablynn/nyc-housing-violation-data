import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

# import the toolkit for plotting matplotlib 3D
from mpl_toolkits import mplot3d

# import the stuff for geographic plots
import plotly.figure_factory as ff
import seaborn as sns
import plotly.express as px

def sum_violations(data, year):
    return len(data.drop(data[data['year_of_violation']==year].index))

df = pd.read_csv('../data_deliverable/data/housing_income_merged.csv')

rich_data = df.drop(df[df['rich']== 0].index)
poor_data = df.drop(df[df['rich']== 1].index)
rich_violate = []
poor_violate = []
high_or_low = []
years = []

for year in range(2011, 2022):
    rich_violate.append(sum_violations(rich_data, year))
    poor_violate.append(sum_violations(poor_data, year))
    years.append(year)

high_or_low = ["High income" for i in range(2011, 2022)]
high_or_low = high_or_low + ["Low income" for i in range(2011, 2022)]

two_sample_data = {
    "Year": years + years,
    "Total violations": rich_violate + poor_violate,
    "Category of income": high_or_low
}
two_sample_df = pd.DataFrame(two_sample_data)


fig = plt.figure(figsize=(8,5))
sns.barplot(data=two_sample_df,
            x="Year",
            y="Total violations",
            hue="Category of income",
            hue_order = ["Low income", "High income"]
            )

plt.xlabel('Year')
plt.ylabel('Total Violations')
plt.title('Total Violations per Year, classified by income level')


plt.savefig("visualizations/avg_violations_year_income.jpg")
plt.show()
