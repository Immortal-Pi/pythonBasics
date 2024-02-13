import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier


data=pd.read_csv('datasets/spambase.csv')
# print(data.columns)
# features=data.columns.drop('spam')
# print(features)
features=data[data.columns.drop('spam')]
print(features)
# x=data[features]
# y=data['spam']
target=data['spam']

xtrain,xtest,ytrain,ytest=train_test_split(features,target,test_size=0.2,random_state=100)
model1=RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
model1.fit(xtrain,ytrain)

print(f'test accuracy: {model1.score(xtest,ytest)} train accuracy: {model1.score(xtrain,ytrain)}')

features_importance=pd.DataFrame(np.array([features.columns,model1.feature_importances_]).T,columns=['feature','importance'])

# print(np.array([features,model1.feature_importances_]).T)
print(features_importance.sort_values(by='importance',ascending=False))
pd1=pd.DataFrame(features_importance)


# test2
# print(data)
# x=data[data.columns.drop('spam')]
# y=data['spam']
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)
# model1=RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
# model1.fit(xtrain,ytrain)
#
# # print(f'accuracy test:{model1.score(1)}')
# importantfeatures=pd.DataFrame(np.array([x.columns,model1.feature_importances_]).T,columns=['feature','importance'])
# print(importantfeatures.sort_values(by='importance',ascending=False))
# # print(pd.DataFrame(np.array([x.columns,model1.feature_importances_]).T))
# pd2=pd.DataFrame(importantfeatures.sort_values(by='importance',ascending=False))
# print(pd1.query('importance>0'))
# print(pd2.query('importance>0'))

data=pd.read_csv('datasets/spambase.csv')
# print(data.columns)
# features=data.columns.drop('spam')
# print(features)
features=data[data.columns.drop('spam')]
print(features)
# x=data[features]
# y=data['spam']
target=data['spam']

xtrain,xtest,ytrain,ytest=train_test_split(features,target,test_size=0.2,random_state=100)
model1=RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
model1.fit(xtrain,ytrain)

print(f'test accuracy: {model1.score(xtest,ytest)} train accuracy: {model1.score(xtrain,ytrain)}')

features_importance=pd.DataFrame(np.array([features.columns,model1.feature_importances_]).T,columns=['feature','importance'])

# print(np.array([features,model1.feature_importances_]).T)
# print(features_importance.sort_values(by='importance',ascending=False))
pd2=pd.DataFrame(features_importance)
# print(pd1.query('importance>0'))
print(pd2.query('importance>0'))
