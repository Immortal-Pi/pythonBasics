import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions

# encoding the species column
data=pd.read_csv('datasets/iris.csv')
print(data['Species'].values)

# #single class classification
#
# change_species=lambda x: 1 if x=='versicolor' else 0
#
# data['Species']= data['Species'].apply(change_species)
# print(data)
#
# x=data[['Petal.Length','Petal.Width']]
# y=data['Species']
#
# sns.pairplot(data,hue='Species',x_vars='Petal.Length',y_vars='Petal.Width',height=5)
# model1=SVC()
# model1.fit(x,y)
#
# feature=np.array(x)
# target=np.array(y)
# plot_decision_regions(feature,target,clf=model1)
# plt.legend()
# # plt.show()

#multi class classification

change_species1= lambda x: 0 if x=='setosa' else (1 if x=='versicolor' else 2)

data['Species']=data['Species'].apply(change_species1)

x=data[['Petal.Length','Petal.Width']]
y=data['Species']
# sns.pairplot(data,hue='Species',x_vars='Petal.Length',y_vars='Petal.Width',height=5)
# plt.show()
model2=SVC()
model2.fit(x,y)

plot_decision_regions(np.array(x),np.array(y),clf=model2)
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Width')
plt.legend()
plt.show()

