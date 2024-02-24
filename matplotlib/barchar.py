import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
import pandas as pd





# python = (85,67,23,98)
# java = (50,67,89,14)
# networking = (60,20,56,22)
# machine_learning = (88,23,10,87)
#
# people=['bob','ana','mark','john']
# style.use('dark_background')
# index = np.arange(4)
# # ax1=plt.subplot(221)
# # ax1.bar(people,python, width=0.2, label='Python',color='r')
# # ax2=plt.subplot(222)
# # ax2.bar(people,java, width=0.2, label='java',color='g')
# # ax3=plt.subplot(223)
# # ax3.bar(people,networking, width=0.2, label='networking',color='y')
# # ax4=plt.subplot(224)
# # ax4.bar(people,machine_learning, width=0.2, label='machine_learning',color='black')
# plt.bar(index,python,width=0.2,label='python')
# plt.bar(index+0.2,java,width=0.2,label='java')
# plt.bar(index+0.4,networking,width=0.2,label='networking')
# plt.bar(index+0.6,machine_learning,width=0.2,label='machine_learning')
# plt.ylabel('MARKS(100)')
# plt.xticks(index+0.2,people)
# plt.legend(loc='upper left')
# # plt.grid()
# plt.ylim(0,150) #limit of y axis

data=pd.read_csv('datasets/auto-mpg.csv')
data['horsepower']=data['horsepower'].mask(data['horsepower']=='?',None)
data.dropna(inplace=True)

fig=plt.figure(figsize=(7,5))
ax=fig.add_axes([0.1,0.1,0.8,0.8])
data2=data.groupby('model year').count()[['car name']]
data2.reset_index(inplace=True)
ax.bar(data2['model year'],data2['car name'])
ax.set_xlabel('number of cars')
ax.set_ylabel('model year')
plt.show()




plt.show()