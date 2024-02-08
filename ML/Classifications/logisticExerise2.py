import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data=pd.read_csv('data_banknote_authentication.csv')
# print(data)
x=data[['variance','skewness','curtosis','entropy']]
y=data['class']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

model=LogisticRegression()
model.fit(xtrain,ytrain)
print(model.score(xtest,ytest))
ypredict=model.predict(xtest)
print(classification_report(ytest,ypredict))
