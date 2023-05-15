import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json


#read in dataset and perform a groupby by zipcode
df = pd.read_csv("./data_deliverable/data/housing_income_merged.csv")
zipcodes_income = df[['zipcode','med_income','year_of_violation']].drop_duplicates().sort_values(by='zipcode')
grouped_zipcode = df.groupby(['zipcode']).size().reset_index(name='counts')


#import geojson for zipcode boundaries
with urlopen('https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/ny_new_york_zip_codes_geo.min.json') as response:
    zipcodes = json.load(response)


#teal chloropleth map
fig = px.choropleth(grouped_zipcode, 
                    geojson=zipcodes, 
                    locations='zipcode', 
                    color='counts',
                    color_continuous_scale="Teal",
                    range_color=(1,50),
                    featureidkey="properties.ZCTA5CE10",
                    scope="usa",
                    labels={'Cluster':'Cluster_Category'}
                    )

#set scope to just New York State
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
      title_text='New York Housing Violations by Zipcode')
fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.show()