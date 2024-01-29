import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

series= pd.Series([10,20,30,40,50],['A','B','C','D','E'])
series.name='myseries'
print(series)

# print(series.iloc[0]) #indexed int position, not posible in dictionary

# print(dict(series)) #convert panada object to dictionary

series2=pd.Series([30,40,20,1,5],['C','D','A','B','E'])
print(series+series2,series2.dtype)

# #first n rows
# print(series.head(3))
#
# #last n rows
# print(series.tail(4))

# functiony=lambda x:x**2
# #apply functions to these objects
# series2=functiony(series2)
#
# # series3=series2.sort_values()
# series2.sort_values(inplace=True)
# print(series2)
index=np.arange(5)

#normal 2d plot
# series2.plot()
# series.plot()


#bar graph plot
# series.plot.bar(index,width=0.2,label='series',color='green')
# series2.plot.bar(index+0.2,width=0.2,label='series2',color='red')

#pie chart
explode=[0,0,0.2,0,0]
series2.plot.pie(autopct='%.2f%%',explode=explode,shadow=True)

#hist plot
# series.plot.hist()

#export to sql server
# series.to_sql()

# print(series.to_json())
print(series.to_csv())
plt.legend(loc='upper left')
plt.show()