#1 get data
#2 remove NAN values
#3 standardize the data
#4 apply k mean clustering to the data
#5 choose k value and plot the cluster
#6 compare with multiple K values




from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#get data
data=pd.read_csv('datasets/force2020_data_unsupervised_learning.csv',index_col='DEPTH_MD')
# print(data)


#remove NAN values
data.dropna(inplace=True)
# print(data)

#standardize the data
scalar=StandardScaler()
data[['RHOB_N','GR_N','NPHI_N','PEF_N','DTC_N']]=scalar.fit_transform(data[['RHOB','GR','NPHI','PEF','DTC']])
# print(data)


#apply k mean clustering

def k_optimize_cluster(data,max_k):
    means=[]
    inertia=[]

    for i in range(1,max_k):
        kmeans=KMeans(n_clusters=i)
        kmeans.fit(data)
        means.append(i)
        inertia.append(kmeans.inertia_)
    # fig =plt.subplot()
    # plt.plot(means,inertia)
    # plt.xlabel('no of clusters')
    # plt.ylabel('inertia')
    # plt.grid(True)
    # plt.show()

k_optimize_cluster(data[['RHOB_N','NPHI_N']],10)

#from the above function we can choose k=3
kmeans3=KMeans(n_clusters=3)
kmeans3.fit(data[['NPHI_N','RHOB_N']])
data['kmean3']=kmeans3.labels_

#visulize
# plt.scatter(x=data['NPHI'],y=data['RHOB'],c=data['kmean3'])
# plt.xlim(-0.1,1)
# plt.ylim(3,1.5)
# plt.show()


#for multiple k values

for i in range(1,6):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(data[['NPHI_N','RHOB_N']])
    data[f'kmeans{i}']=kmeans.labels_

print(data)

fig,axs=plt.subplots(nrows=1,ncols=5,figsize=(20,5))

for i,ax in enumerate(fig.axes,start=1):
    ax.scatter(x=data['NPHI'],y=data['RHOB'],c=data[f'kmeans{i}'])
    ax.set_ylim(3, 1.5)
    ax.set_xlim(0, 1)
    ax.set_title(f'N clusters: {i}')
plt.show()