import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# x=np.arange(0,30,0.2)
# y1=np.sin(x)
# y3=np.tan(x)
# y2=x**2 + 2*x

#plt.subplot(no of rows, no of columns,indexed position in wich to be placed)
# ax1=plt.subplot(221)
# ax2=plt.subplot(222)
#
#
# plt.figure(1)
# ax1.plot(x,y1,'r')
# ax2.plot(x,y2,'g')
#
# plt.figure(2)
# ax3=plt.subplot(111)
# ax3.plot(x,y3,'b')

#graphs not interecting each other
# plt.tight_layout()
# plt.show()

# style.use('fivethirtyeight')
# style.use('ggplot')
# style.use('dark_background')
# style.use('fast')
# style.use('classic')
# style.use('bmh')
x1=np.arange(-10,10,0.2)
y1=np.sin(x1)
y2=np.cos(x1)
y3=np.log(x1)


# plt.figure(1)
#
# ax1=plt.subplot(211)
# plt.title('sin function')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# ax1.plot(x1,y1,'r')
#
#
# ax2=plt.subplot(212)
# plt.title('tan function')
# plt.xlabel('x')
# plt.ylabel('y')
# ax2.plot(x1,y2,'g')
# plt.grid(True)
# plt.tight_layout()
#
#
# plt.figure(2)
# ax3=plt.subplot(121)
# plt.title('Log function')
# plt.xlabel('x')
# plt.ylabel('y')
# ax3.plot(x1,y3,'y')
# plt.grid(True)



plt.figure(3)
plt.title('sin vs cos')
plt.plot(x1,y1,label='sin function',color='r')
plt.plot(x1,y2,label='cos function',color='g')
plt.legend(loc='upper right')
# plt.legend(loc='lower left')
# plt.legend(loc='center')
# plt.legend(loc='center right')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.tight_layout()
plt.grid()

plt.show()

