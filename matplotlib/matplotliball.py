import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=x**2
# plt.plot(x,y)
# plt.show()



#object oriented approach

#1 creating empty canvas/figure
# fig=plt.figure()

#2 axes for figure [left, bottom, width, height]

# ax=fig.add_axes(rect=[0.1,0.1,0.8,0.8])

#3 plotting the lines
# ax.plot(x,y,'b',label='line1')
# ax.plot(x,y*2,'r',label='line2')
#
# ax.set_title('Title of the Plot',fontsize=15)    #setting title
# ax.set_xlabel('Label for X axis',fontsize=15)    # setting X label
# ax.set_ylabel('Label for Y axis',fontsize=15)    # setting Y _label
# plt.legend()
# plt.show()




#plotting multiple things on same figure
fig=plt.figure()
ax1=fig.add_axes([0.1,0.1,0.8,0.8])
ax2=fig.add_axes([0.3,0.3,0.5,0.5])
x=np.arange(2,100,3)
y=np.sin(x)
ax1.plot(x,y,'g',label='line1')
ax2.plot(x,np.cos(x),'r',label='line2')

plt.legend()

plt.show()