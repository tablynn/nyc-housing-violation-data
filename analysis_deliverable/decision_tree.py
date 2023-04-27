from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import cross_val_score

df = pd.read_csv('../data_deliverable/data/housing_income_merged.csv')
df = df.dropna(subset=['class'])
#print(df['class'])

df['status'] = df.status.map(dict(Open=1, Close=0))
X = df[['latitude','longitude','year_of_violation','status', 'zipcode', 'med_income']]
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(max_depth=3)

model.fit(X_train, y_train)

scores = cross_val_score(model, X, y, cv=5)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1 score:', f1)
print("Average accuracy (cross val)", scores.mean())