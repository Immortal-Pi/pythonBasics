import pandas as pd
import numpy as np

data=pd.read_csv('datasets/auto-mpg.csv')
# print(data)
data['horsepower'].mask(data['horsepower']=='?',None,inplace=True)
data.dropna(inplace=True)
#min and max of all numerical values
#aggregate function
list1=[col for col in data.columns if data[col].dtype in ['float','int64']]
# print(list1)

numerical_data=data[list1]
# print(numerical_data.agg(['max','min'],axis=0))
data['horsepower']=data['horsepower'].astype(int)
# print(data.info())
# print(numerical_data.columns,data.columns)
#
# # #groupby operation
# # print(data.groupby(['model year']).count()['car name'])
#
# print(data)
# #group by and aggregation
# data2=data.groupby(['cylinders','model year']).agg({'horsepower':['mean','min','max']})
# # print(data2)
# data2.columns=['hpmean','hpmin','hpmax']
# data2=data2.reset_index()
# print(data2)
#
# print(data.groupby(['model year']).agg({'acceleration':['mean']}))

#frequency distribution
freq=pd.crosstab(data['model year'],data['cylinders'])
print(freq)


#pivot table

data2=pd.pivot_table(numerical_data,index='model year',aggfunc=np.mean)
data3=numerical_data.groupby(['model year'],as_index=False).agg(['mean'])
# data3.columns=numerical_data.columns
# data3= d  .groupby(['model year']).agg({[f'{numerical_data.columns}':['mean']})
print(data2,'\n',data3)
# print(data3.columns)
