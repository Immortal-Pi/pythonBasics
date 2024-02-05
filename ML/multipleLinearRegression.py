import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

data=pd.read_csv('delivery.csv')
# print(data)
# print(data.info())
# sns.pairplot(data)
# plt.tight_layout()

x=data[['n.prod','distance']]
y=data['delTime']

model=LinearRegression()
model.fit(x,y)
# print(f'intercept: {model.intercept_},coefficient: {model.coef_}')
predicted_model=pd.DataFrame(model.intercept_+ model.coef_[0]*data['n.prod']+model.coef_[1]*data['distance'])
# print(predicted_model)
# print(data['delTime'])

x_mesh=np.arange(data['n.prod'].min(),data['n.prod'].max(),1)
y_mesh=np.arange(data['distance'].min(),data['distance'].max(),1)

x_mesh,y_mesh=np.meshgrid(x_mesh,y_mesh)

XY_mesh=pd.DataFrame({
    'n.prod':x_mesh.ravel(),'distance':y_mesh.ravel()
})

out=model.predict(XY_mesh)
# print(predicted_model)
z=np.arange(predicted_model[0].min(),predicted_model[0].max(),1)

ax=plt.axes(projection='3d')
ax.scatter(xs=data['n.prod'],ys=data['distance'],zs=data['delTime'],alpha=1,c='b')
ax.plot_surface(x_mesh,y_mesh,out.reshape(x_mesh.shape),alpha=0.5,label='model',color='green')
ax.scatter(xs=data['n.prod'],ys=data['distance'],zs=predicted_model,alpha=1,c='r',label='formula')
# ax.plot_surface(x_mesh,y_mesh,z.ravel().reshape(x_mesh.shape),alpha=0.5,color='green')
# plt.legend()
# plt.show()


#correletaion beteen n.prod and distance
print(f"correlation:\n{np.corrcoef(data['n.prod'],data['distance'])}")

#variance inflation factor
vif=pd.Series([variance_inflation_factor(x.values,idx) for idx in range(x.shape[1])],index=x.columns)

print(f'\nvif:\n {vif}')


