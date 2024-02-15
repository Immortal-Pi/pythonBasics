import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report


data_train=pd.read_csv('datasets/mnist/train.csv')
data_test=pd.read_csv('datasets/mnist/test.csv')
# print(data_train)

train_data_digit=np.asarray(data_train.iloc[0:1,1:]).reshape(28,28)
test_data_digit=np.asarray(data_test.iloc[0:1,]).reshape(28,28)
# plt.subplot(1,2,1)
# plt.imshow(train_data_digit)
# plt.subplot(1,2,2)
# plt.imshow(test_data_digit)
# plt.show()
# plt.imshow(img)
# plt.show()


x=data_train.iloc[:,1:]
y=data_train.iloc[:,0:1]
# print(data_train.iloc[:,0])
model=MLPClassifier(hidden_layer_sizes=(50))
model.fit(x,data_train.iloc[:,0])

print(model.predict(data_test.iloc[1:2,:]))
plt.imshow(np.asarray(data_test.iloc[1:2,:]).reshape(28,28))
plt.show()
ypredict=model.predict(x)
print(classification_report(y,ypredict))