import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np

data=pd.read_csv('datasets/bank-additional-full.csv')
# print(data[['age','duration']].values)
# print(data.columns)

scalar=MinMaxScaler()
scalar_norm=scalar.fit_transform(data[['age','duration']])

data['age_norm']=scalar_norm[:,0]
data['duration_norm']=scalar_norm[:,1]
print(data)

x=data[['age_norm','duration_norm']]
y=data['y']

xtrain,xtest,ytrain,ytest=train_test_split(x.values,y.values,test_size=0.4)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain,ytrain)

print(f'test accuracy: {model.score(xtest,ytest)}\n train accuracy: {model.score(xtrain,ytrain)}')

k_values=[i for i in range(1,100)]
test_accuracies=[]
train_accuracies=[]
for k in k_values:
    model1=KNeighborsClassifier(n_neighbors=k,metric='euclidean')
    model1.fit(xtrain,ytrain)
    train_accuracies.append(model1.score(xtrain,ytrain))
    test_accuracies.append(model1.score(xtest,ytest))

plt.plot(k_values,train_accuracies,label='train_accuracy')
plt.plot(k_values,test_accuracies,label='test accuracy')
plt.legend()
plt.show()
