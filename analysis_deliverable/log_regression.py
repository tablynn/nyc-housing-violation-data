from sklearn import neighbors, datasets, metrics
import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#predict rich or poor based on type of violation/lat/lon/median income/year

df =  pd.read_csv('../data_deliverable/data/housing_income_merged.csv')

boro_map = {
    'MANHATTAN': 1,
    'BRONX': 2,
    'BROOKLYN': 3,
    'QUEENS': 4,
    'STATEN ISLAND': 5
}

valid_boros = ['MANHATTAN', 'BRONX', 'BROOKLYN', 'QUEENS', 'STATEN ISLAND']

# Replace any borough not in the list with 0
df['boro'] = df['boro'].replace([boro for boro in df['boro'].unique() if boro not in valid_boros], 0)
print('0 counts', df['boro'].value_counts())

df['status'] = df.status.map(dict(Open=1, Close=0))
df['boro'] = df['boro'].replace(boro_map)
print(df['boro'])
df.head()
X = df[['latitude','longitude','year_of_violation','status', 'zipcode', 'boro']]
y = df["med_income"] 

#y = main['rich'] == 1

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0) 

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X_test)

accuracy = r2_score(y_test, y_pred)

print("accuracy", accuracy)
# print("y len", y.value_counts())

# #print("X", X)
# #print('y', y )
# print(y)

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0) 
# #print("y_test", y_test)
# #print('y_train', y_train)

# # instantiate the model 

# logreg =  LogisticRegression(solver='liblinear') 

# # fit the model with data 

# logreg.fit(X_train,y_train) 

# y_pred = logreg.predict(X_test) 


# print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) 

# print("Precision:",metrics.precision_score(y_test, y_pred)) 

# print("Recall:",metrics.recall_score(y_test, y_pred)) 
