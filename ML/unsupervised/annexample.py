#get the test and train data
#plot the digits and check for values both test and train
#select features and precdictors
#predict the test data
#classification report

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report


data_train=pd.read_csv('datasets/mnist/train.csv')
data_test=pd.read_csv('datasets/mnist/test.csv')
print(data_train,data_test)

test_data1=np.asarray(data_test.iloc[0:1,:]).reshape(28,28)
train_data1=np.asarray(data_train.iloc[0:1,1:]).reshape(28,28)

# plt.subplot(1,2,1)
# plt.imshow(test_data1)
# plt.subplot(1,2,2)
# plt.imshow(train_data1)
# plt.show()

x=data_train.iloc[:,1:]
y=data_train.iloc[:,0]
model=MLPClassifier(hidden_layer_sizes=(50))
model.fit(x,y)
print(model.predict(data_test.iloc[5:6,:]))
plt.imshow(np.asarray(data_test.iloc[5:6,:]).reshape(28,28))
ypredict=model.predict(x)
print(classification_report(y,ypredict))
plt.show()