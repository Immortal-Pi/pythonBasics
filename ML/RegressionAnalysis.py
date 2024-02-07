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
print(housedata.shape,housedata.columns)
house_df = housedata[['price','date','bedrooms','bathrooms','sqft_living',  'floors', 'waterfront', 'view', 'condition', 'grade','zipcode' ]]
# print(house_df)


#split year and month from date considering price depends on year and month of sale
# bedrooms, bathrooms, floors, waterfront, view, condition, grade, year and month as categorical features

house_df.loc[:,'year']=housedata['date'].str[0:4]
house_df.loc[:,'month']=housedata['date'].str[4:6]
house_df=house_df.drop(columns=['date'])



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

# print(house_data_df_normalized)

y=house_data_df_normalized['price']
x=house_data_df_normalized[house_data_df_normalized.columns.drop('price')]
print(x,y)

#split test and train
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)

#build model

model=LinearRegression()
model.fit(xtrain,ytrain)

#test score and trained score
# print(model.score(xtrain,ytrain))
# print(model.score(xtest,ytest))


#evaluating model performance using RMSE

train_prediction=model.predict(xtrain)
train_RMSE=mean_squared_error(ytrain,train_prediction)**0.5

test_prediction=model.predict(xtest)
test_RMSE=mean_squared_error(ytest,test_prediction)**0.5

print(f'RMSE: \n train dataset: {train_RMSE}\n test dataset: {test_RMSE}')




