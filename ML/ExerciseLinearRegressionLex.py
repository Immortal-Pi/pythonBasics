import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


data=pd.read_csv('boston_housing.csv')
# print(data)
data=pd.DataFrame(data)
x=data[['RM']]
y=data.MEDV
# print(x,y)


plt.scatter(x,y,c='g',label='plot1')

model=LinearRegression()
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.33)
model.fit(xtrain,ytrain)
print(f'intercept: {model.intercept_} , coefficient:{model.coef_}')
# print(model.score(xtest,ytest))

#calculate mean square error
#c=y-mx
y_prediction1=pd.DataFrame((model.coef_*xtest) + model.intercept_)
data['y_prediction1']=y_prediction1

#prediction without using y=mx+C
y_prediction2=model.predict(xtest)


data['Error']=data.y_prediction1-data.MEDV
print(data)
print(model.score(xtest,y_prediction1))
# plt.plot(xtest,y_prediction1,c='r',label='prediction1')
# plt.plot(xtest,y_prediction2,c='g',label='prediction2')
# mse=mean_squared_error(ytest,y_prediction)
# print(f'mean square error: {mse}')
# print(error)

#calculate R squared method
# print(model.score(xtrain,ytrain))
# print(model.score(xtest,ytest))
# print(model.score(xtest,y_prediction))

plt.title('BOSTON Housing Data')
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.tight_layout()
plt.legend()
plt.show()
