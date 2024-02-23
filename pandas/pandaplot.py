import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#converting horsepower column to int
data=pd.read_csv('datasets/auto-mpg.csv')
data['horsepower'].mask(data['horsepower']=='?',None,inplace=True)
data.dropna(inplace=True)
data['horsepower']=data['horsepower'].astype(int)
print(data.info())

#getting numerical columns
list1=[col for col in data.columns if data[col].dtype in ['float','int64','int32']]
# print(list1)
numeric_data=data[list1]

#the trend of acceleration in different years
numeric_data.plot(x='model year',y='acceleration', kind='scatter')

#mean acceleartion in different years
numeric_data.groupby('model year').mean()[['acceleration']].plot(kind='bar')

#frequency distribution of cylinder
numeric_data['cylinders'].plot(kind='hist')

#the relationship between weight and mpg
numeric_data.plot(x='weight',y='mpg',kind='scatter')

#bar plot to visulize sorted mean values of acceleration with respect to number of cylinders
numeric_data.groupby('cylinders').mean().sort_values('acceleration')[['acceleration']].plot(kind='bar')

numeric_data.ren

plt.show()