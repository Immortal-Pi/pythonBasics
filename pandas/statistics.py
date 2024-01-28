import pandas as pd
import matplotlib.pyplot as plt

data={
    'ID':[22,34,54,66,55,12,50],
    'name':['Anna','bob','john','mike','amruth','akshath','sharath'],
    'age':[29,30,43,66,43,23,44],
    'height':[172,173,167,155,172,178,180],
    'gender':['f','m','f','m','m','m','m']

}


df=pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

#simple operations
# print(df['ID'].count())
# print(df.count())


#simple statistics operations
# print(df['height'].sum())
# print(df.sum())
print(df['height'].mean())
# print(df['height'].median())
print(df['height'].mode()) #most of the occurance
print(df['height'].std())

print(df['height'].min())

#describe - gives summary value
print(df.describe())