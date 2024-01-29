import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


name={
    'ID':[2,5,7,8],
    'name':['amruth','akshath','sharath','subhodh'],

}

ages={
    'ID':[2,5,17,18],
    'age':[22,26,24,25]
}

df1=pd.DataFrame(name)
df2=pd.DataFrame(ages)


df=pd.merge(df1,df2,on='ID',how='outer') #outer join
# df=pd.merge(df1,df2,on='ID',how='inner') #inner join
# df=pd.merge(df1,df2,on='ID',how='left')  #left join
# df=pd.merge(df1,df2,on='ID',how='right')   #right join
df.set_index('ID',inplace=True)
print(df)