import pandas as pd
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import precision_score,recall_score

data=pd.read_csv('bank-additional-full.csv')
print(data)
x=data[data.columns.drop(['duration','y'])]

y=data['y']
# print(x,y)

#encoding
x_encoding=pd.get_dummies(x)

xtrain,xtest,ytrain,ytest=train_test_split(x_encoding,y,test_size=0.2)
model1=DecisionTreeClassifier()
model1.fit(xtrain,ytrain)

print(f'model1 test accuracy: {model1.score(xtest,ytest)}')
print(f'model1 train accuracy: {model1.score(xtrain,ytrain)}')

#graph to visualize
data=export_graphviz(model1,out_file=None,feature_names=x_encoding.columns,class_names=model1.classes_)
graph=graphviz.Source(data)
# print(graph)

#precision and recall
ypredtest=model1.predict(xtest)
ypredtrain=model1.predict(xtrain)

ypredtest_binary=[1 if label=='yes' else 0 for label in ypredtest]
ytest_binary=[1 if label=='yes' else 0 for label in ytest]
# print(ypredtest_binary)

#test precision
print(f'model 1 test precision: {precision_score(ytest_binary,ypredtest_binary)} \n recall: {recall_score(ytest_binary,ypredtest_binary)}')

ypredtrain_binary=[1 if label=='yes' else 0 for label in ypredtrain]
ytrain_binary=[1 if label=='yes' else 0 for label in ytrain]

#train precision
print(f'model 1 train precision : {precision_score(ytrain_binary,ypredtrain_binary)} \n recall: {recall_score(ytrain_binary,ypredtrain_binary)}')


#modify the hyperparameters
model2=DecisionTreeClassifier(min_samples_split=10,min_impurity_decrease=0.005)
model2.fit(xtrain,ytrain)
print(f'model2 test accuracy: {model2.score(xtest,ytest)}')
print(f'model2 train accuracy: {model2.score(xtrain,ytrain)}')

model3=DecisionTreeClassifier(min_samples_split=20,min_impurity_decrease=0.1)
model3.fit(xtrain,ytrain)
print(f'model3 test accuracy: {model3.score(xtest,ytest)}')
print(f'model3 train accuracy: {model3.score(xtrain,ytrain)}')