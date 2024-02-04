from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data =load_wine()

xtrain,xtest,ytrain,ytest=train_test_split(data.data,data.target,test_size=0.3)

clf1=KNeighborsClassifier(n_neighbors=3)
clf2=SVC(kernel='linear',C=3)

clf1.fit(xtrain,ytrain)
clf2.fit(xtrain,ytrain)

print(f'Kneighbor:{clf1.score(xtest,ytest)}\n SVC:{clf2.score(xtest,ytest)}')
