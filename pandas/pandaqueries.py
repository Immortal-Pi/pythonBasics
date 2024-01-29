import pandas as pd
import matplotlib.pyplot as plt


#read from a csv file
df=pd.read_csv('data2.csv',delimiter=',')
df.set_index('name',inplace=True)
print(df)
# df.to_csv('data2.csv',index=True)

# print(df.loc[df['age']>30])
print(df.loc[(df['age']>=30) & (df['height']>170),['ID','height','age']])

# df1=pd.read_excel('amruth universities.xlsx')
# print(df1['Universities Fall 2024'])
#
# dict=dict(df1)
# print(dict)