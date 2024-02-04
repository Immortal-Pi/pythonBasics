import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns


data=pd.read_csv('delivery.csv')
# print(data)
# print(data.info())
# sns.pairplot(data)
# plt.tight_layout()
plt.show()

x=data[['n.prod','distance']]
y=data['delTime']

model=LinearRegression()
model.fit(x,y)
print(f'intercept: {model.intercept_}, coeffecient: {model.coef_}')

ax1=plt.axes(projection='3d')
ax1.scatter(xs=data['n.prod'],ys=data['distance'],zs=data['delTime'],c='blue',marker='o')
ax1.set_xlabel('n.prod')
ax1.set_ylabel('distance')
ax1.set_zlabel('delayTime')


#create a meshgrid
x_surf=np.arange(data['n.prod'].min(),data['n.prod'].max(),1)
y_surf=np.arange(data['distance'].min(),data['distance'].max(),1)
x_surf,y_surf=np.meshgrid(x_surf,y_surf)

X_mesh=pd.DataFrame({'n.prod':x_surf.ravel(),'distance':y_surf.ravel()})

out=model.predict(X_mesh)

ax1.plot_surface(x_surf,y_surf,out.reshape(x_surf.shape),alpha=0.5)


# ax1.plot()
plt.show()