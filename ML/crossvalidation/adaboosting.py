import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


data=pd.read_csv('datasets/spambase.csv')
print(data)

x=data[data.columns.drop('spam')]
y=data['spam']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100)
model1=AdaBoostClassifier(n_estimators=10)
model1.fit(xtrain,ytrain)

print(f'test accuracy: {model1.score(xtest,ytest)}  train accuracy : {model1.score(xtrain,ytrain)}')

df=pd.DataFrame(np.array([x.columns,model1.feature_importances_]).T, columns=['features','importance'])
# print(df.sort_values(by='importance',ascending=False))
print(df.query('importance>0'))