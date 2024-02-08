import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
data=pd.read_csv('bank-additional-full.csv')
# print(data)

x=data[['duration','age','campaign']]
y=data['y']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)

#dummies

model=LogisticRegression()
model.fit(xtrain,ytrain)
print(f'test accuracy:{model.score(xtest,ytest)}')
print(f'train accuracy :{model.score(xtrain,ytrain)}')

prediction_test=model.predict(xtest)
prediction_train=model.predict(xtrain)

testConfusionMatrix=confusion_matrix(ytest,prediction_test)
trainConfusionMatrix=confusion_matrix(ytrain,prediction_train)
print(testConfusionMatrix,trainConfusionMatrix)

test_accuracy=(testConfusionMatrix[0][0]+testConfusionMatrix[1][1])/testConfusionMatrix.sum()
print(f'test accuracy confusion :{test_accuracy}')
train_accuracy=(trainConfusionMatrix[0][0]+trainConfusionMatrix[1][1])/trainConfusionMatrix.sum()
print(f'train accuracy confusion :{train_accuracy}')





