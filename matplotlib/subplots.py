import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x=np.arange(10,1000,9)
# y=x**3+30+np.sin(x)
#
# fig, ([ax1,ax2],[ax3,ax4])= plt.subplots(2,2)
# ax1.plot(x,y,'b',label='line1')
#
# ax2.plot(x,y+2,'r',label='line2')
# ax3.plot(x,y*10,'y',label='line3')
# ax4.plot(x,y**20,'g',label='line4')
#
# plt.tight_layout()
# plt.show()


#plotting dataframe objects from
data=pd.read_csv('datasets/auto-mpg.csv')

condition=data['horsepower']=='?'
data['horsepower']=data['horsepower'].mask(condition,None)
data.dropna(inplace=True)
# print(data)

#boxplots
#Some customers of XYZ Custom Cars are interested in the mileage range of the cars that are restored by the company. They also want to compare the distribution of average mileage and city mileage (25% less than the average mileage).
fig=plt.figure(figsize=[6,6])
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# ax.boxplot(data['mpg'])
# plt.show()
data['city_mileage']=data['mpg']*0.75
ax.set_title('Distribution of Average MPG vs City MPG')
ax.set_ylabel('Mileage per gallon')
ax.boxplot([data['mpg'],data['city_mileage']])
plt.show()