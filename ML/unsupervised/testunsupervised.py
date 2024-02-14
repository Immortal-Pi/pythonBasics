import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

data=pd.read_csv('datasets/mnist_data.csv')

image1=np.asarray(data.iloc[0:1,:]).reshape(28,28)

model=KMeans(n_clusters=30)
model.fit(data)

cluster1=data[model.labels_==0]

# cluster1_img=cluster1.iloc[[np.random.randint(0,cluster1.shape[0]) for i in range(0,5)]]
#
# for i in range(0,cluster1_img.shape[0]):
#     plt.subplot(1,5,i+1)
#     image2=np.asarray(cluster1_img[i:i+1]).reshape(28,28)
#     plt.imshow(image2)
#



# cluster2=data[model.labels_==1]
#
# cluster2_img=cluster2.iloc[[np.random.randint(0,cluster1.shape[0]) for i in range(0,5)]]
#
# for i in range(0,cluster2_img.shape[0]):
#     plt.subplot(1,5,i+1)
#     image=np.asarray(cluster2_img[i:i+1]).reshape(28,28)
#     plt.imshow(image)
#
# plt.show()

# cluster3=data[model.labels_==2]
# cluster3_img=cluster3.iloc[[np.random.randint(0,cluster3.shape[0]) for i in range(0,5)]]
#
# for i in range(0,cluster3_img.shape[0]):
#     plt.subplot(1,5,i+1)
#     im=np.asarray(cluster3_img[i:i+1]).reshape(28,28)
#     plt.imshow(im)
#
# plt.show()

cluster4=data[model.labels_==3]
cluster4_img=cluster4.iloc[[np.random.randint(0,cluster4.shape[0]) for i in range(0,5)]]

for i in range(0,cluster4_img.shape[0]):
    plt.subplot(1,5,i+1)
    im=np.asarray(cluster4_img[i:i+1]).reshape(28,28)
    plt.imshow(im)
plt.show()