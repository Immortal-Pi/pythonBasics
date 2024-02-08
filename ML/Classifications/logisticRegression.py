import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression





data=pd.read_csv('chd_data.csv')
print(data)

#chd =0 - absence of heart disease
#chd =1 - presence of heart disease

plt.scatter(data['age'],data['chd'],c='r')
plt.xlabel('age')
plt.ylabel('chd')

#building a model
x=data[['age']]
y=data['chd']


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=0)

model=LogisticRegression()
model.fit(xtrain,ytrain)

print(f'intercept: {model.intercept_}  coefficient: {model.coef_}')
print(f'accuracy of train data score: {model.score(xtrain,ytrain)}')
print(f'accuracy of test data score: {model.score(xtest,ytest)}')

#sample age 29
test=pd.DataFrame([29])
print(f'prediction for age 29(probability range): {model.predict_proba(test)}')
print(f'prediction choice : {model.predict(test)}')





# plt.show()

