import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data= pd.read_csv('computers.csv')
x=data['Units']
# print(x)
y=data['Minutes']

#Using Linear Regression formulas
x_mean=x.mean()
y_mean=y.mean()
xiyi=x*y
n=len(data)
numerator=xiyi.sum()-n*x_mean*y_mean
denominator=(x**2).sum() - n*(x_mean**2)

# print(numerator/denominator)
m=numerator/denominator
#y=mx+c
c=y_mean-(m*x_mean)
bestfitmodel=m*x+c
print(bestfitmodel-y)
print(f"intercept: {c}, coefficient: {m}")

# SST=SSR+SSE
SST=sum((y-y_mean)**2)
SSE=sum((bestfitmodel-y)**2)

SSR=SST-SSE
print(SSR/SST)


#using Linear Regression Library
x1=data[['Units']]
y1=data['Minutes']
model=LinearRegression()


x1train,x1test,y1train,y1test=train_test_split(x1,y1,test_size=0.3)
model.fit(x1train,y1train)
print(model.coef_,model.intercept_)
print(model.score(x1test,y1test))




# model=LinearRegression()
# model.fit(x,y)
# print(model.intercept_,model.coef_)


#lets includ
