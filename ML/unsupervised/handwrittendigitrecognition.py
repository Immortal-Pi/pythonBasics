import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.client import device_lib


# data=tf.keras.datasets.mnist
#
# data1=data.load_data()
#
# (xtrain,ytrain),(xtest,ytest)=data1
#
# xtrain=tf.keras.utils.normalize(xtrain,axis=1)
# xtest=tf.keras.utils.normalize(xtest,axis=1)
#
# model=tf.keras.models.Sequential()
# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# print(device_lib.list_local_devices())