import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

data=pd.read_csv('datasets/mnist_data.csv')

image1=np.asarray(data.iloc[5:6,:]).reshape(28,28)
# plt.imshow(image1)
# plt.show()

model1=KMeans(n_clusters=10)
model1.fit(data)

print(model1.labels_)

cluster1=data[model1.labels_==0]
cluster1_img=cluster1.iloc[[np.random.randint(0, cluster1.shape[0]) for i in range(0,5)]]

for i in range(0,cluster1_img.shape[0]):
    plt.subplot(1,5,i+1)
    images=np.asarray(cluster1_img[i:i+1]).reshape(28,28)
    plt.imshow(images)

plt.show()
