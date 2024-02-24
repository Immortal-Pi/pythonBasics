import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1 Import the data into Python environment as a Pandas DataFrame.
data=pd.read_csv('datasets/rainfall1627650742214.csv')

#2 Check for missing values, if any and drop the corresponding rows.

data.dropna(inplace=True) #looks like no missing values
print(data.info())

#3 Find the district that gets the highest annual rainfall.
numerical_col_list=[col for col in data.columns if data[col].dtype in ['float64','int']]
numerical_data=data[numerical_col_list]

district_rainfall=data.groupby('DISTRICT').agg({'ANNUAL':['max']})
district_rainfall.columns=['max']
district_rainfall.reset_index(inplace=True)
district_rainfall.sort_values('max',ascending=False,inplace=True)
print(district_rainfall) #answer - TAMENGLONG

#4 Display the top 5 states that get the highest annual rainfall
print(district_rainfall.head(5))

#5 Drop the columns 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'
print(data.columns)
# data2=data.drop(columns=['Jan-Feb','Mar-May', 'Jun-Sep', 'Oct-Dec'])

#6 Display the state-wise mean rainfall for all the months using a pivot table
data3=data.pivot_table(numerical_data,index='STATE_UT_NAME',aggfunc=np.mean)
# print(data3)
#below method a little to complex, above command better
data4=data.groupby('STATE_UT_NAME',as_index=True).agg({f'{col}':['mean'] for col in numerical_data})
# print(data4)

#7 count of dictricts in each state
data5=data.groupby(by='STATE_UT_NAME')['DISTRICT'].count().sort_values(ascending=False)
# print(data5)

#8 For each state, display the district that gets the highest rainfall in May. Also display the recorded rainfall
data6=data.groupby('DISTRICT',as_index=True).agg({'MAY':['max']})
data6.columns=['MAY']

print(data6.sort_values(by='MAY',ascending=False))
