from sklearn import datasets
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
data = datasets.load_diabetes()


x=data.data
y=data.target

print(x)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
model=LinearRegression()
model.fit(xtrain,ytrain)

y_predict_test=model.predict(xtest)
print(f'coeffecient :{model.coef_} intercept:{model.intercept_}')
print(f'mean square: {mean_squared_error(ytest,y_predict_test)}')
print(f'coeff od determination R^2: {r2_score(ytest,y_predict_test)}')

# print(ytest,y_predict_test)
sns.scatterplot(data,x=ytest,y=y_predict_test,alpha=0.5)
# plt.scatter(,y_predict_test)
plt.show()