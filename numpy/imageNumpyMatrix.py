import numpy as np
from skimage.io import imread
from skimage.data import data_dir
import matplotlib.pyplot as plt
import os

img=imread(os.path.join(data_dir,'astronaut.png'))
plt.imshow(img)
# print(img)
print(f'type of image:{type(img)}')
print(f'Dimensions of image:{img.ndim}')
print(f'shape of image:{img.shape}')

plt.show()

