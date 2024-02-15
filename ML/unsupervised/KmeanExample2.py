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
print(data)

#standardize the data
scalar=StandardScaler()
data[['RHOB_N','GR_N','NPHI_N','PEF_N','DTC_N']]=scalar.fit_transform(data[['RHOB','GR','NPHI','PEF','DTC']])
# print(data)

def k_mean_optimize(data,max_k):
    mean=[]
    inertia=[]

    for i in range(1,max_k):
        kmeans=KMeans(n_clusters=i)
        kmeans.fit(data)
        mean.append(i)
        inertia.append(kmeans.inertia_)

    # plt.plot(mean,inertia)
    # plt.xlabel('no of clusters')
    # plt.ylabel('intertia')
    # plt.grid(True)
    # plt.show()

k_mean_optimize(data[['RHOB_N','NPHI_N']],10)


#choosing k=3 as
kmeans=KMeans(n_clusters=3)
kmeans.fit(data[['NPHI_N','RHOB_N']])
data['kmean3']=kmeans.labels_
# print(data)
# fig=plt.subplots()
# plt.scatter(x=data['NPHI'],y=data['RHOB'],c=data['kmean3'])
# plt.ylabel('RHOB')
# plt.xlabel('NPHI')
# plt.xlim(-0.1,1)
# plt.ylim(3,1.5)
# plt.show()


#for all K values
print(data)

for i in range(1,6):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(data[['NPHI_N','RHOB_N']])
    data[f'kmean{i}']=kmeans.labels_

fig,axs=plt.subplots(1,5,figsize=(20,5))

for i,ax in enumerate(fig.axes,start=1):
    ax.scatter(x=data['NPHI'],y=data['RHOB'],c=data[f'kmean{i}'])
    ax.set_ylim(3,1.5)
    ax.set_xlim(-0.1,1)
    ax.set_title(f'no of clusters{i}')
plt.show()


