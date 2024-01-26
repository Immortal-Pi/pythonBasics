import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':

    x=np.linspace(-100,100,200,dtype=int)

    y=x**2+4
    x1=np.log(x)
    y1=np.sin(x) *500000
    print(x)
    # plt.plot(x,y)
    # plt.plot(x,y2)
    # plt.plot(x1)


    x1=np.linspace(-100,100,230,dtype=float)
    y1=np.tan(x1)
    plt.plot(x1,y1,'r')
    plt.show()