import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score,classification_report



train_data=pd.read_csv('datasets/mnist/train.csv')
test_data=pd.read_csv('datasets/mnist/test.csv')


x_train=train_data.iloc[:,1:]
y_train=train_data.iloc[:,0]


# print(x_train)
# print(y_train)

model=MLPClassifier(hidden_layer_sizes=(50))
model.fit(x_train,y_train)

y_train_prediction=model.predict(x_train)
y_test_prediction=model.predict(test_data)

print(y_train_prediction,y_test_prediction)
# print(y_train_prediction)
print(f'train accuracy: {r2_score(x_train,y_train_prediction)}')
# print(classification_report(test_data,y_test_prediction))
