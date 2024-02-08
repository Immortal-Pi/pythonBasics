import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


#using Linear Regression Formulas

data=pd.read_csv('computers.csv')

x=data.Units
y=data.Minutes
x_mean=x.mean()
y_mean=y.mean()
n=len(data)

#y=mx+c
numerator= (x*y).sum() -n*x_mean*y_mean
denominator= (x**2).sum() - n*x_mean**2
m=numerator/denominator
c=y_mean-m*x_mean

bestfitmodel=m*x+c
# print(bestfitmodel-y)
print(f"intercept: {c}, coefficient: {m}")


# SST=SSR-SSE
SST=sum((y-y_mean)**2)
SSE=sum((bestfitmodel-y)**2)
SSR=SST-SSE
print(SSR/SST)



#using LinearRegression Library
model=LinearRegression()
x1=data[['Units']]
y1=data['Minutes']

x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.3)
model.fit(x1_train,y1_train)
print(f'intercept: {model.intercept_}, coefficient:{model.coef_}')
print(model.score(x1_test,y1_test))
