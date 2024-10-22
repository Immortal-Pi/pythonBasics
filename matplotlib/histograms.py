import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import pandas as pd


# mu, sigma= 172,8
# x=mu+sigma*np.random.randn(10000)
# # style.use('ggplot')
# plt.hist(x,100,color='blue',density=True)
# plt.xlabel('heights')
# plt.ylabel('Height of students')
# plt.title('heights of students')
# plt.text(150,0.04,"mu=172, sig=8")
# plt.grid()
# plt.show()


# mu,sigma=82,10
# x=mu+sigma*np.random.randn(10000)
# plt.xlabel('weight')
# plt.ylabel('deviation')
# plt.hist(x,100,density=True,color='gold')
# plt.xlabel('weight')
# plt.ylabel('deviation')
# plt.title('weights of student')
# plt.text(60,0.035,'mu=82,sig=10')
# plt.show()


data=pd.read_csv('datasets/auto-mpg.csv')

condition=data['horsepower']=='?'
data['horsepower']=data['horsepower'].mask(condition,None)
data.dropna(inplace=True)
print(data)

plt.hist(data['horsepower'],bins=20)
plt.ylabel('frequency',fontsize=10)
plt.xlabel('horsepower',fontsize=10)
plt.show()

