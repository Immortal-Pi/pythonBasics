import json

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

df= pd.DataFrame(data)
df=df.set_index('name')
print(df,df.shape,df.dtypes)

#write dataframe object to any type of file
df.to_excel('data.xlsx',index=True)
df.to_csv('data2.csv',index=True)
df.to_json('data3.json')

#transpose of the dataframe
print(df.T)

#access individual columns of dataframe
# print(df['age'].iloc[1])
# print(df.iloc[0:2])


#plot the graph
# df.plot()
# df['age'].plot()
df.plot.bar()
plt.show()

