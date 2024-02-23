import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#create a dictionary

data={
    'ID':[22,34,54,66],
    'name':['Anna','bob','john','mike'],
    'age':[29,30,43,66],
    'height':[172,173,67,55],
    'gender':['f','m','f','m']

}

# df= pd.DataFrame(data)
# df=df.set_index('name')
# print(df,df.shape,df.dtypes)
#
# #write dataframe object to any type of file
# df.to_excel('data.xlsx',index=True)
# df.to_csv('data2.csv',index=True)
# df.to_json('data3.json')
#
# #transpose of the dataframe
# print(df.T)
#
# #access individual columns of dataframe
# # print(df['age'].iloc[1])
# # print(df.iloc[0:2])
#
#
# #plot the graph
# # df.plot()
# # df['age'].plot()
# df.plot.bar()
# plt.show()

#creating dataframes methods
#1single series object

# car_price_dict = {'Swift':  700000,
#                        'Jazz' :  800000,
#                        'Civic' : 1600000,
#                        'Altis' : 1800000,
#                        'Gallardo': 30000000
#                       }
# car=pd.Series(car_price_dict)
# data2=pd.DataFrame(car,columns=['car cost'])
# print(data2)


# data=pd.read_csv('data2.csv')
# print(data)
#
# #conditional filtering
# print(data.loc[data['gender']=='m'])
# #pandas and :- &
# #pandas or :- |
# print(data.loc[(data['gender']=='m') | (data['height'] > 170)])



marks = [{'Chemistry': 67, 'Physics': 45, 'Mathematics': 50, 'English' : 19},
        {'Chemistry': 90, 'Physics': 92, 'Mathematics': 87, 'English' : 90},
        {'Chemistry': 66, 'Physics': 72, 'Mathematics': 81, 'English' : 72},
        {'Chemistry': 32, 'Physics': 40, 'Mathematics': 12, 'English' : 68}]
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])

# marks_df['Results']=marks_df.loc

# condition=marks_df < 33
# marks_df.mask(condition,'Fail',inplace=True)
# print(marks_df)


#sorting by values
# marks_df.sort_values(by='English',inplace=True)
# print(marks_df)
# marks_df.sort_values(by=['Chemistry','English'],inplace=True,ascending=(0,1))
# print(marks_df)


# #encryption of dataframe object
# encrypt_data=np.sin(marks_df)
# print(encrypt_data)
#
# #resetting index
# index_reset=marks_df.reset_index()
# print(index_reset)


#broadcasting
# print(da)
# print(marks_df['Chemistry']+5)

#apply
# print(marks_df)
# print(marks_df.apply(np.sum,axis=1))
# print(marks_df.apply(np.sum,axis=0))



#Aggregation function
list1 = [col for col in marks_df.columns if marks_df[col].dtype in ['float', 'int64']]
#the above function is getting all the column names i.e. int and float because to use min and max i.e. mathematical function
print(list1)
print(marks_df.agg(['min','max']))
