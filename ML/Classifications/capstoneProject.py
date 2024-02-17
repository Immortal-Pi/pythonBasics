import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.neural_network import MLPClassifier
import seaborn as sns

data=pd.read_csv('datasets/HR_comma_sep.csv')
# print(data['left'])

#explore the datasets and check if the data can be used as-is
#check if null values are present because ML models dont accept null values
# print(data.isna())
# print(data.columns)

#Determine the relationship between satisfaction level and working hours of employees who left the organization

# sns.scatterplot(x=data['satisfaction_level'],y=data['average_montly_hours'],hue=data['left'])


#Understand the effect of satisfaction level, department, promotion in last 5 years and salary level of employees

#1 satisfaction level and left
f,ax=plt.subplots(1,4,figsize=(20,4))
sns.barplot(ax=ax[0],x=data['left'],y=data['satisfaction_level'])
# plt.show()

#2 department level and left
# f,ax=plt.subplots(figsize=(10,5))
sns.countplot(ax=ax[1],x=data['Department'],hue=data['left'],data=data)
# plt.show()

#3 promotion in last 5 years and left
sns.countplot(ax=ax[2],x=data['promotion_last_5years'],hue=data['left'],data=data)
# plt.show()

# salary level and left
sns.countplot(ax=ax[3], x=data['salary'],hue=data['left'],data=data)
plt.tight_layout()
# plt.show()


#build machine learning model and use it for prediction

#1 decision tree with random forest

data_x=pd.get_dummies(data[data.columns.drop('left')])

print(data_x.columns)
# transform and check if accuracy increases
scalar=StandardScaler()
data[['satisfaction_level_N','number_project_N']]=scalar.fit(data[['satisfaction_level','number_project']])
y=data['left']
data_x=pd.get_dummies(data[data.columns.drop(['left','satisfaction_level','number_project'])])
print(data_x.columns)
xtrain,xtest,ytrain,ytest=train_test_split(data_x,y,test_size=0.2,random_state=100)
model=RandomForestClassifier(n_estimators=10,min_samples_split=20,min_impurity_decrease=0.05)
model.fit(xtrain,ytrain)
data_features=pd.DataFrame(np.array([data_x.columns,model.feature_importances_]).T,columns=['feaures','importance'])
# print(data)
print(f'Random forest: test score {model.score(xtest,ytest)} train score {model.score(xtrain,ytrain)}')



#2 knn neighbors

x = pd.get_dummies(data[data.columns.drop('left')])
y=data['left']

scalar=StandardScaler()
data_x=scalar.fit_transform(x)
print(data_x)
xtrain,xtest,ytrain,ytest=train_test_split(data_x,y,test_size=0.2,random_state=100)

model=KNeighborsClassifier()

k_grid={'n_neighbors':np.arange(1,15,2)}

data_check=GridSearchCV(model,k_grid,return_train_score=True,verbose=1,scoring='accuracy')
data_check.fit(xtrain,ytrain)
df=pd.DataFrame(data_check.cv_results_)
print(df[['param_n_neighbors','mean_train_score','mean_test_score']])



#3 neural Network

x = pd.get_dummies(data[data.columns.drop('left')])
y=data['left']

scalar=StandardScaler()
data_x=scalar.fit_transform(x)
print(data_x)
xtrain,xtest,ytrain,ytest=train_test_split(data_x,y,test_size=0.2,random_state=100)
model=MLPClassifier(hidden_layer_sizes=(50))
model.fit(xtrain,ytrain)
print(model.score(xtrain,ytrain))







