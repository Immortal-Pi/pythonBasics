import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz

data=pd.read_csv('credit_risk.csv')

x=data[data.columns.drop('class').values]
y=data['class']

#encoding the to convert vatergorical values to numberical values
credit_data_encoding=pd.get_dummies(x)

print(credit_data_encoding.columns)

#split test and train

xtrain,xtest,ytrain,ytest=train_test_split(credit_data_encoding,y,test_size=0.15,random_state=10)
model=DecisionTreeClassifier(random_state=1)
model.fit(xtrain,ytrain)

train_predict=model.predict(xtrain)
test_predict=model.predict(xtest)

dot_data=export_graphviz(model, out_file=None,feature_names=credit_data_encoding.columns,class_names=model.classes_)
graph=graphviz.Source(dot_data)
print(graph)

#test accuracy
train_Accuracy=model.score(xtrain,ytrain)
test_accuracy=model.score(xtest,ytest)

print(f'model train and test accuracy {train_Accuracy,test_accuracy}')

#overfit model :- works good for trained data but not for test data,
#solution:- we have to change the hyperparameters

model1=DecisionTreeClassifier(min_samples_split=10,min_impurity_decrease=0.005)
model1.fit(xtrain,ytrain)
train_Accuracy_model1=model1.score(xtrain,ytrain)
test_accuracy_model1=model1.score(xtest,ytest)
print(f'model1 train and test accuracy {train_Accuracy_model1,test_accuracy_model1}')


model2=DecisionTreeClassifier(min_samples_split=20,min_impurity_decrease=0.1)
model2.fit(xtrain,ytrain)
train_Accuracy_model2=model2.score(xtrain,ytrain)
test_accuracy_model2=model2.score(xtest,ytest)
print(f'model2 train and test accuracy {train_Accuracy_model2,test_accuracy_model2}')




