import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

time_studied=np.array([20,50,32,65,23,43,10,5,22,35,29,5,56])
scores=np.array([56,83,47,93,47,82,45,23,55,67,57,4,89])

model2=LinearRegression()
studied_train,studied_test,scores_train,scores_test=train_test_split(time_studied,scores,test_size=0.3)
model2.fit(studied_train,scores_train)

plt.scatter(studied_train,scores_train)
plt.plot(np.linspace(0,70,100),model2.predict(np.linspace(0,70,100)),'r')
print(model2.score(studied_test,scores_test))
print(model2.predict(np.array([55])))
plt.show()
