import math

import matplotlib.pyplot as plt
import numpy as np
def functionz(x,y):
    return x**2+y**2
ax =plt.axes(projection='3d')

# z=np.linspace(-2,2,10000)
# x = np.sin(z)
# y = np.cos(z)

x=np.linspace(-5,5,1000)
y=np.linspace(-5,5,1000)

x,y=np.meshgrid(x,y)
# z=functionz(x,y)
# print(z)
zValues=lambda x,y: np.sin(np.sqrt(x**2+ y**2))
# print(z.dtype,x.dtype)
# ax.plot_surface(x,y,z)

# ax.plot3D(x,y,z)
ax.plot_surface(x,y,zValues(x,y))
plt.show()