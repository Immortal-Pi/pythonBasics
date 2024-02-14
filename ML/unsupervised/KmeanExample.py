import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans




data= pd.read_csv('datasets/force2020_data_unsupervised_learning.csv', index_col='DEPTH_MD')
# print(data)


#missing values as NaN, ML algorithms cannot accept these values
data.dropna(inplace=True)
print(data.describe())


#standardise the data, since few variables will have more influence over the other

scalar=StandardScaler()
data[['RHOB_N','GR_N','NPHI_N','PEF_N','DTC']]=scalar.fit_transform(data[['RHOB','GR','NPHI','PEF','DTC']])
print(data)

#applying K mean clustering to the data

def optimize_k_means(data,max_k):
    means=[]
    inertias =[]

    for k in range(1,max_k):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        means.append(k)
        inertias.append(kmeans.inertia_)

    # fig=plt.subplot()
    # plt.plot(means,inertias)
    # plt.xlabel('no of clusters')
    # plt.ylabel('Intertia')
    # plt.grid(True)
    # # plt.show()
    # plt.close(fig)


optimize_k_means(data[['RHOB_N','NPHI_N']],10)

#choosing 3 as the number of clusters
# kmeans3= KMeans(n_clusters=3)
# kmeans3.fit(data[['NPHI_N','RHOB_N']])
# data['kmeans3']=kmeans3.labels_
# # print(np.unique(data['kmeans3']))
#
# #visualize the clusters
# plt.scatter(x=data['NPHI'],y=data['RHOB'],c=data['kmeans3'])
# plt.xlim(-0.1,1)
# plt.ylim(3,1.5)
# plt.show()


#comparing for multiple K values

for k in range(1,6):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(data[['NPHI_N','RHOB_N']])
    data[f'kemeans{k}']= kmeans.labels_

print(data)

#visualize with different cluster values K
fig,axs=plt.subplots(nrows=1,ncols=5,figsize=(20,5))

for i, ax in enumerate(fig.axes,start=1):
    ax.scatter(x=data['NPHI'],y=data['RHOB'],c=data[f'kemeans{i}'])
    ax.set_ylim(3,1.5)
    ax.set_xlim(0,1)
    ax.set_title(f'N clusters: {i}')
plt.show()