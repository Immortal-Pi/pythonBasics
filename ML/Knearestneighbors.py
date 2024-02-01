from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np

data=load_wine()
print(data.feature_names)
print(data.target_names)

xtrain,xtest,ytrain,ytest=train_test_split(np.array(data.data),np.array(data.target),test_size=0.3)

clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(xtrain,ytrain)
print(clf.score(xtest,ytest))


