import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(50)
y=np.random.randn(50)

x1=[10,20,30,40,50]
y1=[90,60,20,50,10]
# plt.scatter(x,y,color='green')
plt.scatter(x,y,color='green',marker='x',s=100)
# plt.scatter(x1,y1,color='blue')
plt.show()