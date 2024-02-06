import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
data=pd.read_csv('delivery.csv')
# print(data)
# print(data.info())
# sns.pairplot(data)
# plt.tight_layout()

x=data[['n.prod','distance']]
y=data['delTime']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
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

# this explains that R^2(coeffecient of determination) value is in inflated when predictor values increase
#model with single predictor - n.prod

x1=data[['n.prod']]
y1=data['delTime']
model1=LinearRegression()
x1train,x1test,y1train,y1test=train_test_split(x1,y1,test_size=0.2,random_state=2)
model1.fit(x1,y1)
print(model1.score(x1test,y1test))
print(f'R^2 with 1 predictors:{model1.score(x1test,y1test)}')


#model with multiple predictor - n.prod, distance
x2=data[['n.prod','distance']]
y2=data['delTime']
x2train,x2test,y2train,y2test=train_test_split(x2,y2,test_size=0.2,random_state=5)
model2=LinearRegression()
model2.fit(x2train,y2train)
print(f'R^2 with 2 predictors:{model2.score(x2test,y2test)}')


#model with adjusted R for multiple predictor -n.prod, distance
adjusted_rscore_model2= 1-(1-model2.score(x2,y2))*(len(y2)-1)/(len(y2)-x2.shape[1]-1)
adjusted_rscore_model1= 1-(1-model1.score(x1,y1))*(len(y1)-1)/(len(y1)-x1.shape[1]-1)

print(f'adjusted R^2 model1: {adjusted_rscore_model1}\nadjusted R^2 model2: {adjusted_rscore_model2}')



#catogorical variables
#if the column variables are qualitative values and like a label :- catogorical variables

view= pd.DataFrame(
    {
        'apartmentName':['galleria','RMZ','shoba','123'],
        'view':[1,2,3,4],
        'location':['bangalore','chennai','hebbal','yelanka']
    }
)
view_index=pd.get_dummies(view['view'])
print(view_index)