import pandas as pd
import matplotlib.pyplot as  plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

data=pd.read_csv('kc_house_data.csv')
housedf=data[['price','date','bedrooms','bathrooms','sqft_living',  'floors', 'waterfront', 'view', 'condition', 'grade','zipcode' ]]


housedf['year']=np.array(housedf['date'].str[0:4],dtype=float)
housedf['month']=np.array(housedf['date'].str[4:6],dtype=float)

housedf=housedf.drop(columns=['date'])
print(housedf['year'].dtype)
# print(housedf)
x2=housedf[['bedrooms','bathrooms','sqft_living',  'floors', 'waterfront', 'view', 'condition', 'grade','zipcode']]
y2=housedf['price']
# print(x2.dtype)
# vif=pd.Series([variance_inflation_factor(x2.values,idx) for idx in range(x2.shape[1])],index=x2.columns)
# print(vif)


#categorical features
cat_features=['waterfront','view', 'condition', 'grade','zipcode','year','month']
housedf_catagories=pd.get_dummies(housedf,columns=cat_features)
# print(housedf_catagories.columns.values)

scalar=StandardScaler().fit(housedf[['price','bedrooms','bathrooms','sqft_living','floors']])
house_normalize=scalar.transform(housedf[['price','bedrooms','bathrooms','sqft_living', 'floors']])

# print(house_normalize)
# housedf_catagories_normalize_df = pd.DataFrame(housedf_catagories_normalize,columns=['waterfront','view', 'condition', 'grade','zipcode','year','month'])
# print(housedf_catagories_normalize_df)

housedf_normalize=pd.DataFrame(house_normalize,columns=['price','bedrooms','bathrooms','sqft_living', 'floors'])
# housedf_normalize=housedf_normalize.join(housedf_catagories)
housedf_normalize=housedf_normalize.join(housedf_catagories[housedf_catagories.columns.drop(['price','bedrooms','bathrooms','sqft_living', 'floors'])])
# print(housedf_normalize,housedf_catagories)

y=housedf_normalize['price']
x=housedf_normalize[housedf_normalize.columns.drop(['price'])]

# vif=pd.Series([variance_inflation_factor(x.values,idx) for idx in range(x.shape[1])],index=x2.columns)
# print(vif)
# print(x,y)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)

model1=LinearRegression()
model1.fit(xtrain,ytrain)

print(model1.score(xtrain,ytrain))
print(model1.score(xtest,ytest))

#root mean squared
predictionytest=model1.predict(xtest)
RMEStest= mean_squared_error(ytest,predictionytest)**0.5

predictionytrain=model1.predict(xtrain)
RMEStrain= mean_squared_error(ytrain,predictionytrain)**0.5
print(f'RMSE train: {RMEStrain}\n RMSE test: {RMEStest}')