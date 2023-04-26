from sklearn import neighbors, datasets, metrics
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#predict rich or poor based on type of violation/lat/lon/median income/year

main = housing_merged =  pd.read_csv('../data_deliverable/data/housing_income_merged.csv')

main.status.map(dict(Open=1, Close=0))
main.head()
X = main[['latitude','longitude','year_of_violation','status']]
y = main['rich'] == 1

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0) 

# instantiate the model 

logreg =  LogisticRegression(solver='liblinear') 



# fit the model with data 

logreg.fit(X_train,y_train) 

y_pred=logreg.predict(X_test) 

y_pred 

print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) 

print("Precision:",metrics.precision_score(y_test, y_pred)) 

print("Recall:",metrics.recall_score(y_test, y_pred)) 