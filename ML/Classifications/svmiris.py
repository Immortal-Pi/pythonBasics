import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions


data=pd.read_csv('datasets/iris.csv')

#creating a new column for distinguish versicolor species from rest
versicolor_yn = lambda x: 0 if x=='versicolor' else 1

data['versicolor_yn']=data['Species'].apply(versicolor_yn)
print(data)
sns.pairplot(data,hue='versicolor_yn',x_vars='Sepal.Length',y_vars='Sepal.Width',height=5)
# plt.show()

x=data[['Petal.Length','Petal.Width']]
y=data['versicolor_yn']
model=SVC()
model.fit(x,y)
model.score(x,y)

#model visualization
features=np.array(x)
target=np.array(y).ravel()
# plot_decision_regions(features,target,clf=model)
plt.show()