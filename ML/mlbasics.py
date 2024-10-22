import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd


# time_studied=np.array([20,50,32,65,23,43,10,5,22,35,29,5,56]).reshape(-1,1)
# scores=np.array([56,83,47,93,47,82,45,23,55,67,57,4,89]).reshape(-1,1)
#
# # print(scores)
#
# model = LinearRegression()
# model.fit(time_studied,scores)

# plt.scatter(time_studied,scores)
# plt.plot(np.linspace(0,70,100).reshape(-1,1),model.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
# plt.ylim(0,100)
#
# #predict by giving user input
# print(model.predict(np.array(55).reshape(-1,1)))
# plt.show()


#train the model using 80% data to test the rest 20%
#test_size=0.2 is 20%
# time_train,time_test,score_train,score_test=train_test_split(time_studied,scores,test_size=0.3)
# model1=LinearRegression()
# model1.fit(time_train,score_train)
#
# print(model1.score(time_test,score_test))
# plt.scatter(time_train,score_train)
# plt.plot(np.linspace(0,70,100).reshape(-1,1),model1.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
# plt.show()

# studied_train,studied_test,scores_train,scores_test=train_test_split(time_studied,scores,test_size=0.3)
# model1=LinearRegression()
# model1.fit(studied_train,scores_train)
#
# plt.scatter(studied_train,scores_train)
# plt.plot(np.linspace(0,70,100).reshape(-1,1),model1.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
# # print(model1.predict(np.array([55]).reshape(-1,1)))
# print(model1.score(studied_test,scores_test))
# plt.show()

# time_studied=np.array([20,50,32,65,23,43,10,5,22,35,29,5,56])
# scores=np.array([56,83,47,93,47,82,45,23,55,67,57,4,89])
#
# model2=LinearRegression()
# studied_train,studied_test,scores_train,scores_test=train_test_split(time_studied,scores,test_size=0.3)
# model2.fit(studied_train,scores_train)
#
# plt.scatter(studied_train,scores_train)
# plt.plot(np.linspace(0,70,100),model2.predict(np.linspace(0,70,100)),'r')
# print(model2.score(studied_test,scores_test))
# print(model2.predict(np.array([55])))
# plt.show()


data= pd.read_csv('computers.csv')

model1=data['Minutes'].mean()
model2=10+12*data['Units']
model3=6+18*data['Units']

# print(model1,model2,model3)

fig,ax1=plt.subplots()
ax1.scatter(x='Units',y='Minutes',data=data,label='actual repair time')

ax1.plot(data['Units'],model2,c='b',label='model2')
ax1.plot(data['Units'],model3,c='g',label='model3')




datamodule1=pd.DataFrame(
    {
        'Units':data['Units'],
        'Actual_time':data['Minutes'],
        'predicted_time':model1,
        'Error':(model1-data['Minutes'])
    }
)
print(sum(datamodule1['Error']**2))
# print(datamodule1)


datamodule2=pd.DataFrame(
    {
        'Units':data['Units'],
        'Actual_time':data['Minutes'],
        'predicted_time':model2,
        'Error':(model2-data['Minutes'])
    }
)
print(sum(datamodule2['Error']**2))
# print(datamodule2)


datamodule3=pd.DataFrame(
    {
        'Units':data['Units'],
        'Actual_time':data['Minutes'],
        'predicted_time':model3,
        'Error':(model3-data['Minutes'])
    }
)
print(sum(datamodule3['Error']**2))
# print(datamodule3)


#we find the best model by theortital

x=data.Units
y=data.Minutes
xiyi=x*y
n=len(data)
xmean=x.mean()
ymean=y.mean()

numerator=xiyi.sum()-n*xmean*ymean
denominator= (x**2).sum() - n*(xmean**2)

m=numerator/denominator

c=ymean-(m*xmean)
print(f"intercept: {c} coefficient: {m}")

minutes_best_fit_model=c+m*data['Units']
data['bestfitmodel']=minutes_best_fit_model

# print(data)

databestfitmodel=pd.DataFrame(
    {
        'Units':data['Units'],
        'Actual_time':data['Minutes'],
        'predicted_time':data['bestfitmodel'],
        'Error':(data['bestfitmodel']-data['Minutes'])
    }
)
# print(databestfitmodel)


ax1.plot(data['Units'],data['bestfitmodel'],c='r',label='bestfit model')



ax1.legend()
ax1.set_xlabel('UNITS')
ax1.set_ylabel('MINUTES')
ax1.set_title('Speculated Module')

# SST=SSR=SSE
#with using Linear Regression formulas
SST=sum((data.Minutes-data.Minutes.mean())**2)
SSE=sum(databestfitmodel.Error**2)
SSR=SST-SSE
print(SSR)
Rsq=SSR/SST
print(Rsq)



#using Linear Regression
data1=LinearRegression()
data1.fit(data[["Units"]],data['Minutes'])
print(data1.score(data[['Units']],y))
# plt.show()

