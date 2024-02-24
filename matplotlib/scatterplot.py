import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

# x=np.random.randn(50)
# y=np.random.randn(50)
#
# x1=[10,20,30,40,50]
# y1=[90,60,20,50,10]
# # plt.scatter(x,y,color='green')
# plt.scatter(x,y,color='green',marker='x',s=100)
# # plt.scatter(x1,y1,color='blue')
# plt.show()

#car mileage and horsepower
data=pd.read_csv('datasets/auto-mpg.csv')
data['horsepower']=data['horsepower'].mask(data['horsepower']=='?',None)
data.dropna(inplace=True)

#
fig=plt.figure(figsize=(12,5))
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_title("Scatter plot of Horsepower and Mileage based on Origin",fontsize=16)
ax.set_ylabel('Mileage per gallon',fontsize=12)
ax.set_xlabel('Horsepower',fontsize=12)

origin_list=data['origin'].unique()
color=cm.jet(np.linspace(0,1,len(origin_list)))
print(color)
# print(origin_list)

for color,origin in zip(color,origin_list):
    x=data[data['origin']==origin]['horsepower']
    y=data[data['origin']==origin]['mpg']
    plt.scatter(x,y,color=color,label=origin)

plt.legend()
plt.show()



# plt.show()