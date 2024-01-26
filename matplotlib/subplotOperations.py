import numpy as np
import matplotlib.pyplot as plt


x=np.arange(0,30,0.2)
y1=np.sin(x)
y3=np.tan(x)
y2=x**2 + 2*x

#plt.subplot(no of rows, no of columns,indexed position in wich to be placed)
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(224)

ax1.plot(x,y1,'r')
ax2.plot(x,y2,'g')
ax3.plot(x,y3,'b')

#graphs not interecting each other
plt.tight_layout()
plt.show()