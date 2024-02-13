import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


data=pd.read_csv('datasets/data_banknote_authentication.csv')
print(data)

x=data[data.columns.drop('class')]
y=data['class']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)




#1 random forest model

model1=RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
model1.fit(xtrain,ytrain)
print(f'Random Forest \ntest accuracy: {model1.score(xtest,ytest)}  train accuracy : {model1.score(xtrain,ytrain)}')

#2 Adaptive Boosting model

model2=AdaBoostClassifier(n_estimators=10)
model2.fit(xtrain,ytrain)
print(f'AdaBoost Forest \ntest accuracy: {model2.score(xtest,ytest)}  train accuracy : {model2.score(xtrain,ytrain)}')

#3 Decision tree model

model3=DecisionTreeClassifier()
model3.fit(xtrain,ytrain)
print(f'Decision tree  \ntest accuracy: {model3.score(xtest,ytest)}  train accuracy : {model3.score(xtrain,ytrain)}')

#3 logistic Regression

model4=LogisticRegression()
model4.fit(xtrain,ytrain)
print(f'Logistic regression  \ntest accuracy: {model4.score(xtest,ytest)}  train accuracy : {model4.score(xtrain,ytrain)}')
