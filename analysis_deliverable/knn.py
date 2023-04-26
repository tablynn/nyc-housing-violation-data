from sklearn import neighbors, datasets, metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np


main = housing_merged =  pd.read_csv('../data_deliverable/data/housing_income_merged.csv')
X = main[['latitude','longitude','year_of_violation','med_income']]
y = main['status'] == 'Open'

#NORMALIZE DATA
scaler = MinMaxScaler() #TODO:
norm = scaler.fit_transform(X) #TODO: 

main= pd.DataFrame(norm, columns=X.columns)

#SPLIT TRAIN/VALIDATION/TEST
X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size = 0.4, random_state = 1)
print("Train set:", X_train.shape, y_train.shape)


X_val, X_test, y_val, y_test = train_test_split(X, y, train_size = 0.2, test_size = 0.2) 
print("Validation set:", X_val.shape, y_val.shape)
print("Test set:", X_test.shape, y_test.shape)


k = 4
# Train model
KNN = KNeighborsClassifier(k).fit(X_train, y_train)
cv_scores = cross_val_score(KNN, X, y, cv=10)

print('cv scores', cv_scores)
print('CV average', np.sum(cv_scores)/len(cv_scores))

# Predict test set
yhat = KNN.predict(X_test)
print(yhat[:5])

# Evaluate accuracy of model
print("Train set Accuracy: ", metrics.accuracy_score(y_train, KNN.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


#TRYING OUT DIFFERENT KS
ks = range(1,11)
train_accs = []
val_accs = []

for k in ks:
  # Train model
  KNN = KNeighborsClassifier(k).fit(X_train, y_train)

  # Predict test set
  yhat = KNN.predict(X_val)
  print(yhat[:5])

  train_accs.append(metrics.accuracy_score(y_train, KNN.predict(X_train)))
  val_accs.append(metrics.accuracy_score(y_val, yhat)) 



#pLOT HERE TO FIND OUT WHAT BEST K VALUE IS 
'''
plt.plot(ks, train_accs, 'r', ks, val_accs, 'g')
plt.ylabel("Accuracy")
plt.xlabel("No. of neighbors (k)")
plt.legend(['Training','Validation'])
plt.show()
'''


k = 4 #highest accuracy without overfitting from plotting


KNN = KNeighborsClassifier(k).fit(X_train, y_train) 

# Predict test set
yhat = KNN.predict(X_test)
print(yhat[:5])

# Evaluate accuracy of model
train_acc = metrics.accuracy_score(y_train, KNN.predict(X_train)) 
test_acc = metrics.accuracy_score(y_test, yhat)

print("Train set Accuracy: ", train_acc)
print("Test set Accuracy: ", test_acc)
