# Engineers at XYZ custom cars now want to create a machine learning model
# that can predict the mpg of any car that comes to their garage. MPG refers to Miles per gallon.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
#read
#mpg predict
#scalar transform


#read data from file

data=pd.read_csv('datasets/auto-mpg.csv')
print(data.info())

#remove null values and other data
data['horsepower']=data['horsepower'].mask(data['horsepower']=='?',None)
data.dropna(inplace=True)
data['horsepower']=data['horsepower'].astype(int)
print(data.info())

#predictors and target values
x=data.iloc[:,1:7]
y=data.iloc[:,0:1]
print(y)


#split the data train and test
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=2)


#standardize the data
transform=StandardScaler()
xtrain=transform.fit_transform(xtrain)
xtest=transform.transform(xtest)
# print(xtrain,xtest)


#fit the model
model=LinearRegression()
model.fit(xtrain,ytrain)
print(f'm=:{model.coef_}  c={model.intercept_}')
# print(model.score(xtest,ytest))




y_predict_train=model.predict(xtrain)
y_predict_test=model.predict(xtest)
print(f'train accuracy={r2_score(ytrain,y_predict_train)}')
print(f'test accuracy={r2_score(ytest,y_predict_test)}')




