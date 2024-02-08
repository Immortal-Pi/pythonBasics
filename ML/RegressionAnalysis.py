import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housedata=pd.read_csv('kc_house_data.csv')
# print(housedata.shape,housedata.columns)
house_df = housedata[['price','date','bedrooms','bathrooms','sqft_living',  'floors', 'waterfront', 'view', 'condition', 'grade','zipcode' ]]
# print(house_df)


#split year and month from date considering price depends on year and month of sale
# bedrooms, bathrooms, floors, waterfront, view, condition, grade, year and month as categorical features

house_df.loc[:,'year']=housedata['date'].str[0:4]
house_df.loc[:,'month']=housedata['date'].str[4:6]
house_df1=house_df=house_df.drop(columns=['date'])
# print(house_df.columns.values)



#encoding the categorical features
cat_features= ['waterfront','view','condition','grade','year','month','zipcode']

house_df = pd.get_dummies(house_df,columns=cat_features)
# print(house_df.columns)

#normalizing the contunous numerical features
scalar=StandardScaler().fit(house_df[['price','bedrooms','bathrooms','sqft_living','floors']])

house_data_normalized = scalar.transform(house_df[['price','bedrooms','bathrooms','sqft_living','floors']])
# print(house_data_normalized)

house_data_df_normalized= pd.DataFrame(house_data_normalized,columns=['price','bedrooms','bathrooms','sqft_living','floors'])
house_data_df_normalized=house_data_df_normalized.join(house_df[house_df.columns.drop(['price','bedrooms','bathrooms','sqft_living','floors'])])

print(house_data_df_normalized)

y=house_data_df_normalized['price']
x=house_data_df_normalized[house_data_df_normalized.columns.drop('price')]
print(x.columns.values)
y1=house_df1['price']
x1=house_df1[['bedrooms','bathrooms','sqft_living','floors']]

# print(x1,y1)
# print(x,y)

#split test and train
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)
x1train,x1test,y1train,y1test=train_test_split(x1,y1,test_size=0.2,random_state=100)
#build model

model=LinearRegression()
model.fit(xtrain,ytrain)

model1=LinearRegression()
model1.fit(x1train,y1train)

#test score and trained score
print(model1.score(x1train,y1train))
print(model1.score(x1test,y1test))
adjusted_score= 1-(1-model.score(xtest,ytest))*(len(y)-1)/(len(y)-x.shape[1]-1)
adjusted_score1= 1-(1-model1.score(x1test,y1test))*(len(y1)-1)/(len(y1)-x1.shape[1]-1)
print(f'adjusted score model 1:{adjusted_score}')
print(f'adjusted score model 2:{adjusted_score1}')

#evaluating model performance using RMSE

train_prediction=model.predict(xtrain)
train_RMSE=mean_squared_error(ytrain,train_prediction)**0.5
train_prediction1=model1.predict(x1train)
train_RMSE1=mean_squared_error(y1train,train_prediction)**0.5

test_prediction=model.predict(xtest)
test_RMSE=mean_squared_error(ytest,test_prediction)**0.5
test_prediction1=model1.predict(x1test)
test_RMSE1=mean_squared_error(y1test,test_prediction)**0.5

print(f'RMSE: \n train dataset: {train_RMSE}\n test dataset: {test_RMSE}')
print(f'RMSE: \n train dataset 1: {train_RMSE1}\n test dataset:1 {test_RMSE1}')




