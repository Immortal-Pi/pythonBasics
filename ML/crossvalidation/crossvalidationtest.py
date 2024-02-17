import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns

data=pd.read_csv('datasets/default.csv')

scalar=MinMaxScaler()
scalar_values=scalar.fit_transform(data[['balance','income']])
data['norm_balance']=scalar_values[:,0]
data['norm_income']=scalar_values[:,1]

x=data[['norm_balance','norm_income']]
y=data['default']
print(x)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)
model=KNeighborsClassifier()

#cross validation using GridSearch
k_grid={'n_neighbors':np.arange(1,15,2)}
model_check=GridSearchCV(model,k_grid,return_train_score=True,verbose=1,scoring='accuracy')
model_check.fit(xtrain,ytrain)
df=pd.DataFrame(model_check.cv_results_)
print(df[['param_n_neighbors','mean_train_score','mean_test_score']])

model1=KNeighborsClassifier(n_neighbors=13,metric='euclidean')
model1.fit(xtrain,ytrain)
sns.pairplot(data,hue='default',x_vars='norm_balance',y_vars='norm_income',height=5)
plt.show()
print(f'test accuracy: {model1.score(xtest,ytest)} train accuracy: {model1.score(xtrain,ytrain)}')