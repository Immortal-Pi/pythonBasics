from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data =load_breast_cancer()

x=data.data
y=data.target
# print(x,y)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=23)

clf=SVC(kernel='linear',C=3)

clf2=KNeighborsClassifier(n_neighbors=3)
clf2.fit(xtrain,ytrain)
clf.fit(xtrain,ytrain)
print(f'SVC : {clf.score(xtest,ytest)}')
print(f'Kneighbour:{clf2.score(xtest,ytest)}')