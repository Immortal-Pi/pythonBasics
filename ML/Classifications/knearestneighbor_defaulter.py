import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# data=pd.read_csv('defaulter.csv')
# print(data)
# sns.pairplot(data,hue='defaulter',x_vars='income',y_vars='balance',height=4)
# # plt.show()
#
# x1=data.loc[0,['balance','income']]
# x2=data.loc[1,['balance','income']]
# print(x1,x2)
# #euclidean distance between first and second data point
# print(np.linalg.norm(x1-x2))
#
# #example for limitation of euclidean distance
# t1=np.array([26,1000])
# t2=np.array([66,1000])
# t3=np.array([36,10000])
#
# print(np.linalg.norm(t3-t1))
# print(np.linalg.norm(t2-t3))
# #one attribute might have higher influence in the difference but ecludean distance doesnt capture that
#
# scalar=MinMaxScaler()
# scalar_values = scalar.fit_transform(data[['balance','income']])
# print(scalar_values)
# data['norm_balance'] = scalar_values[:,0]
# data['norm_income'] = scalar_values[:,1]
# print(data)
# x1=data.loc[0,['norm_balance','norm_income']]
# x2=data.loc[1,['norm_balance','norm_income']]
# print(np.linalg.norm(x1-x2))
#
#
#
# x11=data.loc[10,['norm_balance','norm_income']]
#
# # def distance_to_11(x):
# #     return np.linalg.norm(x-x11)
# # distance_to_unknown=data.loc[]
# distance_to_11=lambda x: np.linalg.norm(x-x11)
#
# print(data[['norm_balance','norm_income']])
# data['distanceto11']=data[['norm_balance','norm_income']].apply(distance_to_11,axis=1)
# print(data)


#take 2 building a K nearest neighbor using sklearn

#1: loading data
data=pd.read_csv('datasets/defaulter.csv')

#2: feature engineering - normalization
scalar=MinMaxScaler()
scalar_values=scalar.fit_transform(data[['balance','income']])

data['norm_balance']=scalar_values[:,0]
data['norm_income']=scalar_values[:,1]



#3:- find the normal distance of the unknown from other defaulters

x10=data.loc[10,['norm_balance','norm_income']]
distance_to_10=lambda x: np.linalg.norm(x-x10)

data['distanceto10']=data[['norm_balance','norm_income']].apply(distance_to_10,axis=1)
# print(data)
data.sort_values('distanceto10')
#4: split the dataset into test and train
x=data[['norm_balance','norm_income']]
y=data['defaulter']
# print(x.dtypes,y.dtypes)

xtrain,xtest,ytrain,ytest=train_test_split(x.values,y.values,test_size=0.3)

#4: build a model
model=KNeighborsClassifier(n_neighbors=3,metric="euclidean")
model.fit(xtrain,ytrain)

#5:- evaluate the performance
print(f'train accuracy: {model.score(xtrain,ytrain)} \n test accuracy: {model.score(xtest,ytest)}')

#6:- graph to visualize

test_accuracies = []
train_accuracies =[]

k_values= [i for i in range(1,8)]

print(xtrain,ytrain)
for k in k_values:
    model1=KNeighborsClassifier(n_neighbors=k)
    model1.fit(xtrain,ytrain)
    # train_predicty=model1.predict(xtrain)
    # test_predicty=model1.predict(xtest)
    test_predict=model1.score(xtest,ytest)
    train_predict=model1.score(xtrain,ytrain)
    test_accuracies.append(test_predict)
    train_accuracies.append(train_predict)

plt.plot(k_values,test_accuracies,label='test accuracy')
plt.plot(k_values,train_accuracies,label='train accuracy')
plt.legend()
plt.show()

