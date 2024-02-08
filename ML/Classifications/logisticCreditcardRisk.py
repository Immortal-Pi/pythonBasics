import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
data=pd.read_csv('credit_risk.csv')
# print(data.columns)

# print(data['class'].unique())

x=data.columns.drop('class')
y=data['class']
# print(x)
credit_data_encode=pd.get_dummies(data[x])
print(credit_data_encode)

xtrain,xtest,ytrain,ytest=train_test_split(credit_data_encode,y,test_size=0.15,random_state=100)

model=LogisticRegression()
model.fit(xtrain,ytrain)

print(f'test accuracy : {model.score(xtest,ytest)}')
print(f'train accuracy : {model.score(xtrain,ytrain)}')

#predicting target values based on the model
train_prediction=model.predict(xtrain)
test_prediction=model.predict(xtest)

#creating confusion matrics based on trained data
train_confusion_matrix=confusion_matrix(ytrain,train_prediction)
test_confusion_matrix=confusion_matrix(ytest,test_prediction)
print(f'train prediction :\n {train_confusion_matrix}\n test prediction : \n{test_confusion_matrix}')


#accuracy using confusion matrics
train_accuracy=(train_confusion_matrix[0][0]+train_confusion_matrix[1][1])/train_confusion_matrix.sum()
test_accuracy=(test_confusion_matrix[0][0]+test_confusion_matrix[1][1])/test_confusion_matrix.sum()

print(f'train accuray : {train_accuracy}\n test accuracy : {test_accuracy}')
print(classification_report(ytest,test_prediction))