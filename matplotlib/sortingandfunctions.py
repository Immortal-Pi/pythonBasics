import numpy as np
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
df.set_index('ID',inplace=True)
print(df['height'].apply(lambda x:x/2))

# for k,v in df['age'].items():
#     print('{}:{}'.format(k,v))

for k,v in df.items():
    print('{}:{}'.format(k,v))

#different from keys
for row in df.iterrows():
    print(row)

# print(df.sort_index())

print(df.sort_values('age'))
df.sort_values(by=['age','name'],inplace=True)
print(df)