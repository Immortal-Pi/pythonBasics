import pandas as pd
import matplotlib.pyplot as  plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

data=pd.read_csv('boston_housing.csv')
# print(data)
data1=pd.read_csv('delivery2.csv')
#predictors RM,DIS,TAX,INDUS
#target #MEDV

data_predictors=data[['RM','DIS','TAX','INDUS']]
data_target=data['MEDV']

# print(data_predictors)
vif1=pd.DataFrame()
vif1['features']=data_predictors.columns
vif1['vif']=[variance_inflation_factor(data_predictors.values,x) for x in range(len(data_predictors.columns))]
print(vif1)
# vif=pd.Series([variance_inflation_factor(data_predictors.values,idx) for idx in range(data_predictors.shape[1])],index=data_predictors.columns)
# print(vif)
# print(data1)
# x=data1[['rel','track','n.prod','distance']]
# y=data1['delTime']
# vif=pd.Series([variance_inflation_factor(x.values,idx) for idx in range(x.shape[1])],index=x.columns)
# print(f'\nvif:\n {vif}')

#high corellation
# print(np.corrcoef(data['TAX'],data['INDUS']))
data_predictors.drop(columns=['INDUS','TAX'],inplace=True)
# fig=plt.axes(projection='3d')
plt.scatter(data['RM'],data['MEDV'],c='b',label='DIS vs MEDV')
plt.scatter(data['DIS'],data['MEDV'],c='g',label='INDUS vs MEDV')
plt.xlabel('DIS/INDUS')
plt.ylabel('MEDV')
plt.legend()

x=data_predictors
# print(x)
y=data_target
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(xtrain,ytrain)

print(model.intercept_,model.coef_)
print(f'test score: {model.score(xtest,ytest)}')
print(f'train score: {model.score(xtrain,ytrain)}')
ypredicttrain=model.predict(xtrain)
ypredicttest=model.predict(xtest)
print(f'test RMSE: {mean_squared_error(ypredicttest,ytest)**0.5}')
print(f'train RMSE: {mean_squared_error(ypredicttrain,ytrain)**0.5}')

adjusted_scoretest= 1-(1-model.score(xtest,ytest))*(len(y)-1)/(len(y)-len(x.shape)-1)
adjusted_scoretrain= 1-(1-model.score(xtrain,ytrain))*(len(y)-1)/(len(y)-len(x.shape)-1)
print(f'adjusted score model test:{adjusted_scoretest}')
print(f'adjusted score model train:{adjusted_scoretrain}')
plt.show()